import click

from get_data import main as getter
from settings import *

@click.command()
@click.option('--city', '-city')
@click.option('--typ', '-t')
@click.option('--category', '-cat')
@click.option('--search', '-s')
def main(city, typ, category, search):
    if not (city and typ and category and search):
        click.echo('You missed something')

    url = 'https://www.avito.ru/{}/{}?s={}&q={}'.format(city, typ, category, search)
    click.echo(url)
    getter(url)

if __name__ == '__main__':
    main()
