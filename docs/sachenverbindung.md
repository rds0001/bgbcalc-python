<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## sachenverbindung_eigentumsquoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigentuemer_werte`: Unbenannte Liste mit2..1000 Objekten, jeweils genau eigentuemer_id (eindeutige nichtleere Zeichenfolge) und sachenwert (nichtnegativer exakter EUR-Wert). Werte der beteiligten beweglichen Sachen je bisherigem Eigentümer im Zeitpunkt der Verbindung/Vermischung zusammenfassen. Gleiche Bewertungsbasis; Gesamtwert ohne Hauptsache positiv. Vorbestehende Miteigentumsstrukturen rechtlich zutreffend vorab auflösen; dieses Modell setzt bei Hauptsache einen einzelnen Eigentümer voraus.
- `entstehungsart`: Auswahl verbindung (§947) oder vermischung_vermengung (§948). Keine Grundstücksverbindung oder Verarbeitung zu neuer Sache ungeprüft hier einordnen.
- `wesentliche_bestandteile`: Wahrheitswert, ob die verbundenen beweglichen Sachen wesentliche Bestandteile einer einheitlichen Sache werden. Nur bei entstehungsart=verbindung maßgeblich.
- `untrennbar_vermischt`: Wahrheitswert einer untrennbaren Vermischung/Vermengung. Nur bei entstehungsart=vermischung_vermengung maßgeblich; bloßes Nebeneinanderlegen genügt nicht.
- `trennungskosten_unverhaeltnismaessig`: Wahrheitswert unverhältnismäßiger Trennungskosten bei Vermischung/Vermengung. Nach§948 Absatz2 der Untrennbarkeit gleichgestellt. Keine erfundene Kostenschwelle und nicht auf sonstige Verbindungsfälle übertragen.
- `hauptsachen_eigentuemer`: Optional eindeutige eigentuemer_id aus der Liste des Alleineigentümers einer rechtlich als Hauptsache eingeordneten Sache. None/NULL bedeutet keine solche Hauptsache, dann Wertquoten. Hauptsache nicht automatisch höchste Geldbewertung. Besteht daran Miteigentum, anderes erweitertes Modell erforderlich.
- `bewertungsnachweis`: Nichtleere Beschreibung der beteiligten beweglichen Sachen, rechtlichen Verbindung/Vermischung, Werte im Entstehungszeitpunkt, gegebenenfalls Trennungskostenbewertung und Hauptsacheneigenschaft.

Bei Verbindung wesentliche Bestandteile, bei Vermischung Untrennbarkeit oder unverhältnismäßige Trennungskosten prüfen. Mit rechtlich bestimmter Hauptsache Alleineigentumsquote1 für deren Eigentümer, sonst je Eigentümer Sachenwert/Summe der Werte.

wert ist Liste in Eingabereihenfolge mit eigentuemer_id und eigentumsquote als exaktem Bruch. Quoten summieren sich zu1. Nicht einschlägiger Entstehungstatbestand ergibt NICHT_ANWENDBAR mit null.

Kein automatischer Schluss von höchstem Wert auf Hauptsache; kein bloßes Nebeneinander beweglicher Sachen. Hauptsachen-Miteigentum, Grundstücksverbindung§946, Verarbeitung§950 und Ausgleichsansprüche§951 gesondert. Quoten nach ursprünglichen Werten im Verbindungszeitpunkt, nicht nach beliebig späteren Werten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_947_T0001, BGB_947_T0002, BGB_948_T0001, BGB_948_T0002

```python
from bgbcalc import sachenverbindung_eigentumsquoten
sachenverbindung_eigentumsquoten(
    eigentuemer_werte=[{'eigentuemer_id': 'A', 'sachenwert': '100'}, {'eigentuemer_id': 'B', 'sachenwert': '300'}],
    entstehungsart='verbindung',
    wesentliche_bestandteile=True,
    untrennbar_vermischt=False,
    trennungskosten_unverhaeltnismaessig=False,
    hauptsachen_eigentuemer=None,
    bewertungsnachweis='Synthetische Verbindung beweglicher Sachen verschiedener Eigentümer.',
)
```
