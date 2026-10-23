<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_beschlagnahme_monatsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beschlagnahme_am`: ISO-Datum des im Parameternamen bezeichneten tatsächlichen Ereignisses.
- `einordnungsnachweis`: Nichtleerer Nachweis des passenden Normfalls; keine automatische Rechtsfolgenentscheidung.

§§1123II/1124II: Monatsende, nach dem15.Tag Ende des Folgemonats.

wert enthält die ausdrücklich benannten Kalendergrenzen; keine Zins- oder Haftungsbeträge.

Nur gesetzliche Kalendergrenze für vorqualifizierte Miet-/Pachtfälle.1123 erfordert zusätzlich Fälligkeit, Jahresablauf und Beschlagnahmebezug;1124 vorherige Verfügung. Diese Grenze allein entscheidet weder Haftungsfreiheit noch Wirksamkeit. Nicht auf1126 übertragen; dort gilt eine andere Dreimonatsregel.

Gültige ISO-Daten und Ergebnisse0001..9999,1171-Rechtskraftjahr mindestens0005.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1123_T0001, BGB_1123_T0002, BGB_1123_T0003, BGB_1124_T0001, BGB_1124_T0002, BGB_1124_T0003, BGB_1124_T0004

```python
from bgbcalc import hypothek_beschlagnahme_monatsgrenze
hypothek_beschlagnahme_monatsgrenze(
    beschlagnahme_am='2030-01-15',
    einordnungsnachweis='Qualifiziertes gesetzliches Bezugsereignis ohne Sonderkorrektur.',
)
```

## hypothek_hinterlegung_zeitgrenzen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausschliessungsbeschluss_rechtskraeftig_am`: ISO-Datum des im Parameternamen bezeichneten tatsächlichen Ereignisses.
- `einordnungsnachweis`: Nichtleerer Nachweis des passenden Normfalls; keine automatische Rechtsfolgenentscheidung.

§1171: Beginn des vierten vorangegangenen Kalenderjahres und30Jahre ab Rechtskraft.

wert enthält die ausdrücklich benannten Kalendergrenzen; keine Zins- oder Haftungsbeträge.

Zinsbeginn ist nur früheste zu berücksichtigende Kalendergrenze, kein erfundener Zinsanspruch; Grundbucheintrag des Zinssatzes, tatsächlicher Zinslauf und Höhe gesondert.30Jahre sind Grundfrist für hinterlegten Betrag, keine automatische Erlöschensentscheidung bei vorheriger Meldung. Keine Anwendung anderer Aufgebotsfristen ohne Normprüfung.

Gültige ISO-Daten und Ergebnisse0001..9999,1171-Rechtskraftjahr mindestens0005.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1171_T0001, BGB_1171_T0002, BGB_1171_T0003, BGB_1171_T0004, BGB_1171_T0005

```python
from bgbcalc import hypothek_hinterlegung_zeitgrenzen
hypothek_hinterlegung_zeitgrenzen(
    ausschliessungsbeschluss_rechtskraeftig_am='2030-07-15',
    einordnungsnachweis='Qualifiziertes gesetzliches Bezugsereignis ohne Sonderkorrektur.',
)
```
