<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## kreditwuerdigkeit_zinsermaessigung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kapital`: Nichtnegatives Kapital des einheitlichen Zinsabschnitts in Euro.
- `vertraglicher_sollzins_prozent`: Vereinbarter jährlicher Sollzins in Prozent als exakte Zahl.
- `qualifizierter_marktzins_prozent`: Passender rechtlich bestimmter Marktzinssatz am maßgeblichen Stichtag; keine automatische Marktdatenabfrage.
- `zinsart`: gebunden oder veraenderlich. Gebunden: laufzeitpassender Pfandbriefmarkt; veränderlich: Euro-Dreimonats-Interbankenmarkt nach505dI.
- `marktzins_stichtag_am`: Datum des Vertragsschlusses beziehungsweise der vereinbarten Anpassung YYYY-MM-DD, für diesen Abschnitt rechtlich maßgeblich.
- `zeitanteil_zaehler`: Ganzzahliger Zähler des qualifizierten Jahresanteils.
- `zeitanteil_nenner`: Positiver ganzzahliger Nenner des qualifizierten Jahresanteils.
- `zeitanteil_nachweis`: Nichtleerer Nachweis von Zinsabschnitt und Jahresanteil; keine automatische365-/360-Tage-Konvention.
- `einordnungsnachweis`: Nichtleerer Nachweis der anwendbaren Zinsermäßigung505dI einschließlich Nichtvorliegens der AusnahmenI5/III und Herkunft/Stichtags-/Laufzeitpassung des Marktzinssatzes.

Sollzins auf kleineren qualifizierten Marktzinssatz begrenzen; bestehenden Zinskern für neuen und vertraglichen Abschnitt verwenden und Differenz bilden.

wert mit rechnerischer_sollzins_prozent, rechnerischer_zinsbetrag und rechnerische_zinsdifferenz jeweils als exakter Bruch.

§505dI1/2: bereits rechtlich feststehende Zinsermäßigung; numerisch kleinerer Vertrags-/Marktzinssatz, keine Zinserhöhung. Gebundener Sollzins: Markt für Hypothekenpfandbriefe/öffentliche Pfandbriefe mit entsprechender Bindungslaufzeit; veränderlicher Sollzins: Euro-Dreimonats-Interbankenmarkt. Marktwerte, Vertragsschluss und vereinbarte Anpassungsstichtage vorqualifizieren. Jeder homogene Kapital-/Zinsabschnitt separat; keine Tilgungsplan- oder Zinseszinsannahme. Vorzeichenbehaftete Ergebnisse sind rechnerische Zinsbeträge, kein automatisch festgestellter Zahlungsanspruch bei Negativzinsen. Eine rechtlich anzuwendende Zinsuntergrenze ist vorab in der qualifizierten Zinsgrundlage zu berücksichtigen und nachzuweisen; keine erfundene Nullgrenze. Ausnahmefälle505dI5/III nicht mit dieser Funktion berechnen. Keine automatische Kreditwürdigkeitsprüfung, Pflichtverletzungsentscheidung oder Marktdatenbeschaffung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_505d_T0001, BGB_505d_T0002, BGB_505d_T0003, BGB_505d_T0004, BGB_505d_T0005, BGB_505d_T0006, BGB_505d_T0007

```python
from bgbcalc import kreditwuerdigkeit_zinsermaessigung
kreditwuerdigkeit_zinsermaessigung(
    kapital='10000',
    vertraglicher_sollzins_prozent='6',
    qualifizierter_marktzins_prozent='2',
    zinsart='gebunden',
    marktzins_stichtag_am='2024-01-01',
    zeitanteil_zaehler=1,
    zeitanteil_nenner=2,
    zeitanteil_nachweis='Qualifizierter halber Jahresanteil.',
    einordnungsnachweis='§505dI1/2: bereits rechtlich feststehende Zinsermäßigung; numerisch kleinerer Vertrags-/Marktzinssatz, keine Zinserhöhung. Gebundener Sollzins: Markt für Hypothekenpfandbriefe/öffentliche Pfandbriefe mit entsprechender Bindungslaufzeit; veränderlicher Sollzins: Euro-Dreimonats-Interbankenmarkt. Marktwerte, Vertragsschluss und vereinbarte Anpassungsstichtage vorqualifizieren. Jeder homogene Kapital-/Zinsabschnitt separat; keine Tilgungsplan- oder Zinseszinsannahme. Vorzeichenbehaftete Ergebnisse sind rechnerische Zinsbeträge, kein automatisch festgestellter Zahlungsanspruch bei Negativzinsen. Eine rechtlich anzuwendende Zinsuntergrenze ist vorab in der qualifizierten Zinsgrundlage zu berücksichtigen und nachzuweisen; keine erfundene Nullgrenze. Ausnahmefälle505dI5/III nicht mit dieser Funktion berechnen. Keine automatische Kreditwürdigkeitsprüfung, Pflichtverletzungsentscheidung oder Marktdatenbeschaffung.',
)
```
