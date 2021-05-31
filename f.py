"""
formatting_txt.py

INPUT: DELIMITED TXT FILE OF BULLET POINTS
(ranges of asterisks separate each field)

OUTPUT: "FIXED WIDTH" (delimited with commas) TXT FILE
(Fields aligned in columns with commas between)
"""
import taxonomy_parser

FILE = 'formatting.txt'
level = ['Discipline', 'Branch', 'Subject', 'Field', 'Focus', 'Niche']


def main():
    c = taxonomy_parser.Taxonomy(level, FILE)
    c.write_dict()


if __name__ == '__main__':
    main()
