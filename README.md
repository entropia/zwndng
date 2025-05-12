# zwndng: Kommandozeilenprogramm zur Generierung von Zuwendungsbestätigungen

## Übersicht

**zwndng** ist ein Kommandozeilenprogramm zur Erstellung von Zuwendungsbestätigungen für gemeinnützige Vereine. Es unterstützt die Erstellung von:

- Bestätigungen über Geldzuwendungen
- Bestätigungen über Sachzuwendungen
- Sammelbestätigungen über Geldzuwendungen und Mitgliedsbeiträge

## Installation

```bash
pipx install git+https://github.com/entropia/zwndng.git
```

## Konfiguration

### Konfigurationsdatei

Im Standardpfad `~/.config/zwndng/config.yml` muss eine Konfigurationsdatei existieren. Beispiel:

```yaml
vereinsname: Entropia e.V.
adresse: |
  Steinstr. 23
  76133 Karlsruhe
steuernummer: 35022/25566
finanzamt: Karlsruhe-Stadt
datum_freistellung: 21.02.2023
veranlagungszeitraum: 2019-2021
vereinszweck: >
  der Erziehung, Volks- und Berufsbildung einschließlich der Studentenhilfe,
  Wissenschaft und Forschung, Kunst und Kultur
ort: Karlsruhe
unterschrift_bild: /home/user/.local/share/zwndng/unterschrift.png
```

## Verwendung

```bash
zwndng --help
```

## Eingabeformate

### Geldzuwendung

```json geldzuwendung.json
{
  "geld": {
    "datum": "2025-02-23",
    "art": "Geldzuwendung",
    "betrag": 42.23,
    "verzicht": false
  },
  "spender": {
    "name": "Max Mustermann",
    "adresse": "Platz der Republik 1\n10557 Berlin"
  }
}
```

### Sachzuwendung

```json sachzuwendung.json
{
  "sache": {
    "beschreibung": "Ein Eis",
    "datum": "2025-01-01",
    "wert": 420.69,
    "wertermittlung": true,
    "privatvermögen": true,
    "betriebsvermögen": false
  },
  "spender": {
    "name": "Max Mustermann",
    "adresse": "Platz der Republik 1\n10557 Berlin"
  }
}
```

### Sammelzuwendung

```json sammelzuwendung.json
{
  "zeitraum_beginn": "2024-01-01",
  "zeitraum_ende": "2024-12-31",
  "spender": {
    "name": "Max Mustermann",
    "adresse": "Platz der Republik 1\n10557 Berlin"
  },
  "geld": [
    {
      "datum": "2024-02-23",
      "art": "Geldzuwendung",
      "betrag": 23.42,
      "verzicht": false
    },
    {
      "datum": "2024-04-01",
      "art": "Mitgliedsbeitrag",
      "betrag": 0.02,
      "verzicht": false
    }
  ]
}
```
