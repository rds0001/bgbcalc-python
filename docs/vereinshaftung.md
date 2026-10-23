<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vereins_haftungsprivileg

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `personenrolle`: Auswahl organmitglied, besonderer_vertreter oder vereinsmitglied. Maßgebliche Rolle bei der konkreten schädigenden Tätigkeit, nicht bloße allgemeine Vereinszugehörigkeit.
- `jaehrliche_verguetung`: Nichtnegative rechtlich maßgebliche Jahresvergütung für die einschlägige Tätigkeit in EUR.0 bildet Unentgeltlichkeit ab; bis einschließlich3300EUR nach lokaler Fassung. Jahresabgrenzung und Abgrenzung reinen Aufwendungsersatzes vorab prüfen; keine automatische Zwölfmonats-Hochrechnung.
- `gesetzlicher_taetigkeitsbezug`: Expliziter Wahrheitswert: beim Organ/besonderen Vertreter Schaden bei Wahrnehmung seiner Pflichten; beim Vereinsmitglied bei Wahrnehmung der ihm übertragenen satzungsgemäßen Vereinsaufgaben. Nicht jede private Handlung eines Mitglieds ist begünstigt.
- `vorsatz`: Wahrheitswert, ob der konkrete Schaden vorsätzlich verursacht wurde. Rechtliche Bewertung und Beweiswürdigung sind extern.
- `grobe_fahrlaessigkeit`: Wahrheitswert, ob der konkrete Schaden grob fahrlässig verursacht wurde. Bloß einfache Fahrlässigkeit bedeutet hier FALSE; keine erfundene Schwerequote.
- `drittersatzpflicht_besteht`: Wahrheitswert einer bereits festgestellten Ersatzpflicht gegenüber einem anderen für denselben im gesetzlichen Tätigkeitsbereich verursachten Schaden. Erst dann kommt gesetzliche Befreiung von dieser Verbindlichkeit in Betracht. Befreiung durch den Verein beseitigt nicht von selbst den Anspruch des Dritten.
- `satzungsabweichung_mitgliederhaftung`: Wahrheitswert einer maßgeblichen abweichenden Satzungsregel zu§31a Absatz1 Satz2 gemäß§40. Bei TRUE wird nur der gesetzliche Standardausschluss gegenüber Vereinsmitgliedern nicht bestätigt; andere Ansprüche/Abweichungsfolgen separat. Für reine Vereinsmitgliedsrolle nach§31b ohne Funktion.
- `bewertungsnachweis`: Nichtleere Beschreibung von Rolle, Jahresvergütung, konkretem Aufgabenbezug, Verschulden, gegebenenfalls Drittersatzpflicht und Satzungsabweichung.

Vergütung höchstens3300EUR und gesetzlicher Aufgabenbezug erforderlich. Ohne Vorsatz/grobe Fahrlässigkeit gesetzlicher Haftungsausschluss gegenüber Verein; gegenüber Mitgliedern nur Organ/besonderer Vertreter nach§31a ohne maßgebliche Satzungsabweichung. Befreiung von Drittersatzpflicht zusätzlich nur bei tatsächlich bestehender solcher Pflicht.

wert enthält verguetungsgrenze_eingehalten, haftungsausschluss_gegenueber_verein_nach_31a_31b, haftungsausschluss_gegenueber_mitgliedern_nach_31a und befreiung_von_drittersatzpflicht_nach_31a_31b. Jeder Wahrheitswert bezieht sich nur auf den benannten gesetzlichen Teilmaßstab.

Keine automatische Haftung bei FALSE. Keine pauschale Freistellung von Vereinsmitgliedern gegenüber anderen Mitgliedern aus§31b. Beweislast, Vergütungsjahr, andere Anspruchsgrundlagen und tatsächliche Erfüllung des Befreiungsanspruchs gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_31a_T0001, BGB_31a_T0002, BGB_31a_T0003, BGB_31a_T0004, BGB_31a_T0005, BGB_31b_T0001, BGB_31b_T0002, BGB_31b_T0003, BGB_31b_T0004, BGB_40_T0001

```python
from bgbcalc import vereins_haftungsprivileg
vereins_haftungsprivileg(
    personenrolle='organmitglied',
    jaehrliche_verguetung='0',
    gesetzlicher_taetigkeitsbezug=False,
    vorsatz=False,
    grobe_fahrlaessigkeit=False,
    drittersatzpflicht_besteht=False,
    satzungsabweichung_mitgliederhaftung=False,
    bewertungsnachweis='Synthetische geprüfte Rolle, Jahresvergütung, Aufgabe und Drittersatzpflicht.',
)
```
