
import sys
import requests
import datetime
from bs4 import BeautifulSoup

from data import Data

def get_items(text):
    items = []

    soup = BeautifulSoup(text, 'html.parser')
    divs = soup.find_all('div', 'item')

    for i in divs:
        title = i.find_all('a', 'item-description-title-link')[0].getText().strip()
        about = i.find_all('div', 'about')[0].getText().strip()
        name, year = title.split(', ')
        price, description = about.split('руб.') # No idea how to separate them in any other way

        items.append({'name': name, 'year': year, 'price': price, 'description': description})
    return items


def main(url):
    res = requests.get(url)
    if res.status_code != 200:
        print("Problem with data. Please check your url correctness and website availability.")
        sys.exit()

    text = res.text
    data = Data(get_items(text))

    ans = input("Print or save: ").lower()

    if ans == 'print': data.print_data()
    elif ans == 'save': data.save_data()

    print("\nAll done!")

# if __name__ == "__main__":
#     main()
