Bullet list source: https://en.wikipedia.org/wiki/Outline_of_academic_disciplines#References
# bullet to json
Given bullet point hierarchy return taxonomy json.
1. bullet text to node-type, element csv
2. 


## bullet-to-csv-main.py


## formatting_txt.py
rough draft (irrelevant to program?)

## bullet-to-csv-class.py


## formatting.txt
rename to "bullet.txt"
- delimited text file of bullet points 
- (ranges of asterisks separate each field)
- root not included
````
* elem-a
** child1-elem-a
*** child1-child-1-elem-a
** child2-elem-a
* elem-b
** child1-elem-b
````

## node-element.csv
- CSV of node-type, element pairs
- node-types: Discipline, Branch, Subject, Field, Focus, Niche

## branch.csv
- each line lists an element and its parents to the root.

The bulleted list from http://ontology.buffalo.edu/philosophome/index_files/philosophome.html is good inspiration
