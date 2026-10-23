<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vertragsstrafe_schadensmindestbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `strafbetrag`: Nichtnegative wirksame Vertragsstrafe in EUR als Dezimalzeichenfolge oder exakter Bruch. Bereits rechtswirksam herabgesetzten Betrag verwenden, falls einschlägig; keine automatische Angemessenheitsformel nach§343.
- `ersatzfaehiger_schaden`: Nichtnegativer rechtlich festgestellter Schaden in EUR aus derselben Nichterfüllung oder nicht gehörigen Erfüllung, auf die sich die Strafe bezieht. Andere Schäden/Ansprüche separat; keinen bereits mit Strafe addierten Betrag eingeben.
- `strafart`: Auswahl nichterfuellung (§340) oder nicht_gehoerige_erfuellung (§341, einschließlich Verspätung). Rechtswirksamen Vertragsinhalt vorab einordnen.
- `strafe_verwirkt`: Wahrheitswert einer rechtlich verwirkten wirksamen Vertragsstrafe; Auslöser extern rechtlich qualifizieren. Weitere Einwendungen vorab klären.
- `erfuellung_angenommen`: Wahrheitswert, ob der Gläubiger die Erfüllung angenommen hat. Bei Strafe für nicht gehörige Erfüllung führt dies zur gesetzlichen Vorbehaltsprüfung.
- `vorbehalt_bei_annahme`: Wahrheitswert eines wirksamen Vorbehalts des Rechts auf Strafe gerade bei Annahme der Erfüllung. Späterer Vorbehalt genügt nicht automatisch. Nur bei§341 und erfolgter Annahme maßgeblich.
- `schadensersatzanspruch_besteht`: Wahrheitswert eines bestehenden Schadensersatzanspruchs für denselben gesicherten Verstoß. Strafe allein setzt keinen zusätzlichen Schadensersatzanspruch voraus. Ohne Strafe kann ein unabhängig bestehender Schadensersatzanspruch fortbestehen.
- `bewertungsnachweis`: Nichtleere Beschreibung von wirksamem Strafbetrag, Schadensgrundlage/-höhe, Verwirkung, Strafart und gegebenenfalls Erfüllungsannahme samt Vorbehalt. Keine weiteren Ausschlüsse/Erfüllungseinwände im modellierten Fall.

Verlangbare Strafe als Mindestbetrag: bei nicht gehöriger Erfüllung und Annahme nur mit Vorbehalt. Gesamt=max(verlangbare Strafe, bestehender ersatzfähiger Schaden). Weiterer Schaden=Gesamt minus Strafmindestbetrag.

wert enthält strafe_nach_diesen_voraussetzungen_verlangbar als Wahrheitswert sowie strafmindestbetrag, weiterer_schadensbetrag, gesamtbetrag als exakte EUR-Brüche. Fehlende Verwirkung/Vorbehalt ergibt Strafmindestbetrag0, aber nicht automatisch Schaden0.

Nur Geldansprüche aus demselben gesicherten Verstoß. Keine Addition voller Strafe und voller Schadenhöhe. Keine Entscheidung über Erfüllungsausschluss durch Erklärung§340 Absatz1 oder gerichtliche Herabsetzung§343. Schadenanspruch kann trotz verlorenen Strafanspruchs bestehen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_340_T0001, BGB_340_T0002, BGB_340_T0003, BGB_340_T0004, BGB_341_T0001, BGB_341_T0002, BGB_341_T0003

```python
from bgbcalc import vertragsstrafe_schadensmindestbetrag
vertragsstrafe_schadensmindestbetrag(
    strafbetrag='500',
    ersatzfaehiger_schaden='0',
    strafart='nichterfuellung',
    strafe_verwirkt=False,
    erfuellung_angenommen=False,
    vorbehalt_bei_annahme=False,
    schadensersatzanspruch_besteht=False,
    bewertungsnachweis='Synthetischer wirksamer Strafbetrag und kausaler Schaden desselben Verstoßes.',
)
```
