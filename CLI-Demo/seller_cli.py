import click
import cla

@click.group()
def main():
    """
    Bare Metal Marketplace CLI for Selling Tenant.
    """
    pass

@main.command()
def sell_node():
    """
    Sell a node you own.
    """
    cla.sell_node()

if __name__ == "__main__":
    main()