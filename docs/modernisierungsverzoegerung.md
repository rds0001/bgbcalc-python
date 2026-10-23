<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## modernisierung_arbeitsruhe

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ruhebeginn_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Beginns einer zusammenhängenden Arbeitsruhe, nachdem die bauliche Veränderung bereits begonnen hat. Unzusammenhängende Unterbrechungen nicht aufsummieren.
- `beginnart`: Auswahl tagesbeginn, wenn der erste Ruhetag vom Tagesbeginn an mitzählt, oder ereignis, wenn ein Ereignis im Tagesverlauf den Zeitraum auslöst und der Ereignistag nicht mitzählt. Rechtliche Einordnung§187 vorgeben; keine beliebige Auswahl zur Ergebnissteuerung.
- `wiederaufnahme_am`: ISO-Datum0001..9999 einer rechtlich wirksamen Wiederaufnahme zum Tagesbeginn, mindestens Ruhebeginn und höchstens Prüftag. Dann zählt der Vortag als letzter Ruhetag. NULL/None bedeutet am Prüftag weiterhin ununterbrochene Ruhe. Untertägige Wiederaufnahme nicht ungeprüft als Tagesbeginn normalisieren.
- `prueftag`: ISO-Datum0001..9999, mindestens Ruhebeginn; bei laufender Ruhe Prüfung bis zum Tagesschluss. Bei bereits erfolgter Wiederaufnahme entscheidet letzter Ruhetag, nicht späterer Prüftag.
- `zeitnachweis`: Nichtleere Begründung, dass Bauarbeiten schon begonnen hatten, die Ruhe ununterbrochen war, welche Beginnart gilt und ob/ab wann die Arbeiten rechtlich relevant wiederaufgenommen wurden. Sachlichen/zeitlichen Anwendungsbereich§559d prüfen.

Zwölfmonatsgrenze nach gewählter rechtlicher Beginnart berechnen. Letzter Ruhetag ist Prüftag bei laufender Ruhe, sonst Vortag tagbeginnlicher Wiederaufnahme. Nummer4 nur bei strikt späterem letzten Ruhetag.

wert enthält zwoelfmonatsgrenze, letzter_beruecksichtigter_ruhetag als ISO-Daten und arbeitsruhe_nummer_4 als Wahrheitswert.

Nur eine ununterbrochene Arbeitsruhe nach Baubeginn; keine Addition einzelner Pausen. Taggenaues Modell, untertägige Grenzfälle rechtlich gesondert; objektiver Grund separat. Genau zwölf Monate genügen nicht.

ISO-Daten und berechnete Grenzen0001..9999, explizite Auswahl und nichtleerer Nachweis. Optionale Daten ausschließlich mit der beschriebenen Bedeutung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_559d_T0005

```python
from bgbcalc import modernisierung_arbeitsruhe
modernisierung_arbeitsruhe(
    ruhebeginn_am='2024-01-01',
    beginnart='tagesbeginn',
    wiederaufnahme_am=None,
    prueftag='2024-12-30',
    zeitnachweis='Synthetische ununterbrochene Arbeitsruhe nach Baubeginn; Wiederaufnahme falls angegeben zum Tagesbeginn.',
)
```

## modernisierung_beginnverzoegerung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ankuendigungszugang_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Zugangs der Ankündigung beim Mieter. Ersatzanknüpfung nur, wenn kein Beginn angegeben wurde.
- `angekuendigter_beginn_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen angekündigten Beginns oder NULL/None, wenn hierzu tatsächlich keine Angaben erfolgt sind. Ein unklarer oder nur als Zeitraum angegebener Beginn ist vorher rechtlich zu bestimmen; NULL nicht als unbekanntes Datum missbrauchen.
- `tatsaechlicher_beginn_am`: ISO-Datum0001..9999 des tatsächlichen rechtlich relevanten Beginns der baulichen Veränderung; nicht später als Prüftag. NULL/None bedeutet am Prüftag noch nicht begonnen. Nicht bloße Vorbereitungshandlung ohne Prüfung als Baubeginn zählen.
- `prueftag`: ISO-Datum0001..9999 des Prüftags, mindestens Ankündigungszugang; laufender Sachverhalt wird taggenau bis zum Tagesschluss betrachtet. Bei bereits erfolgtem Beginn wird dessen Tag geprüft, nicht der spätere Prüftag als vermeintliche Verzögerung.
- `zeitnachweis`: Nichtleere Begründung der maßgeblichen Ankündigung, tatsächlicher Beginn/Nichtbeginn, untertägiger Normalisierung und sachlicher/zeitlicher Anwendbarkeit§559d. Andere Ankündigungen oder Änderungen nicht ohne rechtliche Prüfung austauschen.

Zwölfmonatsgrenze ereignisbezogen ab angekündigtem Beginn, nur ersatzweise Ankündigungszugang. Tatsächlicher späterer Beginn oder nach Fristablauf weiterhin fehlender Beginn erfüllt Nummer1.

wert enthält anknuepfung_am und zwoelfmonatsgrenze als ISO-Daten sowie beginnverzoegerung_nummer_1 als Wahrheitswert.

Nur zeitlicher Tatbestand; objektiver Grund und übrige Vermutungsbedingungen separat. Schon rechtzeitiger Beginn wird nicht durch späteren Prüftag verspätet. Keine automatische§193-Verschiebung tatsächlichen Baubeginns.

ISO-Daten und berechnete Grenzen0001..9999, explizite Auswahl und nichtleerer Nachweis. Optionale Daten ausschließlich mit der beschriebenen Bedeutung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_559d_T0002

```python
from bgbcalc import modernisierung_beginnverzoegerung
modernisierung_beginnverzoegerung(
    ankuendigungszugang_am='2023-12-01',
    angekuendigter_beginn_am='2024-02-29',
    tatsaechlicher_beginn_am=None,
    prueftag='2025-02-27',
    zeitnachweis='Synthetisch maßgebliche Ankündigung und tatsächlicher Bauverlauf; rechtlich eingeordnete Tagesdaten.',
)
```
