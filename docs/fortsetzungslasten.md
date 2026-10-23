<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fortgesetzte_guetergemeinschaft_altlasten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `persoenliche_altverbindlichkeiten`: Nichtnegativer exakter EUR-Betrag, getrennt zugeordnet und ohne Doppelanrechnung.
- `altverbindlichkeiten_erbendeckung`: Nichtnegativer exakter EUR-Betrag, getrennt zugeordnet und ohne Doppelanrechnung.
- `ersatzpflicht_zum_gesamtgut`: Nichtnegativer exakter EUR-Betrag, getrennt zugeordnet und ohne Doppelanrechnung.
- `ersatzpflicht_erbendeckung`: Nichtnegativer exakter EUR-Betrag, getrennt zugeordnet und ohne Doppelanrechnung.
- `zuordnungsnachweis`: Nichtleerer Nachweis der persönlichen Innenlast, Ersatzpflicht und fehlenden weiter erlangbaren Erbendeckung; qualifizierte Ausgangsposten, keine Doppelzählung.

Je Ausgangsposten die ihm zugeordnete Erbendeckung abziehen; beide ungedeckten Anrechnungsposten addieren.

wert enthält ungedeckte_altverbindlichkeiten, ungedeckte_ersatzpflicht und anrechnungspostensumme als exakte EUR-Brüche. Noch keine vollständige Teilungsbilanz.

§1500I/II: reine Ermittlung der ungedeckten Anrechnungsposten vor der Auseinandersetzungsbilanz. Ausgangsposten rechtlich getrennt und ohne Überschneidung: persönliche Verbindlichkeiten des Verstorbenen im Innenverhältnis sowie dessen Ersatzpflicht zum Gesamtgut. Erbendeckung umfasst die rechtlich erlangbare Deckung, nicht lediglich bisher tatsächlich eingegangene Zahlung; deren Uneinbringlichkeit/Erreichbarkeit ist qualifiziert. Keine doppelte Deckungszuordnung. Nicht bereits bereinigte Restposten nochmals vermindern. Kein zusätzlicher Geldanspruch gegen Abkömmlinge und keine individuelle Verteilung; nach§1498 besteht die überschießende persönliche Ersatzpflicht des§1476II2 nur für den überlebenden Ehegatten. Gesamtgutsbereinigung, Einrechnung vor Halbteilung, Anrechnung auf die Abkömmlingshälfte sowie§1501/1503 sind nachgelagerte Bilanzschritte, hier nicht als vollständige Teilung ausgegeben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1500_T0001, BGB_1500_T0002

```python
from bgbcalc import fortgesetzte_guetergemeinschaft_altlasten
fortgesetzte_guetergemeinschaft_altlasten(
    persoenliche_altverbindlichkeiten='100',
    altverbindlichkeiten_erbendeckung='30',
    ersatzpflicht_zum_gesamtgut='80',
    ersatzpflicht_erbendeckung='50',
    zuordnungsnachweis='Getrennte qualifizierte Ausgangslasten, zugeordnete Erbendeckung ausgeschöpft, keine Doppelzählung.',
)
```
