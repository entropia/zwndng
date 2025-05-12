from pathlib import Path

from dataclass_wizard import YAMLWizard
from dataclasses import dataclass
from typing import Optional, TextIO


@dataclass
class Config(YAMLWizard, key_transform="SNAKE"):
    vereinsname: str
    adresse: str
    steuernummer: str
    finanzamt: str
    datum_freistellung: str
    veranlagungszeitraum: str
    vereinszweck: str
    ort: str
    unterschrift_bild: Path


@dataclass
class ZwndngContext:
    input: Optional[Path | TextIO] = None
    config: Optional[Config] = None
    output: Optional[Path] = None


ctx = ZwndngContext()
