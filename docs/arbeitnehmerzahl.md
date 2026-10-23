<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## arbeitnehmerzahl_kuendigungsfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beschaeftigte`: Unbenannte Liste mit0..10000 Datensätzen, je rechtlich zum regelmäßigen Arbeitnehmerbestand des Arbeitgebers gehörender Person genau einmal. Jeder Datensatz hat genau wochenstunden (nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt), teilzeitbeschaeftigt (Wahrheitswert des rechtlichen Teilzeitstatus) und zur_berufsbildung_beschaeftigt (Wahrheitswert). Regelmäßige wöchentliche Arbeitszeit, nicht zufällige Ist-Stunden. Berufsbildung wird mit0 gewichtet; Teilzeit bis einschließlich20Stunden mit0,5, über20 bis einschließlich30 mit0,75, sonst1. Vollzeit zählt unabhängig von kurzer branchenüblicher Vollzeit mit1. Auch ausgeschlossene Personen müssen typgültige Felder haben.
- `bestandsnachweis`: Nichtleere Beschreibung des regelmäßigen Arbeitgeberbestands, Beschäftigtenstatus und Arbeitszeiten. Rechtliche Einordnung von Leiharbeit, Organen, Auftragnehmern oder anderen Sondergruppen vorab vornehmen; keine automatische Übernahme einer beliebigen Personalstatistik.

Berufsbildung0; sonst rechtliche Teilzeit bis20h=1/2,bis30h=3/4,sonst1. Einzelgewichte exakt summieren und mit20 einschließlich Gleichheit vergleichen.

wert enthält gewichtete_arbeitnehmerzahl als exakten Bruch, hoechstens_zwanzig als Wahrheitswert und personengewichte als Liste exakter Brüche in Eingabereihenfolge. Leere Liste ergibt0/1 und TRUE.

Zählregel für§622 Absatz5 Satz1 Nummer2. Kein automatischer Nachweis wirksamer Fristverkürzung; einzelvertragliche Grundlage und Mindestfrist vier Wochen gesondert. Andere arbeitsrechtliche Beschäftigtenschwellen nicht übernehmen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_622_T0013, BGB_622_T0015, BGB_622_T0016

```python
from bgbcalc import arbeitnehmerzahl_kuendigungsfrist
arbeitnehmerzahl_kuendigungsfrist(
    beschaeftigte=[{'wochenstunden': '0', 'teilzeitbeschaeftigt': False, 'zur_berufsbildung_beschaeftigt': False}],
    bestandsnachweis='Synthetischer rechtlich bestimmter regelmäßiger Arbeitgeberbestand.',
)
```
