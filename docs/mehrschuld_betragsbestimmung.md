<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## geldschulden_nach_betragsbestimmung_tilgen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `zahlung`: Nichtnegativer tatsächlich verfügbarer ZahlungsbetragEUR.
- `betragsbestimmungen`: Liste1..1000 eindeutiger Schulden mit genau schuld_id,offener_betrag,bestimmter_zahlungsbetrag. Rechtlich wirksame ausdrückliche Betragszuordnung bei Leistung; Summe aller bestimmten Beträge darf Zahlung nicht überschreiten. Nur gleiche Währung und gleichartige Geldforderungen desselben Gläubigers.
- `einordnungsnachweis`: Nichtleerer Nachweis366I: eindeutige rechtlich wirksame Mehrfach-/Betragsbestimmung, bestehende Forderungen, Erfüllbarkeit und vollständige Zuordnung. Fehlende/unklare Bestimmung nicht als Nullzuordnung ausgeben.

Ausdrückliche Betragszuordnung je Geldschuld begrenzt anrechnen und verbleibende Beträge berechnen.

wert.zuordnungen enthält schuld_id,angerechneter_betrag,restforderung; wert.nicht_zugeordnet enthält unverteilten Gesamtzahlungsrest. Beträge alsEurobrüche.

§366I: rechtlich vorgegebene Betragsbestimmung je Schuld bis zur Höhe des offenen Betrags ausführen; verbleibende Forderungen und nicht zugeordneten Teil der Gesamtzahlung ausweisen. Keine zusätzliche Verwendung von Überhängen für andere Schulden entgegen der qualifizierten Bestimmung. Summe der erklärten Betragsbestimmungen größer als Zahlung ist widersprüchliche Eingabe, keine erfundene anteilige Kürzung. Gesetzliche Ersatzreihenfolge366II nur bei fehlender Bestimmung in eigener Funktion;367Bestandteile einer Schuld separat. Nicht zugeordnete Zahlung ist keine automatische Rückforderung. Abweichende Vereinbarungen nur als zuvor rechtlich festgelegte Betragszuordnung, keine freie Vertragsauslegung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_366_T0001

```python
from bgbcalc import geldschulden_nach_betragsbestimmung_tilgen
geldschulden_nach_betragsbestimmung_tilgen(
    zahlung='100',
    betragsbestimmungen=[{'schuld_id': 'A', 'offener_betrag': '80', 'bestimmter_zahlungsbetrag': '60'}, {'schuld_id': 'B', 'offener_betrag': '70', 'bestimmter_zahlungsbetrag': '40'}],
    einordnungsnachweis='§366I: rechtlich vorgegebene Betragsbestimmung je Schuld bis zur Höhe des offenen Betrags ausführen; verbleibende Forderungen und nicht zugeordneten Teil der Gesamtzahlung ausweisen. Keine zusätzliche Verwendung von Überhängen für andere Schulden entgegen der qualifizierten Bestimmung. Summe der erklärten Betragsbestimmungen größer als Zahlung ist widersprüchliche Eingabe, keine erfundene anteilige Kürzung. Gesetzliche Ersatzreihenfolge366II nur bei fehlender Bestimmung in eigener Funktion;367Bestandteile einer Schuld separat. Nicht zugeordnete Zahlung ist keine automatische Rückforderung. Abweichende Vereinbarungen nur als zuvor rechtlich festgelegte Betragszuordnung, keine freie Vertragsauslegung.',
)
```
