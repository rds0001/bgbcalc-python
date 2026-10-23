<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## reiseleistungsarten_mindestzahl

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anzahl_verschiedener_reiseleistungsarten`: Nichtnegative ganze Zahl rechtlich verschiedener Reiseleistungsarten derselben Reise nach651aIII; keine bloße Anzahl einzelner Leistungserbringer.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Zahl rechtlich verschiedener Reiseleistungsarten mit mindestens zwei vergleichen.

wert enthält mindestzahl, fehlende_arten, mindestzahl_erreicht. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur numerische Mindestzahl651aII/651bI; rechtlich verschiedene Arten nach651aIII für dieselbe Reise vorqualifizieren. Mehrere Hotels sind nicht automatisch mehrere Arten. Wesensmäßige Bestandteile anderer Leistungen nicht doppelt zählen. Weitere Voraussetzungen, touristische Nebenleistungsgrenzen und Ausnahmen separat; Ergebnis ist keine abschließende Pauschalreiseentscheidung.

Nichtnegative exakte Eingaben; bei Wertanteil positiver Gesamtwert. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651a_T0001, BGB_651a_T0002, BGB_651a_T0003, BGB_651a_T0004, BGB_651a_T0005, BGB_651a_T0006, BGB_651a_T0007, BGB_651a_T0008, BGB_651a_T0009, BGB_651a_T0010, BGB_651a_T0011, BGB_651a_T0012, BGB_651a_T0013, BGB_651a_T0014, BGB_651a_T0015, BGB_651a_T0016, BGB_651a_T0017, BGB_651a_T0018, BGB_651a_T0019, BGB_651a_T0020, BGB_651a_T0021, BGB_651a_T0022, BGB_651a_T0023, BGB_651b_T0001, BGB_651b_T0002, BGB_651b_T0003, BGB_651b_T0004, BGB_651b_T0005, BGB_651b_T0006, BGB_651b_T0007

```python
from bgbcalc import reiseleistungsarten_mindestzahl
reiseleistungsarten_mindestzahl(
    anzahl_verschiedener_reiseleistungsarten=0,
    einordnungsnachweis='Nur numerische Mindestzahl651aII/651bI; rechtlich verschiedene Arten nach651aIII für dieselbe Reise vorqualifizieren. Mehrere Hotels sind nicht automatisch mehrere Arten. Wesensmäßige Bestandteile anderer Leistungen nicht doppelt zählen. Weitere Voraussetzungen, touristische Nebenleistungsgrenzen und Ausnahmen separat; Ergebnis ist keine abschließende Pauschalreiseentscheidung.',
)
```

## tagesreise_reisepreisgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reisepreis`: Nichtnegativer qualifizierter Gesamtpreis der betrachteten Reise in EUR.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Reisepreis einschließlich Gleichheit mit500EUR vergleichen und Überschreitungsbetrag berechnen.

wert enthält preisgrenze_euro, preisgrenze_eingehalten, ueberschreitungsbetrag. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur Preisgrenze651aV2, nicht gesamte Tagesreiseausnahme. Reisedauer strikt unter24Stunden und keine Übernachtung zusätzlich qualifizieren. Im besonderen651cIII-Fall ist die Tagesreiseausnahme unabhängig vom Preis anzuwenden; dort keinen500EUR-Filter erfinden.

Nichtnegative exakte Eingaben; bei Wertanteil positiver Gesamtwert. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651a_T0001, BGB_651a_T0002, BGB_651a_T0003, BGB_651a_T0004, BGB_651a_T0005, BGB_651a_T0006, BGB_651a_T0007, BGB_651a_T0008, BGB_651a_T0009, BGB_651a_T0010, BGB_651a_T0011, BGB_651a_T0012, BGB_651a_T0013, BGB_651a_T0014, BGB_651a_T0015, BGB_651a_T0016, BGB_651a_T0017, BGB_651a_T0018, BGB_651a_T0019, BGB_651a_T0020, BGB_651a_T0021, BGB_651a_T0022, BGB_651a_T0023, BGB_651c_T0006

```python
from bgbcalc import tagesreise_reisepreisgrenze
tagesreise_reisepreisgrenze(
    reisepreis='0',
    einordnungsnachweis='Nur Preisgrenze651aV2, nicht gesamte Tagesreiseausnahme. Reisedauer strikt unter24Stunden und keine Übernachtung zusätzlich qualifizieren. Im besonderen651cIII-Fall ist die Tagesreiseausnahme unabhängig vom Preis anzuwenden; dort keinen500EUR-Filter erfinden.',
)
```

## touristische_leistung_wertanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `touristischer_teilwert`: Nichtnegativer qualifizierter EUR-Wert der zusätzlichen touristischen Leistungen, höchstens Gesamtwert.
- `gesamtwert_zusammenstellung`: Strikt positiver qualifizierter EUR-Gesamtwert derselben Zusammenstellung auf konsistenter Bewertungsbasis.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Touristischen Teilwert durch positiven Gesamtwert teilen; Anteil strikt mit25Prozent vergleichen.

wert enthält wertanteil, wertanteil_prozent, unter_25_prozent. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

§651aIV: nur rechnerischer touristischer Wertanteil in einer qualifizierten Zusammenstellung aus einer Art651aIII1bis3 und zusätzlichen touristischen Leistungen. Genau25Prozent ist nicht weniger als25Prozent. Teil-/Gesamtwerte derselben Bewertungsbasis, Gesamtwert strikt positiv, Teilwert höchstens Gesamtwert. Wesentliches Merkmal/Bewerbung sowie spätere Auswahl bleiben gesondert; ein kleiner Anteil allein schließt Pauschalreiserecht nicht aus. Keine automatische Bewertung aus unbekannten Einzelpreisen.

Nichtnegative exakte Eingaben; bei Wertanteil positiver Gesamtwert. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651a_T0001, BGB_651a_T0002, BGB_651a_T0003, BGB_651a_T0004, BGB_651a_T0005, BGB_651a_T0006, BGB_651a_T0007, BGB_651a_T0008, BGB_651a_T0009, BGB_651a_T0010, BGB_651a_T0011, BGB_651a_T0012, BGB_651a_T0013, BGB_651a_T0014, BGB_651a_T0015, BGB_651a_T0016, BGB_651a_T0017, BGB_651a_T0018, BGB_651a_T0019, BGB_651a_T0020, BGB_651a_T0021, BGB_651a_T0022, BGB_651a_T0023

```python
from bgbcalc import touristische_leistung_wertanteil
touristische_leistung_wertanteil(
    touristischer_teilwert='24.99',
    gesamtwert_zusammenstellung='100',
    einordnungsnachweis='§651aIV: nur rechnerischer touristischer Wertanteil in einer qualifizierten Zusammenstellung aus einer Art651aIII1bis3 und zusätzlichen touristischen Leistungen. Genau25Prozent ist nicht weniger als25Prozent. Teil-/Gesamtwerte derselben Bewertungsbasis, Gesamtwert strikt positiv, Teilwert höchstens Gesamtwert. Wesentliches Merkmal/Bewerbung sowie spätere Auswahl bleiben gesondert; ein kleiner Anteil allein schließt Pauschalreiserecht nicht aus. Keine automatische Bewertung aus unbekannten Einzelpreisen.',
)
```
