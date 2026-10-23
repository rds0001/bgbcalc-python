<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## anfechtung_fristpruefung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anfechtungsgrund`: Auswahl irrtum (§119), uebermittlungsfehler (§120), arglistige_taeuschung oder widerrechtliche_drohung (§123). Besondere Anfechtungsregeln wie§1954 nicht hiermit ersetzen.
- `willenserklaerung_abgegeben_am`: ISO-Datum0001..9999 der Abgabe der angefochtenen Willenserklärung; Ausgangspunkt der absoluten Zehnjahresgrenze, nicht späterer Zugang oder spätere Kenntnis.
- `kenntnis_oder_zwangslageende_am`: ISO-Datum0001..9999 des rechtlich einschlägigen Fristauslösers: Kenntnis vom Anfechtungsgrund bei§§119/120, Entdeckung der Täuschung beziehungsweise Ende der Zwangslage bei Drohung. Nicht bloß Datum eines Gutachtens oder einer Rechtsberatung.
- `massgeblicher_anfechtungstag`: ISO-Datum0001..9999 des für die geprüften Kalendergrenzen rechtlich maßgeblichen Erklärungstags; nicht vor Abgabe und angegebenem Fristauslöser. Zugang und Sonderregel für unverzügliche Absendung gegenüber Abwesendem§121 Absatz1 Satz2 rechtlich unterscheiden; Versanddatum nicht pauschal als Einhaltung absoluter Grenzen behandeln.
- `unverzueglich_gehandelt`: Wahrheitswert der begründeten Bewertung ohne schuldhaftes Zögern nach Kenntnis. Bei§§119/120 erforderlich, bei§123 für das Ergebnis unbeachtlich, aber typvalidiert. Keine feste gesetzliche Tageszahl erfinden; Absendungsregel§121 Absatz1 Satz2 gegebenenfalls berücksichtigen.
- `massgebliches_jahresfristende`: ISO-Datum0001..9999 des maßgeblichen letzten Tags der Jahresfrist bei Täuschung/Drohung, einschließlich einschlägiger§§206/210/211 und zulässiger Kalenderkorrekturen. Darf berechnete Grundjahresfrist nicht verkürzen. Für Irrtum/Übermittlung optional NULL/None; freiwillig eingegebenes Datum wird validiert, verdrängt dort nicht die Unverzüglichkeitsregel.
- `anfechtungsregel_anwendbar`: Wahrheitswert des sachlichen/zeitlichen Anwendungsbereichs der ausgewählten allgemeinen Anfechtungsregel. FALSE ergibt NICHT_ANWENDBAR. Besonders Erbschaftsannahme/-ausschlagung nach§1954 nicht ungeprüft hier einordnen.
- `einordnungsnachweis`: Nichtleere Begründung von Anfechtungsgrund, Abgabe, Kenntnis/Ende der Zwangslage, maßgeblichem Erklärungstag, Unverzüglichkeit und gegebenenfalls Jahresfristkorrekturen.

Zehnjahresgrenze ab Abgabe. Bei Irrtum/Übermittlung zusätzlich bewertete Unverzüglichkeit; bei Täuschung/Drohung Minimum aus maßgeblichem Jahresfristende und Zehnjahresgrenze.

wert enthält zehnjahresgrenze, rechnerisches_jahresfristende (bei§121 null), massgebliche_kalendergrenze als ISO-Daten, unverzueglichkeit_erforderlich und anfechtung_fristgerecht als Wahrheitswerte. Bei§121 allein Kalendergrenze genügt nicht. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Nur allgemeine Fristprüfung, keine Anfechtungsgrund- oder Erklärungswirksamkeitsentscheidung. Keine automatische Anwendung auf besondere Anfechtungstatbestände. Jahresfristschutz verändert nicht automatisch absolute Zehnjahresgrenze; keine neue Höchstfrist ab späterer Kenntnis.

ISO-Daten und berechnete Grenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis. Optionales Jahresfristende nach beschriebenem Regelweg.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_121_T0001, BGB_121_T0002, BGB_121_T0003, BGB_124_T0001, BGB_124_T0002, BGB_124_T0003, BGB_124_T0004

```python
from bgbcalc import anfechtung_fristpruefung
anfechtung_fristpruefung(
    anfechtungsgrund='irrtum',
    willenserklaerung_abgegeben_am='2014-02-28',
    kenntnis_oder_zwangslageende_am='2023-12-01',
    massgeblicher_anfechtungstag='2024-02-27',
    unverzueglich_gehandelt=False,
    massgebliches_jahresfristende=None,
    anfechtungsregel_anwendbar=True,
    einordnungsnachweis='Synthetisch rechtlich bestimmte Abgabe, Kenntnis/Ende der Zwangslage und Kalendergrenzen; Unverzüglichkeit begründet vorgegeben.',
)
```
