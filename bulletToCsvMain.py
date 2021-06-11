# Author: Izak Schmidlkofer
# Date: 6/5/21
# Description: Asterisk bullet list txt file convert to node-type, element csv
#               Runs "nodeElement.csv through taxonomy parser"

"""
formatting_txt.py
    need to rename to "bulletToCsvMain.py"

INPUT: DELIMITED TXT FILE OF BULLET POINTS
(ranges of asterisks separate each field)

OUTPUT: "FIXED WIDTH" (delimited with commas) TXT FILE
(Fields aligned in columns with commas between)
"""
import bulletToCsvClass

FILE = 'nodeElement.csv'
level = ['Discipline', 'Branch', 'Subject', 'Field', 'Focus', 'Niche']


def main():
    c = bulletToCsvClass.Taxonomy(level, FILE)
    c.write_dict()


if __name__ == '__main__':
    main()
