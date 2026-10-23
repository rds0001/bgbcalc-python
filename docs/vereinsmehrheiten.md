<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vereinsbeschluss_stimmenmehrheit

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beschlussart`: Auswahl ordentlich (§32 Absatz1 Satz3), satzungsaenderung (§33 Absatz1 Satz1) oder aufloesung (§41 Satz2). Zweckänderung nicht als gewöhnliche Satzungsänderung einordnen.
- `massgebliche_abgegebene_stimmen`: Nichtnegative ganze Zahl bis2^53-1 der rechtlich zählenden gültigen abgegebenen Stimmen. Stimmrechtsausschlüsse§34 sowie Behandlung ungültiger Stimmen und Enthaltungen bereits zutreffend bestimmen. Keine automatische Zählung aller anwesenden Personen als abgegebene Stimme.
- `ja_stimmen`: Ganze Zahl0..massgebliche_abgegebene_stimmen der rechtlich zählenden Zustimmungen zum konkreten Beschluss. Mehrfachstimmen nur im rechtlich zulässigen Bezugsmaßstab erfassen.
- `abweichende_satzungsregel`: Wahrheitswert einer wirksamen maßgeblichen abweichenden Satzungsregel. TRUE ergibt NICHT_ANWENDBAR. §40 erlaubt insbesondere keine Abbedingung des Stimmrechtsausschlusses§34.
- `stimmen_nachweis`: Nichtleere Beschreibung von Beschlussart, gültiger Bezugsmenge, ausgeschlossenen/ungültigen Stimmen, Enthaltungen und Satzungslage. Sonstige Wirksamkeitsanforderungen gesondert prüfen.

Ordentlicher Beschluss: mehr als die Hälfte, mindestens floor(n/2)+1 Ja-Stimmen. Satzungsänderung/Auflösung: mindestens ceil(3n/4). Ohne abgegebene Stimmen kein positiver Beschluss; mindestens1Ja-Stimme notwendig. Satzungsabweichung separat.

wert enthält mindestens_ja_stimmen und stimmenmehrheit_erreicht; ohne Stimmen Mindestwert1 bei FALSE. Bei Satzungsabweichung NICHT_ANWENDBAR mit null.

Keine Prüfung von Einberufung, Bezeichnung des Gegenstands, Beschlussfähigkeit, behördlicher Genehmigung oder Stimmrechtsausschluss aus Personenmerkmalen. Zweckänderung und Umlaufbeschluss sind gesondert. Rechnerisch erreichte Mehrheit bestätigt keine umfassende Wirksamkeit.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_32_T0003, BGB_33_T0001, BGB_34_T0001, BGB_40_T0001, BGB_40_T0002, BGB_41_T0002

```python
from bgbcalc import vereinsbeschluss_stimmenmehrheit
vereinsbeschluss_stimmenmehrheit(
    beschlussart='ordentlich',
    massgebliche_abgegebene_stimmen=0,
    ja_stimmen=0,
    abweichende_satzungsregel=False,
    stimmen_nachweis='Synthetisch rechtlich bestimmte gültige Stimmen ohne abweichende Satzung.',
)
```

## vereinsbeschluss_zustimmung_aller

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beschlussart`: ohne_versammlung (§32 Absatz3) oder zweckaenderung (§33 Absatz1 Satz2). Maßstab ist Zustimmung sämtlicher rechtlich maßgeblicher Mitglieder, nicht nur der Anwesenden.
- `mitgliederzahl`: Positive ganze Zahl bis2^53-1 sämtlicher für diesen gesetzlichen Zustimmungsmaßstab maßgeblicher Mitglieder. Keine unbegründete Reduktion auf Anwesende oder Antwortende; Stimmrechtsfragen vorab rechtlich bestimmen.
- `zustimmende_mitglieder`: Ganze Zahl0..mitgliederzahl der Mitglieder, deren Zustimmung zum identischen Beschlussinhalt wirksam erklärt wurde.
- `erforderliche_textform_gewahrt`: Wahrheitswert: beim Beschluss ohne Versammlung sämtliche Zustimmungen in Textform; bei Zweckänderung die Zustimmungen der nicht erschienenen Mitglieder in Textform. Bei keiner erforderlichen nachträglichen Zustimmung und sonst erfülltem Formmaßstab TRUE vorgeben.
- `abweichende_satzungsregel`: Wahrheitswert, ob eine nach§40 wirksame maßgebliche Satzungsabweichung den gesetzlichen Standard ersetzt. TRUE ergibt NICHT_ANWENDBAR; abweichender Beschlussmodus eigenständig prüfen.
- `zustimmungsnachweis`: Nichtleere Beschreibung des vollständigen Mitgliederbestands, identischen Beschlussinhalts, der Zustimmungen, Anwesenheit und erforderlichen Textform.

