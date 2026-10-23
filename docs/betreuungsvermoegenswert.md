<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betreuung_vermoegenswert_ohne_immobilien

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vermoegenspositionen`: Liste1..10000 qualifizierter Vermögenspositionen, je genau wert (nichtnegative exakte EUR-Zahl) und immobilie (echter Wahrheitswert). Anteilige Berechtigung bewertet, keine verborgene Verbindlichkeitsverrechnung im Wert; kein Vermögen als einzelne Nullposition.
- `verbindlichkeiten`: Nichtnegative dokumentierte Verbindlichkeiten in EUR. Werden validiert, aber nach§1860I gerade nicht abgezogen.
- `bewertungsnachweis`: Nichtleerer Nachweis von Stichtag, vollständiger Positionszuordnung, Immobilienqualifikation und Werten ohne unzulässige Vorab-Schuldenverrechnung.

Nichtimmobilienwerte summieren, Immobilienwerte separat ausweisen; Verbindlichkeiten nicht abziehen.

wert enthält anzusetzender_vermoegenswert und nicht_beruecksichtigter_immobilienwert als exakte EUR-Brüche. Kein Befreiungsstatus.

§1860I schreibt Berechnung ohne Immobilien und Verbindlichkeiten vor. Positionen und Werte zum maßgeblichen Stichtag rechtlich qualifiziert, anteilige Berechtigungen bereits bewertet. Wert einer Nichtimmobilienposition nicht vorher um separat zu berücksichtigende Verbindlichkeiten vermindern; sonst würde der gesetzlich ausgeschlossene Schuldenabzug verdeckt nachgeholt. Verbindlichkeiten werden als nichtnegative dokumentierte Eingabe validiert und bewusst nicht abgezogen. Immobilienzuordnung ist Nutzervorgabe, keine automatische Objektklassifikation. Kein Vermögen als einzelne Nullposition angeben. Die6000EUR-Schwelle, Antrag, richterliches Ermessen, Gefährdung und sonstige Befreiungswege werden nicht als eigenständige Befreiungsentscheidung berechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1860_T0001

```python
from bgbcalc import betreuung_vermoegenswert_ohne_immobilien
betreuung_vermoegenswert_ohne_immobilien(
    vermoegenspositionen=[{'wert': '4000', 'immobilie': False}, {'wert': '2000', 'immobilie': False}, {'wert': '1000000', 'immobilie': True}],
    verbindlichkeiten='10000',
    bewertungsnachweis='Vollständige qualifizierte Positionen zum maßgeblichen Stichtag, keine Verbindlichkeiten vorab abgezogen.',
)
```
