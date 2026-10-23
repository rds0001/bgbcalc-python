<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## aufrechnung_betragswirkung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigene_forderung`: Nichtnegative eigene Forderung des Aufrechnenden in EUR in der rechtlich bestimmten konkreten Paarung, zum maßgeblichen Aufrechnungslage-Zeitpunkt. Spätere Zinsen nicht ungeprüft einschließen.
- `gegenforderung`: Nichtnegative gegen den Aufrechnenden gerichtete Forderung des anderen Teils in EUR, gleiche zeitliche und sachliche Bewertung wie eigene Forderung. Keine automatische Mehrforderungs-/Kostenrangfolge.
- `aufrechnungslage_am`: ISO-Datum0001..9999 des rechtlich bestimmten Zeitpunkts, in dem gerade diese Forderungen aufrechnungsgeeignet gegenüberstanden. Taggenau normalisiert; untertägige Reihenfolge gesondert. Nicht später als Erklärung.
- `erklaerung_am`: ISO-Datum0001..9999 der rechtlich wirksamen Aufrechnungserklärung. Erlöschenswirkung wird auf rechtlich bestimmtes Datum der Aufrechnungslage zurückbezogen, nicht automatisch auf dieses Erklärungsdatum.
- `aufrechnung_zulaessig_und_erklaert`: Wahrheitswert rechtlich zulässiger und wirksam erklärter Aufrechnung dieser Paarung. Grundvoraussetzungen, Verbote/Einreden, Sonderregeln und Reihenfolge bereits geklärt.
- `forderungsnachweis`: Nichtleere Beschreibung der Forderungspaarung, Beträge, maßgeblichen früheren Aufrechnungslage, wirksamen Erklärung und sämtlicher Zulässigkeitsprüfungen. Zinsfolgen der Rückwirkung separat.

Deckung=min(eigene Forderung,Gegenforderung). Beide Forderungen um Deckung vermindern; Erlöschenswirkung auf vorgegebenen Zeitpunkt der Aufrechnungslage beziehen.

wert enthält erloschener_betrag_je_forderung, rest_eigene_forderung, rest_gegenforderung als exakte EUR-Brüche sowie erloeschenszeitpunkt_am. Bei fehlender zulässiger Erklärung NICHT_ANWENDBAR/null.

Eine Paarung gleichartiger EUR-Forderungen. Bei mehreren Forderungen§396/§366 und bei Kosten/Zinsen§367 separat; keine rückwirkende Zinskorrektur aus unbelegten Werten. Taggenaue Daten ersetzen keine untertägige Rechtsprüfung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_389_T0001

```python
from bgbcalc import aufrechnung_betragswirkung
aufrechnung_betragswirkung(
    eigene_forderung='0',
    gegenforderung='0',
    aufrechnungslage_am='2024-01-01',
    erklaerung_am='2025-01-01',
    aufrechnung_zulaessig_und_erklaert=True,
    forderungsnachweis='Synthetisch rechtlich bestimmte Aufrechnungslage vor Erklärung ohne weitere Zinspositionen.',
)
```
