<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## widerruf_verbraucherdarlehen_betrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `darlehensbetrag`: Nichtnegativer tatsächlich ausgezahlter und im betrachteten Zeitraum unverändert genutzter Darlehensbetrag in EUR. Teilrückzahlungen oder weitere Auszahlungen durch getrennte zutreffende Abschnitte abbilden; kein bloßer Kreditrahmen.
- `sollzinssatz_prozent`: Nichtnegativer vereinbarter jährlicher Sollzinssatz in Prozent als Dezimalzeichenfolge oder Bruchobjekt, beispielsweise4 für4Prozent. Effektivzins nicht einsetzen. Modell umfasst nichtnegative Sätze; Änderungen abschnittsweise.
- `zeitanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich/vertraglich bestimmten Jahresanteils zwischen Auszahlung und Rückzahlung, höchstens2^53-1. Anteil darf bei längerem Zeitraum größer1 sein.
- `zeitanteil_nenner`: Positive ganze Bezugsgröße desselben Jahresanteils, höchstens2^53-1. Keine automatisch vorgegebene365-Tage-Konvention.
- `zeitanteil_nachweis`: Nichtleere Beschreibung von Auszahlung/Rückzahlung, Kapitalbasis, Vertrags-Sollzins, maßgeblicher Zinskonvention und gegebenenfalls nachgewiesenem Gebrauchsvorteil. Vollständigen Bezug zu genau diesem Abschnitt belegen.
- `immobiliar_verbraucherdarlehen`: Wahrheitswert der rechtlichen Darlehensart. Nur beim Immobiliar-Verbraucherdarlehen eröffnet§357b Absatz3 Satz2/3 die hier modellierte niedrigere Gebrauchsvorteilsalternative.
- `niedrigerer_gebrauchsvorteil_nachgewiesen`: Wahrheitswert des rechtlich geeigneten Nachweises des Gebrauchsvorteils. Die numerische Niedrigkeit wird zusätzlich anhand des Betrags verglichen. Bei gewöhnlichem Verbraucherdarlehen kein Abzug allein wegen TRUE.
- `gebrauchsvorteil_betrag`: Nichtnegativer nachgewiesener Gebrauchsvorteil in EUR für denselben Kapital-/Zeitabschnitt, kein Jahreszinssatz. Pflicht bei Immobiliar-Verbraucherdarlehen mit Nachweis; sonst optional, bei Angabe validiert. Höherer Betrag erhöht den Sollzinsbetrag nicht.
- `nicht_rueckforderbare_oeffentliche_aufwendungen`: Nichtnegative tatsächlich vom Darlehensgeber gegenüber öffentlichen Stellen erbrachte und nicht zurückverlangbare Aufwendungen in EUR. Andere Gebühren, interne Kosten und erstattungsfähige Abgaben ausschließen; bei mehreren Zinsabschnitten insgesamt nur einmal erfassen.
- `widerruf_anwendbar`: Wahrheitswert eines wirksamen Widerrufs eines Verbraucherdarlehens im sachlich/zeitlich einschlägigen§357b Absatz3. FALSE ergibt NICHT_ANWENDBAR. Finanzierungshilfen und andere Sonderfälle gesondert.

Sollzinsbetrag=Kapital×Sollzinssatz/100×Jahresanteil. Bei Immobiliar-Verbraucherdarlehen und geeignetem Nachweis Minimum aus Sollzinsbetrag und Gebrauchsvorteil desselben Abschnitts. Nur qualifizierte öffentliche Aufwendungen hinzufügen.

wert enthält vertraglicher_sollzinsbetrag, geschuldeter_nutzungsbetrag, oeffentliche_aufwendungen und gesamtbetrag als exakte EUR-Brüche; gesamtbetrag ohne Kapitalrückzahlung. Ohne Anwendungsfall null und NICHT_ANWENDBAR.

Nur Verbraucherdarlehen im bezeichneten Anwendungsbereich, nicht sämtliche Finanzierungshilfen. Nichtnegative Sollzinssätze und einheitlicher Kapital-/Zinsabschnitt. Kapitalrückzahlung separat; keine erfundene Zinstagekonvention. Öffentliche Aufwendungen nicht mehrfach bei Abschnittsrechnung erfassen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_357b_T0011, BGB_357b_T0012, BGB_357b_T0013, BGB_357b_T0015

```python
from bgbcalc import widerruf_verbraucherdarlehen_betrag
widerruf_verbraucherdarlehen_betrag(
    darlehensbetrag='10000',
    sollzinssatz_prozent='6',
    zeitanteil_zaehler=1,
    zeitanteil_nenner=2,
    zeitanteil_nachweis='Synthetischer einheitlicher Kapital-/Zinsabschnitt über ein halbes Zinsjahr.',
    immobiliar_verbraucherdarlehen=False,
    niedrigerer_gebrauchsvorteil_nachgewiesen=False,
    gebrauchsvorteil_betrag='0',
    nicht_rueckforderbare_oeffentliche_aufwendungen='20',
    widerruf_anwendbar=True,
)
```
