import json
from argparse import ArgumentParser
from dict2xml import dict2xml


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def get_attribute_dict(self):
        return self.__dict__

    def convert_to_json(self):
        with open('text.json', 'w') as file:
            file.write(json.dumps(self.get_attribute_dict()))

    def convert_to_xml(self):
        with open('text.xml', 'w') as file:
            file.write(dict2xml(self.get_attribute_dict(), wrap='box', indent="   "))


parser = ArgumentParser(description='Our cli parser ')

parser.add_argument('--name', help='Name from command')
parser.add_argument('--age', help='Age from command')
parser.add_argument('--gender', help='Gender command')
parser.add_argument('--birth_year', help='Birth year')
parser.add_argument('--parser_type', help='Data type from our cli command you want to get Human info in')

args = parser.parse_args()
arguments = {key: value for key, value in args.__dict__.items()}

if __name__ == "__main__":
    human = Human(arguments["name"], arguments["age"], arguments["gender"], arguments["birth_year"])
    if arguments["parser_type"] == "json":
        human.convert_to_json()
    elif arguments["parser_type"] == "xml":
        human.convert_to_xml()
    else:
        print("Put json or xml")


# to get json text:
# --name=Pavlo --age=32 --gender=male --birth_year=1990 --parser_type=json

# to get xml text:
# --name=Anna --age=31 --gender=female --birth_year=1991 --parser_type=xml
