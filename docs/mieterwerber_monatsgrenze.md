<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## miete_erwerber_monatsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `regelfall`: Genau vorausverfuegung_566b (Eigentumsübergang maßgeblich) oder mietergeschaeft_566c (Kenntnis des Mieters vom Eigentumsübergang maßgeblich).
- `massgebliches_ereignis_am`: Qualifizierter maßgeblicher TagYYYY-MM-DD entsprechend regelfall. Datum des Eigentumsübergangs nicht mit Kaufvertragsschluss verwechseln; Kenntnistag bei566c eigenständig bestimmen.
- `einordnungsnachweis`: Nichtleerer Nachweis des Normfalls und Ereignistags; weitere Kenntnis-/Chronologieausnahmen gesondert geprüft.

Bis einschließlich Tag15 das laufende Monatsende, ab Tag16 das Ende des Folgemonats als zeitliche Mietgrenze bestimmen.

wert: zeitliche_mietgrenzeYYYY-MM-DD einschließlich dieses Monatsendes, folgemonat_einbezogen als Wahrheitswert.

§566bI und566cSatz1/2: nur zeitliche Grundgrenze der erfassten Mietzeiträume. Ereignis am15. verlängert nicht, am16. verlängert um einen Kalendermonat. Bei566bII kann Kenntnis des Erwerbers weitergehende Vorausverfügungen wirksam werden lassen; bei566cSatz3 kann ein nach Eigentumsübergang mit Kenntnis vorgenommenes Mietergeschaft trotz dieses Zeitfensters unwirksam sein. Diese Ausnahmen nicht aus dem Datumsresultat ableiten. Für566d ist die zeitliche Grenze nur ein Bestandteil; Erwerbs-/Fälligkeitschronologie der Gegenforderung separat. Keine Kündigungsfrist, keine automatische193Verschiebung und kein Wirksamkeitsentscheid.

Kalenderdaten0001..9999 einschließlich Grenz- und Folgedaten; keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_566b_T0001, BGB_566b_T0002, BGB_566b_T0003, BGB_566c_T0001, BGB_566c_T0002, BGB_566c_T0003, BGB_566d_T0001, BGB_566d_T0002

```python
from bgbcalc import miete_erwerber_monatsgrenze
miete_erwerber_monatsgrenze(
    regelfall='vorausverfuegung_566b',
    massgebliches_ereignis_am='2024-01-15',
    einordnungsnachweis='§566bI und566cSatz1/2: nur zeitliche Grundgrenze der erfassten Mietzeiträume. Ereignis am15. verlängert nicht, am16. verlängert um einen Kalendermonat. Bei566bII kann Kenntnis des Erwerbers weitergehende Vorausverfügungen wirksam werden lassen; bei566cSatz3 kann ein nach Eigentumsübergang mit Kenntnis vorgenommenes Mietergeschaft trotz dieses Zeitfensters unwirksam sein. Diese Ausnahmen nicht aus dem Datumsresultat ableiten. Für566d ist die zeitliche Grenze nur ein Bestandteil; Erwerbs-/Fälligkeitschronologie der Gegenforderung separat. Keine Kündigungsfrist, keine automatische193Verschiebung und kein Wirksamkeitsentscheid.',
)
```
