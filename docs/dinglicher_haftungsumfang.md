<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dinglicher_haftungsumfang

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `regelfall`: hypothek_1118 oder pfand_1210.
- `forderungsbestandteile`: Objekt mit genau den folgenden nichtnegativen EUR-Komponenten. {'hypothek_1118': ['forderung', 'gesetzliche_zinsen', 'kuendigungskosten', 'rechtsverfolgungskosten'], 'pfand_1210': ['forderung', 'zinsen', 'vertragsstrafen', 'verwendungsersatz', 'kuendigungskosten', 'rechtsverfolgungskosten', 'pfandverkaufskosten']} Nicht bestehende Beträge ausdrücklich mit0, nichtNULL. Hauptforderung ohne getrennt erfasste Nebenbeträge.
- `zuordnungsnachweis`: Nichtleere rechtliche Zuordnung zu gedeckten Komponenten, ohne doppelte Erfassung. Bei1210Absatz1Satz2 keine ausgeschlossenen rechtsgeschäftlichen Erweiterungen.

Addition der rechtlich gedeckten Forderungskomponenten.

wert ist der nominale gedeckte Gesamtbetrag als exakter EUR-Bruch; keine tatsächliche Erlösdeckung.

Nur Umfang bereits rechtlich zugeordneter, nicht überlappender gedeckter Forderungsbestandteile.1118 enthält gesetzliche Zinsen sowie Kündigung und Rechtsverfolgung zur Befriedigung aus dem Grundstück.1210: nachträgliche rechtsgeschäftliche Erweiterungen des persönlichen Schuldners bei abweichendem Pfandeigentümer ausgeschlossen. Forderung ohne nochmals getrennt erfasste Nebenbeträge angeben. Keine Ermittlung von Zinslauf, Rang, Verwertungserlös oder tatsächlicher Deckung; externe Sonderbegrenzungen gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1118_T0001, BGB_1210_T0001, BGB_1210_T0002, BGB_1210_T0003

```python
from bgbcalc import dinglicher_haftungsumfang
dinglicher_haftungsumfang(
    regelfall='hypothek_1118',
    forderungsbestandteile={'forderung': '100', 'gesetzliche_zinsen': '3', 'kuendigungskosten': '2', 'rechtsverfolgungskosten': '5'},
    zuordnungsnachweis='Qualifizierte gedeckte Forderungsbestandteile ohne Doppelzählung.',
)
```
