# Answers for Questions of Week 3 Assignments:

## For classifying product names to categories:

### What precision (P@1) were you able to achieve?
0.888

### What fastText parameters did you use?
The best P@1 was achieved with the following settings:
1. min_products = 200
2. Learning Rate, lr=1.0 
3. epoch=100, 
4. wordNgrams=2

### How did you transform the product names?
1. Lowercased the names entirely
2. Removed all the punctuations
3. Stemmed each word of the product name using the NLTK Snowball Stemmer, removed extra white spaces and reconstructed the names

### How did you prune infrequent category labels, and how did that affect your precision?
To prune infrequent category labels, kept a corresponding counter list for each category tagged and looped through to populate this counter list. While writing the output file, checked if the category counter for the specific category identified in that iteration of the loop is greater than or equal to the one provided through the min_products parameter, and printed it only in that case.

The following table shows the progress with the change of parameters and its effect on P@1:

| min_product | lr      | labels   | epoch | ngrams | P@1   | R@1   |
|-------------|---------|----------|-------|------- |-------|-------|
| 0           | 1.0     | 1343     | 25    | 1      | 0.627 | 0.627 |
| 0           | 1.0     | 1343     | 25    | 2      | 0.623 | 0.623 |
| 10          | 1.0     | 1170     | 25    | 1      | 0.631 | 0.631 |
| 10          | 1.0     | 1170     | 25    | 2      | 0.629 | 0.629 |
| 50          | 1.0     | 520      | 25    | 1      | 0.721 | 0.721 |
| 50          | 1.0     | 520      | 25    | 2      | 0.727 | 0.727 |
| 50          | 1.0     | 520      | 50    | 2      | 0.729 | 0.729 |
| 100         | 1.0     | 269      | 25    | 1      | 0.806 | 0.806 |
| 100         | 1.0     | 269      | 25    | 2      | 0.810 | 0.810 |
| 100         | 1.0     | 269      | 50    | 2      | 0.812 | 0.812 |
| 100         | 1.0     | 269      | 100   | 2      | 0.812 | 0.812 |
| 200         | 1.0     | 113      | 25    | 1      | 0.883 | 0.883 |
| 200         | 1.0     | 113      | 25    | 2      | 0.888 | 0.888 |
| 200         | 1.0     | 113      | 50    | 2      | 0.887 | 0.887 |
| 200         | 1.0     | 113      | 100   | 2      | 0.888 | 0.888 |


### How did you prune the category tree, and how did that affect your precision?
For pruning the category tree, I introduced another command line parameter called category_level and passed values through it. 0 was kept to indicate the default behavior - that is, considering the leaf node. But if the user passes values 1 through 4, then, the categories printed to the output file would be of that specific level (1 through 4, whichever is selected) for each product. So, the file would have the category id of the same level for all products. 

To check the precision, kept the following parameters as constant:
lr = 1.0, min_products = 100, epoch = 25, ngrams = 2

| cat_level   | min_product | lr      | labels   | epoch | ngrams | P@1   | R@1   |
|-------------|-------------|---------|----------|-------|------- |-------|-------|
| 0 (default) | 100         | 1.0     | 269      | 25    | 2      | 0.810 | 0.810 |
| 1           | 100         | 1.0     | 1        | 25    | 2      | 1.000 | 1.000 |
| 2           | 100         | 1.0     | 17       | 25    | 2      | 0.923 | 0.923 |
| 3           | 100         | 1.0     | 102      | 25    | 1      | 0.894 | 0.894 |
| 4           | 100         | 1.0     | 223      | 25    | 2      | 0.866 | 0.866 |



## For deriving synonyms from content:

### What 20 tokens did you use for evaluation?
#### Product types
1. camera
2. laptop
3. guitar
4. speaker
5. oven

#### Brands
1. microsoft
2. hp
3. panasonic
4. nintendo
5. toshiba

#### Models
1. iphone
2. linksys
3. vaio
4. playstation
5. ipad

#### Attributes
1. blue
2. flat
3. wireless
4. external
5. red

### What fastText parameters did you use?
minCount = default, 10, 20, 50

### How did you transform the product names?
Did the following in addition to the newline replacement that was already present:
1. Replcaed all the Registered(®), Trademark (™) and Copyright (©) symbols with white spaces.
2. Lowercased the names entirely
3. Removed all the punctuations
4. Stemmed each word of the product name using the NLTK Snowball Stemmer, removed extra white spaces and reconstructed the names

