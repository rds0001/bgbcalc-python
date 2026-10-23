<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## kauf_digitale_mindesthaftungsdauer

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ablieferung_am`: Qualifizierter Ablieferungstag der WareYYYY-MM-DD; nicht ungeprüft Gefahrübergang, Bestellung oder Beginn eines eigenständigen Digitalproduktvertrags.
- `bereitstellung_bis`: Bei befristeter Bereitstellung qualifiziertes EndeYYYY-MM-DD einschließlich Endtag, nicht vor Ablieferung. Bei unbefristeter Bereitstellung zwingendNULL/None; unbekannte Dauer ist kein unbefristeter Fall.
- `bereitstellung_unbefristet`: Expliziter Wahrheitswert. FALSE erfordert bestimmtes rechtlich maßgebliches Bereitstellungsende; TRUE bedeutet qualifiziert unbefristete Bereitstellung.
- `einordnungsnachweis`: Nichtleerer Nachweis einer Ware mit digitalen Elementen und vereinbarter dauerhafter Bereitstellung475cI. Bei nicht ausdrücklich bestimmter Dauer rechtliche Konkretisierung475cI2/475bIV2 vorab vornehmen.

Zweijahresgrenze ab Ablieferung berechnen und mit qualifiziertem Bereitstellungsende das spätere Ende bestimmen.

wert: zweijahresgrenzeYYYY-MM-DD und massgebliches_zeitraumendeYYYY-MM-DD oderNULL bei qualifiziert unbefristeter Dauer.

§475cII: zeitlicher Umfang der Anforderungen an dauerhaft bereitzustellende digitale Elemente, mindestens zwei Jahre ab Ablieferung. Bei längerem qualifizierten Bereitstellungszeitraum gilt dessen Ende; bei unbefristeter Bereitstellung kein bestimmtes Gesamtende. Keine Verjährungsfrist und keine Beweislastvermutung477II; Mangel, übrige Anspruchsvoraussetzungen und rechtliche Bestimmung des Bereitstellungszeitraums separat. Keine193Verschiebung. Nur hier festgelegte endliche oder tatsächlich unbefristete Dauer; unbekannte Dauer darf nicht als unbefristet eingesetzt werden.

Strikte ISO-Kalendertage0001..9999; keine automatische Feiertagsverschiebung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_475c_T0001, BGB_475c_T0002, BGB_475c_T0003

```python
from bgbcalc import kauf_digitale_mindesthaftungsdauer
kauf_digitale_mindesthaftungsdauer(
    ablieferung_am='2024-02-29',
    bereitstellung_bis='2025-01-01',
    bereitstellung_unbefristet=False,
    einordnungsnachweis='§475cII: zeitlicher Umfang der Anforderungen an dauerhaft bereitzustellende digitale Elemente, mindestens zwei Jahre ab Ablieferung. Bei längerem qualifizierten Bereitstellungszeitraum gilt dessen Ende; bei unbefristeter Bereitstellung kein bestimmtes Gesamtende. Keine Verjährungsfrist und keine Beweislastvermutung477II; Mangel, übrige Anspruchsvoraussetzungen und rechtliche Bestimmung des Bereitstellungszeitraums separat. Keine193Verschiebung. Nur hier festgelegte endliche oder tatsächlich unbefristete Dauer; unbekannte Dauer darf nicht als unbefristet eingesetzt werden.',
)
```

## miete_schonfrist_wiederholungszeitraum

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fruehere_geheilte_kuendigung_am`: DatumYYYY-MM-DD der früheren durch Schonfrist nach569III2Satz1 unwirksam gewordenen Kündigung. Datum der Kündigung, nicht Zahlungstag oder Rechtshängigkeit.
- `erneute_kuendigung_am`: DatumYYYY-MM-DD der nun betrachteten späteren Kündigung, strikt nach früherer Kündigung.
- `einordnungsnachweis`: Nichtleerer Nachweis der vorangegangenen Schonfristheilung und Zuordnung beider Kündigungen. Nur numerische Zweijahresgrenze, keine automatische Wirksamkeitsentscheidung.

Frühere geheilte Kündigung um zwei Jahre fortschreiben und erneute Kündigung einschließlich des Grenztags vergleichen.

wert: zweijahresgrenzeYYYY-MM-DD und innerhalb_wiederholungszeitraum als Wahrheitswert.

§569III2Satz2: erneute Kündigung innerhalb von einschließlich zwei Jahren nach früherer, durch Schonfrist unwirksam gewordener Kündigung. Eine bloß erfolgte Mietzahlung ohne diese frühere Heilung genügt nicht als Bezugsvorgang. Zeitraum keine Handlungsfrist; keine193Verschiebung. Ergebnis betrifft nur die Wiederholungsgrenze der Schonfrist, nicht jede Zahlung, Aufrechnung oder sonstige Unwirksamkeit der neuen Kündigung.

Strikte ISO-Kalendertage0001..9999; keine automatische Feiertagsverschiebung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_569_T0001, BGB_569_T0002, BGB_569_T0003, BGB_569_T0004, BGB_569_T0005, BGB_569_T0006, BGB_569_T0007, BGB_569_T0008, BGB_569_T0009, BGB_569_T0010, BGB_569_T0011, BGB_569_T0012, BGB_569_T0013, BGB_569_T0014, BGB_569_T0015, BGB_569_T0016

```python
from bgbcalc import miete_schonfrist_wiederholungszeitraum
miete_schonfrist_wiederholungszeitraum(
    fruehere_geheilte_kuendigung_am='2024-02-29',
    erneute_kuendigung_am='2026-02-27',
    einordnungsnachweis='§569III2Satz2: erneute Kündigung innerhalb von einschließlich zwei Jahren nach früherer, durch Schonfrist unwirksam gewordener Kündigung. Eine bloß erfolgte Mietzahlung ohne diese frühere Heilung genügt nicht als Bezugsvorgang. Zeitraum keine Handlungsfrist; keine193Verschiebung. Ergebnis betrifft nur die Wiederholungsgrenze der Schonfrist, nicht jede Zahlung, Aufrechnung oder sonstige Unwirksamkeit der neuen Kündigung.',
)
```
