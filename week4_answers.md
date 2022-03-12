# Answers for Questions of Week 4 Assignments:

## For query classification:

### How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 100? To 1000?
1. 879 (for min_queries = 100)
2. 387 (for min_queries = 1000)

### What values did you achieve for P@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category as well as trying different fastText parameters or query normalization. Report at least 3 of your runs.

| min_queries | lr      | categories | epoch | ngrams | P@1   | R@1   | R@3   | R@5   |
|-------------|---------|----------  |-------|------- |-------|-------|-------|-------|
| 100         | def.    | 879        | def.  | def.   | 0.467 | 0.467 | 0.618 | 0.681 |
| 100         | def.    | 879        | 25    | def.   | 0.519 | 0.519 | 0.699 | 0.759 |
| 100         | 0.4     | 879        | 25    | def.   | 0.518 | 0.518 | 0.696 | 0.757 |
| 100         | def.    | 879        | 25    | 2      | 0.517 | 0.517 | 0.696 | 0.756 |
| 100         | def.    | 879        | 50    | 2      | 0.517 | 0.517 | 0.695 | 0.758 |
| 1000        | def.    | 387        | def.  | def.   | 0.481 | 0.481 | 0.641 | 0.703 |
| 1000        | def.    | 387        | 25    | def.   | 0.526 | 0.526 | 0.705 | 0.770 |
| 1000        | 0.4     | 387        | 25    | def.   | 0.522 | 0.522 | 0.703 | 0.767 |
| 1000        | def.    | 387        | 25    | 2      | 0.527 | 0.527 | 0.709 | 0.774 |
| 1000        | def.    | 387        | 50    | 2      | 0.522 | 0.522 | 0.706 | 0.769 |


## For integrating query classification with search:

### Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.

- Query: __ipad__
- Results without filtering: 6,049
- Results with filtering: 48
- pcmcat209000050007 ("iPad")= 0.62286848

<br/>

- Query: __lumix__
- Results without filtering: 298
- Results with filtering: 59
- ['abcat0401004', 'pcmcat214000050002'] (["Fun & Basic Cameras", "Long Zoom Cameras"]) = [0.46442983, 0.38164318]

<br/>

- Query: __router__
- Results without filtering: 777
- Results with filtering: 256
- abcat0503002 ("Wireless Routers")= 0.69201607

<br/>

- Query: __speaker__
- Results without filtering: 9,121
- Results with filtering: 882
- ['abcat0515039', 'pcmcat223000050007', 'pcmcat144700050004', 'abcat0205001', 'abcat0208011'] (['Computer Speakers', '2-Way Speakers', 'All Headphones', 'Bookshelf Speakers', 'iPod & MP3 Speakers, Docks & Radios']) = [0.23492932, 0.08128799, 0.06664631, 0.06163386, 0.05802042]
- Effectively filters out speaker stands, keynote speaker DVDs, motivational speaker CDs, etc.


### Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

This was difficult to find! Most results were good.

- Query: __notebook__
- Results without filtering: 2,728
- Results with filtering: 122
- ['pcmcat247400050000', 'pcmcat164200050013', 'pcmcat236800050000', 'pcmcat159400050011'] (['PC Laptops', 'All Netbooks', 'Hello Kitty Merchandise', 'Treadmills']) = [0.24276432, 0.17273185, 0.07304551, 0.07300881]
- Reason it could be bad: Filters out the movie "The Notebook" or actual writing notebooks

<br/>

- Query: __olympus__
- Results without filtering: 957
- Results with filtering: 236
- ['pcmcat174700050005', 'abcat0805003', 'abcat0401004'] ([0.21181969, 0.16006, 0.15514867]) = ['PC Games', 'Voice Recorders', 'Fun & Basic Cameras']
- Reason it could be bad: Filters out the music CDs / DVDs of Olympus, which could very well be the search intent
