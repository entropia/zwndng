import typer
from typing_extensions import Annotated
from pathlib import Path
from sys import stdin
from zwndng.state import ctx, Config
from zwndng import data
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
):
    """
    Generieren von Zuwendungsbestätigungen für gemeinnützige Vereine.
    """
    ctx.input = (stdin if input == Path("-") else open(input)).read()
    ctx.config = Config.from_yaml_file(config)

    print(ctx)

    print(data.sach_pdf_path().is_file())
    print(data.geld_pdf_path().is_file())
    print(data.sammel_pdf_path().is_file())


@app.command()
def sach():
    """
    Generieren von Bestätigungen über Sachzuwendungen für gemeinnützige Vereine.
    """
    sachzuwendung = Sachzuwendung.from_json(ctx.input)
    print(sachzuwendung)


@app.command()
def geld():
    """
    Generieren von Bestätigungen über Geldzuwendungen für gemeinnützige Vereine.
    """
    geldzuwendung = Geldzuwendung.from_json(ctx.input)
    print(geldzuwendung)


@app.command()
def sammel():
    """
    Generieren von Sammelbestätigungen über Geldzuwendungen für gemeinnützige Vereine.
    """
    sammelzuwendung = Sammelzuwendung.from_json(ctx.input)
    print(sammelzuwendung)
