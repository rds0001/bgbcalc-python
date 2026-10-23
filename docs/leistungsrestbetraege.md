<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## miete_nach_ersparnis_und_verwertung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zeitraumsmiete`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `ersparte_aufwendungen`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `anderweitiger_verwertungsvorteil`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls, einheitlichen Abrechnungszeitraums und rechtlich qualifizierter Beträge.

Vom qualifizierten Mietbetrag ersparte Aufwendungen und anderweitigen Verwertungsvorteil abziehen, Rest mindestens null

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur §537 Absatz1 bei persönlicher Gebrauchshinderung des Mieters. Zeitraumsmiete muss Zeiträume nach Absatz2 ausschließen, für die wegen Drittüberlassung kein Mietanspruch besteht. Abzüge für denselben Zeitraum rechtlich bewerten und überschneidungsfrei eingeben. Kein zusätzlicher Anspruch auf einen negativen Rest; Mietminderung und andere Einwendungen gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_537_T0002

```python
from bgbcalc import miete_nach_ersparnis_und_verwertung
miete_nach_ersparnis_und_verwertung(
    zeitraumsmiete='1000',
    ersparte_aufwendungen='100',
    anderweitiger_verwertungsvorteil='200',
    einordnungsnachweis='Qualifizierter537I-Zeitraum ohne537II.',
)
```

## pacht_vorenthaltung_nutzungsanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_jahrespacht`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `nutzungswert_vorenthaltung`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `nutzungswert_pachtjahr`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls, einheitlichen Abrechnungszeitraums und rechtlich qualifizierter Beträge.

Vereinbarte Jahrespacht mal qualifizierter Nutzungswert der Vorenthaltung geteilt durch positiven Nutzungswert des ganzen Pachtjahrs

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur §584b für einen Abschnitt innerhalb eines Pachtjahrs; gezogene oder objektiv erzielbare Nutzungen gleichartig bewerten. Keine automatische Gleichsetzung des Nutzungsanteils mit einem Tagesanteil. Bei mehreren Pachtjahren getrennt rechnen. Weiterer Schaden und Anspruchsvoraussetzungen gesondert; nicht §597-Landpachtrechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_584b_T0001

```python
from bgbcalc import pacht_vorenthaltung_nutzungsanteil
pacht_vorenthaltung_nutzungsanteil(
    vereinbarte_jahrespacht='1200',
    nutzungswert_vorenthaltung='100',
    nutzungswert_pachtjahr='300',
    einordnungsnachweis='Qualifizierte vergleichbare Nutzungswerte eines Pachtjahrs.',
)
```

## werk_abschlagsrestbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wert_geschuldeter_erbrachter_leistungen`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `bereits_gezahlte_abschlaege`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `qualifizierter_zurueckbehaltungsbetrag`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt; einheitlicher Zeitraum und keine Doppelzählung. Jahresnutzungswert positiv und mindestens Vorenthaltungsnutzungswert.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anwendungsfalls, einheitlichen Abrechnungszeitraums und rechtlich qualifizierter Beträge.

Kumulierten Wert geschuldeter erbrachter Leistungen um bereits gezahlte Abschläge und qualifizierten Zurückbehaltungsbetrag vermindern, Rest mindestens null

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur §632a kumulierte, nachgewiesene vertragsgeschuldete Leistungen derselben Abrechnung. Nicht bloß Rechnungsnennbetrag. Angemessenen Einbehalt, einschließlich entsprechend §641 Absatz3, extern qualifizieren (vorhandener werk_maengeleinbehalt-Kern). Stoffe/Bauteile nur bei qualifiziert erfüllten Sicherungs-/Eigentumsvoraussetzungen. Keine automatische Rückforderung bei Überzahlung und kein doppelter Abzug schon verrechneter Abschläge oder Mängel. Verbraucherbau-Gesamtgrenze und Herstellungssicherheit nach §650m zusätzlich gesondert anwenden.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_632a_T0001, BGB_632a_T0002, BGB_632a_T0004

```python
from bgbcalc import werk_abschlagsrestbetrag
werk_abschlagsrestbetrag(
    wert_geschuldeter_erbrachter_leistungen='10000',
    bereits_gezahlte_abschlaege='4000',
    qualifizierter_zurueckbehaltungsbetrag='2000',
    einordnungsnachweis='Kumuliert erbrachte geschuldete Leistungen und qualifizierter Einbehalt ohne Doppelzählung.',
)
```
