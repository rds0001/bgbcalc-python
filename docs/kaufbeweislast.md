<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## kauf_beweislastvermutung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gefahruebergang_am`: ISO-Datum0001..9999 des rechtlich bestimmten Gefahrübergangs. Nicht ungeprüft Vertragsschluss oder Rechnungsdatum. Zeitpunkt nach den jeweils einschlägigen Regeln bestimmen.
- `zustand_zeigt_sich_am`: ISO-Datum0001..9999, an dem sich der konkret betrachtete abweichende Zustand zeigt; nicht späteres Reklamations-, Klage- oder Gutachtendatum einsetzen. Nicht vor Gefahrübergang.
- `lebendes_tier`: Wahrheitswert, ob der Kauf eines lebenden Tieres vorliegt; dann sechs Monate statt eines Jahres. Tierart oder Kaufpreis ändern diese gesetzliche Zeitregel nicht automatisch.
- `zustand_abweichend`: Wahrheitswert der rechtlich bewerteten Abweichung von Anforderungen§434/§475b, die sich am angegebenen Datum zeigt. Zeitablauf allein belegt keinen abweichenden Zustand.
- `vermutung_mit_art_unvereinbar`: Wahrheitswert der Unvereinbarkeit der Vermutung mit Art der Ware oder des mangelhaften Zustands. Keine automatische Ausnahme für Gebrauchtware oder jedes Tier.
- `regel_477_absatz_eins_anwendbar`: Wahrheitswert des sachlichen und zeitlichen Anwendungsbereichs von§477 Absatz1. FALSE ergibt NICHT_ANWENDBAR. Für dauerhafte digitale Bereitstellung Absatz2 eigenständig prüfen.
- `einordnungsnachweis`: Nichtleere Beschreibung von Gefahrübergang, Auftreten der Abweichung, Tierstatus, Unvereinbarkeit und gesetzlichem Anwendungsbereich.

Ereignisbezogenes Jahresende, bei lebendem Tier Sechsmonatsende bestimmen. Auftreten spätestens am letzten Tag UND Abweichung UND keine Unvereinbarkeit begründen gesetzliche Vermutung.

wert enthält vermutungszeitraum_ende als ISO-Datum, innerhalb_vermutungszeitraum und mangel_bei_gefahruebergang_vermutet als Wahrheitswerte. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Keine Verjährung, keine automatische endgültige Mangelhaftigkeitsentscheidung. Tatsächlicher Auftretenszeitraum ohne automatische§193-Verschiebung. Gefahrübergang und untertägige Reihenfolge vorher rechtlich bestimmen.

Explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis; Versuchszahl ganzzahlig0..2^53-1; Kalenderdaten und berechnete Grenzen0001..9999, sofern jeweiliger Parameter einschlägig.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_477_T0001, BGB_477_T0002

```python
from bgbcalc import kauf_beweislastvermutung
kauf_beweislastvermutung(
    gefahruebergang_am='2024-02-29',
    zustand_zeigt_sich_am='2024-02-29',
    lebendes_tier=False,
    zustand_abweichend=False,
    vermutung_mit_art_unvereinbar=False,
    regel_477_absatz_eins_anwendbar=True,
    einordnungsnachweis='Synthetisch rechtlich bestimmter Gefahrübergang und Auftreten des konkreten abweichenden Zustands.',
)
```

## kauf_digitale_beweislastvermutung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gefahruebergang_am`: ISO-Datum0001..9999 des rechtlich bestimmten Gefahrübergangs. Nicht ungeprüft Vertragsschluss oder Rechnungsdatum. Zeitpunkt nach den jeweils einschlägigen Regeln bestimmen.
- `zustand_zeigt_sich_am`: ISO-Datum0001..9999, an dem sich der konkret betrachtete abweichende Zustand zeigt; nicht späteres Reklamations-, Klage- oder Gutachtendatum einsetzen. Nicht vor Gefahrübergang.
- `bereitstellung_ab`: ISO-Datum0001..9999 des rechtlich maßgeblichen Beginns der dauerhaften digitalen Bereitstellung. Nicht mit Gefahrübergang gleichsetzen, wenn vertraglich/gesetzlich anderer Beginn maßgeblich ist.
- `bereitstellung_bis`: ISO-Datum0001..9999 des rechtlich letzten Bereitstellungstags einschließlich, mindestens bereitstellung_ab. NULL/None bedeutet ausdrücklich unbefristet fortlaufende Bereitstellung; kein Platzhalter für ein unbekanntes Enddatum. Tatsächliche technische Unterbrechung nicht ohne rechtliche Prüfung als Vertragsende einsetzen.
- `dauerhafte_bereitstellung_vereinbart`: Wahrheitswert, dass im Kaufvertrag dauerhafte Bereitstellung der digitalen Elemente vereinbart ist. Nicht bloß einmalige Lieferung eines digitalen Produkts.
- `digitaler_zustand_abweichend`: Wahrheitswert einer Abweichung gerade der digitalen Elemente von vertraglichen Anforderungen§434/§475b am angegebenen Datum. Sonstige körperliche Warenmängel nicht ungeprüft einsetzen.
- `regel_477_absatz_zwei_anwendbar`: Wahrheitswert des sachlichen und zeitlichen Anwendungsbereichs des Absatz2 bei Ware mit digitalen Elementen. FALSE ergibt NICHT_ANWENDBAR; die gesonderte Vereinbarungsbedingung wird zusätzlich geprüft.
- `einordnungsnachweis`: Nichtleere Beschreibung von Ware, digitalen Elementen, Gefahrübergang, vereinbarter dauerhafter Bereitstellung mit Zeitgrenzen und Auftreten der Abweichung. Unbefristeten Zeitraum bei NULL ausdrücklich begründen.

Zweijahresende seit Gefahrübergang und Bereitstellungsintervall getrennt prüfen. Vereinbarte dauerhafte Bereitstellung UND digitale Abweichung UND (innerhalb Zweijahreszeitraum ODER innerhalb Bereitstellungsdauer).

wert enthält zweijahreszeitraum_ende als ISO-Datum, innerhalb_zweijahreszeitraum, innerhalb_bereitstellungsdauer und mangel_waehrend_bisheriger_bereitstellung_vermutet als Wahrheitswerte. Vermutung betrifft bisherige Dauer, nicht bloß Gefahrübergang. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Keine Verkürzung des Zweijahreswegs auf kürzere Bereitstellung und keine Begrenzung längerer Bereitstellung auf zwei Jahre. Keine automatische Übernahme der Unvereinbarkeitsausnahme ausAbsatz1. Kein allgemeiner Digitalproduktvertrag.

Explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis; Versuchszahl ganzzahlig0..2^53-1; Kalenderdaten und berechnete Grenzen0001..9999, sofern jeweiliger Parameter einschlägig.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_477_T0003

```python
from bgbcalc import kauf_digitale_beweislastvermutung
kauf_digitale_beweislastvermutung(
    gefahruebergang_am='2024-02-29',
    zustand_zeigt_sich_am='2026-02-27',
    bereitstellung_ab='2024-02-29',
    bereitstellung_bis='2027-02-28',
    dauerhafte_bereitstellung_vereinbart=False,
    digitaler_zustand_abweichend=False,
    regel_477_absatz_zwei_anwendbar=True,
    einordnungsnachweis='Synthetisch rechtlich bestimmte dauerhafte digitale Bereitstellung und Auftreten der Abweichung.',
)
```
