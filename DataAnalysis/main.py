import click

from get_data import main as getter
from settings import *


@click.command()
@click.option('--city', '-city', help='Name of needed city')
@click.option('--type', '-t', help='What are we looking for?')
@click.option('--category', '-cat', help='Number of category')
@click.option('--search', '-s', help='Searching query')
def main(city, typ, category, search):
    if not (city and typ and category and search):
        click.echo('You missed something')

    url = 'https://www.avito.ru/{}/{}?s={}&q={}'.format(city, category, typ, search)
    getter(url)

if __name__ == '__main__':
    main()
