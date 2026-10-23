<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fortsetzung_interne_schuldanteile

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `gesamtgutschuld`: Qualifizierte unter1504fallende Gesamtgutschuld.
- `abkoemmlinge`: Nichtleere Liste mit abkoemmling_id und positivem anteil_gesamtgut; vollstaendige haftende Gruppe, Anteilssumme hoechstens eins.
- `haftungsnachweis`: Haftung1480, Anteilswerte und gegenstaendliche Beschraenkung1504/1990/1991 rechtlich bestimmen.

Gesamtgutschuld intern nach relativen qualifizierten Gesamtgutsanteilen verteilen; gegenstaendliche Haftungsgrenze nicht in Gelddeckel umdeuten.

Liste abkoemmling_id und interner_schuldanteil, keine Aussage ueber persoenlich durchsetzbaren Geldbetrag.

§1504 interne Verteilung der qualifizierten Gesamtgutschuld nach relativer Groesse der Gesamtgutsanteile der anteilsberechtigten Abkoemmlinge. Vorhandenen exakten Beguenstigten-Gewichtskern rein rechnerisch wiederverwenden; keine Anwendung1503III auf Glaeubigerschulden behaupten. Die Verpflichtung beschraenkt sich auf zugeteilte Gegenstaende: kein pauschaler Gelddeckel in Hoehe ihres Schaetzwerts und keine allgemeine persoenliche Nachschusspflicht. Ergebnis ist interne Schuldzuordnung vor gegenstaendlicher Vollstreckungs-/Haftungspruefung, kein bezifferter individuell durchsetzbarer Zahlungsanspruch. Keine automatische Ausfallumlage.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1480_T0001, BGB_1480_T0002, BGB_1504_T0001, BGB_1504_T0002, BGB_1990_T0001, BGB_1990_T0002, BGB_1990_T0003, BGB_1991_T0001, BGB_1991_T0002, BGB_1991_T0003, BGB_1991_T0004

```python
from bgbcalc import fortsetzung_interne_schuldanteile
fortsetzung_interne_schuldanteile(
    gesamtgutschuld='120',
    abkoemmlinge=[{'abkoemmling_id': 'A', 'anteil_gesamtgut': {'zaehler': '1', 'nenner': '8'}}, {'abkoemmling_id': 'B', 'anteil_gesamtgut': {'zaehler': '3', 'nenner': '8'}}],
    haftungsnachweis='§1504 interne Verteilung der qualifizierten Gesamtgutschuld nach relativer Groesse der Gesamtgutsanteile der anteilsberechtigten Abkoemmlinge. Vorhandenen exakten Beguenstigten-Gewichtskern rein rechnerisch wiederverwenden; keine Anwendung1503III auf Glaeubigerschulden behaupten. Die Verpflichtung beschraenkt sich auf zugeteilte Gegenstaende: kein pauschaler Gelddeckel in Hoehe ihres Schaetzwerts und keine allgemeine persoenliche Nachschusspflicht. Ergebnis ist interne Schuldzuordnung vor gegenstaendlicher Vollstreckungs-/Haftungspruefung, kein bezifferter individuell durchsetzbarer Zahlungsanspruch. Keine automatische Ausfallumlage.',
)
```
