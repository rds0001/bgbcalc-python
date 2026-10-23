<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gemeinschaftsquoten_aufloesen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gemeinschaftlicher_anteil`: Positive bereits rechtlich bestimmte exakte Oberquote höchstens1, bezogen auf ganze Erbschaft/vermachten Gegenstand.
- `gruppenmitglieder`: Rekursive Liste je2..1000 Mitglieder, insgesamt höchstens1000 Knoten und20 Ebenen. Je Objekt genau knoten_id (global eindeutige nichtleere Kennung), bestimmter_anteil (positive Quote≤1 relativ zur unmittelbaren Gruppe oder NULL für testamentarisch unbestimmt), untergruppe (NULL für Person oder weitere vollständige Mitgliederliste).
- `regelkontext`: gemeinschaftlicher_erbteil_2093 oder gemeinschaftliches_vermaechtnis_2157;2157 mehrere Bedachte desselben Gegenstands.
- `gruppeneinsetzung_qualifiziert`: Pflichtwahrheitswert zu rechtlich qualifizierter vollständiger gemeinschaftlicher Einsetzung und anwendbaren2089–2092-Regeln; FALSE NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis der Oberquote, Gruppenstruktur und relativen Binnenquoten.

In jeder vollständigen Gruppe vorhandenen testament_erbquoten-Kern mit Normalisierung auf gesamte Gruppenquote anwenden; Binnenquote rekursiv mit Oberquote multiplizieren.

wert.aufgeloeste_anteile enthält person_id und exakten Gesamtbruch anteil für sämtliche Blätter.

Keine Wegfall-/Anwachsungs-/Ersatzerbautomatik, kein zusätzlicher gesetzlicher Rest innerhalb vollständig bestimmter Gruppe. Gleiche Person in mehreren Zweigen außerhalb Modell; separate Anteilstitel gesondert rechnen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2093_T0001, BGB_2157_T0001

```python
from bgbcalc import gemeinschaftsquoten_aufloesen
gemeinschaftsquoten_aufloesen(
    gemeinschaftlicher_anteil='0.5',
    gruppenmitglieder=[{'knoten_id': 'A', 'bestimmter_anteil': None, 'untergruppe': None}, {'knoten_id': 'B', 'bestimmter_anteil': None, 'untergruppe': None}],
    regelkontext='gemeinschaftlicher_erbteil_2093',
    gruppeneinsetzung_qualifiziert=True,
    einordnungsnachweis='Synthetisch qualifizierte vollständige Gruppe.',
)
```
