<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## auslobung_belohnungsanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtbelohnung`: Nichtnegative teilbare Geldbelohnung in EUR.
- `verteilungsart`: gleichzeitige_handlung nach659II, gleiche_preiswuerdigkeit nach661III oder mitwirkungsanteil nach660I; Rechtsgrund vorqualifiziert.
- `anzahl_berechtigte`: Nur Gleichverteilung: ganze Zahl mindestens2, höchstens2^53-1. Bei Mitwirkungsquote null.
- `anteil_zaehler`: Nur Mitwirkungsquote: nichtnegative ganze Zahl höchstens Nenner und2^53-1. Bei Gleichverteilung null.
- `anteil_nenner`: Nur Mitwirkungsquote: positive ganze Zahl höchstens2^53-1. Bei Gleichverteilung null.
- `verteilungsnachweis`: Nichtleerer Nachweis des Verteilungsfalls, der Teilbarkeit und des fehlenden Einzelempfängervorbehalts beziehungsweise der verbindlich festgestellten Mitwirkungsquote; Gesamtquoten müssen eins ergeben.

Geldbelohnung durch Anzahl gleichberechtigter Personen teilen oder mit qualifizierter Mitwirkungsquote multiplizieren.

wert: exakter EUR-Bruch des Anteils der betrachteten Person; keine Aussage über sofortige Durchsetzbarkeit.

§659II/661III: rechtlich festgestellte Gleichzeitigkeit beziehungsweise gleiche Preiswürdigkeit, teilbare Geldbelohnung und kein Vorbehalt nur eines Empfängers. Losentscheid bei Unteilbarkeit/Einzelempfängervorbehalt außerhalb dieser Berechnung. §660I: verbindlich festgestellter billiger Mitwirkungsanteil; Funktion bewertet Beiträge nicht. Bei mehreren Einzelaufrufen müssen sämtliche qualifizierten Mitwirkungsquoten zusammen eins ergeben, keine mehrfachen Vollbelohnungen. Streitbedingtes Leistungsverweigerungsrecht660II, Hinterlegung und Preisvergabewirksamkeit gesondert. Keine Rundung oder Abrechnung bereits gezahlter Teilbeträge.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_659_T0002, BGB_659_T0003, BGB_660_T0001, BGB_660_T0002, BGB_661_T0004

```python
from bgbcalc import auslobung_belohnungsanteil
auslobung_belohnungsanteil(
    gesamtbelohnung='100',
    verteilungsart='gleichzeitige_handlung',
    anzahl_berechtigte=2,
    anteil_zaehler=None,
    anteil_nenner=None,
    verteilungsnachweis='§659II/661III: rechtlich festgestellte Gleichzeitigkeit beziehungsweise gleiche Preiswürdigkeit, teilbare Geldbelohnung und kein Vorbehalt nur eines Empfängers. Losentscheid bei Unteilbarkeit/Einzelempfängervorbehalt außerhalb dieser Berechnung. §660I: verbindlich festgestellter billiger Mitwirkungsanteil; Funktion bewertet Beiträge nicht. Bei mehreren Einzelaufrufen müssen sämtliche qualifizierten Mitwirkungsquoten zusammen eins ergeben, keine mehrfachen Vollbelohnungen. Streitbedingtes Leistungsverweigerungsrecht660II, Hinterlegung und Preisvergabewirksamkeit gesondert. Keine Rundung oder Abrechnung bereits gezahlter Teilbeträge.',
)
```
