<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ratenlieferung_massgebliche_teilzahlungssumme

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `teilzahlungen`: Unbenannte Liste1..10000 qualifizierter vertraglicher Teilzahlungen mit genau zahlungs_id (nichtleer, eindeutig), faellig_utc (rechtlicher FälligkeitszeitpunktYYYY-MM-DDTHH:MM:SSZ), betrag (nichtnegativer exakter EUR-Dezimaltext/Bruch). Vollständiger maßgeblicher Zahlungsplan, einschließlich bereits gezahlter Raten, ohne Überschneidungen; bei tatsächlich keiner Teilzahlung ausdrücklich eine Nullposition.
- `fruehestmoeglicher_kuendigungszeitpunkt_utc`: Rechtlich maßgeblicher frühestmöglicher Kündigungszeitpunkt gemäß510III als normalisierter UTC-ZeitpunktYYYY-MM-DDTHH:MM:SSZ; Vertragsauslegung und Wirksamkeit der Kündigungsregel extern bestimmen.
- `einordnungsnachweis`: Nichtleerer Nachweis des510-Falls, vollständigen Ratenplans, rechtlich maßgeblichen Kündigungszeitpunkts und sekundengenauer Normalisierung. Keine unbekannten Uhrzeiten oder Subsekunden künstlich vereinfachen.

Vertragliche Teilzahlungen mit Fälligkeit bis einschließlich des qualifizierten frühestmöglichen Kündigungszeitpunkts auswählen und exakt summieren.

wert: massgebliche_teilzahlungssumme als exakter EUR-Bruch, anzahl_einbezogener_teilzahlungen und anzahl_spaeter_faelliger_teilzahlungen.

§510III2: gesetzliche Ersatzbezugsgröße für den Nettodarlehensbetrag491II2Nr1. Alle bis zum maßgeblichen Kündigungszeitpunkt zu entrichtenden Teilzahlungen einbeziehen, auch bereits entrichtete; keine Berechnung bloß des offenen Saldos. Später fällige Raten nicht einbeziehen. Mehrere verschiedene Raten dürfen denselben Fälligkeitszeitpunkt haben, aber jede Zahlung nur einmal erfassen. Kündigungsregel und Zahlungsplan extern qualifizieren; Ergebnis entscheidet keine weiteren491-Ausnahmen, kein Widerrufsrecht und keine tatsächliche Restschuld. Strikte UTC-Zeitpunkte ohne Zeitzonenannahmen; vorhandenen Standard-Datumsparser wiederverwenden.

Nichtnegative exakte EUR-Dezimaltexte/Brüche nach NUMERIK.md. Kostenlisten ohne doppelte Positionen, keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_510_T0008, BGB_510_T0009

```python
from bgbcalc import ratenlieferung_massgebliche_teilzahlungssumme
ratenlieferung_massgebliche_teilzahlungssumme(
    teilzahlungen=[{'zahlungs_id': 'A', 'faellig_utc': '2024-01-01T00:00:00Z', 'betrag': '100'}, {'zahlungs_id': 'B', 'faellig_utc': '2024-02-01T00:00:00Z', 'betrag': '100'}, {'zahlungs_id': 'C', 'faellig_utc': '2024-02-01T00:00:01Z', 'betrag': '100'}],
    fruehestmoeglicher_kuendigungszeitpunkt_utc='2024-02-01T00:00:00Z',
    einordnungsnachweis='§510III2: gesetzliche Ersatzbezugsgröße für den Nettodarlehensbetrag491II2Nr1. Alle bis zum maßgeblichen Kündigungszeitpunkt zu entrichtenden Teilzahlungen einbeziehen, auch bereits entrichtete; keine Berechnung bloß des offenen Saldos. Später fällige Raten nicht einbeziehen. Mehrere verschiedene Raten dürfen denselben Fälligkeitszeitpunkt haben, aber jede Zahlung nur einmal erfassen. Kündigungsregel und Zahlungsplan extern qualifizieren; Ergebnis entscheidet keine weiteren491-Ausnahmen, kein Widerrufsrecht und keine tatsächliche Restschuld. Strikte UTC-Zeitpunkte ohne Zeitzonenannahmen; vorhandenen Standard-Datumsparser wiederverwenden.',
)
```
