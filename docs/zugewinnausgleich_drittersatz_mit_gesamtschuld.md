<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zugewinnausgleich_drittersatz_mit_gesamtschuld

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `ausgleichsforderung`: Ursprüngliche rechtlich bestimmte Ausgleichsforderung vor den hier erfassten Erfüllungen.
- `endnettovermoegen`: Vorzeichenbehafteter Wert nach Verbindlichkeitsabzug bei Beendigung des Güterstands; Tatbestandsvergleich, nicht Zahlungshöchstbetrag.
- `bereicherungsrechtlicher_zuwendungswert`: Nach818qualifizierter Geldherausgabewert vor dem getrennt eingegebenen Entreicherungsabzug.
- `anrechenbare_entreicherung`: Rechtlich zulässiger Entreicherungsabzug; verschärfte Haftung vorher beurteilen.
- `erfuellung_ehegatte`: Bereits schuldbefreiend auf dieselbe Ausgleichsforderung geleisteter Betrag des Ehegatten.
- `erfuellung_dritter`: Bereits schuldbefreiend auf dieselbe Ausgleichsforderung geleisteter Betrag des Dritten; keine zusätzliche zweite Forderung.
- `begrenzungsmodell`: Zwingend rechtlich qualifiziert: ausgleichsforderung_als_obergrenze. Keine stillschweigende Begrenzung auf bloßen Vermögensfehlbetrag.
- `methodennachweis`: 1390I/II-Benachteiligungs-/Kenntnisvoraussetzungen, bereicherungsrechtliche Bewertung, Forderungsobergrenze und Erfüllungswirkung ausdrücklich belegen.

Vermögensfehlbetrag als Tatbestandsvergleich bestimmen, qualifizierten Bereicherungsrest auf Forderung begrenzen und gemeinsame Erfüllungen ohne Doppelabzug verrechnen.

Betragsmerkmal, Vermögensfehlbetrag, Bereicherungsrest, bedingter Drittgrundbetrag, gemeinsame Restforderung und verbleibender Drittersatz.

Bedingtes1390-Geldersatzmodell mit ausdrücklich qualifizierter Forderungsobergrenze: Tatbestandsmerkmal ursprünglicheAusgleichsforderung>Endnettovermögen selbst vergleichen. Bereicherungsrest durch vorhandenen818-Kern. Drittgrundbetrag bei erfülltem Betragsmerkmal=min(Bereicherungsrest,ursprünglicheAusgleichsforderung), nicht min(...,Vermögensfehlbetrag). Rechtliche Geltung dieser Forderungsobergrenze wird als Voraussetzung verlangt, nicht abschließend aus der Reformbegründung2009 behauptet. Beide Erfüllungsbeträge einmal von der gemeinsamen Forderung abziehen; Drittrest=min(noch offener gemeinsamer Forderung,Drittgrundbetrag-Dritterfüllung). Ehegattenzahlung verkleinert die gemeinsame Restforderung, ist aber nicht zusätzlich nochmals vom individuellen Drittrahmen abzuziehen. Ursprüngliches Betragsmerkmal nicht nachträglich anhand der bereits getilgten Forderung neu prüfen. Keine über den ursprünglichen Anspruch hinausgehenden Nebenforderungen; Sachherausgabe zur Abwendung nur bei rechtlich bestimmter Erfüllungsbewertung als Erfüllungsbetrag erfassen. §1390III-Verjährungsbeginn bleibt separate Kalenderbindung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_422_T0001, BGB_422_T0002, BGB_422_T0003, BGB_818_T0001, BGB_818_T0002, BGB_818_T0003, BGB_818_T0004, BGB_1390_T0001, BGB_1390_T0002, BGB_1390_T0003, BGB_1390_T0004, BGB_1390_T0005, BGB_1390_T0006, BGB_1390_T0007, BGB_1390_T0008, BGB_1390_T0009, BGB_1390_T0010

```python
from bgbcalc import zugewinnausgleich_drittersatz_mit_gesamtschuld
zugewinnausgleich_drittersatz_mit_gesamtschuld(
    ausgleichsforderung='100',
    endnettovermoegen='80',
    bereicherungsrechtlicher_zuwendungswert='50',
    anrechenbare_entreicherung='0',
    erfuellung_ehegatte='0',
    erfuellung_dritter='0',
    begrenzungsmodell='ausgleichsforderung_als_obergrenze',
    methodennachweis='Bedingtes1390-Geldersatzmodell mit ausdrücklich qualifizierter Forderungsobergrenze: Tatbestandsmerkmal ursprünglicheAusgleichsforderung>Endnettovermögen selbst vergleichen. Bereicherungsrest durch vorhandenen818-Kern. Drittgrundbetrag bei erfülltem Betragsmerkmal=min(Bereicherungsrest,ursprünglicheAusgleichsforderung), nicht min(...,Vermögensfehlbetrag). Rechtliche Geltung dieser Forderungsobergrenze wird als Voraussetzung verlangt, nicht abschließend aus der Reformbegründung2009 behauptet. Beide Erfüllungsbeträge einmal von der gemeinsamen Forderung abziehen; Drittrest=min(noch offener gemeinsamer Forderung,Drittgrundbetrag-Dritterfüllung). Ehegattenzahlung verkleinert die gemeinsame Restforderung, ist aber nicht zusätzlich nochmals vom individuellen Drittrahmen abzuziehen. Ursprüngliches Betragsmerkmal nicht nachträglich anhand der bereits getilgten Forderung neu prüfen. Keine über den ursprünglichen Anspruch hinausgehenden Nebenforderungen; Sachherausgabe zur Abwendung nur bei rechtlich bestimmter Erfüllungsbewertung als Erfüllungsbetrag erfassen. §1390III-Verjährungsbeginn bleibt separate Kalenderbindung.',
)
```
