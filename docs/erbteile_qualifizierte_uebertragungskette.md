<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbteile_qualifizierte_uebertragungskette

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `erben_ids`: 1..1000 eindeutige Kennungen aller in der Kette vorkommenden Erben/Ersatzerben.
- `ursprungsanteile`: 1..1000 Objekte ursprung_id, erbe_id, erbquote; unterschiedliche belastete Sonderteile mit unterschiedlichen Urspruengen, Gesamtquote hoechstens1.
- `uebertragungsschritte`: 0..1000 chronologisch rechtlich qualifizierte Schritte: abgebender_erbe_id, ursprung_ids, uebertragungsquote (positiv bis1), empfaenger mit erbe_id und positivem verteilungsgewicht.
- `einordnungsnachweis`: 2094/2098Empfaengerkreise je Stufe, Gruppenvorrang auch bei verschachtelten Gruppen, Ersatzvorrang/Teilsperren und normgerechte relative Gewichte belegen. Keine bereits ausgerechneten Endquoten erforderlich.

Qualifizierte Anteilstransfers chronologisch exakt verteilen, Restanteile fortschreiben und Sonderteile nach Urspruengen erhalten.

Positive Sonderteile je Ursprung/Erbe, Gesamtquoten aller Erben einschliesslich null und unveraenderte erfasste Gesamtquote.

§§2094/2095/2098/2099: rein rechnerische Fortfuehrung rechtlich bestimmter einzelner Uebertragungsschritte. Je ausgewahltem Ursprungsanteil aktuelle Quote des Abgebenden mit Uebertragungsquote multiplizieren, danach nach qualifizierten relativen Gewichten auf Empfaenger verteilen; Rest beim Abgebenden belassen. Jede spaetere Stufe verwendet den fortgeschriebenen Bestand, jeder angewachsene Sonderteil behaelt seinen Ursprung2095. Verschachtelte Gruppenvorraenge, individuelle Sperren und Ersatzerben bestimmen den rechtlich vorgegebenen Empfaengerkreis je Stufe; sie sind keine automatisch aus Namen erschlossene Familientopologie. Relative Gewichte muessen zum jeweiligen Normfall passen, insbesondere nicht blind aktuelle durch vorherige Anwachsung vergroesserte Gesamtquoten als urspruengliche Einsetzungsgewichte verwenden. Vorhandene2094/2098Grundfunktionen koennen passende Empfaenger-/Quotenbelege liefern. Nicht zu uebertragende oder rechtlich ungeklärte Teile bleiben getrennt; keine automatische Zuteilung an gesetzliche Erben. Gesamtquoten nur Summen, keine Aufhebung von Vermächtnis-/Auflagen-/Ausgleichungslasten am Ursprung. Keine Aussage, dass ein konkreter Wegfallgrund oder eine konkrete Testamentseinsetzung wirksam ist.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2094_T0001, BGB_2094_T0002, BGB_2094_T0003, BGB_2094_T0004, BGB_2095_T0001, BGB_2098_T0001, BGB_2098_T0002, BGB_2099_T0001

```python
from bgbcalc import erbteile_qualifizierte_uebertragungskette
erbteile_qualifizierte_uebertragungskette(
    erben_ids=['A', 'B', 'C'],
    ursprungsanteile=[{'ursprung_id': 'UA', 'erbe_id': 'A', 'erbquote': '0.25'}, {'ursprung_id': 'UB', 'erbe_id': 'B', 'erbquote': '0.25'}, {'ursprung_id': 'UC', 'erbe_id': 'C', 'erbquote': '0.5'}],
    uebertragungsschritte=[{'abgebender_erbe_id': 'A', 'ursprung_ids': ['UA'], 'uebertragungsquote': '1', 'empfaenger': [{'erbe_id': 'B', 'verteilungsgewicht': '1'}]}, {'abgebender_erbe_id': 'B', 'ursprung_ids': ['UA', 'UB'], 'uebertragungsquote': '1', 'empfaenger': [{'erbe_id': 'C', 'verteilungsgewicht': '1'}]}],
    einordnungsnachweis='§§2094/2095/2098/2099: rein rechnerische Fortfuehrung rechtlich bestimmter einzelner Uebertragungsschritte. Je ausgewahltem Ursprungsanteil aktuelle Quote des Abgebenden mit Uebertragungsquote multiplizieren, danach nach qualifizierten relativen Gewichten auf Empfaenger verteilen; Rest beim Abgebenden belassen. Jede spaetere Stufe verwendet den fortgeschriebenen Bestand, jeder angewachsene Sonderteil behaelt seinen Ursprung2095. Verschachtelte Gruppenvorraenge, individuelle Sperren und Ersatzerben bestimmen den rechtlich vorgegebenen Empfaengerkreis je Stufe; sie sind keine automatisch aus Namen erschlossene Familientopologie. Relative Gewichte muessen zum jeweiligen Normfall passen, insbesondere nicht blind aktuelle durch vorherige Anwachsung vergroesserte Gesamtquoten als urspruengliche Einsetzungsgewichte verwenden. Vorhandene2094/2098Grundfunktionen koennen passende Empfaenger-/Quotenbelege liefern. Nicht zu uebertragende oder rechtlich ungeklärte Teile bleiben getrennt; keine automatische Zuteilung an gesetzliche Erben. Gesamtquoten nur Summen, keine Aufhebung von Vermächtnis-/Auflagen-/Ausgleichungslasten am Ursprung. Keine Aussage, dass ein konkreter Wegfallgrund oder eine konkrete Testamentseinsetzung wirksam ist.',
)
```
