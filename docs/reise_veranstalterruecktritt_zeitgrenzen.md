<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## reise_veranstalterruecktritt_zeitgrenzen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `reisedauer_tage`: Positive rechtlich maßgebliche Reisedauer in Tagen als exakte Dezimalzahl/Bruch; nicht automatisch aus gezählten Übernachtungen oder angefangenen Tagen ableiten.
- `reisebeginn_lokal_am`: Maßgeblicher lokaler Kalendertag des Reisebeginns.
- `reisebeginn_utc`: Reisebeginn als hinreichend genauer UTC-Sekundenzeitpunkt.
- `ruecktrittszugang_lokal_am`: Kalendertag des wirksamen Rücktrittszugangs am rechtlich maßgeblichen Ort.
- `ruecktrittszugang_utc`: Derselbe Zugang alsUTC-Sekundenzeitpunkt.
- `vertraglicher_letzter_ruecktritt_utc`: Rechtlich bestimmte letzte vertraglich zulässige Rücktrittszeit; genau dieser Zeitpunkt noch eingeschlossen.
- `zeitnachweis`: 651hIV1Mindestteilnehmerfall, rechtlich maßgebliche Reisedauer, Ereignistag-Rückwärtsanalogie für20/7Tage, konsistente lokale/UTC-Zuordnung und vertragliche Frist ausdrücklich qualifizieren.

Reisedauerklasse bestimmen, gesetzliche20/7Kalendertage oder48Stunden prüfen und mit vertraglicher Rücktrittszeitgrenze verbinden.

Gesetzliche Vorlaufart, optionale Kalendertage/letzter voller Zugangstag sowie getrennte und kombinierte Zeitgrenzenmerkmale.

651hIV1: mehrals6Tage→20Kalendertage Vorlauf; mindestens2bis6Tage→7Kalendertage; wenigerals2Tage→48echteStunden. Für Tagesvorläufe ausdrücklich ereignistagbezogene Rückwärtsanalogie: Grenze beginnt am zurückliegenden Vergleichstag, Zugang spätestens bis zum vorhergehenden vollen Tag; keine Umrechnung in480/168Stunden. KurzeReise sekundengenau mindestens48Stunden vor Reisebeginn. Gesetzliche und tatsächliche Vertragsgrenze müssen beide eingehalten sein; vertragliche Frist darf gesetzlichen Mindestschutz nicht verkürzen. Kein automatischer Teilnehmerzahl-/Rücktrittsgrundtest und keine Geldfolge. Reisedauer ist qualifizierte Tagesgröße; Zeitspanne der Reise nicht ungeprüft in24Stunden-Tage umdeuten. Lokaldaten gehören zuUTC-Ereignissen, keine Zeitzone erraten. Keine193-Verlängerung dieses Mindestvorlaufs.651hIV2unverzüglich bleibt qualitative Anforderung, kein erfundener fixer Stundenwert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651h_T0012, BGB_651h_T0013, BGB_651h_T0014, BGB_651h_T0015, BGB_651h_T0016, BGB_651h_T0017, BGB_651h_T0018

```python
from bgbcalc import reise_veranstalterruecktritt_zeitgrenzen
reise_veranstalterruecktritt_zeitgrenzen(
    reisedauer_tage='7',
    reisebeginn_lokal_am='2024-07-21',
    reisebeginn_utc='2024-07-21T12:00:00Z',
    ruecktrittszugang_lokal_am='2024-06-30',
    ruecktrittszugang_utc='2024-06-30T12:00:00Z',
    vertraglicher_letzter_ruecktritt_utc='2024-07-20T12:00:00Z',
    zeitnachweis='651hIV1: mehrals6Tage→20Kalendertage Vorlauf; mindestens2bis6Tage→7Kalendertage; wenigerals2Tage→48echteStunden. Für Tagesvorläufe ausdrücklich ereignistagbezogene Rückwärtsanalogie: Grenze beginnt am zurückliegenden Vergleichstag, Zugang spätestens bis zum vorhergehenden vollen Tag; keine Umrechnung in480/168Stunden. KurzeReise sekundengenau mindestens48Stunden vor Reisebeginn. Gesetzliche und tatsächliche Vertragsgrenze müssen beide eingehalten sein; vertragliche Frist darf gesetzlichen Mindestschutz nicht verkürzen. Kein automatischer Teilnehmerzahl-/Rücktrittsgrundtest und keine Geldfolge. Reisedauer ist qualifizierte Tagesgröße; Zeitspanne der Reise nicht ungeprüft in24Stunden-Tage umdeuten. Lokaldaten gehören zuUTC-Ereignissen, keine Zeitzone erraten. Keine193-Verlängerung dieses Mindestvorlaufs.651hIV2unverzüglich bleibt qualitative Anforderung, kein erfundener fixer Stundenwert.',
)
```
