<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbteile_gleichzeitige_anwachsung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eingesetzte_erben`: Vollständige Liste2..1000 Originalerben mit erbe_id,positiver erbquote,gemeinschaft_id(NULL oder einfache gemeinsameGruppe). Quoten bei vollständigem gesetzlichenAusschluss zusammen1,sonst striktunter1.
- `weggefallene_erben_ids`: Liste1..1000 eindeutiger IDs aus Originalerben; gemeinsamer rechtlich qualifizierter Wegfallzeitpunkt.
- `gesetzliche_erbfolge_ausgeschlossen`: Pflichtwahrheitswert der vollständigen testamentarischen Verdrängung gesetzlicherErbfolge.
- `anwachsung_testamentarisch_ausgeschlossen`: Pflichtwahrheitswert eines einheitlichen Ausschlusses aller untersuchtenAnwachsungen.
- `vorrangiges_ersatzerbrecht`: Pflichtwahrheitswert eines einheitlichen Ersatzerbvorrangs für sämtliche Wegfälle.
- `gemeinsamer_wegfall_qualifiziert`: Pflichtwahrheitswert gemeinsamer Wegfälle vor jedem Anwachsungsschritt; FALSE NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis gemeinsamer Wegfallkonstellation/Originalquoten/einfacherGruppen; keine gestaffelteKaskade.

Alle weggefallenenIDs zuerst aus Empfängerkreis entfernen; jeden Originalteil gruppenvorrangig beziehungsweise bei vollständigemgesetzlichenAusschluss allgemein nach verbleibendenOriginalquoten verteilen. Sonderteile je Ursprung bewahren.

Sonderteile nach Ursprung mit Einzelverteilungen,je verbleibendemErben Original/Zusatz/Gesamtquote sowie nichtangewachseneWegfallquote.

Keine zeitlich gestaffelte Anwachsung,verschachtelteGruppen,individuellenTeilsperren oder2098Ersatzerbeneinsetzungen. NichtangewachseneQuoten keinemErben automatischzuordnen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2094_T0001, BGB_2094_T0002, BGB_2094_T0003, BGB_2094_T0004, BGB_2095_T0001, BGB_2099_T0001

```python
from bgbcalc import erbteile_gleichzeitige_anwachsung
erbteile_gleichzeitige_anwachsung(
    eingesetzte_erben=[{'erbe_id': 'A', 'erbquote': '0.25', 'gemeinschaft_id': 'G'}, {'erbe_id': 'B', 'erbquote': '0.25', 'gemeinschaft_id': 'G'}, {'erbe_id': 'C', 'erbquote': '0.25', 'gemeinschaft_id': None}, {'erbe_id': 'D', 'erbquote': '0.25', 'gemeinschaft_id': None}],
    weggefallene_erben_ids=['A', 'C'],
    gesetzliche_erbfolge_ausgeschlossen=True,
    anwachsung_testamentarisch_ausgeschlossen=False,
    vorrangiges_ersatzerbrecht=False,
    gemeinsamer_wegfall_qualifiziert=True,
    einordnungsnachweis='Synthetische gleichzeitig qualifizierte WegfälleA,C; A/Bgemeinschaftlich, C/DohneGruppe.',
)
```
