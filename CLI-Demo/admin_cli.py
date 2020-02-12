import click
import cla

@click.group()
def main():
    """
    Simple CLI for interfacing the Bare Metal Marketplace
    """
    pass

@main.command()
def list_nodes():
    """This outputs a list of nodes that you currently own or are renting"""
    click.echo("Here is a list of your nodes:")
    click.echo("Node A, Status: In Use")
    click.echo("Node B, Status: In Use")
    click.echo("Node C, Status: In Use")
    click.echo("Node D, Status: In Use")
    click.echo("Node E, Status: In Use")

@main.command()
def get_node():
    """This interactive CLI provides more specific information about a node."""
    cla.get_node()
    
@main.command()
@click.argument('user')
def get_user(user):
    """This returns user permissions at + below administrative level"""
    click.echo(user)
    click.echo("This is user!")


if __name__ == "__main__":
    main()