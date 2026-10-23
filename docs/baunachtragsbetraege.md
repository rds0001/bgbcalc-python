<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## bau_nachtragsverguetung_differenz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erforderliche_mehrkosten`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `angemessene_zuschlaege_mehrkosten`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `entfallende_kosten`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `entfallende_zuschlaege`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anordnungs-/Nachtragsfalls, der Zulässigkeit des Berechnungswegs und der qualifizierten Preisbestandteile.

Tatsächlich erforderliche Mehrkosten und angemessene Zuschläge addieren; entfallende Kosten und zugehörige entfallende Zuschläge abziehen

wert ist ein exakter EUR-Bruch; bei bau_nachtragsverguetung_differenz kann er als Vergütungsminderung negativ sein.

Nur qualifizierte Anordnung nach §650b Absatz2 und Berechnung nach §650c Absatz1; positiver Wert bedeutet Mehrvergütung, negativer Wert Vergütungsminderung. Die vier nichtnegativen Kostenkomponenten müssen in derselben Preisbasis ohne Doppelzählung vorliegen; Zuschläge für Geschäftskosten, Wagnis und Gewinn sind qualifizierte Geldbeträge, keine erfundenen Prozentsätze. Nach §650c Absatz1 Satz2 ausgeschlossener vermehrter Planungsaufwand darf nicht enthalten sein. Urkalkulationsmethode nach Absatz2, Fälligkeit und Abschlagsberechnung gesondert.

Nichtnegative Komponenten; vorzeichenbehaftete exakte Vergütungsdifferenz. Gemeinsame sichere Zahlengrenzen gelten für Zwischenwerte.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_650c_T0001

```python
from bgbcalc import bau_nachtragsverguetung_differenz
bau_nachtragsverguetung_differenz(
    erforderliche_mehrkosten='1000',
    angemessene_zuschlaege_mehrkosten='100',
    entfallende_kosten='200',
    entfallende_zuschlaege='20',
    einordnungsnachweis='Qualifizierte Anordnung und tatsächlich erforderliche Kosten samt Zuschlägen ohne ausgeschlossene Planung.',
)
```

## bau_nachtrag_ueberzahlungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gezahlte_vorlaeufige_nachtragsverguetung`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `geschuldete_mehrverguetung`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anordnungs-/Nachtragsfalls, der Zulässigkeit des Berechnungswegs und der qualifizierten Preisbestandteile.

Vorläufig gezahlte Nachtragsvergütung minus endgültig geschuldete Mehrvergütung, mindestens null

wert ist ein exakter EUR-Bruch; bei bau_nachtragsverguetung_differenz kann er als Vergütungsminderung negativ sein.

Nur Zahlungen nach §650c Absatz3 Satz1 und rechtlich feststehende nichtnegative Mehrvergütung nach Absatz1/2. Mehrfachzahlungen nur einmal summieren; echte Vergütungsminderungsfälle gesondert abrechnen. Überzahlungszinsen ab jeweiligem Zahlungseingang nach entsprechend §288 Absatz1 Satz2/Absatz2 ohne Zinseszins (§289 Satz1); vorhandene Zinskerne mit qualifizierter Überzahlungszuordnung und Datumsbasis separat verwenden, nicht pauschal gesamte Bruttozahlung verzinsen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_650c_T0007, BGB_650c_T0008

```python
from bgbcalc import bau_nachtrag_ueberzahlungsbetrag
bau_nachtrag_ueberzahlungsbetrag(
    gezahlte_vorlaeufige_nachtragsverguetung='800',
    geschuldete_mehrverguetung='600',
    einordnungsnachweis='Qualifizierte vorläufige Zahlungen und endgültig geschuldete Mehrvergütung.',
)
```

## bau_nachtrag_vorlaeufiger_abschlagsansatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `angebotene_mehrverguetung`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; dieselbe Preis-/Abrechnungsbasis ohne Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anordnungs-/Nachtragsfalls, der Zulässigkeit des Berechnungswegs und der qualifizierten Preisbestandteile.

Qualifizierte angebotene Mehrvergütung mit vier Fünfteln multiplizieren

wert ist ein exakter EUR-Bruch; bei bau_nachtragsverguetung_differenz kann er als Vergütungsminderung negativ sein.

Nur gewählter zulässiger80%-Weg nach §650c Absatz3 Satz1; fehlende Einigung und gerichtliche Entscheidung rechtlich qualifizieren. Ergebnis ist der anzusetzende Nachtragsanteil, nicht automatisch eine fällige Gesamtabschlagszahlung. Bereits gezahlte Abschläge und §632a-Einbehalt sowie §650m-Grenzen separat anwenden. Keine80%-Kürzung der endgültigen geschuldeten Vergütung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_650c_T0005

```python
from bgbcalc import bau_nachtrag_vorlaeufiger_abschlagsansatz
bau_nachtrag_vorlaeufiger_abschlagsansatz(
    angebotene_mehrverguetung='1000',
    einordnungsnachweis='Qualifizierter zulässiger und gewählter80-Prozent-Weg.',
)
```
