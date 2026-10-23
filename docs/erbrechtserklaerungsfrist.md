<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbausschlagung_grundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erbfall_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Erbfalls. Kenntnis vom tatsächlichen Anfall nicht vor diesem Ereignis ansetzen.
- `kenntnis_anfall_berufungsgrund_am`: ISO-Datum0001..9999, an dem der Erbe von Anfall UND Grund der Berufung Kenntnis erlangt hat; mindestens Erbfall. Kenntnis bloß vom Tod ohne eigene Berufung nicht automatisch ausreichend.
- `berufung_durch_verfuegung`: Wahrheitswert, ob Berufung durch Verfügung von Todes wegen vorliegt. Dann Bekanntgabe durch Nachlassgericht als zusätzliche Startgrenze berücksichtigen.
- `gerichtliche_bekanntgabe_am`: ISO-Datum0001..9999 der rechtlich maßgeblichen Bekanntgabe der Verfügung durch das Nachlassgericht. Bei berufung_durch_verfuegung=TRUE erforderlich und nicht vor Erbfall. Sonst optional NULL/None; private frühere Kenntnis von Testament nicht ohne Weiteres als gerichtliche Bekanntgabe einsetzen.
- `erblasser_letzter_wohnsitz_nur_ausland`: Wahrheitswert, ob der Erblasser seinen letzten Wohnsitz NUR im Ausland hatte. Ein zusätzlicher Auslandswohnsitz neben einem inländischen erfüllt diese Alternative nicht automatisch.
- `erbe_bei_fristbeginn_im_ausland`: Wahrheitswert des Aufenthalts des Erben im Ausland gerade beim rechtlich bestimmten Fristbeginn. Bei späterer gerichtlicher Bekanntgabe deren Auswirkung auf den Beginn berücksichtigen; keine spätere Urlaubsreise einsetzen.
- `ausschlagungsregel_anwendbar`: Wahrheitswert des konkreten sachlichen/zeitlichen Ausschlagungstatbestands nach§1944. FALSE ergibt NICHT_ANWENDBAR; frühere Annahme und andere Ausschlüsse gesondert prüfen.
- `einordnungsnachweis`: Nichtleere Begründung von Erbfall, Berufung, Kenntnis, gerichtlicher Bekanntgabe und Auslandsverhältnissen gerade am maßgeblichen Zeitpunkt.

Fristbeginn Kenntnis von Anfall und Berufungsgrund, bei Verfügung frühestens gerichtliche Bekanntgabe: späteres Datum. Sechs Wochen; bei mindestens einer gesetzlichen Auslandsalternative sechs Monate.

wert enthält fristbeginnereignis_am, rechnerischer_letzter_tag als ISO-Daten, fristdauer=6 und fristeinheit wochen oder monate. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Nur Grundfrist vor§§206/210 und erforderlichen Kalenderkorrekturen. Keine automatische Ausschlagung oder Annahmefiktion; tatsächliche/formgerechte Erklärung und§1943 separat.

ISO-Daten und berechnete Fristgrenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis. Optionale Bekanntgabe nur im beschriebenen Fall.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1944_T0001, BGB_1944_T0002, BGB_1944_T0003, BGB_1944_T0004, BGB_1944_T0005

```python
from bgbcalc import erbausschlagung_grundfrist
erbausschlagung_grundfrist(
    erbfall_am='2024-01-01',
    kenntnis_anfall_berufungsgrund_am='2024-02-29',
    berufung_durch_verfuegung=False,
    gerichtliche_bekanntgabe_am='2024-02-15',
    erblasser_letzter_wohnsitz_nur_ausland=False,
    erbe_bei_fristbeginn_im_ausland=False,
    ausschlagungsregel_anwendbar=True,
    einordnungsnachweis='Synthetisch Kenntnis von Anfall und Berufungsgrund, gegebenenfalls gerichtliche Bekanntgabe und rechtlich maßgebliche Auslandsverhältnisse.',
)
```

