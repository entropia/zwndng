import fitz

from babel.numbers import format_currency
from num2words import num2words

from zwndng.data import *
from zwndng.state import ctx

FONT_SIZE = 8
FONT_COLOR = (0, 0, 0)

# Convert millimeters to points
mm: float = 72 / 25.4


def today() -> str:
    from datetime import datetime

    return datetime.now().strftime("%d.%m.%Y")


def today_file() -> str:
    from datetime import datetime

    return datetime.now().strftime("%Y_%m_%d")


def betragstext(betrag: float) -> str:
    """
    Gibt einen Geldbetrag nach DIN 5008 als ausgeschriebene Textrepräsentation zurück.
    Beispiel: 1000.45 → "eintausend Euro und fünfundvierzig Cent"
    """
    euro = int(betrag)
    cent = int(round((betrag - euro) * 100))

    euro_text = num2words(euro, lang="de")
    if cent > 0:
        cent_text = num2words(cent, lang="de")
        return f"{euro_text} Euro und {cent_text} Cent"
    else:
        return f"{euro_text} Euro"


def add_font(page: fitz.Page) -> None:
    page.insert_font(fontname="FiraSans", fontfile=fira_regular_path())
    page.insert_font(fontname="FiraSans-Bold", fontfile=fira_bold_path())
    page.insert_font(fontname="FiraSans-Italic", fontfile=fira_italic_path())


def add_common_data(page: fitz.Page) -> None:
    add_font(page)

    page.insert_text(
        (17 * mm, 21 * mm),
        "\n".join([ctx.config.vereinsname, ctx.config.adresse]),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
