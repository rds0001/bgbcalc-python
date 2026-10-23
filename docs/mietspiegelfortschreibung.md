<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mietspiegel_folgestichtage

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `datenerhebungsstichtag`: ISO-Datum des maßgeblichen ursprünglichen Datenerhebungsstichtags des qualifizierten Mietspiegels; nicht späteres Anerkennungs-/Veröffentlichungsdatum.
- `stichtagsnachweis`: Nichtleerer Nachweis des ursprünglichen Erhebungsstichtags und des Anwendungsbereichs558dII; zwischenzeitliche Anpassung setzt die Vierjahresfrist nicht neu in Gang.

Erste Anpassung und Neuerstellung zwei beziehungsweise vier Jahre nach Erhebungsstichtag.

wert: anpassung_stichtag und neuerstellung_stichtag als ISO-Daten.

§558dII: erste Zweijahresanpassung und Vierjahresneuerstellung eines qualifizierten Mietspiegels, ausgehend vom Datenerhebungsstichtag der ursprünglichen Erstellung. Eine zwischenzeitliche Indexanpassung setzt die Vierjahresneuerstellung nicht neu in Gang; nicht deren Veröffentlichungsdatum als neuen Ausgangspunkt einsetzen. Keine automatische Feiertagsverschiebung, Gültigkeitsvermutung oder Aussage über verspätete Veröffentlichung. Veröffentlichung und wissenschaftliche/formelle Voraussetzungen gesondert prüfen; keine Fristberechnung aus einem beliebig ausgewählten Indexmonat.

Exakte nichtnegative Basis und positive Indexstände; sichere Ganzzahlen nach NUMERIK.md. Kalenderdaten0001..9999 einschließlich Folgestichtagen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558d_T0004, BGB_558d_T0005, BGB_558d_T0006, BGB_558d_T0007, BGB_558d_T0008

```python
from bgbcalc import mietspiegel_folgestichtage
mietspiegel_folgestichtage(
    datenerhebungsstichtag='2024-01-31',
    stichtagsnachweis='Ursprünglicher Erhebungsstichtag des qualifizierten Mietspiegels.',
)
```

## mietspiegel_indexfortschreibung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausgangswert`: Nichtnegativer qualifizierter Mietspiegelwert in EUR je explizit belegter Bezugseinheit; passend zum Ausgangsindex.
- `ausgangsindex`: Positiver amtlicher Ausgangsindex derselben Reihe und Basis wie der neue Index, als exakter Dezimalwert oder Bruch.
- `neuer_index`: Positiver neuer amtlicher Indexstand; auch Senkungen zulässig.
- `indexnachweis`: Nichtleerer Nachweis qualifizierter Indexfortschreibung558dII, amtlicher Reihe, gleicher Basis, Bezugszeitpunkte und Einheit des Mietspiegelwerts.

Qualifizierten Mietspiegelwert mit dem Verhältnis vergleichbarer Indexstände fortschreiben.

wert: indexverhaeltnis dimensionslos, fortgeschriebener_wert und wertveraenderung als exakte EUR-Brüche je qualifizierter Bezugseinheit. Veränderung kann negativ sein.

§558dII2: nur qualifizierte Indexanpassung, keine Stichprobenauswertung. Amtliche Indexreihe, identische Basis und rechtlich maßgebliche Bezugszeitpunkte vorgeben; Indexstände nicht selbst beschaffen oder schätzen. Ausgangswert und Ergebnis behalten dieselbe qualifizierte Mietspiegel-Bezugseinheit, beispielsweise EUR je Quadratmeter und Monat. Keine automatische Cent-Rundung, Gültigkeitsfeststellung oder konkrete Mieterhöhung; Anerkennung, Erstellungsmethode und einschlägige Verordnung gesondert. Indexsenkungen werden ebenfalls gerechnet; keine erneute Anwendung bereits berücksichtigter Änderungen.

Exakte nichtnegative Basis und positive Indexstände; sichere Ganzzahlen nach NUMERIK.md. Kalenderdaten0001..9999 einschließlich Folgestichtagen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558d_T0004, BGB_558d_T0005, BGB_558d_T0006, BGB_558d_T0007, BGB_558d_T0008

```python
from bgbcalc import mietspiegel_indexfortschreibung
mietspiegel_indexfortschreibung(
    ausgangswert='10',
    ausgangsindex='100',
    neuer_index='110',
    indexnachweis='Vergleichbare amtliche Indexwerte; Basis EUR je Quadratmeter und Monat, qualifizierte Anpassung558dII.',
)
```
