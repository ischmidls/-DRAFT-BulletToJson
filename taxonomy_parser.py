# Author: Izak Schmidlkofer
# Date: 6/5/21
# Description: Defines class such that asterisk bullet list txt file convert to node-type, element csv

"""
taxonomy_parser.py
    neeed to rename to "bullet-to-csv-class.py"

"""


class Format:
    """
    """
    
    def __init__(self, ll):
        """
        """
    
        self.temp = ''  # INITIALIZE NEW LINE
        self.num = ''  # INITIALIZE COUNTER
        self.ll = ll

    def sentinel(self):
        """
        """
    
        s = ','  # ^^ SENTINEL
        i = 0  # ^^ INDEX
        while not s:  # WHILE SENTINEL NOT COMMA
            ch = self.ll[i]  # GET CHARACTER IN LINE
            i += 1  # ADD 1 TO INDEX
            s = ch  # SENTINEL = CHARACTER
            self.temp += ch  # ADD CHARACTER TO NEW LINE
        for ch in self.ll[1:]:
            if ch != ",":
                self.temp += ch
        print(f'{self.temp}=temp {self.ll}=ll')

    def del_com(self):
        """
        >>> ls = ["d,o,g", "d,,og", ",dog,"]
        >>> del_com(ls)
        ["d,og", "d,og", ",dog"]
        """
        
        for ch in self.ll:
            if ch == ",":
                self.num += ch  # COUNT COMMAS
        if len(self.num) > 1:  # IF MORE THAN ONE COMMA IN LINE
            self.sentinel()
        if self.temp == '':
            return self.ll.split(',')
        else:
            return self.temp.split(',')


class Taxonomy:
    """
    """
    
    def __init__(self, level, input_file):
        """
        """
        
        self.taxonomy = {}
        self.nodes = {}
        self.root = ''
        self.level = level
        self.input_file = input_file

    def read_txt(self):
        """
        Input = name of file with pairs = (level)
        """
        
        f = open(self.input_file, encoding='utf-8-sig')
        ll = []
        for e in f:
            ll.append(Format(e.strip()).del_com())
        f.close()
        self.root = ll[0][0]
        self.nodes = ll


    def sort_dict(self):
        """
        Input = level list = (top, ..., bottom)
        """
        
        self.read_txt()

        n = self.nodes
        r = self.root
        t = self.taxonomy
        level = self.level

        for e in range(1, len(level)):  # EACH RANK IS A LEVEL OF DICTIONARIES
            t[level[e]] = []  # INITIALIZE LEVELS

        t[r] = []  # ROOT
        t[r].append({'name': r})  # ROOT_KEY

        for i in range(1, len(n)):  # FOR EACH LINE
            lv = n[i][0]  # LEVEL
            t[lv].append({'name': n[i][1]})
            print(f"{t[lv]} { {'name': n[i][1]}}")
            for v in reversed(n[:i]):  # FOR THE LINES BEFORE IN REVERSE ORDER
                if level.index(v[0]) < level.index(n[i][0]):
                    if v[0] == 'Academics':
                        t[lv][-1]['parent'] = r
                    else:
                        t[lv][-1]['parent'] = v[1]
                    break
        print(t)
        return t

    def write_dict(self):
        """
        """
        
        self.sort_dict()

        level = self.level
        t = self.taxonomy

        f = open('file.txt', 'w+', encoding='utf-8-sig')
        for k in t:  # key tax
            for i in range(len(t[k])):  # dict key
                f.writelines(f"{t[k][i]['name']} \n")

