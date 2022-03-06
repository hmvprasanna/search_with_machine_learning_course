import argparse
import os
import random
import xml.etree.ElementTree as ET
import string
from collections import Counter
from nltk.stem.snowball import SnowballStemmer
from pathlib import Path

def transform_name(product_name):
    
    stemmer = SnowballStemmer('english')
    
    product_name_lower = product_name.lower()
    punct_trans = product_name_lower.maketrans(string.punctuation, ' '*len(string.punctuation))
    product_name_wspace = product_name_lower.translate(punct_trans)
    product_name_stemmed = " ".join([stemmer.stem(word) for word in product_name_wspace.split()])
    
    return product_name_stemmed

# Directory for product data
directory = r'/workspace/search_with_machine_learning_course/data/pruned_products/'

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--input", default=directory,  help="The directory containing product data")
general.add_argument("--output", default="/workspace/datasets/fasttext/output.fasttext", help="the file to output to")

# Consuming all of the product data will take over an hour! But we still want to be able to obtain a representative sample.
general.add_argument("--sample_rate", default=1.0, type=float, help="The rate at which to sample input (default is 1.0)")

# IMPLEMENT: Setting min_products removes infrequent categories and makes the classifier's task easier.
general.add_argument("--min_products", default=0, type=int, help="The minimum number of products per category (default is 0).")

general.add_argument("--category_level", default=0, type=int, help="The category level to be output as label, if that level is present (default is 0 that corresponds to leaf node).")

args = parser.parse_args()
output_file = args.output
path = Path(output_file)
output_dir = path.parent
if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)

if args.input:
    directory = args.input

min_products = args.min_products
sample_rate = args.sample_rate
category_level = args.category_level
#print("category_level: %s" % category_level)

categories = []
if min_products > 0:
    print("Category Counting Loop:")
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            print("Processing %s" % filename)
            f = os.path.join(directory, filename)
            tree = ET.parse(f)
            root = tree.getroot()
            if category_level == 0:
                for child in root:
                    # Check to make sure category name is valid
                    if (child.find('name') is not None and child.find('name').text is not None and
                        child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                        child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text is not None):
                            # Choose last element in categoryPath as the leaf categoryId
                            # Append to the categories list to count occurrences
                            categories.append(child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text)
                            
            else:
                for child in root:
                    # Check to make sure category name is valid
                    if (child.find('name') is not None and child.find('name').text is not None and
                        child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                        category_level <= len(child.find('categoryPath')) and 
                        child.find('categoryPath')[category_level - 1][0].text is not None):
                            # Choose to map categoryPath at level category_level to cat
                            categories.append(child.find('categoryPath')[category_level-1][0].text)

# Count each category and store
categoryCounter = Counter(categories)
print(categoryCounter)

print("Writing results to %s" % output_file)
with open(output_file, 'w') as output:
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            print("Processing %s" % filename)
            f = os.path.join(directory, filename)
            tree = ET.parse(f)
            root = tree.getroot()
            if category_level == 0:
                for child in root:
                    if random.random() > sample_rate:
                        continue
                    # Check to make sure category name is valid
                    if (child.find('name') is not None and child.find('name').text is not None and
                        child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                        child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text is not None):
                            # Choose last element in categoryPath as the leaf categoryId
                            cat = child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text

                            # Replace newline chars with spaces so fastText doesn't complain
                            name = child.find('name').text.replace('\n', ' ')

                            if min_products == 0 or categoryCounter[cat] >= min_products:
                                output.write("__label__%s %s\n" % (cat, transform_name(name)))
            else:
                for child in root:
                    if random.random() > sample_rate:
                        continue
                    # Check to make sure category name is valid
                    if (child.find('name') is not None and child.find('name').text is not None and
                        child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                        category_level <= len(child.find('categoryPath')) and 
                        child.find('categoryPath')[category_level - 1][0].text is not None):
                            # Choose the category_level path
                            cat = child.find('categoryPath')[category_level-1][0].text

                            # Replace newline chars with spaces so fastText doesn't complain
                            name = child.find('name').text.replace('\n', ' ')

                            if min_products == 0 or categoryCounter[cat] >= min_products:
                                output.write("__label__%s %s\n" % (cat, transform_name(name)))
