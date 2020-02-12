import click
import cla

@click.group()
def main():
    """
    Operator CLI for the Bare Metal Marketplace.
    """
    pass

@main.command()
def add_credits():
    """Add credits to any organization."""
    cla.add_credits()


@main.command()
def remove_credits():
    """Remvoe credits from any organization."""
    cla.remove_credits()
if __name__ == "__main__":
    main()