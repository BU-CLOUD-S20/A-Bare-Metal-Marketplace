import click
import requests
import json

market_url = 'http://206.189.232.188:5000'
project_id = 'deadbeef-abcd-0000-aaaa-deadbeef1234'

def get(path, parameters):
    response = requests.get(market_url+path, params=parameters)
    json_list = response.json()
    return json.dumps(json_list, indent=2)


@click.group()
def cli():
    pass

@cli.command()
def add_bid():
    click.echo('Added Bid')

@cli.command()
def get_bids():
    path = '/get_bids'
    bids = get(path, {})
    click.echo('Here are your bids:')
    click.echo(bids)


@cli.command()
def add_offer():
    click.echo('Added Offer')

@cli.command()
def get_offers():
    click.echo('Here are your offers:')



#@click.command()
#@click.option('--count', default=1, help='number of greetings')
#@click.argument('name')
#def cli(count, name):
#    for x in range(count):
#       click.echo('Hello %s!' % name)

if __name__ == '__main__':
    cli()