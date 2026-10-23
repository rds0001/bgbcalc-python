<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## draufgabe_geldanrechnung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `anrechnungsfall`: leistung_337 oder schadensersatz_338; rechtlich bereits feststehende Anrechnung einer Geld-Draufgabe.
- `geschuldeter_betrag`: Vor Anrechnung noch geschuldeter, sachlich bestimmter Leistungs- oder Schadensersatzbetrag in Euro.
- `draufgabebetrag`: Auf denselben Betrag rechtlich anrechenbare Geld-Draufgabe in Euro; keine automatisch bewertete Sachleistung.
- `einordnungsnachweis`: Nichtleerer Nachweis von Draufgabeeigenschaft, Anrechenbarkeit und gewähltem337/338-Fall; keine entgegenstehende Vereinbarung.

Anrechenbare Geld-Draufgabe bis zur bestimmten Leistung oder zum Schadensersatz anrechnen, Restbetrag und nicht angerechneten Draufgabenteil ausweisen.

wert.angerechneter_betrag, verbleibender_betrag und nicht_angerechnete_draufgabe als exakte nichtnegative Eurobrüche.

§337I beziehungsweise338Satz2: Anrechnung einer qualifizierten Geld-Draufgabe auf den bestimmten Leistungs- beziehungsweise Schadensersatzbetrag. Anrechnung höchstens in Höhe des geschuldeten Betrags, danach rechnerischer Rest. Ein nicht angerechneter Draufgabenteil wird separat ausgewiesen; daraus folgt weder Rückzahlungsanspruch noch Verwirkung. Insbesondere bei338 keine automatische Rückzahlung des den Schaden übersteigenden Betrags. Nicht anrechenbare Sach-Draufgaben und reine Rückgabepflichten337II/338 sind keine eigenständige Geldberechnung; weder Geldersatz noch Eigentums-/Rückgabeentscheidung wird erfunden. Keine automatische Bestimmung der gesetzlichen Zweifelregel oder Anrechnung auf zusätzliche Zinsen/Kosten.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_337_T0001, BGB_338_T0001, BGB_338_T0002

```python
from bgbcalc import draufgabe_geldanrechnung
draufgabe_geldanrechnung(
    anrechnungsfall='leistung_337',
    geschuldeter_betrag='100',
    draufgabebetrag='30',
    einordnungsnachweis='§337I beziehungsweise338Satz2: Anrechnung einer qualifizierten Geld-Draufgabe auf den bestimmten Leistungs- beziehungsweise Schadensersatzbetrag. Anrechnung höchstens in Höhe des geschuldeten Betrags, danach rechnerischer Rest. Ein nicht angerechneter Draufgabenteil wird separat ausgewiesen; daraus folgt weder Rückzahlungsanspruch noch Verwirkung. Insbesondere bei338 keine automatische Rückzahlung des den Schaden übersteigenden Betrags. Nicht anrechenbare Sach-Draufgaben und reine Rückgabepflichten337II/338 sind keine eigenständige Geldberechnung; weder Geldersatz noch Eigentums-/Rückgabeentscheidung wird erfunden. Keine automatische Bestimmung der gesetzlichen Zweifelregel oder Anrechnung auf zusätzliche Zinsen/Kosten.',
)
```
