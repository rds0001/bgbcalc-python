<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## digitalprodukt_beweislastzeitvergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `bereitstellungsart`: einmalig, befristet_dauerhaft oder unbefristet_dauerhaft. Rechtlich bestimmte Bereitstellungsart, keine Gleichsetzung dauerhafter Nutzung mit dauerhafter Bereitstellung.
- `bereitstellung_an_verbraucher_am`: ISO-Datum des tatsächlichen Bereitstellungsbeginns beim Verbraucher; auch im Regress§327uIII nicht die frühere Bereitstellung an den Vertriebspartner.
- `abweichung_gezeigt_am`: ISO-Datum des tatsächlichen Auftretens des abweichenden Zustands. Bei gleichem Datum wie Bereitstellung muss das tatsächliche Auftreten nach Bereitstellung rechtlich feststehen.
- `bereitstellungsende_am`: Bei befristet_dauerhaft: ISO-Datum des letzten eingeschlossenen Bereitstellungstags. Sonst ausdrücklich null/NULL; unbekanntes Ende darf nicht als unbefristet deklariert werden.
- `einordnungsnachweis`: Nichtleere Qualifikation von §§327kI/II, gegebenenfalls327uIII, Bereitstellungsart und tatsächlichen Zeitpunkten. Mangel, Gegenbeweis und Ausnahmen327kIII/IV gesondert.

Auftreten eines abweichenden Zustands mit Jahresgrundgrenze oder tatsächlichem dauerhaften Bereitstellungszeitraum vergleichen.

wert enthält zeitfenster_beginn_am, zeitfenster_ende_am (null/NULL nur für unbefristete Dauerbereitstellung) und abweichung_im_zeitfenster. Zeitliche Voraussetzung, keine abschließende Beweislastentscheidung.

Bei einmaliger Bereitstellung Jahresgrundgrenze nach§327kI/§§187I/188; bei dauerhafter Bereitstellung tatsächlicher qualifizierter Bereitstellungszeitraum nach§327kII. Beginn jeweils Bereitstellung an den Verbraucher, auch nach§327uIII. Abweichung muss innerhalb einschließlich Anfangs-/Endtag auftreten; tatsächliche Reihenfolge am selben Tag ist qualifiziert. Unbefristete Bereitstellung hat keine erfundene maximale Jahresgrenze. Ergebnis bezeichnet ausschließlich zeitliche Voraussetzung, keine automatische Beweislast-, Mangel- oder Haftungsentscheidung. Technische Umgebung, Mitwirkung und Belehrung nachAbsätzen3/4 separat; keine193Verlängerung des Beobachtungszeitraums.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_327k_T0001, BGB_327k_T0002, BGB_327k_T0003, BGB_327k_T0004, BGB_327k_T0005, BGB_327k_T0006, BGB_327k_T0007, BGB_327k_T0008, BGB_327u_T0007

```python
from bgbcalc import digitalprodukt_beweislastzeitvergleich
digitalprodukt_beweislastzeitvergleich(
    bereitstellungsart='befristet_dauerhaft',
    bereitstellung_an_verbraucher_am='2024-01-01',
    abweichung_gezeigt_am='2025-06-30',
    bereitstellungsende_am='2025-06-30',
    einordnungsnachweis='Bei einmaliger Bereitstellung Jahresgrundgrenze nach§327kI/§§187I/188; bei dauerhafter Bereitstellung tatsächlicher qualifizierter Bereitstellungszeitraum nach§327kII. Beginn jeweils Bereitstellung an den Verbraucher, auch nach§327uIII. Abweichung muss innerhalb einschließlich Anfangs-/Endtag auftreten; tatsächliche Reihenfolge am selben Tag ist qualifiziert. Unbefristete Bereitstellung hat keine erfundene maximale Jahresgrenze. Ergebnis bezeichnet ausschließlich zeitliche Voraussetzung, keine automatische Beweislast-, Mangel- oder Haftungsentscheidung. Technische Umgebung, Mitwirkung und Belehrung nachAbsätzen3/4 separat; keine193Verlängerung des Beobachtungszeitraums.',
)
```
