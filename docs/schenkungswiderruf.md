<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## schenkung_widerrufsausschluss

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kenntnis_widerrufsvoraussetzungen_am`: ISO-Datum0001..9999 der Kenntnis des Widerrufsberechtigten vom Eintritt der Voraussetzungen seines Rechts. Nicht automatisch Schenkungstag, bloßer Verdacht oder Tod des Schenkers.
- `massgebliches_jahresfristende`: ISO-Datum0001..9999 des rechtlich maßgeblichen letzten Widerrufstags nach Jahresfrist und etwaigen zulässigen Kalenderkorrekturen. Mindestens berechnete Jahresgrundfrist; spätere Grenze im Nachweis rechtlich belegen.
- `widerrufserklaerung_am`: ISO-Datum0001..9999 des für die Fristprüfung rechtlich maßgeblichen Erklärungstags, insbesondere Zugang statt bloßer Absendung prüfen. Alle persönlichen Ausschlussmerkmale auf diesen Zeitpunkt beziehen.
- `schenker_hat_verziehen`: Wahrheitswert rechtlich wirksamer Verzeihung des Schenkers gegenüber Beschenktem. Nicht bloß Kontaktaufnahme oder Schweigen ohne Bewertung gleichsetzen.
- `beschenkter_bereits_verstorben`: Wahrheitswert, ob der Beschenkte beim maßgeblichen Widerrufszeitpunkt bereits verstorben ist. Nicht Tod des Schenkers einsetzen; untertägige Reihenfolge rechtlich prüfen.
- `pflicht_oder_anstandsschenkung`: Wahrheitswert der Privilegierung§534 als Pflicht-/Anstandsschenkung; keine pauschale Wertgrenze erfinden.
- `einordnungsnachweis`: Nichtleere Begründung von Kenntniszeitpunkt, Jahresfrist/Korrekturen, Erklärungstag, Verzeihung, Beschenktentod und Schenkungsprivilegierung.

Jahresfrist seit Kenntnis berechnen und rechtlich maßgebliches Ende prüfen. Fristüberschreitung, Verzeihung, vorheriger Tod des Beschenkten oder§534-Privilegierung sind alternative Ausschlüsse.

wert enthält rechnerisches_jahresfristende als ISO-Datum und jahresfrist_ueberschritten sowie widerruf_nach_532_oder_534_ausgeschlossen als Wahrheitswerte. FALSE bestätigt keinen Widerruf.

Keine vollständige Widerrufsprüfung:§530, Erklärung§531, Verzicht§533 und andere Voraussetzungen separat. Kein automatischer Ausschluss nur durch Tod des Schenkers. Maßgebliche Jahresgrenze nicht frei wählbar.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_532_T0001, BGB_532_T0002, BGB_534_T0001

```python
from bgbcalc import schenkung_widerrufsausschluss
schenkung_widerrufsausschluss(
    kenntnis_widerrufsvoraussetzungen_am='2024-02-29',
    massgebliches_jahresfristende='2025-02-28',
    widerrufserklaerung_am='2025-02-27',
    schenker_hat_verziehen=False,
    beschenkter_bereits_verstorben=False,
    pflicht_oder_anstandsschenkung=False,
    einordnungsnachweis='Synthetisch Kenntnis aller Voraussetzungen und tatsächlicher Erklärungstag; persönliche Ausschlüsse geprüft.',
)
```
