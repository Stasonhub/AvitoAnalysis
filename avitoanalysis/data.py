from settings import *

def format_data(items, fn):
    for i in items:
        for str in i:
            fn('{}: {}\n'.format(str, i[str]))
        fn('\n')

class Data:
    def __init__(self, items):
        self.items = items

    def save_data(self):
        name = '{}-{}'.format(CITY.lower(), Q.lower().replace(' ', '-'))
        with open('data/{}.txt'.format(name), 'w+') as file:
            format_data(self.items, file.write)

    def print_data(self):
        format_data(self.items, print)
