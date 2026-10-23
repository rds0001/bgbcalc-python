<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## heizungsmodernisierung_mit_jahresfoerderung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kosten_wohnung`: Der Wohnung rechtlich zugeordnete Kosten vor Erhaltungspauschale/Förderabzug.
- `von_erhaltungspauschale_ausgenommene_kosten`: Qualifizierter Ausnahmeanteil nach lokaler559eII2-Fassung; sonst0.
- `kapitalzuschuesse`: Einmalige kostenmindernde559aI-Mittel;0bei ausschließlich qualifizierter laufender/Zinsförderung.
- `jaehrliche_zinsermaessigung`: Mit vorhandenem559aII/III-Kern errechneter Jahreszinsvorteil; keine Darlehenshauptsumme.
- `jaehrliche_laufende_foerderung`: Rechtlich einschlägiger559aII4-Jahresbetrag, ohne doppelte Erfassung eines Kapitalzuschusses.
- `monatliche_restkappung`: Mit559eIII/559IIIa-Kern berechnete Restkappung für diese Wohnung.
- `abzugsreihenfolge`: Zwingend qualifiziert: abzug_vor_kappung oder abzug_nach_kappung.
- `methodennachweis`: 559e-Fördertatbestand sowie Anwendung der559aII-Jahresabzugsmethode auf den konkreten559e-Fall ausdrücklich rechtlich begründen; Kappungsreihenfolge ebenfalls zwingend vorgeben.

559e-Kostenbasis und10%-Jahresumlage mit ausdrücklich qualifizierter559aII-Jahresförderung/Kappungsreihenfolge verbinden.

Erhaltungspauschale, Kostenbasis, Jahresumlage vor laufender Förderung und beide Förderkappungswege.

Bedingte Heizungsrechnung nach559e:15%des nicht nach lokaler559eII2ausgenommenen Kostenanteils als Erhaltungspauschale, dann einmaliger Kapitalbeitrag, positive Kostenbasis*10%jährlich. Qualifizierte559aII-Zins-/laufende Jahresförderung mit bestehendem Förderkappungskern berücksichtigen. Die rechtliche Übertragung dieser Jahresabzugsmethode auf den konkreten559e-Förderfall wird ausdrücklich vorausgesetzt, nicht als allgemein geklärt behauptet. Der Nennbetrag eines rückzahlbaren Darlehens wird nicht ohne Rechtsgrund als verlorener Kapitalzuschuss behandelt. Mindestens eine tatsächliche berücksichtigungsfähige Förderung erforderlich; ohne Förderung ist559-Verfahren gesondert. Kein doppelter Abzug tatsächlicher Erhaltungskosten zusätzlich zur Pauschale; keine automatische Härte-/Förderfähigkeitsentscheidung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_559_T0001, BGB_559_T0002, BGB_559_T0003, BGB_559_T0004, BGB_559_T0005, BGB_559_T0006, BGB_559_T0007, BGB_559_T0008, BGB_559_T0009, BGB_559_T0010, BGB_559_T0011, BGB_559_T0012, BGB_559_T0013, BGB_559_T0014, BGB_559_T0015, BGB_559a_T0001, BGB_559a_T0002, BGB_559a_T0003, BGB_559a_T0004, BGB_559a_T0005, BGB_559a_T0006, BGB_559a_T0007, BGB_559a_T0008, BGB_559a_T0009, BGB_559e_T0001, BGB_559e_T0002, BGB_559e_T0003, BGB_559e_T0004, BGB_559e_T0005, BGB_559e_T0006, BGB_559e_T0007, BGB_559e_T0008

```python
from bgbcalc import heizungsmodernisierung_mit_jahresfoerderung
heizungsmodernisierung_mit_jahresfoerderung(
    kosten_wohnung='10000',
    von_erhaltungspauschale_ausgenommene_kosten='0',
    kapitalzuschuesse='2000',
    jaehrliche_zinsermaessigung='100',
    jaehrliche_laufende_foerderung='20',
    monatliche_restkappung='25',
    abzugsreihenfolge='abzug_vor_kappung',
    methodennachweis='Bedingte Heizungsrechnung nach559e:15%des nicht nach lokaler559eII2ausgenommenen Kostenanteils als Erhaltungspauschale, dann einmaliger Kapitalbeitrag, positive Kostenbasis*10%jährlich. Qualifizierte559aII-Zins-/laufende Jahresförderung mit bestehendem Förderkappungskern berücksichtigen. Die rechtliche Übertragung dieser Jahresabzugsmethode auf den konkreten559e-Förderfall wird ausdrücklich vorausgesetzt, nicht als allgemein geklärt behauptet. Der Nennbetrag eines rückzahlbaren Darlehens wird nicht ohne Rechtsgrund als verlorener Kapitalzuschuss behandelt. Mindestens eine tatsächliche berücksichtigungsfähige Förderung erforderlich; ohne Förderung ist559-Verfahren gesondert. Kein doppelter Abzug tatsächlicher Erhaltungskosten zusätzlich zur Pauschale; keine automatische Härte-/Förderfähigkeitsentscheidung.',
)
```
