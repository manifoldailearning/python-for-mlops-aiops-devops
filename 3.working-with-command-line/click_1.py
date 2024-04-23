import click

@click.command()
def hello():
    click.echo("Hello, World!")

if __name__ == '__main__':
    hello()  # Call the command