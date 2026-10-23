<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## rueckwaertsfrist_kalendergrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `bezugstag`: ISO-Kalendertag des rechtlich maßgeblichen rückwärts betrachteten Ereignisses oder Tagesendes.
- `anzahl`: Positive ganze Zahl der zurückzurechnenden Einheiten, höchstens3652059.
- `einheit`: tage,wochen,monate oder jahre; keine Umrechnung von Monaten in30Tage.
- `bezugsart`: ereignistag: Bezugstag rückwärts nicht mitzählen, Grenze am Beginn des namens-/zahlgleichen zurückliegenden Tages. tagesende: Bezug am Ende des Bezugstags, rückwärts mitzählen, Grenze am Beginn des Folgetags des zurückliegenden Vergleichstags.
- `monatsendregel`: nur_taggleiche_monate: fehlende Tageszahl im Zielmonat wird als nicht freigegebener Fall zurückgewiesen. letzter_monatstag: ausdrücklich rechtlich qualifizierte analoge188III-Monatsendregel anwenden. Keine stillschweigende Auswahl.
- `methodennachweis`: Nichtleere Begründung der für die konkrete Norm einschlägigen Rückwärtsanalogie, Bezugsart und gegebenenfalls Monatsendregel. Keine pauschale Anwendung auf sämtliche BGB-Vorläufe.

Qualifizierten Kalenderabstand rückwärts mit bestehenden Datumshelfern berechnen; Grenztagesbeginn und vorausgehenden vollen Tag ausweisen.

grenztag_beginn und letzter_voller_tag_vor_grenze als ISO-Daten; rechtliche Verwendung nach gewähltem Normzweck.

Bedingter Kalenderkern zur ausdrücklich qualifizierten Rückwärtsanalogie187/188. Ereignistag: zurückliegender gleichbenannter/gleichzahliger Tag beginnt die Grenze; letzter voller vorausgehender Handlungstag ist dessen Vortag. Tagesende: rückwärts mitgezählter Bezugstag, Grenze am Folgetagesbeginn des zurückliegenden Vergleichstags; letzter voller Handlungstag ist Vergleichstag. Für reine Zeitfenster ist die Grenztagesbeginn-Ausgabe zu verwenden, nicht ungeprüft der letzte Handlungstag. Untertägige Zeitpunkte und rechtliche Einschließung einer einzelnen Grenzhandlung gesondert bestimmen. Monatsende nur auf ausdrückliche Methodenvorgabe; nur_taggleiche_monate verhindert eine ungesicherte Ersatzregel. Kein193-Automatismus: Verfahrenszwecke können unterschiedliche Werktagskorrekturen verlangen. Keine Inversion durch Suche nach einem beliebigen vorwärts passenden Datum. Standardkalender und bestehende Datumshelfer, unveränderte Vorwärtsfunktionen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003

```python
from bgbcalc import rueckwaertsfrist_kalendergrenze
rueckwaertsfrist_kalendergrenze(
    bezugstag='2025-12-13',
    anzahl=33,
    einheit='monate',
    bezugsart='tagesende',
    monatsendregel='nur_taggleiche_monate',
    methodennachweis='Bedingter Kalenderkern zur ausdrücklich qualifizierten Rückwärtsanalogie187/188. Ereignistag: zurückliegender gleichbenannter/gleichzahliger Tag beginnt die Grenze; letzter voller vorausgehender Handlungstag ist dessen Vortag. Tagesende: rückwärts mitgezählter Bezugstag, Grenze am Folgetagesbeginn des zurückliegenden Vergleichstags; letzter voller Handlungstag ist Vergleichstag. Für reine Zeitfenster ist die Grenztagesbeginn-Ausgabe zu verwenden, nicht ungeprüft der letzte Handlungstag. Untertägige Zeitpunkte und rechtliche Einschließung einer einzelnen Grenzhandlung gesondert bestimmen. Monatsende nur auf ausdrückliche Methodenvorgabe; nur_taggleiche_monate verhindert eine ungesicherte Ersatzregel. Kein193-Automatismus: Verfahrenszwecke können unterschiedliche Werktagskorrekturen verlangen. Keine Inversion durch Suche nach einem beliebigen vorwärts passenden Datum. Standardkalender und bestehende Datumshelfer, unveränderte Vorwärtsfunktionen.',
)
```
