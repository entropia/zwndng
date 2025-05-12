from os import makedirs

import typer
from typing_extensions import Annotated
from pathlib import Path
from sys import stdin
from zwndng import render
from zwndng.state import ctx, Config
from zwndng.input import Sachzuwendung, Geldzuwendung, Sammelzuwendung

app = typer.Typer()

APP_NAME = "zwndng"


@app.callback()
def main(
    input: Annotated[
        Path,
        typer.Option(
            help="Pfad zur Datei aus der der JSON input gelesen werden soll, '-' für stdin"
        ),
    ] = "-",
    config: Annotated[Path, typer.Option(help="Pfad zur Konfigurationsdatei")] = Path(
        typer.get_app_dir(APP_NAME)
    )
    / "config.yml",
    output: Annotated[
        Path,
        typer.Option(
            help="Pfad zum Ordner wo die Zuwendungsbescheinigungen abgelegt werden sollen"
        ),
    ] = "output",
):
    """
    Generieren von Zuwendungsbestätigungen für gemeinnützige Vereine.
    """
    ctx.input = (stdin if input == Path("-") else open(input)).read()
    ctx.config = Config.from_yaml_file(config)
    ctx.output = output

    makedirs(ctx.output, exist_ok=True)


@app.command()
def sach():
    """
    Generieren von Bestätigungen über Sachzuwendungen für gemeinnützige Vereine.
    """
    sachzuwendung = Sachzuwendung.from_json(ctx.input)
    render.sachzuwendung(sachzuwendung)


@app.command()
def geld():
    """
    Generieren von Bestätigungen über Geldzuwendungen für gemeinnützige Vereine.
    """
    geldzuwendung = Geldzuwendung.from_json(ctx.input)
    render.geldzuwendung(geldzuwendung)


@app.command()
def sammel():
    """
    Generieren von Sammelbestätigungen über Geldzuwendungen für gemeinnützige Vereine.
    """
    sammelzuwendung = Sammelzuwendung.from_json(ctx.input)
    render.sammelzuwendung(sammelzuwendung)
