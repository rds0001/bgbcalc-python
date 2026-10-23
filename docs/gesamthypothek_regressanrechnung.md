<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamthypothek_regressanrechnung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `verbleibender_gesamthypothekenbetrag`: Gemeinschaftlicher Restbetrag nach dem Teilübergang auf den persönlichen Schuldner; nicht der ursprüngliche Gesamtbetrag.
- `eigentuemerquote`: Nach1172 ermittelte Quote des ersatzpflichtigen Eigentümers zwischen0und1.
- `uebergegangener_regressbetrag`: Auf den persönlichen Schuldner übergegangener Teilbetrag nach1174II.
- `anwendungsnachweis`: Teilübergang und Quote rechtlich qualifizieren; Restbetrag bereits um den Übergang vermindert.

Restbetrag mit Eigentümerquote multiplizieren und übergegangenen Regressbetrag anrechnen; positiven Anteil und Überhang getrennt ausweisen.

Anteil vor Anrechnung, vorzeichenbehafteter Saldo, nichtnegativer Restanteil und nicht verrechenbarer Regress.

Unmittelbare Anrechnung gemäß1174II: Anteil am übrig bleibenden Betrag=Restbetrag*1172Quote. Davon den übergegangenen Regressbetrag abziehen. Negativen rechnerischen Saldo gesondert ausweisen; positiver verbleibender Anteil=max(Saldo,0), nicht am Anteil verrechenbarer Regress=max(-Saldo,0). Der übergegangene dingliche Regress wird durch diese Anrechnung nicht getilgt. Keine zusätzliche persönliche Zahlungspflicht aus negativem Saldo, keine erfundene Umverteilung an andere Eigentümer. Die Funktion berechnet ausschließlich die individuelle Anrechnung, nicht eine vollständige Neuverteilung oder Rangvollstreckung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1172_T0001, BGB_1172_T0002, BGB_1172_T0003, BGB_1174_T0001, BGB_1174_T0002

```python
from bgbcalc import gesamthypothek_regressanrechnung
gesamthypothek_regressanrechnung(
    verbleibender_gesamthypothekenbetrag='80',
    eigentuemerquote='0.5',
    uebergegangener_regressbetrag='20',
    anwendungsnachweis='Unmittelbare Anrechnung gemäß1174II: Anteil am übrig bleibenden Betrag=Restbetrag*1172Quote. Davon den übergegangenen Regressbetrag abziehen. Negativen rechnerischen Saldo gesondert ausweisen; positiver verbleibender Anteil=max(Saldo,0), nicht am Anteil verrechenbarer Regress=max(-Saldo,0). Der übergegangene dingliche Regress wird durch diese Anrechnung nicht getilgt. Keine zusätzliche persönliche Zahlungspflicht aus negativem Saldo, keine erfundene Umverteilung an andere Eigentümer. Die Funktion berechnet ausschließlich die individuelle Anrechnung, nicht eine vollständige Neuverteilung oder Rangvollstreckung.',
)
```
