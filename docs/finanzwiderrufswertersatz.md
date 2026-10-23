<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## finanzwiderruf_leistungswertersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtverguetung`: Nichtnegative exakte vereinbarte EUR-Vergütung für den gesamten betrachteten Leistungsumfang.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bewerteten bis zum Widerruf erbrachten Leistungsanteils, höchstens Nenner und2^53-1.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der Gesamtleistung im selben Bewertungsmaßstab, höchstens2^53-1; Anteil0..1.
- `verguetung_unverhaeltnismaessig_hoch`: Expliziter Wahrheitswert der rechtlich festgestellten Unverhältnismäßigkeit der vereinbarten Vergütung; keine automatische Prozentbewertung.
- `marktwert_erbrachte_leistung`: Nur bei unverhältnismäßig hoher Vergütung erforderlicher nichtnegativer exakter EUR-Marktwert bereits erbrachter Leistung. Sonst zwingendNULL/None. Nicht Marktwert der gesamten erst geplanten Leistung.
- `einordnungsnachweis`: Nichtleerer Nachweis des einschlägigen Finanzdienstleistungs-/Finanzierungshilfe-Widerrufsfalls, der gesetzlich erforderlichen Unterrichtung/Zustimmung, des rechtlich geschuldeten Wertersatzes und der Leistungs-/Marktwertbewertung.

Vertraglichen Vergütungsanteil bestimmen oder auf den Marktwert der bereits erbrachten Leistung umstellen.

wert: exakter EUR-Wertersatzbruch; Vertragspreisanteil oder Marktwert der bereits erbrachten Leistung, keine zusätzliche Quotenkürzung des Marktwerts.

§357bII undIII4: Wertersatz für bis zum Widerruf erbrachte Finanzdienstleistung beziehungsweise qualifizierte Finanzierungshilfe. Je nach Anwendungsfall erforderliche vorherige Unterrichtung, ausdrückliche Zustimmung zum vorzeitigen Beginn und Sonderverweise auf357a/506IV rechtlich vorqualifizieren. Bei digitalen Inhalten die besonderen Voraussetzungen357bII3 beachten. Keine ungeprüfte Übertragung auf gewöhnliche Darlehensnutzungszinsen357bIII; diese separat berechnen. Vereinbarte Vergütung entsprechend rechtlich bewertetem Leistungsanteil, keine automatische Zeitquote. Bei unverhältnismäßig hohem Gesamtpreis ist der eingegebene Marktwert bereits derjenige der erbrachten Leistung und wird nicht nochmals mit der Quote multipliziert. Keine feste Prozentgrenze für Unverhältnismäßigkeit erfinden; Rückzahlungen und weitere Aufwendungen getrennt, keine automatische Aufrechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_357b_T0002, BGB_357b_T0003, BGB_357b_T0004, BGB_357b_T0005, BGB_357b_T0006, BGB_357b_T0007, BGB_357b_T0008, BGB_357b_T0009, BGB_357b_T0010, BGB_357b_T0011, BGB_357b_T0012, BGB_357b_T0013, BGB_357b_T0014, BGB_357b_T0015

```python
from bgbcalc import finanzwiderruf_leistungswertersatz
finanzwiderruf_leistungswertersatz(
    gesamtverguetung='1000',
    leistungsanteil_zaehler=1,
    leistungsanteil_nenner=4,
    verguetung_unverhaeltnismaessig_hoch=False,
    marktwert_erbrachte_leistung=None,
    einordnungsnachweis='§357bII undIII4: Wertersatz für bis zum Widerruf erbrachte Finanzdienstleistung beziehungsweise qualifizierte Finanzierungshilfe. Je nach Anwendungsfall erforderliche vorherige Unterrichtung, ausdrückliche Zustimmung zum vorzeitigen Beginn und Sonderverweise auf357a/506IV rechtlich vorqualifizieren. Bei digitalen Inhalten die besonderen Voraussetzungen357bII3 beachten. Keine ungeprüfte Übertragung auf gewöhnliche Darlehensnutzungszinsen357bIII; diese separat berechnen. Vereinbarte Vergütung entsprechend rechtlich bewertetem Leistungsanteil, keine automatische Zeitquote. Bei unverhältnismäßig hohem Gesamtpreis ist der eingegebene Marktwert bereits derjenige der erbrachten Leistung und wird nicht nochmals mit der Quote multipliziert. Keine feste Prozentgrenze für Unverhältnismäßigkeit erfinden; Rückzahlungen und weitere Aufwendungen getrennt, keine automatische Aufrechnung.',
)
```
