from dataclass_wizard import YAMLWizard
from dataclasses import dataclass
from typing import Optional


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


@dataclass
class ZwndngContext:
    input: Optional[str] = None
    config: Optional[Config] = None


ctx = ZwndngContext()
