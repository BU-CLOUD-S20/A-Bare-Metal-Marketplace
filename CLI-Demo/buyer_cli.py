import click

@click.group()
def main():
    """
    Simple CLI for interfacing the Bare Metal Marketplace
    """
    pass

@main.command()
def list_users():
    """This searches users at + below administrative level"""
    click.echo("List of users")


@main.command()
@click.argument('user')
def get_user(user):
    """This returns user permissions at + below administrative level"""
    click.echo(user)
    click.echo("This is user!")


if __name__ == "__main__":
    main()