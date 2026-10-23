<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbteilung_leistungsausgleich

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlasswert_der_ausgleichungsgemeinschaft`: Nichtnegativer EUR-Nachlasswert ausschließlich des den ausgleichenden Miterben zustehenden Anteils; andere Erben nicht durch Abzug der Ausgleiche mitbelasten.
- `miterben`: Unbenannte Liste mit2..1000 eindeutigen Miterben; je genau miterbe_id (nichtleere Zeichenfolge), relative_erbquote (positive exakte Quote höchstens1 innerhalb der Ausgleichungsgemeinschaft, Summe1) und leistungs_ausgleichsbetrag (nichtnegative exakte EUR-Zahl). Beträge rechtlich nach§2057a Absatz3 billig bemessen und unter Ausschlüssen des Absatz2 bereinigen. Summe der Ausgleichsbeträge höchstens zugehöriger Nachlasswert; bei Überschreitung keine erfundene Kürzung.
- `leistungsausgleich_2057a_anwendbar`: Wahrheitswert: Abkömmlinge, gesetzliche Erbfolge oder§2052, besondere Leistungen/Pflege und Anspruchsberechtigung nach§2057a rechtlich geprüft. Angemessen vergütete oder durch andere Ansprüche gedeckte Leistungen nicht nochmals ansetzen.
- `weitere_ausgleichungsposten_vorhanden`: Wahrheitswert: weitere auszugleichende Zuwendungen oder sonstige Ausgleichungsposten berühren dieselbe Teilung. TRUE ergibt NICHT_ANWENDBAR, da dieses Modell isolierten Leistungsausgleich berechnet.
- `bewertungsnachweis`: Nichtleere Begründung der Gemeinschaft, relativen Quoten, Nachlasszuordnung und individuell billig bestimmten, anspruchsbereinigten Ausgleichsbeträge. Keine pauschale Pflegevergütungsformel.

Summe qualifizierter Leistungsausgleichsbeträge vom Gemeinschaftsnachlass abziehen. Rest nach relativen Erbquoten teilen und jedem Miterben seinen Ausgleichsbetrag zusätzlich zuordnen.

wert enthält verteilungsrest als EUR-Bruch und zuteilungen in Eingabereihenfolge mit miterbe_id/erbteil_nach_leistungsausgleich als EUR-Bruch. Summe der Zuteilungen gleich Gemeinschaftsnachlass. Außerhalb Anwendungsbereich NICHT_ANWENDBAR/null.

Nur isolierter Leistungsausgleich, keine kombinierte Ausgleichung weiterer Zuwendungen. Anspruch und Billigkeitsbewertung vorgegeben. Kein erfundener Stundensatz, keine automatische Kürzung bei zu hohen Ausgleichsbeträgen.

2..1000 eindeutige Miterben mit positiven relativen Quoten der Summe1. Nichtnegative EUR-Beträge, Ausgleichssumme höchstens Gemeinschaftsnachlass. Exakte Ganzzahl-Zwischenwerte höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2057a_T0001, BGB_2057a_T0002, BGB_2057a_T0003, BGB_2057a_T0004, BGB_2057a_T0005, BGB_2057a_T0006, BGB_2057a_T0007

```python
from bgbcalc import erbteilung_leistungsausgleich
erbteilung_leistungsausgleich(
    nachlasswert_der_ausgleichungsgemeinschaft='100',
    miterben=[{'miterbe_id': '0', 'relative_erbquote': {'zaehler': '1', 'nenner': '2'}, 'leistungs_ausgleichsbetrag': {'zaehler': '20', 'nenner': '1'}}, {'miterbe_id': '1', 'relative_erbquote': {'zaehler': '1', 'nenner': '2'}, 'leistungs_ausgleichsbetrag': {'zaehler': '0', 'nenner': '1'}}],
    leistungsausgleich_2057a_anwendbar=True,
    weitere_ausgleichungsposten_vorhanden=False,
    bewertungsnachweis='Synthetisch isolierter, rechtlich qualifizierter Leistungsausgleich unter den beteiligten Abkömmlingen.',
)
```
