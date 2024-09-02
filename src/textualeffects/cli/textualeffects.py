from importlib import metadata

import typer

from textualeffects.app import app

cli = typer.Typer()


@cli.command()
def textualeffects(
    version: bool = typer.Option(None, "--version", "-v"),
):

    if version:
        typer.echo(f"textualeffects v{metadata.version('textualeffects')}")
        exit(0)
    app.run()


if __name__ == "__main__":
    cli()
