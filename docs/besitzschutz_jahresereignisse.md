<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## besitzschutz_jahresereignisse

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `stoerung_lokal_am`: Rechtlich maßgeblicher lokaler Kalendertag der Besitzentziehung/Störung.
- `stoerung_utc`: Derselbe tatsächliche Zeitpunkt als UTC-Sekundenzeitpunkt.
- `ereignisse`: Liste0..1000 mit genau ereignis_id,lokal_am,zeitpunkt_utc. Tatsächliche Besitzerlangung oder Dienstbarkeitsausübung je Normfall; jede Ereigniskennung eindeutig.
- `monatsendregel`: Explizite Monatsendmethode des gemeinsamen Rückwärtskerns: nur_taggleiche_monate oder letzter_monatstag.
- `einordnungsnachweis`: Rechtlich einschlägiger861II/862II/1029-Jahresrückblick, Ereignisart sowie konsistente lokale undUTC-Zeitpunkte. Ereignistagbezogene Rückwärtsanalogie ausdrücklich bestätigen.

Jahresrückblick berechnen, rechtlich qualifizierte Ereignisse nach lokalem Grenztag und tatsächlicher UTC-Reihenfolge auswählen und zählen.

Jahresfensterbeginn, ausgewählte Ereigniskennungen in Eingabereihenfolge, Anzahl und mindestens-ein-Merkmal.

861II/862II: zeitliches Merkmal der konkreten Besitzerlangung im letzten Jahr vor Entziehung/Störung; rechtliche Fehlerhaftigkeit und Gegenüberbeziehung separat.1029: mindestens eine qualifizierte Dienstbarkeitsausübung im Jahresfenster, keine Mindesthäufigkeit über einmal hinaus. Gemeinsamer Rückwärtskern bestimmt Grenztagesbeginn mit ausdrücklich vorgegebener Monatsendmethode. Ereignisse am Grenztag zählen, Ereignisse am Störungstag nur soweit ihrUTC-Zeitpunkt tatsächlich vor der Störung liegt. Spätere/gleichzeitige Ereignisse zählen nicht. Für861/862die konkret betrachtete Besitzerlangung eingeben; nicht jede beliebige Ausübung als Neuerwerb behandeln. Vollständige und konsistente Zeitpunkte rechtlich vorqualifiziert, keine stille UTC-zu-Lokaldatum-Umrechnung. Ausgabe nur Zeitmerkmale, keine Besitzschutzentscheidung.864-Erlöschen/Anspruchswahrung getrennt.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_861_T0001, BGB_861_T0002, BGB_862_T0001, BGB_862_T0002, BGB_862_T0003, BGB_1029_T0001

```python
from bgbcalc import besitzschutz_jahresereignisse
besitzschutz_jahresereignisse(
    stoerung_lokal_am='2024-05-10',
    stoerung_utc='2024-05-10T12:00:00Z',
    ereignisse=[{'ereignis_id': 'alt', 'lokal_am': '2023-05-09', 'zeitpunkt_utc': '2023-05-09T12:00:00Z'}, {'ereignis_id': 'grenze', 'lokal_am': '2023-05-10', 'zeitpunkt_utc': '2023-05-10T12:00:00Z'}, {'ereignis_id': 'vorher_am_tag', 'lokal_am': '2024-05-10', 'zeitpunkt_utc': '2024-05-10T11:59:59Z'}, {'ereignis_id': 'gleich', 'lokal_am': '2024-05-10', 'zeitpunkt_utc': '2024-05-10T12:00:00Z'}, {'ereignis_id': 'nachher', 'lokal_am': '2024-05-10', 'zeitpunkt_utc': '2024-05-10T12:00:01Z'}],
    monatsendregel='nur_taggleiche_monate',
    einordnungsnachweis='861II/862II: zeitliches Merkmal der konkreten Besitzerlangung im letzten Jahr vor Entziehung/Störung; rechtliche Fehlerhaftigkeit und Gegenüberbeziehung separat.1029: mindestens eine qualifizierte Dienstbarkeitsausübung im Jahresfenster, keine Mindesthäufigkeit über einmal hinaus. Gemeinsamer Rückwärtskern bestimmt Grenztagesbeginn mit ausdrücklich vorgegebener Monatsendmethode. Ereignisse am Grenztag zählen, Ereignisse am Störungstag nur soweit ihrUTC-Zeitpunkt tatsächlich vor der Störung liegt. Spätere/gleichzeitige Ereignisse zählen nicht. Für861/862die konkret betrachtete Besitzerlangung eingeben; nicht jede beliebige Ausübung als Neuerwerb behandeln. Vollständige und konsistente Zeitpunkte rechtlich vorqualifiziert, keine stille UTC-zu-Lokaldatum-Umrechnung. Ausgabe nur Zeitmerkmale, keine Besitzschutzentscheidung.864-Erlöschen/Anspruchswahrung getrennt.',
)
```
