<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_verfahrenshemmungskette

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristlauf_erster_tag`: Erster rechtlich qualifizierter VerjährungslauftagISO.
- `grundfrist_letzter_tag`: Letzter Tag ohne diese Hemmungen, nicht vor erstem Fristtag.
- `verfahrensabschnitte`: Liste0..10000 abgeschlossener Abschnitte, je genau hemmungsbeginn_am, nachlaufereignis_am, nachlaufgrund. Grund:rechtskraeftige_entscheidung/anderweitige_beendigung/stillstand_letzte_verfahrenshandlung. Anfang erster Hemmungsbeginn oder qualifiziertes Weiterbetreiben, Ereignis nicht früher. Überlappungen zulässig.
- `einordnungsnachweis`: Nichtleerer Nachweis des204II-Falls und abgeschlossener, auf ganze Kalendertage normalisierter Abschnitte.

Je Nachlaufereignis6Monate nach Ereignisregel, daraus Intervalle bilden, vorhandener209-Kern vereinigt und berücksichtigt im tatsächlich fortgeschriebenen Lauf.

wert enthält rechnerischer_letzter_tag und beruecksichtigte_hemmungstage.

Kein fiktives Ende laufender Verfahren, keine automatische rechtliche Ereignisqualifikation. Besondere204I/III-Fristen, weitere Hemmungen, Neubeginn und193 separat.

ISO-Daten/Resultate0001..9999, höchstens10000abgeschlosseneAbschnitte.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_204_T0024, BGB_204_T0025, BGB_204_T0026

```python
from bgbcalc import verjaehrung_verfahrenshemmungskette
verjaehrung_verfahrenshemmungskette(
    fristlauf_erster_tag='2030-01-01',
    grundfrist_letzter_tag='2030-01-10',
    verfahrensabschnitte=[{'hemmungsbeginn_am': '2030-01-01', 'nachlaufereignis_am': '2030-01-01', 'nachlaufgrund': 'stillstand_letzte_verfahrenshandlung'}],
    einordnungsnachweis='Qualifizierter Stillstand und anschließendes Weiterbetreiben; abgeschlossene Kalendertage.',
)
```
