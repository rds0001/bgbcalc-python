<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## reallast_flaechenanteile

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `teilbare_leistungsmenge`: Nichtnegative exakte Menge der tatsächlich teilbaren Reallastleistung in einer einheitlichen Leistungsmaßeinheit.
- `grundstuecksteile`: Vollständige Liste1..1000 mit genau grundstueck_id und flaeche. Eindeutige nichtleere IDs und strikt positive exakte Flächen in derselben Flächeneinheit.
- `verteilungsnachweis`: Nichtleerer Nachweis des Grundfalls§1109I ohne abweichende Rechtszuordnung nachAbsatz2 oder3; Teilbarkeit und maßgebliche Flächen vorqualifiziert.

Anteil=Einzelfläche/Gesamtfläche; Leistungsanteil=Gesamtleistung×Anteil.

wert: Liste mit grundstueck_id, anteilsquote und leistungsanteil als exakte Brüche.

Nur qualifizierter Grundfall des§1109Absatz1 nach Teilung des berechtigten Grundstücks. Leistung ist tatsächlich teilbar und in einer gemeinsamen Einheit bewertet; sämtliche betroffenen Teile mit positiver Fläche in derselben Flächeneinheit erfassen. Keine abweichende wirksame Zuordnung nachAbsatz2, keine Beschränkung auf einen allein begünstigten Teil nachAbsatz3. Unteilbare Leistungen nach§432 und Ausübungsmodalitäten bleiben außerhalb dieser Mengenverteilung. Keine automatische Feststellung dinglicher Rechte.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1109_T0001, BGB_1109_T0002, BGB_1109_T0003, BGB_1109_T0004, BGB_1109_T0005, BGB_1109_T0006, BGB_1109_T0007

```python
from bgbcalc import reallast_flaechenanteile
reallast_flaechenanteile(
    teilbare_leistungsmenge='900',
    grundstuecksteile=[{'grundstueck_id': 'A', 'flaeche': {'zaehler': '2', 'nenner': '1'}}, {'grundstueck_id': 'B', 'flaeche': {'zaehler': '1', 'nenner': '1'}}],
    verteilungsnachweis='Teilbare Reallast von900Einheiten auf Flächen2:1; keine abweichende Rechtszuordnung.',
)
```