Alle-Zustimmung nur, wenn Anzahl zustimmender Mitglieder gleich vollständiger Mitgliederzahl. Zusätzliche Erfüllung der erforderlichen Textform notwendig. Wirksame Satzungsabweichung führt aus Standardmodell.

wert enthält zustimmung_aller_erreicht und zustimmungs_und_textformvoraussetzungen_erfuellt. Satzungsabweichung ergibt NICHT_ANWENDBAR und null.

Keine bloße Einstimmigkeit einer Teilversammlung. Sonstige Wirksamkeit, Sonderrechte§35 und gegebenenfalls Genehmigung§33 Absatz2 gesondert prüfen. Keine automatische Prüfung eingereichter Erklärungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_32_T0007, BGB_33_T0002, BGB_40_T0001

```python
from bgbcalc import vereinsbeschluss_zustimmung_aller
vereinsbeschluss_zustimmung_aller(
    beschlussart='ohne_versammlung',
    mitgliederzahl=7,
    zustimmende_mitglieder=0,
    erforderliche_textform_gewahrt=False,
    abweichende_satzungsregel=False,
    zustimmungsnachweis='Synthetischer vollständiger Bestand und geprüfte Zustimmungserklärungen.',
)
```

## vorstand_vertretungsmehrheit

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vorstandsmitglieder`: Positive ganze Zahl der rechtlich maßgeblichen gesamten Vorstandsmitglieder, höchstens2^53-1. Nicht nur anwesende oder bereits zustimmende Mitglieder zählen. Besetzung, Vakanzen und besondere Vertretungsregelungen vorab prüfen.
- `mitwirkende_vorstandsmitglieder`: Ganze Zahl0..vorstandsmitglieder der bei der konkreten Vertretung mitwirkenden Mitglieder. Kein bloßer Beschlussstimmenzähler.
- `rechtsform`: Auswahl verein für§26 Absatz2 Satz1 oder stiftung für§84 Absatz2 Satz2. Einzelvorstand nach jeweiligem Vertretungsgrundsatz mit einer Person.
- `abweichende_satzungsregel`: Wahrheitswert, ob eine im konkreten Fall maßgebliche wirksame abweichende Satzungsregel den gesetzlichen Mehrheitsmaßstab ersetzt. TRUE ergibt NICHT_ANWENDBAR; alternative Regel nicht automatisch unwirksam oder gleichbedeutend mit fehlender Vertretung.
- `bestandsnachweis`: Nichtleere Beschreibung des maßgeblichen Vorstandbestands, der Mitwirkung und Satzungslage. Register-/Drittwirkung und weitere Vertretungsbeschränkungen vorab einordnen.

Gesetzliche strikte Mehrheit: mindestens floor(Vorstandsmitglieder/2)+1 Mitwirkende. Erreicht, wenn Mitwirkende mindestens diese Zahl. Satzungsabweichung führt zu NICHT_ANWENDBAR.

wert enthält mindestens_mitwirkende als ganze Zahl und vertretungsmehrheit_erreicht als Wahrheitswert. Bei NICHT_ANWENDBAR null.

Aktive Vertretung von Verein/Stiftung, nicht Vorstandsbeschluss und nicht Empfang einer Erklärung. Kein abschließender Vertretungsnachweis, keine automatische Entscheidung über Vakanzen oder Umfang der Vertretungsmacht.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_26_T0002, BGB_26_T0004, BGB_40_T0001, BGB_84_T0003, BGB_84_T0004, BGB_84_T0006

```python
from bgbcalc import vorstand_vertretungsmehrheit
vorstand_vertretungsmehrheit(
    vorstandsmitglieder=1,
    mitwirkende_vorstandsmitglieder=0,
    rechtsform='verein',
    abweichende_satzungsregel=False,
    bestandsnachweis='Synthetischer vollständiger Vorstand ohne abweichende Satzungsregel.',
)
```
