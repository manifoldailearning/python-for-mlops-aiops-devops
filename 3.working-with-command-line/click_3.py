import click

@click.command()
@click.argument("number", type=int) # requires an integer argument
@click.option('--repeat', default=1, help='Number of times to repeat') 
def repeat_output(number,repeat):
    for _ in range(repeat):
        click.echo(f"Number is : {number}!")

if __name__ == '__main__':
    repeat_output()  # Call the command