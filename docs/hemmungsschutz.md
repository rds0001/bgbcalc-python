<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_familienhemmung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beziehungsart`: Auswahl ehegatten, lebenspartner, kind_eltern, kind_partner_elternteil, vormund_muendel, betreuer_betreuter, pfleger_pflegling oder kind_gegen_beistand. Letztere ausschließlich Anspruch des Kindes gegen den Beistand, nicht umgekehrte Richtung. Bei den anderen Arten Anspruch zwischen beiden bezeichneten Personen; keine beliebigen Angehörigen.
- `rechtsbeziehung_besteht`: Expliziter Wahrheitswert, ob die bezeichnete rechtliche Beziehung am Stichtag besteht. Bei Ehe/Lebenspartnerschaft rechtlicher Bestand, nicht bloß Zusammenwohnen. Bei Kind/Elternteilpartner rechtlich einschlägige Verbindung geprüft; Vormundschaft/Betreuung/Pflegschaft/Beistandschaft für maßgeblichen Zeitraum belegen.
- `stichtag`: ISO-Datum0001..9999 zur Prüfung des Hemmungstatbestands. Tatsachen müssen gerade zu diesem Tag zutreffen; kein abschließender Verjährungstag und keine automatische Feststellung des Fristbeginns.
- `geburtsdatum_kind`: ISO-Geburtsdatum für kind_eltern und kind_partner_elternteil erforderlich, sonst optional. Bei Angabe nicht nach Stichtag. Altersgrenze Vollendung21 wird nur für diese beiden Beziehungstypen angewandt. Geburtstag29.Februar führt in Nichtschaltjahren zur Vollendung am1.März; berechnete Grenze muss im Kalenderbereich liegen.
- `einordnungsnachweis`: Nichtleere Beschreibung von Anspruchsrichtung, rechtlicher Beziehung, deren Bestand am Stichtag und gegebenenfalls Geburtsdatum. Eintritt vor Ablauf der betreffenden Verjährung gesondert prüfen.

Rechtsbeziehung am Stichtag muss bestehen. Zusätzlich nur bei Kind/Eltern beziehungsweise Kind/Elternteilpartner: Stichtag vor Vollendung21. Beistandschaft nur Anspruchsrichtung Kind gegen Beistand.

wert enthält altersbegrenzung_anwendbar, altersvoraussetzung_erfuellt (ohne Altersgrenze TRUE) und hemmungstatbestand_am_stichtag als Wahrheitswerte.

Keine Berechnung von Hemmungstagen;§208 bleibt unabhängig. Keine Hemmung allein wegen beliebiger Verwandtschaft oder bloß tatsächlichen Zusammenwohnens. Keine Wiederbelebung einer bereits verjährten Forderung.

ISO-Daten0001..9999; explizite Wahrheitswerte; nichtleerer Nachweis. Fehlende Pflichtwerte EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_207_T0001, BGB_207_T0002, BGB_207_T0003, BGB_207_T0004, BGB_207_T0005, BGB_207_T0006, BGB_207_T0007, BGB_207_T0008, BGB_207_T0009, BGB_207_T0010, BGB_207_T0011

```python
from bgbcalc import verjaehrung_familienhemmung
verjaehrung_familienhemmung(
    beziehungsart='ehegatten',
    rechtsbeziehung_besteht=False,
    stichtag='2025-02-28',
    geburtsdatum_kind='2004-02-29',
    einordnungsnachweis='Synthetische rechtlich eingeordnete Personenbeziehung und Anspruchsrichtung.',
)
```

## verjaehrung_sexuelle_selbstbestimmung_hemmung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `geburtsdatum`: ISO-Geburtsdatum des Gläubigers, nicht nach Stichtag. Vollendung21 nach§§187/188, einschließlich Schaltjahrregeln; berechnete Altersgrenze muss0001..9999 sein.
- `stichtag`: ISO-Datum0001..9999, für das der Hemmungstatbestand geprüft wird. Anspruch und Verjährungslage rechtlich vorab einordnen; kein automatischer Beginn oder Ablauf der Frist.
- `anspruch_wegen_sexueller_selbstbestimmung`: Wahrheitswert zur rechtlichen Anspruchseinordnung gerade wegen Verletzung sexueller Selbstbestimmung. FALSE schließt nur den Tatbestand des§208 aus, nicht sämtliche Hemmungsgründe.
- `gemeinschaft_bei_verjaehrungsbeginn`: Wahrheitswert, ob Gläubiger bei Beginn der betreffenden Verjährung mit Schuldner in häuslicher Gemeinschaft lebte. Später erstmals begründete Gemeinschaft hier nicht einsetzen.
- `gemeinschaft_ununterbrochen_bis_stichtag`: Wahrheitswert, ob dieselbe bei Verjährungsbeginn bestehende Gemeinschaft am Stichtag noch nicht beendet ist. Erneutes Zusammenleben nach Beendigung nicht als ununterbrochene Fortsetzung behandeln. Nur zusammen mit gemeinschaft_bei_verjaehrungsbeginn maßgeblich; keine Gleichsetzung mit bloßer Ehe.
- `einordnungsnachweis`: Nichtleere Beschreibung von Anspruchsart, Geburtsdatum, maßgeblichem Verjährungsbeginn und Bestand beziehungsweise Beendigung derselben häuslichen Gemeinschaft. Rechtliche Normalisierung untertägiger Änderungen gesondert.

Bei qualifiziertem Anspruch Hemmung bis Vollendung21 ODER solange die bereits bei Verjährungsbeginn bestehende häusliche Gemeinschaft noch ununterbrochen fortbesteht. Beide Gründe einzeln und als Vereinigung ausweisen.

wert enthält altershemmung, gemeinschaftshemmung und hemmungstatbestand_am_stichtag als Wahrheitswerte; fehlende Anspruchsqualifikation ergibt alle FALSE.

Keine automatische Tatsachenbewertung, keine Addition überlappender Hemmungen, kein endgültiger Verjährungstag. Wiederaufnahme einer beendeten Gemeinschaft nicht als durchgehende Hemmung behandeln. Andere Gründe wie§207 bleiben gesondert.

ISO-Daten0001..9999; explizite Wahrheitswerte; nichtleerer Nachweis. Fehlende Pflichtwerte EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_208_T0001, BGB_208_T0002, BGB_207_T0011

```python
from bgbcalc import verjaehrung_sexuelle_selbstbestimmung_hemmung
verjaehrung_sexuelle_selbstbestimmung_hemmung(
    geburtsdatum='2004-02-29',
    stichtag='2025-02-28',
    anspruch_wegen_sexueller_selbstbestimmung=False,
    gemeinschaft_bei_verjaehrungsbeginn=False,
    gemeinschaft_ununterbrochen_bis_stichtag=False,
    einordnungsnachweis='Synthetischer qualifizierter Anspruch und zeitlich abgegrenzte Gemeinschaft.',
)
```
