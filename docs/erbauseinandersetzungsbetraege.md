<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ausgleichung_zuschuss_mehrbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zuwendungswert`: Nichtnegativer exakter EUR-Wert qualifizierter Einkünftezuschüsse oder Berufsvorbildungskosten2050II.
- `angemessenes_mass`: Nichtnegative rechtlich bewertete angemessene Summe nach Vermögensverhältnissen des Erblassers auf vergleichbarer Wertgrundlage. Keine erfundene gesetzliche Prozentgrenze.
- `zuwendung_nach_2050_abs2_qualifiziert`: Pflichtwahrheitswert: Ausgleichungsfall2050II rechtlich festgestellt. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis des Anwendungsfalls und angemessenen Maßes.

Zuwendungswert minus angemessenes Maß, mindestens null.

wert ist ausgleichungsrelevanter Mehrbetrag als exakter EUR-Bruch; kein sofortiger Zahlungsanspruch.

Keine automatische Angemessenheitsprüfung, Bewertung2055 oder abschließende Ausgleichung2055/2056. Keine unqualifizierte Zusammenrechnung verschiedener Zuwendungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2050_T0002

```python
from bgbcalc import ausgleichung_zuschuss_mehrbetrag
ausgleichung_zuschuss_mehrbetrag(
    zuwendungswert='100',
    angemessenes_mass='60',
    zuwendung_nach_2050_abs2_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierte Vorbildungskosten und angemessenes Maß.',
)
```

## erbnachlass_ueberschussanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlasswert`: Nichtnegativer exakter EUR-Nachlasswert vor den eingegebenen Abzügen.
- `gemeinsame_verbindlichkeiten`: Nichtnegative gemeinsame zu berichtigende Lasten; bereits aus Nachlass bezahlte Lasten nicht erneut erfassen. Nur einigen Erben obliegende Lasten2046II ausschließen.
- `erforderlicher_rueckbehalt`: Nichtnegative rechtlich bewertete Reserve für nicht fällige/streitige gemeinsame Verbindlichkeiten, überschneidungsfrei zu gemeinsamen_verbindlichkeiten.
- `erbquote_zaehler`: Ganzzahl0..Nenner, Anteil des betrachteten Erben.
- `erbquote_nenner`: Ganzzahl1..2^53−1.
- `einfaches_teilungsmodell_qualifiziert`: Pflichtwahrheitswert: vollständige gemeinsame Lasten/Reserve und einfache Quotenverteilung ohne Ausgleichung oder abweichende Teilungsanordnungen. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der rechtlichen Bewertungen und Abgrenzung.

Nachlass minus gemeinsame Lasten minus Reserve; positiver Rest mal Erbquote. Signierten Nettobetrag getrennt ausweisen.

wert enthält nettobetrag_nach_lasten_und_reserve (signed), verteilbarer_ueberschuss und anteil_am_ueberschuss als exakte EUR-Brüche.

Kein voller Teilungsplan, keine Insolvenzfeststellung, keine Verteilung nur einigen Erben obliegender Lasten2046II oder Ausgleichung2050ff.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2046_T0001, BGB_2046_T0002, BGB_2047_T0001

```python
from bgbcalc import erbnachlass_ueberschussanteil
erbnachlass_ueberschussanteil(
    nachlasswert='100',
    gemeinsame_verbindlichkeiten='20',
    erforderlicher_rueckbehalt='10',
    erbquote_zaehler=1,
    erbquote_nenner=2,
    einfaches_teilungsmodell_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierte Lasten und Reserve.',
)
```
