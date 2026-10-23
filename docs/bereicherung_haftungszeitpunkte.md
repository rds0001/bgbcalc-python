<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## bereicherung_haftungszeitpunkte

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `empfang_utc`: Tatsächlicher Empfang, sekundengenaues UTC.
- `kenntnis_rechtsgrundmangel_utc`: 819I-Kenntnis; None/NULL bedeutet keine rechtlich qualifizierte Kenntnis. Kenntnis schon vor Empfang wird erst ab Empfang wirksam.
- `rechtshaengigkeit_utc`: Tatsächliche818IV-Rechtshängigkeit; None/NULL wenn nicht eingetreten.
- `haftung_ab_empfang_qualifiziert`: 819II oder820I rechtlich erfüllt: Haftungsbeginn ab Empfang unabhängig von späterer Kenntnis.
- `sonderfall_820_qualifiziert`: 820I/II-Sonderfall rechtlich erfüllt; gesonderte Zins-/Nutzungsgrenze.
- `kenntnis_erfolgsverfehlung_utc`: 820II-Kenntnis von ausgebliebenem Erfolg/weggefallenem Grund; nur bei Sonderfall, None/NULL bedeutet noch nicht eingetreten.
- `einordnungsnachweis`: Tatbestände und tatsächliche UTC-Zeitpunkte qualifizieren. Allgemeine Haftungsregeln und konkrete Verlustzurechnung bleiben gesondert.

Frühestes qualifiziertes Haftungsereignis ab Empfang bestimmen; getrennten820II-Kenntniszeitpunkt ausweisen.

Optionaler Beginn verschärfter Haftung und davon getrennter optionaler820II-Zins-/Nutzungskenntniszeitpunkt.

818IV/819: frühesten einschlägigen Haftungszeitpunkt aus Rechtshängigkeit,819I-Kenntnis und qualifiziertem Empfangstatbestand berechnen; keine Haftung vor Empfang.820I setzt Haftung ab Empfang voraus;820II-Zins-/Nutzungsgrenze bleibt davon getrennt beim tatsächlichen Kenntniszeitpunkt. Fehlende Kenntnis erzeugt keinen fiktiven Zinsstart. Keine automatische Gleichsetzung mit dem Folgetag eines291-Prozesszinsbeginns; Umrechnung auf rechtlich qualifizierte Zinstage mit vorhandener Kalender-/Zinsrechnung gesondert. Keine pauschale Streichung jeder Entreicherung nach einem Datum: allgemeine Haftungsregeln, Zurechnung und820II-Nutzungsentreicherung unterscheiden.821-Verjährungseinrede hat keine weitere Betragsformel.822-Herausgabe des Dritten nur im rechtlich festgestellten Umfang des durch unentgeltliche Weitergabe verursachten Haftungsausschlusses, keine doppelte Forderung für denselben Vermögenswert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_818_T0001, BGB_818_T0002, BGB_818_T0003, BGB_818_T0004, BGB_819_T0001, BGB_819_T0002, BGB_820_T0001, BGB_820_T0002, BGB_820_T0003, BGB_821_T0001, BGB_822_T0001

```python
from bgbcalc import bereicherung_haftungszeitpunkte
bereicherung_haftungszeitpunkte(
    empfang_utc='2024-01-01T00:00:00Z',
    kenntnis_rechtsgrundmangel_utc='2024-01-10T12:00:00Z',
    rechtshaengigkeit_utc='2024-01-20T12:00:00Z',
    haftung_ab_empfang_qualifiziert=False,
    sonderfall_820_qualifiziert=False,
    kenntnis_erfolgsverfehlung_utc=None,
    einordnungsnachweis='818IV/819: frühesten einschlägigen Haftungszeitpunkt aus Rechtshängigkeit,819I-Kenntnis und qualifiziertem Empfangstatbestand berechnen; keine Haftung vor Empfang.820I setzt Haftung ab Empfang voraus;820II-Zins-/Nutzungsgrenze bleibt davon getrennt beim tatsächlichen Kenntniszeitpunkt. Fehlende Kenntnis erzeugt keinen fiktiven Zinsstart. Keine automatische Gleichsetzung mit dem Folgetag eines291-Prozesszinsbeginns; Umrechnung auf rechtlich qualifizierte Zinstage mit vorhandener Kalender-/Zinsrechnung gesondert. Keine pauschale Streichung jeder Entreicherung nach einem Datum: allgemeine Haftungsregeln, Zurechnung und820II-Nutzungsentreicherung unterscheiden.821-Verjährungseinrede hat keine weitere Betragsformel.822-Herausgabe des Dritten nur im rechtlich festgestellten Umfang des durch unentgeltliche Weitergabe verursachten Haftungsausschlusses, keine doppelte Forderung für denselben Vermögenswert.',
)
```
