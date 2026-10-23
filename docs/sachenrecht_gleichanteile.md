<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## sachenrecht_gleichanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtmenge`: Nichtnegative Gesamtfläche, Frucht-/Holzmenge oder Wirtschaftsplankosten in einer gemeinsamen Einheit; Kosten inEUR.
- `anzahl_berechtigte`: Ganze Zahl2..1000 betroffener Grundstücksseiten; bei Wirtschaftsplankosten genau2:Eigentümer und Nießbraucher. Miteigentümer einer Seite nicht mehrfach zählen.
- `regelfall`: grenzflaeche_920; grenzbaum_fruechte_923; grenzbaum_holz_923; wirtschaftsplan_kosten_1038.
- `verteilungsnachweis`: Nichtleerer Nachweis des gesetzlichen Gleichverteilungsfalls, ohne abweichende Billigkeits-/Verzichtsregel. Keine rechtliche Entscheidung durch den Rechner.

Einzelanteil=Gesamtmenge/Anzahl; Quote=1/Anzahl.

wert enthält anteilsquote und einzelanteil als exakte Brüche.

Nur qualifizierte Gleichverteilung.920Absatz2-Billigkeit und923Verzicht nicht in dieser Grundverteilung. Räumliche Grenzziehung, Sachbewertung und die interne Verteilung mehrerer Miteigentümer einer Nachbarseite separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_920_T0002, BGB_920_T0003, BGB_923_T0001, BGB_923_T0004, BGB_923_T0006, BGB_1038_T0003, BGB_1038_T0004

```python
from bgbcalc import sachenrecht_gleichanteil
sachenrecht_gleichanteil(
    gesamtmenge='901',
    anzahl_berechtigte=2,
    regelfall='grenzflaeche_920',
    verteilungsnachweis='Qualifizierte Wirtschaftsplankosten, Eigentümer und Nießbraucher tragen je die Hälfte.',
)
```
