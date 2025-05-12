from dataclasses import dataclass
from dataclass_wizard import JSONWizard, Pattern
from datetime import date
from typing import Annotated, Literal


@dataclass
class Spender:
    name: str
    adresse: str


@dataclass
class Geld:
    datum: Annotated[date, Pattern("%y-%m-%d")]
    art: Literal["Geldzuwendung", "Mitgliedsbeitrag"]
    verzicht: bool
    betrag: float


@dataclass
class Geldzuwendung(JSONWizard, key_case="SNAKE"):
    geld: Geld
    spender: Spender


@dataclass
class Sammelzuwendung(JSONWizard, key_case="SNAKE"):
    geld: list[Geld]
    zeitraum_beginn: Annotated[date, Pattern("%y-%m-%d")]
    zeitraum_ende: Annotated[date, Pattern("%y-%m-%d")]
    spender: Spender


@dataclass
class Sache:
    datum: Annotated[date, Pattern("%y-%m-%d")]
    wert: float
    wertermittlung: bool
    privatvermögen: bool
    betriebsvermögen: bool
    beschreibung: str


@dataclass
class Sachzuwendung(JSONWizard, key_case="SNAKE"):
    sache: Sache
    spender: Spender
