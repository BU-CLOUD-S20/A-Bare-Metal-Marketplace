import click
import requests
import json

market_url  = 'http://206.189.232.188:5000'
account_url = 'http://206.189.232.188:5001'
project_id  = 'deadbeef-abcd-0000-aaaa-deadbeef1234'

def get(path, sendData):
    response = requests.get(market_url+path, json=sendData)
    json_list = response.json()
    return json.dumps(json_list, indent=2)


@click.group()
def cli():
    pass

@cli.command()
@click.option('--quantity', default = 1)
@click.option('--expire', default = "2020:6:1:0:0")
@click.option('--memory-gb', default = 1)
@click.option('--cpu-arch', default = 'x86-64')
@click.option('--cpu-count', default = 1)
@click.option('--core-count', default = 1)
@click.option('--cpu-ghz', default = 2)
@click.argument('start_time')
@click.argument('end_time')
@click.argument('cost')
def add_bid(quantity, expire, memory_gb, cpu_arch, cpu_count, core_count, cpu_ghz, start_time, end_time, cost):
    expire_time = start_time
    if expire != "0:0:0:0:0":
        expire_time = expire
    
    sendData = {
        'project_id': project_id, 
        'quantity':   quantity,
        'start_time': [int(i) for i in start_time.split(':')],
        'end_time': [int(i) for i in end_time.split(':')],
        'expire_time': [int(i) for i in expire_time.split(':')],
        'config_query': {'memory_gb': memory_gb, 'cpu_arch': cpu_arch, 'cpu_physical_count': cpu_count, 'cpu_core_count': core_count, 'cpu_ghz': cpu_ghz},
        'cost': cost,
    }

    #jsonData = json.dumps(sendDict)

    path = '/user_add_bid'
    response = requests.post(market_url+path, json=sendData)
    
    click.echo('Sent Bid')
    click.echo(response)

@cli.command()
def get_bids():
    path = '/user_get_bids'

    sendData = {'project_id': project_id}

    bids = get(path, sendData)
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