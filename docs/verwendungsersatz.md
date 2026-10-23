<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## besitzer_landwirtschaftlicher_verwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ordnungsgemaesse_fruchtkosten`: Nichtnegative Kosten in EUR der konkret betrachteten noch ungetrennten Früchte, soweit ordnungsmäßiger Wirtschaft entsprechend; keine erfundene Kürzungsquote.
- `wert_noch_ungetrennter_fruechte`: Nichtnegativer Wert in EUR derselben noch ungetrennten Früchte. Keine automatische Gleichsetzung mit prognostiziertem Umsatz.
- `landwirtschaftliches_grundstueck_herauszugeben`: Wahrheitswert: landwirtschaftliches Grundstück ist herauszugeben.
- `fruechte_noch_ungetrennt`: Wahrheitswert: die betrachteten Früchte sind noch nicht getrennt.
- `trennung_vor_wirtschaftsjahresende_ordnungsgemaess`: Wahrheitswert: Früchte sind nach Regeln ordnungsmäßiger Wirtschaft vor Ende des Wirtschaftsjahrs zu trennen. Wirtschaftsjahr nicht automatisch Kalenderjahr; fachliche Einordnung erforderlich.
- `bewertungsnachweis`: Nichtleere Begründung von Kosten-/Fruchtzuordnung, Wert und ordnungsmäßiger Wirtschaft einschließlich Trennbarkeit vor Wirtschaftsjahresende.

Bei kumulativ erfüllten Voraussetzungen Minimum aus qualifizierten Verwendungskosten und gesetzlicher Wertgrenze bilden.

wert ist exakter EUR-Bruch des begrenzten Ersatzbetrags; bei nicht erfülltem Anwendungsbereich NICHT_ANWENDBAR/null.

Andere Anspruchsgrundlagen, Geltendmachung nach§1001 und Erlöschen nach§1002 gesondert prüfen. Keine doppelte Erstattung desselben Aufwands. Bewertungen sind belegte Nutzervorgaben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_998_T0001

```python
from bgbcalc import besitzer_landwirtschaftlicher_verwendungsersatz
besitzer_landwirtschaftlicher_verwendungsersatz(
    ordnungsgemaesse_fruchtkosten='80',
    wert_noch_ungetrennter_fruechte='100',
    landwirtschaftliches_grundstueck_herauszugeben=True,
    fruechte_noch_ungetrennt=True,
    trennung_vor_wirtschaftsjahresende_ordnungsgemaess=True,
    bewertungsnachweis='Synthetisch rechtlich und wirtschaftlich eingeordnete Verwendungen mit belegtem Wert.',
)
```

## besitzer_nuetzlicher_verwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verwendungskosten`: Nichtnegative tatsächliche Kosten der betrachteten anderen als notwendigen Verwendungen in EUR; notwendige Verwendungen separat.
- `fortbestehende_werterhoehung`: Nichtnegative gerade durch diese Verwendungen verursachte Werterhöhung, die noch bei Wiedererlangung der Sache durch Eigentümer besteht. Keine Gleichsetzung mit Aufwand oder früherer Wertsteigerung.
- `andere_als_notwendige_verwendung`: Wahrheitswert der rechtlichen Abgrenzung gegenüber notwendigen Verwendungen nach§994/995.
- `vor_rechtshaengigkeit_verwendet`: Wahrheitswert: betrachtete Verwendungen vor Eintritt der Rechtshängigkeit gemacht. Zeitliche Reihenfolge fachlich feststellen; gleicher Kalendertag allein genügt nicht.
- `vor_haftungsbeginn_990_verwendet`: Wahrheitswert: betrachtete Verwendungen vor Beginn der Haftung nach§990 gemacht; zusätzlich zur Grenze der Rechtshängigkeit erforderlich.
- `eigentuemer_besitzer_verhaeltnis_anwendbar`: Wahrheitswert des geprüften Anwendungsbereichs des Eigentümer-Besitzer-Verhältnisses.
- `bewertungsnachweis`: Nichtleere Begründung von Anspruchsregime, Kosten, kausaler fortbestehender Werterhöhung und beiden zeitlichen Voraussetzungen.

Bei kumulativ erfüllten Voraussetzungen Minimum aus qualifizierten Verwendungskosten und gesetzlicher Wertgrenze bilden.

wert ist exakter EUR-Bruch des begrenzten Ersatzbetrags; bei nicht erfülltem Anwendungsbereich NICHT_ANWENDBAR/null.

Andere Anspruchsgrundlagen, Geltendmachung nach§1001 und Erlöschen nach§1002 gesondert prüfen. Keine doppelte Erstattung desselben Aufwands. Bewertungen sind belegte Nutzervorgaben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_996_T0001

```python
from bgbcalc import besitzer_nuetzlicher_verwendungsersatz
besitzer_nuetzlicher_verwendungsersatz(
    verwendungskosten='80',
    fortbestehende_werterhoehung='100',
    andere_als_notwendige_verwendung=True,
    vor_rechtshaengigkeit_verwendet=True,
    vor_haftungsbeginn_990_verwendet=True,
    eigentuemer_besitzer_verhaeltnis_anwendbar=True,
    bewertungsnachweis='Synthetisch rechtlich und wirtschaftlich eingeordnete Verwendungen mit belegtem Wert.',
)
```