## erbrecht_anfechtungsgrundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anfechtungsfall`: Auswahl annahme, ausschlagung oder ausschlagungsfristversaeumung. Für Fristversäumung gilt§1956 entsprechend Annahme; kein allgemeiner§121/124-Fall.
- `angefochtenes_ereignis_am`: ISO-Datum0001..9999 der angefochtenen Annahme/Ausschlagung. Bei Fristversäumung rechtlich maßgeblichen Eintritt der Annahmefiktion aus§1943/§1956 bestimmen, nicht Erbfall oder spätere Kenntnis einsetzen. Ausgangspunkt der Dreißigjahresgrenze.
- `fristbeginn_am`: ISO-Datum0001..9999 des einschlägigen Anfechtungsfristbeginns: bei Drohung Ende der Zwangslage, sonst Kenntnis des Anfechtungsgrunds. Mindestens angefochtenes Ereignis. Kein automatischer Beginn mit Erbfall und keine pauschale Gleichsetzung mit Ausschlagungsfristbeginn.
- `erblasser_letzter_wohnsitz_nur_ausland`: Wahrheitswert, ob letzter Wohnsitz des Erblassers ausschließlich im Ausland lag, wie§1954 Absatz3 verlangt.
- `erbe_bei_fristbeginn_im_ausland`: Wahrheitswert des Auslandsaufenthalts gerade zu Beginn dieser Anfechtungsfrist. Zeitpunkt kann vom Beginn der ursprünglichen Ausschlagungsfrist abweichen.
- `anfechtungsregel_anwendbar`: Wahrheitswert, dass der angegebene erbrechtliche Fall anfechtbar ist und§1954/§1956 sachlich/zeitlich gilt. FALSE ergibt NICHT_ANWENDBAR; tatsächliche Anfechtungsgründe/Form nicht durch bloße Fristberechnung ersetzen.
- `einordnungsnachweis`: Nichtleere Begründung von Anfechtungsfall, angefochtenem Ereignis, Kenntnis beziehungsweise Zwangslageende und Auslandsverhältnissen am richtigen Fristbeginn.

Sechs Wochen, bei einer gesetzlichen Auslandsalternative sechs Monate ab einschlägigem Anfechtungsfristbeginn. Zusätzlich absolute Dreißigjahresgrenze ab Annahme/Ausschlagung beziehungsweise gleichgestelltem Ereignis; früheres Datum auswählen.

wert enthält fristdauer=6, fristeinheit wochen/monate und rechnerisches_grundfristende, dreissigjahresgrenze, rechnerischer_letzter_tag als ISO-Daten. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Nur Grundfrist und Höchstgrenze. §§206/210/211 sowie zulässige Kalenderkorrekturen können relative Frist verändern, nicht automatisch absolute Höchstgrenze. Diese danach weiter prüfen; keine allgemeinen Zehnjahresgrenzen§121/124 importieren.

ISO-Daten und berechnete Fristgrenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis. Optionale Bekanntgabe nur im beschriebenen Fall.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1954_T0001, BGB_1954_T0002, BGB_1954_T0003, BGB_1954_T0004, BGB_1954_T0005, BGB_1956_T0001

```python
from bgbcalc import erbrecht_anfechtungsgrundfrist
erbrecht_anfechtungsgrundfrist(
    anfechtungsfall='annahme',
    angefochtenes_ereignis_am='2000-01-01',
    fristbeginn_am='2024-02-29',
    erblasser_letzter_wohnsitz_nur_ausland=False,
    erbe_bei_fristbeginn_im_ausland=False,
    anfechtungsregel_anwendbar=True,
    einordnungsnachweis='Synthetisch rechtlich bestimmter erbrechtlicher Anfechtungsfall und Kenntnis/Ende der Zwangslage; Auslandsverhältnisse zum Beginn.',
)
```
