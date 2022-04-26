import typer


main = typer.Typer(help="Beer Management App")

@main.command("add")
def add(name: str, style: str):
    """ Add a new beer to database
    """
    print(name, style)

@main.command("list")
def list_beer(style: str):
    """ List beers from database
    """
    print(style)