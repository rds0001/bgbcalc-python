<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## nachlass_dreissigster_zeitraum

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erbfall_am`: ISO-Datum des Todes/Erbfalls; Ereignistag wird nicht mitgezählt.
- `prueftag`: ISO-Datum ab Erbfall einschließlich; Prüfung eines Kalendertages.
- `familienangehoeriger`: Expliziter Wahrheitswert der rechtlich qualifizierten Familienangehörigkeit zum Erblasser.
- `hausstandszugehoerigkeit_bei_erbfall`: Expliziter Wahrheitswert der Zugehörigkeit zum Hausstand gerade im Todeszeitpunkt, nicht nur früherer gemeinsamer Wohnsitz.
- `unterhalt_vom_erblasser_bezogen`: Expliziter Wahrheitswert des relevanten tatsächlichen Unterhaltsbezugs vom Erblasser. Abstrakte gesetzliche Unterhaltsberechtigung genügt nicht automatisch.
- `abweichende_letztwillige_anordnung`: Expliziter Wahrheitswert einer rechtlich wirksamen abweichenden letztwilligen Anordnung. TRUE ergibt NICHT_ANWENDBAR; die Anordnung kann den Anspruch verändern, erweitern oder ausschließen und wird nicht automatisch ausgelegt.
- `einordnungsnachweis`: Nichtleere Begründung der familiären, hausstandsbezogenen und unterhaltsbezogenen Einordnung sowie der letztwilligen Anordnungen.

Erbfalltag nicht mitzählen. Gesetzlicher Zeitraum vom Folgetag bis zum dreißigsten Folgetag einschließlich. Familienangehörigkeit, Hausstand im Todeszeitpunkt und Unterhaltsbezug kumulativ; Prüftag innerhalb beider Grenzen.

wert enthält zeitraumbeginn, zeitraumende, persoenliche_voraussetzungen_erfuellt, prueftag_im_zeitraum und gesetzliche_zeit_und_personenvoraussetzungen_erfuellt. Keine abschließende Anspruchsentscheidung. Abweichende Anordnung ergibt wert=null.

Abweichende letztwillige Anordnung verlangt individuelle Auslegung und ergibt NICHT_ANWENDBAR. Nur Zeit- und persönliche Voraussetzungen; Vermächtnisvorschriften nach Absatz2, Einwendungen und Haftungsbeschränkungen separat. Keine Monetarisierung des Unterhalts oder der Wohnungs-/Hausratsbenutzung. Keine automatische Feiertagsverschiebung des Versorgungszeitraums.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1969_T0001, BGB_1969_T0002, BGB_1969_T0003

```python
from bgbcalc import nachlass_dreissigster_zeitraum
nachlass_dreissigster_zeitraum(
    erbfall_am='2030-01-31',
    prueftag='2030-03-02',
    familienangehoeriger=False,
    hausstandszugehoerigkeit_bei_erbfall=False,
    unterhalt_vom_erblasser_bezogen=False,
    abweichende_letztwillige_anordnung=False,
    einordnungsnachweis='Synthetisch qualifizierter Familienangehöriger im Hausstand mit tatsächlichem Unterhaltsbezug.',
)
```
