<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## miete_formmangel_beendigungsgrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `ueberlassung_am`: Tag der tatsaechlichen Ueberlassung im qualifizierten550Fall.
- `ordentlicher_beendigungstag`: Nach einschlaegiger Kuendigungsfrist bereits errechneter regulaerer Monatsendtermin, etwa aus wohnraummiete_kuendigungstermin.
- `einordnungsnachweis`: Vertragsdauer laenger als ein Jahr, einschlaegiger Schriftformmangel, ordentliche Kuendigung zu Monatsende und Zugang/Wirksamkeit rechtlich qualifizieren.

Jahresmindestbindung550mit regulaerem Monatsendtermin verbinden und erforderlichenfalls bis zum naechsten zulaessigen Monatsende verschieben.

Jahresmindestgrenze und fruehester damit vereinbarer Monatsendtermin, keine automatische Vertragsbeendigung.

§550Satz2: regulaeren ordentlichen Monatsendtermin mit dem Ablauf eines Jahres nach tatsaechlicher Ueberlassung vergleichen. Liegt der regulaere Termin davor, ersten Monatsendtermin bestimmen, der die Jahresgrenze erreicht. Nicht bloss das Maximum mit einem mitten im Monat liegenden Jahrestag als angeblich zulaessigen Kuendigungstermin ausgeben. Ueberlassungsereignis nach187I, keine pauschale365Tage-Dauer. Die ordentliche Frist wird vom bestehenden Wohnraummietkern berechnet; diese Funktion fuegt nur550-Mindestbindung hinzu. Kein automatischer Formmangelentscheid, keine Kuendigungssperre fuer ausserordentliche wichtige Gruende und keine Behandlung abweichender wirksamer Terminvereinbarungen. Bei rechtlich anderem Beginn187II gesondert qualifizieren.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_550_T0001, BGB_550_T0002, BGB_573c_T0001, BGB_573c_T0002, BGB_573c_T0003, BGB_573c_T0004, BGB_573c_T0005

```python
from bgbcalc import miete_formmangel_beendigungsgrenze
miete_formmangel_beendigungsgrenze(
    ueberlassung_am='2024-02-15',
    ordentlicher_beendigungstag='2024-12-31',
    einordnungsnachweis='§550Satz2: regulaeren ordentlichen Monatsendtermin mit dem Ablauf eines Jahres nach tatsaechlicher Ueberlassung vergleichen. Liegt der regulaere Termin davor, ersten Monatsendtermin bestimmen, der die Jahresgrenze erreicht. Nicht bloss das Maximum mit einem mitten im Monat liegenden Jahrestag als angeblich zulaessigen Kuendigungstermin ausgeben. Ueberlassungsereignis nach187I, keine pauschale365Tage-Dauer. Die ordentliche Frist wird vom bestehenden Wohnraummietkern berechnet; diese Funktion fuegt nur550-Mindestbindung hinzu. Kein automatischer Formmangelentscheid, keine Kuendigungssperre fuer ausserordentliche wichtige Gruende und keine Behandlung abweichender wirksamer Terminvereinbarungen. Bei rechtlich anderem Beginn187II gesondert qualifizieren.',
)
```
