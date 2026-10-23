<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## schenkungsauflage_rueckforderungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bereicherungsrechtlicher_geschenkwert`: Nichtnegative exakte EUR-Zahl als Dezimalzeichenfolge/Bruchobjekt des nach Bereicherungsrecht herauszugebenden Geschenkswerts. Bereicherung, Entreicherung und etwaige Sachherausgabe vorher rechtlich bewerten; kein automatischer ursprünglicher Kaufpreis.
- `fuer_auflage_einzusetzender_geschenkwert`: Nichtnegative exakte EUR-Zahl des Teils des Geschenks, der zur Vollziehung gerade der nicht vollzogenen Auflage hätte verwendet werden müssen. Nicht beliebige gesamte Auflagenkosten oder Sanktionspauschale verwenden.
- `auflage_nicht_vollzogen`: Wahrheitswert des Unterbleibens der konkreten Auflage. Bei Teilvollziehung den betroffenen verbleibenden Gegenstand/Wert rechtlich abgrenzen.
- `ruecktrittsvoraussetzungen_erfuellt`: Wahrheitswert der nach§527 erforderlichen Voraussetzungen des Rücktrittsrechts gegenseitiger Verträge, einschließlich erforderlicher Fristsetzung/Entbehrlichkeit und Beachtung rechtmäßiger Verweigerung§526. Nicht bloß Nichtvollziehung gleichsetzen.
- `dritter_zur_vollziehung_berechtigt`: Wahrheitswert eines Vollziehungsanspruchs eines Dritten im Sinne§527 Absatz2; dann dieser Rückforderungsweg ausgeschlossen.
- `pflicht_oder_anstandsschenkung`: Wahrheitswert einer Schenkung zur Erfüllung sittlicher Pflicht oder aus einer auf Anstand zu nehmenden Rücksicht§534. Dann keine Rückforderung in diesem Modell.
- `einordnungsnachweis`: Nichtleere Begründung der Auflage, Nichtvollziehung, rechtlichen Rücktrittsvoraussetzungen, Drittberechtigung, Schenkungseinordnung und beider Wertgrenzen.

Bei Nichtvollziehung und Rücktrittsvoraussetzungen ohne Drittrecht/§534-Ausschluss: Minimum aus bereicherungsrechtlichem Geschenkwert und für Auflage einzusetzendem Geschenkwert.

wert ist exakter EUR-Bruch. Bei fehlenden Voraussetzungen/Ausschluss NICHT_ANWENDBAR/null, kein abschließendes Urteil über andere Anspruchsgrundlagen.

Geldmäßiger Bewertungsrahmen, keine automatische Umwandlung von Sachherausgabe in Geld. §526, Bereicherungsrecht und sonstige rechtliche Voraussetzungen vorher prüfen; nicht gesamtes Geschenk automatisch fordern.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_527_T0001, BGB_527_T0002, BGB_534_T0001

```python
from bgbcalc import schenkungsauflage_rueckforderungsbetrag
schenkungsauflage_rueckforderungsbetrag(
    bereicherungsrechtlicher_geschenkwert='1000',
    fuer_auflage_einzusetzender_geschenkwert='300',
    auflage_nicht_vollzogen=True,
    ruecktrittsvoraussetzungen_erfuellt=True,
    dritter_zur_vollziehung_berechtigt=False,
    pflicht_oder_anstandsschenkung=False,
    einordnungsnachweis='Synthetisch rechtlich abgegrenzte nicht vollzogene Auflage und bewertete Herausgabe-/Verwendungsgrenzen.',
)
```

## schenkung_verarmungsrueckforderung_ausschluss

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `geschenk_geleistet_am`: ISO-Datum0001..9999 der rechtlich fristauslösenden Leistung des geschenkten Gegenstands. Nicht bloß Schenkungsversprechen oder ungeprüfter Grundbuch-/Vertragstag. Mehrere Leistungen separat beurteilen.
- `beduerftigkeit_eingetreten_am`: ISO-Datum0001..9999 des rechtlich relevanten Eintritts der Bedürftigkeit des Schenkers, nicht Datum der späteren Rückforderung oder Klage. Vor Leistung liegende Bedürftigkeit führt hier nur zu keinem zeitlichen Ausschluss; Anspruchsvoraussetzungen§528 gesondert.
- `beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig`: Wahrheitswert, dass Schenker gerade seine Bedürftigkeit vorsätzlich oder grob fahrlässig herbeigeführt hat. Einfache Fahrlässigkeit oder allein freiwillige Schenkung nicht automatisch gleichsetzen.
- `pflicht_oder_anstandsschenkung`: Wahrheitswert der rechtlichen Privilegierung§534; sittliche Pflicht/Anstand bewerten, keine feste Betragsgrenze erfinden.
- `einordnungsnachweis`: Nichtleere Begründung von Schenkungsleistung, maßgeblichem Bedürftigkeitseintritt, schwerer Eigenverursachung und Schenkungsprivilegierung.

Zehnjahresereignisfrist ab Leistung. Bedürftigkeitseintritt nach Fristablauf ODER vorsätzliche/grob fahrlässige Herbeiführung ODER§534-Privilegierung schließt betrachtete Rückforderung aus.

wert enthält zehnjahreszeitraum_ende als ISO-Datum und zehnjahresfrist_bei_beduerftigkeit_abgelaufen sowie rueckforderung_nach_529_absatz_eins_oder_534_ausgeschlossen als Wahrheitswerte. FALSE bestätigt keinen Anspruch.

Nur§529 Absatz1/§534; Schutz des Beschenkten§529 Absatz2, Anspruchsvoraussetzungen§528, Bereicherungsrecht und Mehrbeschenktenrangfolge nicht mitberechnet. Keine Schenkungsabschmelzung§2325 und keine Verjährungsprüfung der Rückforderung.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_529_T0001, BGB_534_T0001

```python
from bgbcalc import schenkung_verarmungsrueckforderung_ausschluss
schenkung_verarmungsrueckforderung_ausschluss(
    geschenk_geleistet_am='2014-02-28',
    beduerftigkeit_eingetreten_am='2014-02-27',
    beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig=False,
    pflicht_oder_anstandsschenkung=False,
    einordnungsnachweis='Synthetisch fristauslösende Leistung und rechtlich maßgeblicher Bedürftigkeitseintritt, nicht spätere Anspruchserhebung.',
)
```
