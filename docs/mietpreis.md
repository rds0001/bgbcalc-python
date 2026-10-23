<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mietpreisbegrenzung_ausnahmen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erstmalige_nutzung`: ISO-Datum0001..9999 der rechtlich maßgeblichen ersten Nutzung der Wohnung; keine automatische Gleichsetzung mit Baujahr oder Beginn des aktuellen Mietvertrags.
- `erstmalige_vermietung`: ISO-Datum0001..9999 der rechtlich maßgeblichen erstmaligen Vermietung der Wohnung. Beide Daten müssen nach dem01.10.2014 liegen; der01.10.2014 selbst erfüllt Satz1 nicht.
- `erste_vermietung_nach_umfassender_modernisierung`: Expliziter Wahrheitswert, ob gerade die beurteilte Vermietung die erste Vermietung nach rechtlich als umfassend eingeordneter Modernisierung ist. Eine beliebige Modernisierung oder zweite Vermietung genügt nicht.
- `bewertungsnachweis`: Nichtleere Herkunfts-/Bewertungsbeschreibung der erstmaligen Daten und gegebenenfalls der umfassenden Modernisierung. Datumseinordnung wird nicht aus Belegen automatisch ermittelt.

Satz1 erfordert Erstnutzung und Erstvermietung jeweils strikt nach01.10.2014. Ausnahme von§556d liegt nach§556f vor, wenn Satz1 oder erste Vermietung nach umfassender Modernisierung. Satz2 bezieht auch§556e ein.

wert enthält ausnahme_nach_satz_1, ausnahme_von_556d, ausnahme_von_556e_nach_satz_2 als Wahrheitswerte. BERECHNET bedeutet durchgeführte Prüfung, nicht zwingend TRUE.

Nur Ausnahmetatbestand§556f. Tatsächliche Berufungsmöglichkeit unterliegt insbesondere§556g Absatz1a und Übergangsrecht; diese Voraussetzungen werden nicht automatisch erfüllt. FALSE bei Ausnahme von§556e nach Satz2 bestätigt nicht dessen Anwendbarkeit.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556f_T0001, BGB_556f_T0002, BGB_556f_T0003

```python
from bgbcalc import mietpreisbegrenzung_ausnahmen
mietpreisbegrenzung_ausnahmen(
    erstmalige_nutzung='2014-09-30',
    erstmalige_vermietung='2014-09-30',
    erste_vermietung_nach_umfassender_modernisierung=False,
    bewertungsnachweis='Synthetische rechtlich eingeordnete Nutzungsdaten.',
)
```

## mietpreisbegrenzung_grundbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ortsuebliche_vergleichsmiete`: Nichtnegative rechtlich festgestellte ortsübliche Vergleichsmiete in EUR pro Monat für die konkrete Wohnung und den maßgeblichen Zeitpunkt. Betrag der ganzen Wohnung, nicht EUR/m²; alternativ vorgelagert Wohnfläche multiplizieren. Keine automatische Mietspiegelauswertung.
- `gebiet_rechtswirksam_bestimmt`: Wahrheitswert: Wohnung liegt zum maßgeblichen Zeitpunkt im wirksam nach§556d Absatz2 bestimmten Gebiet. Die lokale Fassung verlangt Außerkrafttreten spätestens31.12.2029; konkrete Geltungsdauer, Begründung und räumliche Lage vorab prüfen. Diese Funktion enthält keine Verordnungsdatenbank.
- `ausnahme_von_556d`: Wahrheitswert einer im konkreten Fall rechtlich nutzbaren Ausnahme von§556d. Bei Verwendung von mietpreisbegrenzung_ausnahmen müssen insbesondere Berufungshindernisse nach§556g Absatz1a gesondert ausgeschlossen sein. Ein bloßer Ausnahmetatbestand trotz fehlender Auskunft genügt nicht automatisch.
- `anwendungsnachweis`: Nichtleere Beschreibung von Bewertungszeitpunkt, Vergleichsmiete, örtlicher Verordnung, Übergangsrecht und etwaiger rechtlich nutzbarer Ausnahme. Bei Staffeln maßgeblichen Zeitpunkt nach§557a Absatz4 vorgeben.

