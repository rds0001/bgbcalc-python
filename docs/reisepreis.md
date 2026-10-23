<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pauschalreise_preiserhoehungsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reisepreis`: Positiver vereinbarter Reisepreis der konkreten Pauschalreise in EUR, als exakte Dezimalzeichenfolge oder Bruchobjekt. Basis der Achtprozentprüfung; keine bereits erhöhte Basis zur Umgehung der Grenze.
- `erhoehungsbetrag`: Nichtnegativer konkret verlangter Erhöhungsbetrag in EUR, aus dem zulässigen vertraglichen Berechnungsweg. Zusammengehörige Änderungen nicht künstlich aufteilen; die gesetzliche Achtprozentgrenze selbst berechtigt nicht zu einem pauschalen Aufschlag.
- `reisebeginn`: ISO-Datum0001..9999 des rechtlich maßgeblichen Reisebeginns. Für den taggenauen Vorlauf wird20Kalendertage zurückgerechnet; Ergebnis muss im Datumsbereich liegen.
- `unterrichtungstag`: ISO-Datum der tatsächlichen rechtlich maßgeblichen Unterrichtung des Reisenden, kein Versanddatum. Genau20Tage vor Beginn genügt; spätere oder erst nach Reisebeginn liegende Unterrichtung ist nicht fristgerecht.
- `aenderungsvorbehalt_ordnungsgemaess`: Expliziter Wahrheitswert zur Vertragsgrundlage nach§651f Absatz1 Satz1 Nummer1 einschließlich Hinweis auf Senkungspflicht und Angabe des Berechnungsverfahrens. Die bloße Erwähnung möglicher Erhöhungen genügt nicht automatisch.
- `zulaessiger_kostengrund`: Expliziter Wahrheitswert, dass die konkrete Erhöhung sich unmittelbar aus einer nach Vertragsschluss eingetretenen zulässigen Energie-/Beförderungskosten-, Abgaben- oder Wechselkursänderung nach§651f Absatz1 Satz1 Nummer2 ergibt. Keine frei gewählte Kostensteigerung oder automatische Marktdatenabfrage.
- `unterrichtung_formgerecht`: Expliziter Wahrheitswert: klar und verständlich auf dauerhaftem Datenträger über Erhöhung, Gründe und Berechnung unterrichtet. Zeitliche Rechtzeitigkeit wird zusätzlich berechnet.
- `berechnungsnachweis`: Nichtleere Beschreibung des vertraglichen Berechnungswegs, Kostenereignisses, Reisepreises und Unterrichtung. Preisformel aus Vertrag nicht vom Programm erfunden.

Achtprozentbetrag=Reisepreis×2/25. Einseitige Grenze überschritten nur bei größerem Erhöhungsbetrag. Unterrichtung spätestens Reisebeginn minus20Kalendertage. Voraussetzungen der einseitigen Erhöhung nur bei eingehaltenen beiden Grenzen und drei vorgegebenen Vertrags-/Grund-/Formbedingungen.

wert enthält achtprozentbetrag als EUR-Bruch, achtprozentgrenze_ueberschritten, spaetester_unterrichtungstag als ISO-Datum, zwanzigtage_vorlauf_eingehalten und einseitige_erhoehungsvoraussetzungen_erfuellt. BERECHNET kann FALSE-Ergebnisse enthalten.

Keine Berechnung zulässiger Vertragsformel aus Energie-/Abgaben-/Wechselkursdaten. Über8Prozent ist keine einseitige Erhöhung möglich; Angebotsweg§651g mit Informations-/Annahmevoraussetzungen bleibt getrennt. Sonstige Vertragsänderungen nicht mitberechnet. Keine Feiertagsverschiebung zu Lasten des Vorlaufs.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651f_T0001, BGB_651f_T0002, BGB_651f_T0003, BGB_651f_T0004, BGB_651f_T0005, BGB_651f_T0006, BGB_651f_T0007, BGB_651f_T0008, BGB_651g_T0001, BGB_651g_T0006

```python
from bgbcalc import pauschalreise_preiserhoehungsgrenze
pauschalreise_preiserhoehungsgrenze(
    reisepreis='1000',
    erhoehungsbetrag='79.99',
    reisebeginn='2026-06-21',
    unterrichtungstag='2026-05-31',
    aenderungsvorbehalt_ordnungsgemaess=False,
    zulaessiger_kostengrund=False,
    unterrichtung_formgerecht=False,
    berechnungsnachweis='Synthetische geprüfte Vertragsformel und nachvertragliche Kostenänderung.',
)
```

## pauschalreise_preissenkung_erstattung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reisepreis`: Nichtnegativer ursprünglicher Reisepreis in EUR vor der konkreten Senkung nach§651f Absatz4.
- `preissenkungsbetrag`: Nichtnegativer gesetzlich/vertraglich korrekt ermittelter Senkungsbetrag in EUR, höchstens Reisepreis. Bereits bewertete Ersparnisfolge der einschlägigen Kostenänderung; keine allgemeine Minderung wegen Reisemängeln.
- `geleistete_zahlung`: Nichtnegative bereits geleistete Zahlung auf den Reisepreis in EUR. Ein noch nicht gezahlter Preisanteil ist keine rückzahlbare Überzahlung.
- `tatsaechliche_verwaltungsausgaben`: Nichtnegative tatsächlich entstandene und im konkreten Fall gesetzlich abzugsfähige Verwaltungsausgaben in EUR; keine pauschal angenommene Bearbeitungsgebühr. Abzug nur aus gezahltem Mehrbetrag, höchstens dessen Höhe.
- `senkungsvoraussetzungen_erfuellt`: Wahrheitswert: vertraglicher Erhöhungsvorbehalt besteht und einschlägige nach Vertragsschluss, vor Reisebeginn eingetretene Preis-/Abgaben-/Wechselkursänderung führt zu geringeren Veranstalterkosten. Berechnungsweg rechtlich geprüft; FALSE ergibt NICHT_ANWENDBAR.
- `berechnungsnachweis`: Nichtleere Beschreibung von Kostenänderung, Senkungsberechnung, Zahlungen und tatsächlich abzugsfähigen Verwaltungsausgaben; Nachweisverlangen des Reisenden gesondert erfüllen.

Gesenkter Preis=Reisepreis minus Senkung. Gezahlter Mehrbetrag=max(Zahlung minus gesenkter Preis,0). Verwaltungsabzug=min(tatsächliche abzugsfähige Ausgaben,Mehrbetrag). Erstattung=Mehrbetrag minus Abzug.

wert enthält gesenkter_reisepreis, gezahlter_mehrbetrag, verwaltungsabzug und erstattungsbetrag als exakte EUR-Brüche; bei fehlender Anwendbarkeit null.

Nur Senkung§651f Absatz4, nicht Reisemangelminderung. Verwaltungskosten erhöhen nicht den gesenkten Vertragspreis und erzeugen keine zusätzliche Forderung. Kostenänderungsformel und tatsächliche Abzugsfähigkeit extern; keine Pauschalgebühr erfinden.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651f_T0013, BGB_651f_T0014, BGB_651f_T0015, BGB_651f_T0016

```python
from bgbcalc import pauschalreise_preissenkung_erstattung
pauschalreise_preissenkung_erstattung(
    reisepreis='1000',
    preissenkungsbetrag='100',
    geleistete_zahlung='0',
    tatsaechliche_verwaltungsausgaben='0',
    senkungsvoraussetzungen_erfuellt=True,
    berechnungsnachweis='Synthetische Senkungsberechnung und tatsächlich entstandene abzugsfähige Ausgaben.',
)
```
