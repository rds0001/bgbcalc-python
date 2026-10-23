<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## schuldverschreibung_vorlegungsfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `urkundenart`: hauptschuldverschreibung, zinsschein, rentenschein oder gewinnanteilschein; rechtlich qualifizierte Urkunde im Anwendungsbereich§801.
- `leistungszeit_am`: ISO-Datum des Eintritts der für die Leistung bestimmten Zeit; nicht automatisch Ausgabe oder Erwerb der Urkunde.
- `leistungszeit_beginnart`: ereignis oder tagesbeginn: rechtliche Einordnung der bestimmten Leistungszeit bei Hauptschuldverschreibung nach§187. Ein festgelegter Tagesbeginn zählt mit. Bei Scheinen ohne Einfluss auf den gesetzlichen Jahresschlussbeginn; Eingabe wird dennoch validiert.
- `prueftag`: ISO-Datum ab Eintritt der Leistungszeit. Prüfung zum Ende des Prüftags: Ablauf/Erlöschen ab Ablauf des Endtags; tatsächliche rechtzeitige Wahrung am Endtag wird berücksichtigt.
- `vorlegung_am`: Optionales ISO-Datum qualifizierter Vorlegung gerade beim Aussteller zur Einlösung, zwischen Leistungszeit und Prüftag. NULL bedeutet nicht erfolgt, nicht unbekannt. Frühere Handlungen außerhalb dieses Modells.
- `gerichtliche_geltendmachung_am`: Optionales rechtlich maßgebliches ISO-Datum gerichtlicher Geltendmachung gerade des Anspruchs aus der Urkunde, zwischen Leistungszeit und Prüftag. NULL bedeutet nicht erfolgt. Bloße Mahnung/Verlustanzeige ist kein Ersatz.
- `gesetzlicher_unveraenderter_fristenlauf`: Expliziter Wahrheitswert: gesetzliche Fristen ohne abweichende Urkundenbestimmung§801 Absatz3, ohne Zahlungssperrenhemmung§802, sonstige Hemmung/Neubeginn oder Kalenderkorrekturen. FALSE ergibt NICHT_ANWENDBAR; solche Änderungen nicht als Standardsachverhalt berechnen.
- `einordnungsnachweis`: Nichtleere Begründung von Urkundenart, Leistungszeit/Beginnart, Vorlegung/Geltendmachung und unverändertem Fristenlauf.

Hauptschuldverschreibung30 Jahre ab bestimmter Leistungszeit; Scheine4 Jahre ab Ende des Leistungsjahrs. Vorlegung oder gerichtliche Geltendmachung spätestens am Fristende wahrt. Ohne Wahrung Erlöschen zum Ablauf des Endtags; bei Wahrung zweijährige Verjährungsgrundfrist ab Vorlegungsfristende, nicht ab tatsächlicher Vorlegung.

wert enthält vorlegungsfristende, vorlegungsfrist_gewahrt, anspruch_nach_801_erloschen, verjaehrungsgrundfristende (nur bei Wahrung, sonst null), verjaehrungsgrundfrist_abgelaufen. Keine automatische Ausübung einer Verjährungseinrede.

Abweichende Urkundenfristen und sonstige Friständerungen einschließlich§802 nicht im Standardmodell. Keine Gleichsetzung Verjährung/Erlöschen. Eigenständige Verlustansprüche§804 und Selbständigkeit der Zinsscheine§803 separat.

ISO-Daten und Grenzen0001..9999, geschlossene Urkunden-/Beginnartauswahl, expliziter Wahrheitswert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_801_T0001, BGB_801_T0002, BGB_801_T0003, BGB_801_T0004, BGB_801_T0005, BGB_801_T0006

```python
from bgbcalc import schuldverschreibung_vorlegungsfrist
schuldverschreibung_vorlegungsfrist(
    urkundenart='hauptschuldverschreibung',
    leistungszeit_am='2000-01-15',
    leistungszeit_beginnart='tagesbeginn',
    prueftag='2030-01-14',
    vorlegung_am=None,
    gerichtliche_geltendmachung_am=None,
    gesetzlicher_unveraenderter_fristenlauf=True,
    einordnungsnachweis='Synthetisch qualifizierte Inhaberschuldverschreibung; Leistung ab Tagesbeginn, keine Friständerung.',
)
```