### What threshold score did you use? 
For most cases, a threshold of 0.90 looks decent.

### What synonyms did you obtain for those tokens?
Results obtained for minCount = 20:

camera : [(0.994641900062561, '1mp'), (0.9943810105323792, 'shot'), (0.9936113357543945, 'finepix'), (0.9930093288421631, '0mp'), (0.9921373128890991, '2mp'), (0.9905740022659302, 'canon'), (0.9901690483093262, 'megapixel'), (0.9895358681678772, 'nikon'), (0.9883928298950195, 'lumix'), (0.9878947734832764, 'powershot')]

laptop : [(0.9881325960159302, 'athlon'), (0.9860821962356567, 'processor'), (0.9839940071105957, 'lenovo'), (0.9839091300964355, 'i3'), (0.9821134209632874, 'pavilion'), (0.9819977283477783, 'i5'), (0.9807158708572388, 'pentium'), (0.9790855646133423, 'x2'), (0.9786447882652283, 'inspiron'), (0.978037416934967, 'aspir')]

guitar : [(0.984932541847229, 'string'), (0.9696850776672363, 'full'), (0.9688027501106262, 'natur'), (0.9596007466316223, 'acoust'), (0.9579064846038818, 'solo'), (0.9550053477287292, 'size'), (0.9378662705421448, 'schecter'), (0.9332837462425232, 'bass'), (0.9182549715042114, 'satin'), (0.9166398048400879, 'custom')]

speaker : [(0.9606893062591553, 'coaxial'), (0.9554100036621094, 'polypropylen'), (0.9517672061920166, 'polk'), (0.951647937297821, 'kicker'), (0.9478958249092102, 'pair'), (0.9434272646903992, 'way'), (0.9372372627258301, 'pioneer'), (0.9362984895706177, 'marin'), (0.9068105816841125, 'each'), (0.8971624374389648, 'channel')]

oven : [(0.9872056245803833, 'self'), (0.9859551191329956, 'rang'), (0.9827976226806641, 'slide'), (0.9821126461029053, '27'), (0.981596052646637, 'convert'), (0.9801732301712036, 'convect'), (0.9779697060585022, '36'), (0.975744366645813, 'clean'), (0.9732869267463684, 'hood'), (0.9710336327552795, 'doubl')]

microsoft : [(0.9762718677520752, 'softwar'), (0.9750625491142273, 'offic'), (0.9686927199363708, 'univers'), (0.9676843285560608, 'b'), (0.9676380753517151, 'netgear'), (0.9674831032752991, 'south'), (0.9664851427078247, 'psp'), (0.9659983515739441, 'dj'), (0.9646308422088623, 'delux'), (0.9634240865707397, 'pillow')]

hp : [(0.9868324995040894, 'pavilion'), (0.9844958186149597, 'inspiron'), (0.9844799637794495, 'intel'), (0.979242742061615, 'lenovo'), (0.9780336618423462, 'processor'), (0.9762036800384521, 'athlon'), (0.9761234521865845, 'gateway'), (0.975130021572113, 'i5'), (0.9739858508110046, 'i7'), (0.9732442498207092, 'compaq')]

panasonic : [(0.9816227555274963, 'panason'), (0.8893975615501404, 'definit'), (0.8754435777664185, 'samsonit'), (0.8590495586395264, 'jvc'), (0.8570737242698669, 'philip'), (0.847176730632782, '3m'), (0.8365058302879333, 'red'), (0.8313085436820984, 'sound'), (0.8310793042182922, 'remot'), (0.8307209014892578, 'replac')]

nintendo : [(0.981205403804779, 'wii'), (0.9676461815834045, 'advanc'), (0.9664614200592041, 'gamecub'), (0.9646183848381042, 'window'), (0.9630606174468994, 'ps2'), (0.9532612562179565, 'world'), (0.94940584897995, '360'), (0.9472029209136963, 'edit'), (0.946491003036499, 'game'), (0.9425137042999268, 'legend')]

toshiba : [(0.9416524171829224, 'refurbish'), (0.9119134545326233, 'desk'), (0.9092615842819214, 'monitor'), (0.8988065123558044, '64'), (0.8965994119644165, '98'), (0.8953199982643127, 'packag'), (0.8934403657913208, 'inspiron'), (0.8922111988067627, 'led'), (0.8913952708244324, 'factori'), (0.8904769420623779, 'asus')]

