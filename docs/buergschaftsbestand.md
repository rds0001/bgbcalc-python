<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## buergschaft_schuldkomponenten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schuldpositionen`: Unbenannte Liste1..1000 Objekte mit genau positions_id (eindeutiger nichtleerer Text), betrag (nichtnegativer exakter EUR-Dezimaltext/Bruch), spaetere_rechtsgeschaeftliche_erweiterung (expliziter Wahrheitswert). Nur den Erweiterungsanteil in einer gesonderten Position markieren. Alle übrigen Positionen bereits dem gesicherten aktuellen Hauptschuldbestand beziehungsweise erstattungsfähigen Kosten767II zugeordnet.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesicherten Bestands, der Komponenten und ihrer Ursachen/Zeitpunkte; keine automatische Vertragsauslegung oder Einredenprüfung.

Qualifizierte Schuldkomponenten summieren; spätere rechtsgeschäftliche Erweiterungen getrennt ausschließen.

wert: schuldumfang_nach_767 und ausgeschlossene_erweiterungen als exakte EUR-Brüche.

§767I/II: qualifizierter gegenwärtiger Hauptschuldbestand einschließlich zurechenbarer Verschuldens-/Verzugsfolgen und vom Hauptschuldner zu ersetzender Kündigungs-/Rechtsverfolgungskosten. Jede Komponente nur einmal erfassen. Durch ein nach Übernahme der Bürgschaft vorgenommenes Rechtsgeschäft des Hauptschuldners bewirkte Erweiterungen gesondert ausschließen; nur den Erweiterungsanteil als eigene Position kennzeichnen, nicht die unveränderte gesamte Hauptschuld. Ursache, Zeitpunkt, wirksame Bürgschaft und Zuordnung extern qualifizieren. Vertragliche Höchstbeträge, weitere Haftungsgrenzen, Einreden768/770, Mitbürgen769 und bereits geleistete Zahlungen gesondert berücksichtigen. Numerischer Umfang nach767, kein abschließender durchsetzbarer Zahlungsanspruch. Keine Positionen ausdrücklich als einzelne Nullposition eingeben.

Nichtnegative exakte EUR-Dezimaltexte/Brüche nach NUMERIK.md. Kostenlisten ohne doppelte Positionen, keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_767_T0001, BGB_767_T0002, BGB_767_T0003, BGB_767_T0004

```python
from bgbcalc import buergschaft_schuldkomponenten
buergschaft_schuldkomponenten(
    schuldpositionen=[{'positions_id': 'hauptschuld', 'betrag': '1000', 'spaetere_rechtsgeschaeftliche_erweiterung': False}, {'positions_id': 'verzug', 'betrag': '50', 'spaetere_rechtsgeschaeftliche_erweiterung': False}, {'positions_id': 'kuendigung', 'betrag': '10', 'spaetere_rechtsgeschaeftliche_erweiterung': False}, {'positions_id': 'rechtsverfolgung', 'betrag': '40', 'spaetere_rechtsgeschaeftliche_erweiterung': False}, {'positions_id': 'vertragserweiterung', 'betrag': '200', 'spaetere_rechtsgeschaeftliche_erweiterung': True}],
    einordnungsnachweis='Hauptschuld, zurechenbare Verzugsfolgen und erstattungsfähige Kosten qualifiziert; spätere rechtsgeschäftliche Erweiterungen einzeln abgegrenzt.',
)
```
