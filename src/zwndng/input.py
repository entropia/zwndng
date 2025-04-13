from dataclasses import dataclass
from dataclass_wizard import JSONWizard, Pattern
from datetime import date
from typing import Annotated


@dataclass
class Spender:
    name: str
    address: str


@dataclass
class Geld:
    datum: Annotated[date, Pattern("%y-%m-%d")]
    art: str
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


@dataclass
class Sachzuwendung(JSONWizard, key_case="SNAKE"):
    sache: Sache
    spender: Spender
