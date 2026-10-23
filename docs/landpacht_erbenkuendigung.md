<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## landpacht_erbenkuendigung_quartalstermin

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kuendigungszugang_am`: Rechtlich wirksamer ZugangYYYY-MM-DD innerhalb der gesondert qualifizierten einmonatigen Ausübungsfrist nach594dI.
- `einordnungsnachweis`: Nichtleerer Nachweis594dI: Tod des Pächters, zutreffende Kenntnis und rechtzeitige formwirksame Kündigung durch Erben oder Verpächter. Keine automatische Prüfung dieser Voraussetzungen.

Sechsmonatige Kündigungsfrist auf nächstes zulässiges Kalenderquartalsende ausrichten.

wert.sechsmonatige_kuendigungsfrist_letzter_tag und rechnerischer_pachtendtermin alsISO-Daten.

§594dI: sechs Kalendermonate ab tatsächlichem Kündigungszugang berechnen, anschließend erstes Kalenderquartalsende auswählen, das nicht vor dieser Fristgrenze liegt. Einmonatige Ausübungsfrist ab Kenntnis ist eigenständig; sechs Monate beginnen nicht schon mit Tod oder Kenntnis. Erbenwiderspruch594dII und Fortsetzungsentscheidung gesondert. Keine automatische Feiertagsverschiebung des Pachtendtermins.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_594d_T0001

```python
from bgbcalc import landpacht_erbenkuendigung_quartalstermin
landpacht_erbenkuendigung_quartalstermin(
    kuendigungszugang_am='2024-03-31',
    einordnungsnachweis='§594dI: sechs Kalendermonate ab tatsächlichem Kündigungszugang berechnen, anschließend erstes Kalenderquartalsende auswählen, das nicht vor dieser Fristgrenze liegt. Einmonatige Ausübungsfrist ab Kenntnis ist eigenständig; sechs Monate beginnen nicht schon mit Tod oder Kenntnis. Erbenwiderspruch594dII und Fortsetzungsentscheidung gesondert. Keine automatische Feiertagsverschiebung des Pachtendtermins.',
)
```
