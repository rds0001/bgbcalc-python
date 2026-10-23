<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## geldschulden_nach_bestimmung_oder_rang_tilgen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `zahlung`: Zur Tilgung gleichartiger Geldschulden verfügbarer Betrag in Euro.
- `schulden`: Liste1..1000 mit genau schuld_id, offener_betrag(positivEUR), faellig(Wahrheitswert), sicherheitsrang, laestigkeitsrang, altersrang(positive ganze Zahlen). Niedriger Rang: geringere Sicherheit, größere Lästigkeit, älter. Auch noch nicht fällige Schulden müssen erfüllbar sein.
- `bestimmte_schuld_id`: Nichtleere Kennung bei rechtlich wirksamer eindeutiger Bestimmung genau einer Schuld nach366I;NULL bedeutet festgestellt keine Bestimmung und Anwendung366II. Andere Bestimmungsmodelle separat.
- `einordnungsnachweis`: Nichtleerer Nachweis366-Anwendung, gleicher Schuldner/Gläubiger, gleichartiger erfüllbarer Geldschulden, wirksamer Bestimmung oder gesetzlicher Rangmerkmale. Keine vorrangige Spezialregel.

Eindeutige Tilgungsbestimmung ausführen oder gesetzliche Fälligkeits-/Sicherheits-/Lästigkeits-/Altersgruppen proportional bedienen.

wert.zuordnungen in Eingabereihenfolge mit schuld_id, tilgungsbetrag und restschuld; nicht_zugeordnet. Beträge als exakte Eurobrüche.

§366I/II: bei qualifizierter eindeutiger Tilgungsbestimmung nur bestimmte Schuld bedienen; Überschuss bleibt unzugeordnet, keine erfundene weitere Schuldnerbestimmung. Ohne Bestimmung fällige vor nicht fälligen Schulden, dann geringere Sicherheit, größere Lästigkeit, höheres Alter; bei vollständigem Gleichrang verhältnismäßig nach offenen Beträgen. Nicht fällige Forderungen müssen vorzeitig erfüllbar sein. Qualifizierte Rangwerte sind keine automatisch bewertete Sicherheit/Lästigkeit. Mehrfachbestimmungen, Gläubiger-/Parteivereinbarungen und Spezialregeln gesondert. Innerhalb jeder Schuld Kosten/Zinsen/Hauptforderung367 separat; keine automatische Erstattung des unzugeordneten Betrags.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_366_T0001, BGB_366_T0002

```python
from bgbcalc import geldschulden_nach_bestimmung_oder_rang_tilgen
geldschulden_nach_bestimmung_oder_rang_tilgen(
    zahlung='60',
    schulden=[{'schuld_id': 'A', 'offener_betrag': '100', 'faellig': True, 'sicherheitsrang': 9, 'laestigkeitsrang': 9, 'altersrang': 9}, {'schuld_id': 'B', 'offener_betrag': '100', 'faellig': False, 'sicherheitsrang': 1, 'laestigkeitsrang': 1, 'altersrang': 1}],
    bestimmte_schuld_id=None,
    einordnungsnachweis='§366I/II: bei qualifizierter eindeutiger Tilgungsbestimmung nur bestimmte Schuld bedienen; Überschuss bleibt unzugeordnet, keine erfundene weitere Schuldnerbestimmung. Ohne Bestimmung fällige vor nicht fälligen Schulden, dann geringere Sicherheit, größere Lästigkeit, höheres Alter; bei vollständigem Gleichrang verhältnismäßig nach offenen Beträgen. Nicht fällige Forderungen müssen vorzeitig erfüllbar sein. Qualifizierte Rangwerte sind keine automatisch bewertete Sicherheit/Lästigkeit. Mehrfachbestimmungen, Gläubiger-/Parteivereinbarungen und Spezialregeln gesondert. Innerhalb jeder Schuld Kosten/Zinsen/Hauptforderung367 separat; keine automatische Erstattung des unzugeordneten Betrags.',
)
```
