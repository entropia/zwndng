from zwndng.input import Sachzuwendung, Geldzuwendung, Sammelzuwendung
from zwndng.util import *


def sachzuwendung(sachzuwendung: Sachzuwendung) -> None:
    document: fitz.Document = fitz.open(sach_pdf_path())
    page: fitz.Page = document[0]

    add_common_data(page)

    page.insert_text(
        (17 * mm, 56 * mm),
        "\n".join([sachzuwendung.spender.name, sachzuwendung.spender.adresse]),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    page.insert_text(
        (17 * mm, 76 * mm),
        format_currency(sachzuwendung.sache.wert, "EUR", locale="de_DE"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    page.insert_text(
        (63 * mm, 76 * mm),
        betragstext(sachzuwendung.sache.wert),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    # Zuwendungsdatum
    page.insert_text(
        (152 * mm, 76 * mm),
        sachzuwendung.sache.datum.strftime("%d.%m.%Y"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    # ToDo: Automatisch umbrechen wenn Zeilen zu lang sind
    # Bezeichnung der Sachzuwendung
    page.insert_text(
        (17 * mm, 88 * mm),
        sachzuwendung.sache.beschreibung,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    # Herkunft aus Betriebsvermögen
    if sachzuwendung.sache.betriebsvermögen and not sachzuwendung.sache.privatvermögen:
        page.insert_text(
            (21.7 * mm, 137 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )

    # Herkunft aus Privatvermögen
    if sachzuwendung.sache.privatvermögen and not sachzuwendung.sache.betriebsvermögen:
        page.insert_text(
            (21.7 * mm, 143 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )

    # Keine Herkunft
    if (
        not sachzuwendung.sache.privatvermögen
        and not sachzuwendung.sache.betriebsvermögen
    ):
        page.insert_text(
            (21.7 * mm, 148.6 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )

    # Geeignete Unterlagen zur Wertermittlung
    if sachzuwendung.sache.wertermittlung:
        page.insert_text(
            (21.7 * mm, 153.8 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )

    # Freistellung
    page.insert_text(
        (21.7 * mm, 159 * mm),
        "X",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    page.insert_text(
        (29.4 * mm, 167 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (29.2 * mm, 181 * mm),
        ctx.config.finanzamt,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (95 * mm, 181 * mm),
        ctx.config.steuernummer,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (140 * mm, 181 * mm),
        ctx.config.datum_freistellung,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (70 * mm, 186 * mm),
        ctx.config.veranlagungszeitraum,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # Bestätigung
    page.insert_text(
        (17 * mm, 235 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    page.insert_text(
        (17 * mm, 251 * mm),
        f"{ctx.config.ort}, {today()}",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # ToDo: Keep aspect ratio
    # img = fitz.Pixmap(ctx.config.unterschrift_bild)

    # Unterschrift
    width = 80
    height = 44.48

    page.insert_image(
        fitz.Rect(50 * mm, 243 * mm, 50 * mm + width, 243 * mm + height),
        filename=ctx.config.unterschrift_bild,
    )

    # Dokument speichern
    filename = sachzuwendung.spender.name.replace(" ", "_")
    document.save(ctx.output / f"{today_file()}_Sachzuwendung_{filename}.pdf")
    document.close()


def geldzuwendung(geldzuwendung: Geldzuwendung) -> None:
    document: fitz.Document = fitz.open(geld_pdf_path())
    page: fitz.Page = document[0]

    add_common_data(page)

    page.insert_text(
        (17 * mm, 58 * mm),
        "\n".join([geldzuwendung.spender.name, geldzuwendung.spender.adresse]),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    page.insert_text(
        (17 * mm, 82.5 * mm),
        format_currency(geldzuwendung.geld.betrag, "EUR", locale="de_DE"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    page.insert_text(
        (63 * mm, 82.5 * mm),
        betragstext(geldzuwendung.geld.betrag),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    page.insert_text(
        (152 * mm, 82.5 * mm),
        geldzuwendung.geld.datum.strftime("%d.%m.%Y"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    if geldzuwendung.geld.verzicht:
        page.insert_text(
            (120 * mm, 98 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )
    else:
        page.insert_text(
            (140 * mm, 98 * mm),
            "X",
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            fontname="FiraSans",
        )

    # Freistellung
    page.insert_text(
        (21.7 * mm, 109 * mm),
        "X",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    page.insert_text(
        (29.4 * mm, 122 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (29.2 * mm, 136 * mm),
        ctx.config.finanzamt,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (95 * mm, 136 * mm),
        ctx.config.steuernummer,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (140 * mm, 136 * mm),
        ctx.config.datum_freistellung,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    page.insert_text(
        (70 * mm, 141 * mm),
        ctx.config.veranlagungszeitraum,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # Bestätigung
    page.insert_text(
        (17 * mm, 200 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    page.insert_text(
        (17 * mm, 241 * mm),
        f"{ctx.config.ort}, {today()}",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # ToDo: Keep aspect ratio
    # img = fitz.Pixmap(ctx.config.unterschrift_bild)

    # Unterschrift
    width = 80
    height = 44.48

    page.insert_image(
        fitz.Rect(50 * mm, 233 * mm, 50 * mm + width, 233 * mm + height),
        filename=ctx.config.unterschrift_bild,
    )

    # Dokument speichern
    filename = geldzuwendung.spender.name.replace(" ", "_")
    document.save(ctx.output / f"{today_file()}_Geldzuwendung_{filename}.pdf")
    document.close()


def sammelzuwendung(sammelzuwendung: Sammelzuwendung) -> None:
    document: fitz.Document = fitz.open(sammel_pdf_path())
    summary_page: fitz.Page = document[0]

    add_common_data(summary_page)

    summary_page.insert_text(
        (17 * mm, 54 * mm),
        "\n".join([sammelzuwendung.spender.name, sammelzuwendung.spender.adresse]),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    # Freistellung
    summary_page.insert_text(
        (21.7 * mm, 85 * mm),
        "X",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    summary_page.insert_text(
        (29.4 * mm, 97 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    summary_page.insert_text(
        (29.2 * mm, 111 * mm),
        ctx.config.finanzamt,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    summary_page.insert_text(
        (95 * mm, 111 * mm),
        ctx.config.steuernummer,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    summary_page.insert_text(
        (140 * mm, 111 * mm),
        ctx.config.datum_freistellung,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )
    summary_page.insert_text(
        (70 * mm, 116 * mm),
        ctx.config.veranlagungszeitraum,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # Bestätigung
    summary_page.insert_text(
        (17 * mm, 171 * mm),
        ctx.config.vereinszweck,
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    summary_page.insert_text(
        (17 * mm, 238 * mm),
        f"{ctx.config.ort}, {today()}",
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans-Bold",
    )

    # Einzelspenden
    detail_page: fitz.Page = document[1]
    add_font(detail_page)
    gesamtsumme: float = 0

    # ToDo: Skript um mehrere Seiten mit Einzelspenden erweitern.
    if len(sammelzuwendung.geld) > 28:
        raise IndexError("Zu viele Einzelspenden.")

    for i, spende in enumerate(sammelzuwendung.geld):
        detail_page.insert_text(
            (25 * mm, (37 + 8 * i) * mm),
            spende.datum.strftime("%d.%m.%Y"),
            fontsize=FONT_SIZE + 1,
            color=FONT_COLOR,
            fontname="FiraSans",
        )
        detail_page.insert_text(
            (70 * mm, (37 + 8 * i) * mm),
            spende.art,
            fontsize=FONT_SIZE + 1,
            color=FONT_COLOR,
            fontname="FiraSans",
        )
        detail_page.insert_text(
            (115 * mm, (37 + 8 * i) * mm),
            "ja" if spende.verzicht else "nein",
            fontsize=FONT_SIZE + 1,
            color=FONT_COLOR,
            fontname="FiraSans",
        )
        detail_page.insert_text(
            (160 * mm, (37 + 8 * i) * mm),
            format_currency(spende.betrag, "EUR", locale="de_DE"),
            fontsize=FONT_SIZE + 1,
            color=FONT_COLOR,
            fontname="FiraSans",
        )
        gesamtsumme += spende.betrag

    # Zusammenfassung
    detail_page.insert_text(
        (160 * mm, 263 * mm),
        format_currency(gesamtsumme, "EUR", locale="de_DE").replace("€", ""),
        fontsize=FONT_SIZE + 1,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    summary_page.insert_text(
        (17 * mm, 75.5 * mm),
        format_currency(gesamtsumme, "EUR", locale="de_DE").replace("€", ""),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    summary_page.insert_text(
        (72 * mm, 75.5 * mm),
        betragstext(gesamtsumme),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    summary_page.insert_text(
        (154 * mm, 75.5 * mm),
        sammelzuwendung.zeitraum_beginn.strftime("%d.%m.%Y"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )
    summary_page.insert_text(
        (175 * mm, 75.5 * mm),
        sammelzuwendung.zeitraum_ende.strftime("%d.%m.%Y"),
        fontsize=FONT_SIZE,
        color=FONT_COLOR,
        fontname="FiraSans",
    )

    # ToDo: Keep aspect ratio
    # img = fitz.Pixmap(ctx.config.unterschrift_bild)

    # Unterschrift
    width = 80
    height = 44.48

    summary_page.insert_image(
        fitz.Rect(50 * mm, 230 * mm, 50 * mm + width, 230 * mm + height),
        filename=ctx.config.unterschrift_bild,
    )

    # Dokument speichern
    filename = sammelzuwendung.spender.name.replace(" ", "_")
    document.save(ctx.output / f"{today_file()}_Sammelzuwendung_{filename}.pdf")
    document.close()
