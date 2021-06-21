from re import match, compile
import argparse

'''
Example Usage : python q3_can_create.py --list back end front end tree --inputStr frontend
'''

class CanCreate:
    def __init__(self, list_of_strings: str, input_string: str):
        self.list_of_strings = list_of_strings
        self.input_string = input_string
        self.regx = None


    def can_create(self) -> bool:
        if self.input_string in self.list_of_strings:
            return True
        else:
            regx = compile("(?:" + "|".join(self.list_of_strings) + ")*$")
            if regx.match(self.input_string) != None:
                 return True
        return False



if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Check if the input string can be formed with joining list of strings')
    my_parser.add_argument('--list',metavar='list_of_strings',
                       nargs = "+",
                       default = ["back", "end", "front", "tree"], 
                       help='Enter ')
    my_parser.add_argument('--inputStr',metavar='input_string',
                       type=str,
                       default = "frontend",
                       help='Enter input string')
    args = my_parser.parse_args()
    list_of_strings = args.list
    input_string = args.inputStr
    CANCREATE = CanCreate(list_of_strings, input_string)
    print(CANCREATE.can_create())
