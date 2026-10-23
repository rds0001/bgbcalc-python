<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vereins_minderheitenverlangen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `mitgliederzahl`: Positive ganze Zahl bis2^53-1 sämtlicher rechtlich maßgeblicher Vereinsmitglieder. Die Satzungsquote bezieht sich auf Mitglieder, nicht bloß auf anwesende oder stimmberechtigt abstimmende Personen einer bestimmten Versammlung.
- `verlangende_mitglieder`: Ganze Zahl0..mitgliederzahl der Mitglieder, die das gleiche konkrete Einberufungsverlangen unterstützen.
- `satzungsquote`: Optional: wirksamer satzungsmäßig bestimmter Mitgliederanteil als exakte Dezimalzeichenfolge oder Bruchobjekt, größer0 bis einschließlich1. None/NULL bedeutet keine abweichende Quote und wählt1/10. Keine automatische rechtliche Billigung einer eingegebenen Satzungsquote. Allgemeine Numerikgrenze2^53-1 gilt auch für exakte Zwischenzähler.
- `verlangen_schriftlich_begruendet`: Expliziter Wahrheitswert: Verlangen schriftlich unter Angabe des Zweckes und der Gründe, wie§37 Absatz1 verlangt. Bloßes Erreichen einer Unterschriftenzahl erfüllt die Form-/Inhaltsvoraussetzung nicht automatisch.
- `bestandsnachweis`: Nichtleere Beschreibung des vollständigen Mitgliederbestands, des verlangenden Kreises und gegebenenfalls rechtlich wirksamer Satzungsquote.

Quote aus wirksamer Satzung oder1/10. Mindestzahl=ceil(Mitgliederzahl×Quote); nur ganze Mitglieder zählen. Zusätzlich schriftliches Verlangen mit Zweck und Gründen.

wert enthält massgebliche_quote als Bruch, mindestens_verlangende als ganze Zahl sowie minderheitenschwelle_erreicht und verlangen_nach_diesen_voraussetzungen_ausreichend.

Keine automatische Zulässigkeit beliebiger Satzungsquote. Gerichtliche Ermächtigung§37 Absatz2 und weitere Verfahrensschritte nicht enthalten. Keine Abrundung bei Bruchteilen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_37_T0001

```python
from bgbcalc import vereins_minderheitenverlangen
vereins_minderheitenverlangen(
    mitgliederzahl=1,
    verlangende_mitglieder=0,
    satzungsquote=None,
    verlangen_schriftlich_begruendet=True,
    bestandsnachweis='Synthetischer vollständiger Mitgliederbestand und wirksame Satzungslage.',
)
```

## vereins_mitgliederschwellen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `mitgliederzahl`: Nichtnegative ganze Zahl bis2^53-1 der Mitglieder zum maßgeblichen Beurteilungszeitpunkt. Für Eintragung und späteres Unterschreiten den jeweils relevanten Bestand vorgeben.
- `satzungsunterzeichner`: Nichtnegative ganze Zahl bis2^53-1 rechtlich zählender Mitgliedsunterschriften unter der Satzung. Nicht bloß Zahl beliebiger Unterschriften. Dieser historisch maßgebliche Unterschriftenbestand muss nicht ungeprüft mit dem heutigen Mitgliederbestand gleichgesetzt werden.

Eintragungszahl erreicht bei mindestens7Mitgliedern. Unterschriftenzahl erreicht bei mindestens7zählenden Mitgliedsunterschriften. Untergrenze unterschritten nur bei weniger als3Mitgliedern, nicht bei genau3.

wert enthält eintragungs_mitgliederzahl_erreicht, satzungsunterschriftenzahl_erreicht und mitgliederzahl_unter_drei als Wahrheitswerte. Keine kombinierte Registerfreigabe.

Nur drei numerische Prädikate. Weitere Voraussetzungen, Soll-Regelungen, Satzungsdatum und registergerichtliche Entscheidungen getrennt. Unter3 bewirkt nicht automatisch Entziehung; Dreimonatsfrist/Anhörung§73 hier nicht berechnet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_56_T0001, BGB_59_T0003, BGB_73_T0001

```python
from bgbcalc import vereins_mitgliederschwellen
vereins_mitgliederschwellen(
    mitgliederzahl=0,
    satzungsunterzeichner=0,
)
```
