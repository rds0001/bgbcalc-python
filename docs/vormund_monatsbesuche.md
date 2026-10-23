<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vormund_monatliche_besuchszahlen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `pruefmonate`: Liste1..1000 eindeutiger Kalendermonate YYYY-MM, in denen der gesetzliche Regelfall einmaligen Monatsbesuchs gelten soll. Angefangene Betreuungsmonate und abweichend gebotene Intervalle zuvor rechtlich einordnen.
- `besuche`: Liste0..10000 tatsächlicher Besuche beim selben Mündel mit genau besuch_id und besuch_am als ISO-Datum. Kennungen eindeutig; verschiedene Besuche am selben Tag möglich.
- `einordnungsnachweis`: Nichtleere Qualifikation von §1790III, einheitlichem Mündel und Monaten mit Regelhäufigkeit. Besuchseigenschaft/Ort und abweichend gebotene Häufigkeit nicht aus bloßen Daten ableiten.

Tatsächliche Besuchszahlen je ausgewähltem Kalendermonat zählen und mit mindestens einem Besuch vergleichen.

wert.monate enthält chronologisch geordnet monat,besuchszahl,regelmaessiger_mindestbesuch_erreicht; zusätzlich alle_monate_mit_mindestbesuch und besuche_ausserhalb_pruefmonate. Kein abschließender Erfüllungsnachweis rechtlicher Kontaktpflichten.

§1790III nennt in der Regel einmal im Monat. Die Funktion zählt tatsächliche Besuche je qualifiziertem Kalendermonat und vergleicht mit mindestens1; sie ersetzt dies nicht durch starre30-Tage-Abstände. Alle ausgewählten Monate werden ausgewiesen, auch ohne Besuch. Besuche außerhalb der Prüfmonate werden gesondert gezählt. Kürzere/längere gebotene Besuchsabstände, ein anderer Ort, Beginn/Ende der Vormundschaft und qualitative Kontaktpflichten sind rechtlich zu bestimmen; keine automatische Pflichtverletzungs- oder Haftungsentscheidung. Mehrere Mündel getrennt auswerten.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1790_T0005, BGB_1790_T0006

```python
from bgbcalc import vormund_monatliche_besuchszahlen
vormund_monatliche_besuchszahlen(
    pruefmonate=['2024-01', '2024-02'],
    besuche=[{'besuch_id': 'A', 'besuch_am': '2024-01-31'}, {'besuch_id': 'B', 'besuch_am': '2024-02-29'}],
    einordnungsnachweis='§1790III nennt in der Regel einmal im Monat. Die Funktion zählt tatsächliche Besuche je qualifiziertem Kalendermonat und vergleicht mit mindestens1; sie ersetzt dies nicht durch starre30-Tage-Abstände. Alle ausgewählten Monate werden ausgewiesen, auch ohne Besuch. Besuche außerhalb der Prüfmonate werden gesondert gezählt. Kürzere/längere gebotene Besuchsabstände, ein anderer Ort, Beginn/Ende der Vormundschaft und qualitative Kontaktpflichten sind rechtlich zu bestimmen; keine automatische Pflichtverletzungs- oder Haftungsentscheidung. Mehrere Mündel getrennt auswerten.',
)
```
