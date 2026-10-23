<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vaterschaftsanfechtung_vertretergrundfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vertreterkenntnis_am`: Tag der rechtlich maßgeblichen Kenntnis des gesetzlichen Vertreters.
- `kind_geboren_am`: Geburt des Kindes, dessen Vaterschaft angefochten wird.
- `berechtigter_geboren_am`: Geburt des minderjährigen Anfechtungsberechtigten; nicht zwingend identisch mit Kindesgeburt.
- `anerkennung_wirksam_am`: Wirksame maßgebliche Anerkennung, sonst None/NULL.
- `einordnungsnachweis`: Vertreteranfechtung nach1600bII4 der festen lokalen Fassung ausdrücklich rechtlich qualifizieren; keine eigene Anfechtung des Minderjährigen.

Vorhandene allgemeine Zweijahresgrundfrist mit Mindestablauf Vollendung21 kombinieren; kein Volljährigkeitsaufschub bei Vertreteranfechtung.

Zweijahresgrundfristende, Mindestablauf Vollendung21 und späteres kombiniertes Grundfristende; ISO-Daten.

1600bII4 nimmt für Vertreteranfechtung nur Satz2 aus, nicht Satz3. Deshalb Zweijahresgrundfrist aus Vertreterkenntnis/Geburt/Anerkennung ohne Volljährigkeitsaufschub, aber Mindestablauf Vollendung21 des Berechtigten. Rechtliche Vertretungsbefugnis und zeitlich anwendbare Fassung sind vorqualifiziert. Keine automatische Hemmung1600bIV,193-Korrektur oder Zulässigkeitsprüfung. Bestehenden Kalenderkern verwenden. Vollendung21 bedeutet Ablauf des nach187II berechneten Vortags, nicht einen zusätzlichen Tag.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1600b_T0001, BGB_1600b_T0002, BGB_1600b_T0003, BGB_1600b_T0004, BGB_1600b_T0005, BGB_1600b_T0006, BGB_1600b_T0007, BGB_1600b_T0008, BGB_1600b_T0009, BGB_1600b_T0010, BGB_1600b_T0011, BGB_1600b_T0012, BGB_1600b_T0013

```python
from bgbcalc import vaterschaftsanfechtung_vertretergrundfrist
vaterschaftsanfechtung_vertretergrundfrist(
    vertreterkenntnis_am='2020-02-01',
    kind_geboren_am='2020-01-01',
    berechtigter_geboren_am='2005-03-15',
    anerkennung_wirksam_am=None,
    einordnungsnachweis='1600bII4 nimmt für Vertreteranfechtung nur Satz2 aus, nicht Satz3. Deshalb Zweijahresgrundfrist aus Vertreterkenntnis/Geburt/Anerkennung ohne Volljährigkeitsaufschub, aber Mindestablauf Vollendung21 des Berechtigten. Rechtliche Vertretungsbefugnis und zeitlich anwendbare Fassung sind vorqualifiziert. Keine automatische Hemmung1600bIV,193-Korrektur oder Zulässigkeitsprüfung. Bestehenden Kalenderkern verwenden. Vollendung21 bedeutet Ablauf des nach187II berechneten Vortags, nicht einen zusätzlichen Tag.',
)
```
