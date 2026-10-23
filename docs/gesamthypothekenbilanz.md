<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamthypothek_glaeubigerrest

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausgangsforderung`: Nichtnegativer exakter EUR-Betrag der rechtlich abgegrenzten gesicherten Ausgangsforderung; frühere bereits abgezogene Zahlungen nicht nochmals ansetzen.
- `befriedigungsbetraege`: Liste1..10000 nichtnegativer exakter EUR-Dezimaltexte oder Bruchobjekte. Rechtlich zugeordnete, überschneidungsfreie Positionen; Wenn keine Beträge anzusetzen sind, ausdrücklich eine einzelne Null angeben. Grundstücks-/Zahlungsbelege im Einordnungsnachweis zuordnen.
- `einordnungsnachweis`: Nichtleerer Nachweis der einheitlichen gesicherten Forderung, zugehörigen Grundstücke, Betragszuordnung und des qualifizierten1132-Falls.

Alle auf dieselbe gesicherte Forderung wirkenden Befriedigungen einmal summieren; Rest beim bisherigen Gläubiger und übersteigenden Zahlbetrag getrennt bestimmen.

wert enthält exakte EUR-Brüche für beruecksichtigte_befriedigung, verbleibende_glaeubigerforderung, uebersteigender_zahlbetrag.

§1132I: dieselbe Forderung wird nicht mit der Zahl belasteter Grundstücke multipliziert. Qualifizierte Befriedigungen aus verschiedenen Grundstücken und sonstigen Quellen nur einmal auf dieselbe Ausgangsforderung anrechnen. Zahlung auf Kosten/Zinsen oder andere Forderungen zuerst richtig zuordnen; Ausgangsforderung und Beträge müssen denselben Umfang und Zeitraum betreffen. Ergebnis ist der Rest beim bisherigen Gläubiger, kein allgemeines Erlöschensurteil: Forderungs-/Hypothekenübergang insbesondere1143/1150, Ausgleich und verbleibende Eigentümerrechte separat. Übersteigender Zahlbetrag begründet keinen automatisch festgestellten Erstattungsanspruch.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1132_T0001, BGB_1132_T0002

```python
from bgbcalc import gesamthypothek_glaeubigerrest
gesamthypothek_glaeubigerrest(
    ausgangsforderung='100',
    befriedigungsbetraege=['30', '40'],
    einordnungsnachweis='§1132I: dieselbe Forderung wird nicht mit der Zahl belasteter Grundstücke multipliziert. Qualifizierte Befriedigungen aus verschiedenen Grundstücken und sonstigen Quellen nur einmal auf dieselbe Ausgangsforderung anrechnen. Zahlung auf Kosten/Zinsen oder andere Forderungen zuerst richtig zuordnen; Ausgangsforderung und Beträge müssen denselben Umfang und Zeitraum betreffen. Ergebnis ist der Rest beim bisherigen Gläubiger, kein allgemeines Erlöschensurteil: Forderungs-/Hypothekenübergang insbesondere1143/1150, Ausgleich und verbleibende Eigentümerrechte separat. Übersteigender Zahlbetrag begründet keinen automatisch festgestellten Erstattungsanspruch.',
)
```

## gesamthypothek_verteilungsrahmen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausgangsforderung`: Nichtnegativer exakter EUR-Betrag der rechtlich abgegrenzten gesicherten Ausgangsforderung; frühere bereits abgezogene Zahlungen nicht nochmals ansetzen.
- `zugeteilte_teilforderungen`: Liste1..10000 nichtnegativer exakter EUR-Dezimaltexte oder Bruchobjekte. Rechtlich zugeordnete, überschneidungsfreie Positionen; Wenn keine Beträge anzusetzen sind, ausdrücklich eine einzelne Null angeben. Grundstücks-/Zahlungsbelege im Einordnungsnachweis zuordnen.
- `einordnungsnachweis`: Nichtleerer Nachweis der einheitlichen gesicherten Forderung, zugehörigen Grundstücke, Betragszuordnung und des qualifizierten1132-Falls.

Zugewiesene Teilforderungen summieren, auf vorhandene Gesamtforderung begrenzen und noch nicht zugeordneten rechnerischen Betrag bestimmen.

wert enthält exakte EUR-Brüche für summe_teilforderungen, noch_nicht_zugeteilter_betrag.

§1132II: numerische Verteilungsplanung mit ausdrücklich zugeordneten Teilbeträgen. Keine proportionale oder gleiche Verteilung erfinden; die rechtlich gewählte Zuordnung bleibt Eingabe. Summe darf die vorhandene Forderung nicht übersteigen. Ein positiver noch nicht zugeteilter Betrag zeigt eine unvollständige Planung, keine automatisch vollzogene teilweise Aufteilung oder Freigabe von Grundstücken. Voraussetzungen875/876/878, Grundbuchvollzug, Rang und Eigentümerrechte außerhalb der Rechnung. Bereits geleistete Zahlungen vorab eindeutig berücksichtigen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1132_T0003, BGB_1132_T0004

```python
from bgbcalc import gesamthypothek_verteilungsrahmen
gesamthypothek_verteilungsrahmen(
    ausgangsforderung='100',
    zugeteilte_teilforderungen=['30', '40'],
    einordnungsnachweis='§1132II: numerische Verteilungsplanung mit ausdrücklich zugeordneten Teilbeträgen. Keine proportionale oder gleiche Verteilung erfinden; die rechtlich gewählte Zuordnung bleibt Eingabe. Summe darf die vorhandene Forderung nicht übersteigen. Ein positiver noch nicht zugeteilter Betrag zeigt eine unvollständige Planung, keine automatisch vollzogene teilweise Aufteilung oder Freigabe von Grundstücken. Voraussetzungen875/876/878, Grundbuchvollzug, Rang und Eigentümerrechte außerhalb der Rechnung. Bereits geleistete Zahlungen vorab eindeutig berücksichtigen.',
)
```