Bei wirksam reguliertem Gebiet und keiner nutzbaren Ausnahme: Grundbetrag=ortsübliche Vergleichsmiete×11/10. Sonst NICHT_ANWENDBAR.

wert ist der exakte Grundbetrag als EUR-Bruch; bei NICHT_ANWENDBAR null.

Keine automatische höhere Grenze nach§556e, keine Auskunftsprüfung§556g, kein vollständiger Anspruch. Eine unwirksame oder abgelaufene Gebietsverordnung nicht als TRUE vorgeben. Keine automatische Rundung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556d_T0001, BGB_556d_T0002, BGB_556d_T0009, BGB_556d_T0013

```python
from bgbcalc import mietpreisbegrenzung_grundbetrag
mietpreisbegrenzung_grundbetrag(
    ortsuebliche_vergleichsmiete='0',
    gebiet_rechtswirksam_bestimmt=True,
    ausnahme_von_556d=False,
    anwendungsnachweis='Synthetische gültige Gebietsverordnung und Vergleichsmiete; keine nutzbare Ausnahme.',
)
```

## mietpreisbegrenzung_vormietgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `grundbetrag_556d`: Nichtnegativer exakter EUR-Monatsbetrag nach§556d Absatz1 im konkreten Anwendungsfall. Kann aus mietpreisbegrenzung_grundbetrag stammen; deren NICHT_ANWENDBAR-Ergebnis nicht durch null EUR ersetzen.
- `beruecksichtigungsfaehige_vormiete`: Nichtnegative, rechtlich geschuldete letzte Vormiete in EUR pro Monat, bereits um die Nichtberücksichtigung von Mietminderungen und im letzten Jahr vor Beendigung vereinbarten Mieterhöhungen nach§556e Absatz1 Satz2 bereinigt. Tatsächlich gezahlter Betrag kann abweichen; keine automatische Vertrags-/Zeitreihenprüfung.
- `vormietprivileg_nutzbar`: Wahrheitswert, ob die bereinigte Vormiete im konkreten Anwendungsfall berücksichtigt werden darf, einschließlich Auskunftsvoraussetzungen§556g Absatz1a und Übergangsrecht. FALSE belässt den Grundbetrag; diese Funktion modelliert ausschließlich Grundbetrag versus Vormietweg, keine anderen Erhöhungstatbestände.
- `vormietnachweis`: Nichtleere Beschreibung der zuletzt geschuldeten Vormiete, Bereinigung und rechtlichen Nutzbarkeit einschließlich Auskunftslage. Die Höhe darf nicht frei gewählt werden.

Bei nutzbarem Vormietprivileg: höherer Betrag aus Grundbetrag und berücksichtigungsfähiger Vormiete; sonst Grundbetrag. Vormiete wird nicht zum Grundbetrag addiert.

wert ist der exakte EUR-Monatsbetrag für den Grund-/Vormietweg. BERECHNET ist kein abschließender Nachweis eines wirksamen Mietpreises.

Nur Absatz1. Modernisierungsweg nach Absatz2 separat; keine Addition eines Modernisierungsbetrags auf die Vormietgrenze. Bereinigung der Vormiete und Auskunftsvoraussetzungen sind explizite Nutzervorgaben, nicht hier automatisch geprüfte Teilregeln.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556e_T0001, BGB_556e_T0002, BGB_556e_T0005

```python
from bgbcalc import mietpreisbegrenzung_vormietgrenze
mietpreisbegrenzung_vormietgrenze(
    grundbetrag_556d='880',
    beruecksichtigungsfaehige_vormiete='0',
    vormietprivileg_nutzbar=False,
    vormietnachweis='Synthetische bereinigte rechtlich geschuldete Vormiete; Auskünfte geprüft.',
)
```