iphone : [(0.957145631313324, 'phone'), (0.9564388990402222, 'motorola'), (0.9527695775032043, 'iphon'), (0.9456384778022766, 'mobil'), (0.9397907853126526, 'charger'), (0.9353570938110352, 'no'), (0.9348233342170715, '4g'), (0.933239221572876, 'cell'), (0.9331803321838379, 'charg'), (0.9233303666114807, 'htc')]

linksys : [(0.9862367510795593, 'link'), (0.9592228531837463, 'devic'), (0.9576180577278137, 'handheld'), (0.9576016664505005, 'remot'), (0.9420264959335327, 'optic'), (0.9418908357620239, 'logitech'), (0.9413135647773743, 'industri'), (0.9392748475074768, 'energ'), (0.938048243522644, 'lite'), (0.9337506890296936, 'd')]

vaio : [(0.976337730884552, 'duo'), (0.9746724367141724, 'pentium'), (0.9722492694854736, 'laptop'), (0.9687905311584473, '6gb'), (0.9686661958694458, 'i5'), (0.9668456315994263, 'x2'), (0.9658925533294678, 'athlon'), (0.965785801410675, 'processor'), (0.9650949239730835, 'lenovo'), (0.9645541906356812, 'i3')]

playstation : [(0.9756302833557129, 'microsoft'), (0.9592729210853577, 'giant'), (0.9589866399765015, 'playstat'), (0.9561360478401184, 'time'), (0.9533935189247131, 'softwar'), (0.9533370137214661, 'offic'), (0.9531551003456116, 'netgear'), (0.9525994062423706, 'chicago'), (0.9473304748535156, 'box'), (0.9465207457542419, 'alfr')]

ipad : [(0.9746991395950317, 'generat'), (0.9711917042732239, 'folio'), (0.9703501462936401, 'appl'), (0.9702061414718628, '3rd'), (0.9674965143203735, 'touch'), (0.9672091007232666, '4th'), (0.9665222764015198, 'nano'), (0.9572277069091797, 'griffin'), (0.956985354423523, 'jacket'), (0.9543188810348511, '3g')]

blue : [(0.9545992016792297, 'red'), (0.9518585801124573, 'grip'), (0.9445019960403442, 'handycam'), (0.9421891570091248, 'casio'), (0.9421758055686951, 'batteri'), (0.9413702487945557, 'pink'), (0.9404120445251465, 'lamp'), (0.9379482865333557, 'pouch'), (0.9334744811058044, 'backpack'), (0.9252049326896667, 'recharg')]

flat : [(0.9879446625709534, 'tv'), (0.9790893197059631, 'tvs'), (0.9710183143615723, 'panel'), (0.958629846572876, 'design'), (0.956811249256134, 'to'), (0.9523305296897888, '42'), (0.9513938426971436, 'up'), (0.9322376847267151, 'dlp'), (0.9315533638000488, '32'), (0.9203444123268127, 'tube')]

wireless : [(0.9181423187255859, 'headset'), (0.9111297726631165, 'logitech'), (0.909612238407135, 'netgear'), (0.8965802788734436, 'link'), (0.8935914039611816, 'devic'), (0.8920538425445557, 'n'), (0.8903325200080872, 'vtech'), (0.8901684880256653, 'control'), (0.8885903358459473, 'bluetooth'), (0.887479305267334, 'lite')]

external : [(0.9626892805099487, 'extern'), (0.9545168280601501, 'western'), (0.9498308300971985, 'seagat'), (0.9422675967216492, 'firewir'), (0.9375340342521667, 'live'), (0.9370428323745728, 'my'), (0.9336052536964417, 'usb'), (0.9212222099304199, 'attaché'), (0.9211907982826233, 'fire'), (0.9172006845474243, 'media')]

red : [(0.9663658738136292, 'handycam'), (0.9599830508232117, 'casio'), (0.9545990824699402, 'blue'), (0.9503653049468994, 'backpack'), (0.9500633478164673, 'kodak'), (0.9469444751739502, 'lowepro'), (0.9443446397781372, 'silver'), (0.9414575099945068, 'carri'), (0.9410473108291626, 'lumix'), (0.9408974647521973, 'tripod')]
