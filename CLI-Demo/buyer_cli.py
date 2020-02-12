import click
import cla

@click.group()
def main():
    """
    Bare Metal Marketplace CLI for Renting Tenant.
    """
    pass

@main.command()
def rent_node():
    """
    Rent a node with your specifications and prices
    """
    cla.rent_node()

if __name__ == "__main__":
    main()