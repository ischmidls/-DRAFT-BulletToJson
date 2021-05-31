"""
formatting_txt.py

INPUT: DELIMITED TXT FILE OF BULLET POINTS
(ranges of asterisks separate each field)

OUTPUT: "FIXED WIDTH" (delimited with commas) TXT FILE
(Fields aligned in columns with commas between)
"""

"""
txt_dict = {
*branch
**disciplines
***subjects
****fields
*****focuses

txt_dict = {["branch"]:
    {["disciplines"]:
      {["subjects"]: 
         {["fields"]:
            {["focuses]"
                }}}}}

txt_dict[branch][discipline][subject][field][focus]
txt_dict[*][**][***]****][*****]

txt_dict = 
    {"art":
        {"performance":
          {"dance": 
             {"interpretive":
                {["native", "fictional", ...]
                    }}}}},
        {"visual":
            {"painting": 
                 {"modern":
                    {["abstract", "historical", ...]
                        }}}}},
    {"philosophy":
        {"metaphysics":
          {"ontology": 
             {"dualism":
                {["dualist conflict", "fictional dualism", ...]
                    }}}}},
        {"axiology":
            {"ethics": 
                 {"bioethics":
                    {["euthanasia", "abortion", ...]
                        }}}}},
"""

INPUT_FILE = open('formatting.txt')  # file with delimited bullet points
# OUTPUT_FILE = open('output.txt', 'a')  # create empty file
NUM_AST = 5  # number of asterisks

branch = {}  # create an empty dictionary to hold nested bullet points
line_string_list = []  # create empty list to hold lines from txt

def main():
    line_string_list = file_to_list()
    print(line_string_list)
    i_am_tired(line_string_list, branch)
    print(branch)

"""
FIRST LETTER OF LINE STRING VALUE IS PART OF i_string 

** M 1158 aterials Science and Engineering
** M 1168 echanical Engineering
** S 1190 ystems science
** M 1239 edicine and health
"""
def debug_one(line_string_start, line_string_index, line_string_value):
    for ch in line_string_start:
        if ch != '*' and ch != ' ':
            print(f"{line_string_start} {line_string_index} {line_string_value}")

"""
MOVING THE FILE TO A LIST ALLOWS LINES (as strings) TO BE ACCESSED AT INDEXES
"""


def file_to_list():
    for line in INPUT_FILE.readlines():
        # REMOVE \n FROM LINE
        line_string = line[:-1]
        #  ADD LINE TO LIST
        line_string_list.append(line_string)
    INPUT_FILE.close()

    # Remove odd characters at beginning
    return line_string_list[1:]


"""
GIVEN THE THE STRING IN THE LIST, THE NUMBER OF
ASTERISKS IN THE iATION, AND THE iATION
COMPUTE THE ACTUAL STRING BEGINNING, AND COMPARE IT TO THE THEORETICAL BEGINNING
"""


def start_of_string_matches_iation(line_string, i_num_ast, i_len_string):
    # IF THE LINE BEGINS WITH 1,2,3,4,5 ASTERISKS
    line_string_start = line_string[:i_len_string]  # THE LINE BEGINS e.g. "* philosphy", "** metphysics"
    i_string = '*' * i_num_ast + ' '

    return line_string_start, i_string


"""
GIVEN THE THE STRING IN THE LIST, THE LIST OF LINE STRINGS,
AND THE iATION
COMPUTE THE VALUE STORED IN THE STRING AND THE STRING INDEX
"""


def value_and_index(line_string, line_string_list, i_len_string):
    # THE LINE WITHOUT ASTERISKS
    line_string_value = line_string[i_len_string:]
    # THE INDEX OF THE LINE
    line_string_index = line_string_list.index(line_string)
    return line_string_value, line_string_index


"""
LOOP THROUGH THE LIST, UPDATING THE branch DICTIONARY FOR EACH TIER
OF THE ASTERISK HIERARCHY.

THE TXT IS ORDERED, BUT NOT LINEARLY.

LOOP THROUGH FILE LIST NUM_AST TIMES (5)
IN EACH iATION OF THE FOR LOOP, THE VARIABLE i IS
EQUAL TO THE NUMBER OF ASTERISKS - 1 (0,1,2,3,4)
"""


def i_am_tired(line_string_list, branch):
    for i in range(NUM_AST):
        i_num_ast = i + 1  # NUMBER OF ASTERISKS TARGETED IN iATION
        i_len_string = i + 2  # len of string start for each iation

        for line_string in line_string_list:  # for string in line list

            # COMPUTE THE ACTUAL STRING BEGINNING AND THE THEORETICAL BEGINNING
            line_string_start, i_string = start_of_string_matches_iation(line_string, i_num_ast, i)

            # COMPUTE THE VALUE IN THE STRING AND THE STRING INDEX
            line_string_value, line_string_index = value_and_index(line_string, line_string_list, i)

            debug_one(line_string_start, line_string_index, line_string_value)

            value_at_index_lower(i_num_ast, line_string_value, line_string_index,
                                 line_string_start, i_len_string)


"""
ADD THE VALUES FROM STRINGS IN THE HIERARCHY MIDDLE (MIN,**, ***,...MAX)
(NEITHER MOST NOR LEAST ASTERISKS)
TO A DICT WITH A KEY EQUAL TO 
THE FIRST LOWER INDEX STRING IN THE LIST 
THAT IS HIGHER IN THE HIERARCHY (HAS LESS ASTERISKS)

e.g. line_string_index > lower_index 
     line_string_list(lower_index)

immediate lower list index 
== immediate (values in strings in list) or (values in lines above in txt)
== higher or equal tier in hierarchy 
"""


def value_at_index_lower(i_num_ast, line_string_value,
                         line_string_index, line_string_start, i_len_string):
    list_tiers = []  # FIND PATH FROM LOWEST HIERARCHY TO TOP
    focus = []  # LOWEST HIERARCHY

    # Find the value of each immediately higher tier
    for j in range(i_num_ast):

        # count down variable for lower indexes
        lower_index = line_string_index

        # While the start of the string is shorter than the start determined by the iation
        while len(line_string_start) - j >= i_len_string - j:
            lower_index -= 1

        outer = line_string_list[lower_index]
        list_tiers.append(outer)
    if i_num_ast == 1:
        branch.update({line_string_value: {}})
    elif i_num_ast == 2:
        branch[list_tiers[1]] = {line_string_value: {}}
    elif i_num_ast == 3:
        branch[list_tiers[1]][list_tiers[2]] = {line_string_value: {}}
    elif i_num_ast == 4:
        branch[list_tiers[1]][list_tiers[2]][list_tiers[3]] = {line_string_value: {}}
    elif i_num_ast == 5:
        focus.append(line_string_value)
        branch[list_tiers[1]][list_tiers[2]][list_tiers[3]][list_tiers[4]] = focus


if __name__ == '__main__':
    main()
