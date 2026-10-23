<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbraucherbau_widerruf_wertersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtverguetung`: Nichtnegative exakte vereinbarte EUR-Vergütung für den gesamten betrachteten Leistungsumfang.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bewerteten bis zum Widerruf erbrachten Leistungsanteils, höchstens Nenner und2^53-1.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der Gesamtleistung im selben Bewertungsmaßstab, höchstens2^53-1; Anteil0..1.
- `verguetung_unverhaeltnismaessig_hoch`: Expliziter Wahrheitswert der rechtlich festgestellten Unverhältnismäßigkeit der vereinbarten Vergütung; keine automatische Prozentbewertung.
- `marktwert_erbrachte_leistung`: Nur bei unverhältnismäßig hoher Vergütung erforderlicher nichtnegativer exakter EUR-Marktwert bereits erbrachter Leistung. Sonst zwingendNULL/None. Nicht Marktwert der gesamten erst geplanten Leistung.
- `einordnungsnachweis`: Nichtleerer Nachweis des Verbraucherbauwiderrufs, naturgemäß ausgeschlossener Rückgewähr und der Leistungs-/Marktwertbewertung.

Vertraglichen Vergütungsanteil bestimmen oder auf den Marktwert der bereits erbrachten Leistung umstellen.

wert: exakter EUR-Wertersatzbruch; Vertragspreisanteil oder Marktwert der bereits erbrachten Leistung, keine zusätzliche Quotenkürzung des Marktwerts.

§357e: qualifizierter wirksamer Widerruf eines Verbraucherbauvertrags und nach ihrer Natur ausgeschlossene Rückgewähr der bis zum Widerruf erbrachten Leistung. Leistungsanteil nach Wert/Umfang, keine automatische Zeitquote. Bei unverhältnismäßig hoher vereinbarter Vergütung bezeichnet marktwert_erbrachte_leistung bereits den Marktwert der erbrachten Leistung; diesen nicht nochmals mit dem Leistungsanteil multiplizieren. Unverhältnismäßigkeit und Bewertung extern bestimmen; keine erfundene feste Prozentschwelle. Keine ungeprüfte Übernahme der zusätzlichen Voraussetzungen357aII. Vorauszahlungen, sonstige Rückgewähr und Aufrechnung gesondert, keine automatische Saldierung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_357e_T0001, BGB_357e_T0002, BGB_357e_T0003

```python
from bgbcalc import verbraucherbau_widerruf_wertersatz
verbraucherbau_widerruf_wertersatz(
    gesamtverguetung='1000',
    leistungsanteil_zaehler=1,
    leistungsanteil_nenner=4,
    verguetung_unverhaeltnismaessig_hoch=False,
    marktwert_erbrachte_leistung=None,
    einordnungsnachweis='§357e: qualifizierter wirksamer Widerruf eines Verbraucherbauvertrags und nach ihrer Natur ausgeschlossene Rückgewähr der bis zum Widerruf erbrachten Leistung. Leistungsanteil nach Wert/Umfang, keine automatische Zeitquote. Bei unverhältnismäßig hoher vereinbarter Vergütung bezeichnet marktwert_erbrachte_leistung bereits den Marktwert der erbrachten Leistung; diesen nicht nochmals mit dem Leistungsanteil multiplizieren. Unverhältnismäßigkeit und Bewertung extern bestimmen; keine erfundene feste Prozentschwelle. Keine ungeprüfte Übernahme der zusätzlichen Voraussetzungen357aII. Vorauszahlungen, sonstige Rückgewähr und Aufrechnung gesondert, keine automatische Saldierung.',
)
```
