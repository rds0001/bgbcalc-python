<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zinsscheine_zurueckbehaltungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zinsscheine`: Liste0..1000 eindeutiger Zinsscheine derselben Hauptschuldverschreibung. Je exakt schein_id (nichtleerer eindeutiger Text), zahlbetrag (nichtnegative exakte EUR-Dezimalzeichenfolge/Bruchobjekt), zurueckgegeben (expliziter Wahrheitswert), zahlungspflicht_nach_803_absatz_1 (qualifizierter Wahrheitswert). Letzterer umfasst weiterbestehende Zahlungspflicht nach Prüfung entgegenstehender Scheinbestimmungen/Einwendungen; keine automatische Ableitung allein aus Status Hauptforderung. Auch ausgeschlossene Beträge werden validiert.
- `einloesung_der_hauptschuldverschreibung`: Expliziter Wahrheitswert, dass die Einlösung gerade der zugehörigen Hauptschuldverschreibung vorliegt; FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung der Zuordnung, Rückgabe, fortbestehenden Zahlungspflicht und tatsächlich geschuldeten Beträge aller Scheine.

Bei Einlösung der Hauptschuldverschreibung Summe der tatsächlichen Zahlbeträge genau jener Zinsscheine, die nicht zurückgegeben wurden und für die Zahlungspflicht nach Absatz1 fortbesteht.

wert ist exakte EUR-Summe als zaehler/nenner; leere Liste oder keine einschlägigen Scheine0/1, fehlender Einlösungsanwendungsfall null/NICHT_ANWENDBAR.

Nur Rückbehaltungsberechtigung, keine automatische Ausübung, endgültige Forderungskürzung oder zusätzliche Zahlungspflicht. Zahlungspflicht und entgegenstehende Scheinbestimmungen qualifiziert; keine Risiko-/Abzinsungsformel. Keine anderen Scheinarten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_803_T0001, BGB_803_T0002

```python
from bgbcalc import zinsscheine_zurueckbehaltungsbetrag
zinsscheine_zurueckbehaltungsbetrag(
    zinsscheine=[{'schein_id': 'A', 'zahlbetrag': '10.25', 'zurueckgegeben': False, 'zahlungspflicht_nach_803_absatz_1': True}],
    einloesung_der_hauptschuldverschreibung=True,
    einordnungsnachweis='Synthetisch qualifizierte Zinsscheine derselben Haupturkunde.',
)
```
