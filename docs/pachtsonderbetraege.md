<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pacht_holzmehrnutzung_wertersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eingeschlagene_holzmenge`: Nichtnegativer exakter Dezimalwert/Bruch; Inventarwerte in EUR zu einheitlichen Endpreisen, Holzmengen in identischer Einheit/Qualität, Einheitswert in EUR je Mengeneinheit.
- `ordnungsgemaess_zulaessige_holzmenge`: Nichtnegativer exakter Dezimalwert/Bruch; Inventarwerte in EUR zu einheitlichen Endpreisen, Holzmengen in identischer Einheit/Qualität, Einheitswert in EUR je Mengeneinheit.
- `wert_je_mengeneinheit`: Nichtnegativer exakter Dezimalwert/Bruch; Inventarwerte in EUR zu einheitlichen Endpreisen, Holzmengen in identischer Einheit/Qualität, Einheitswert in EUR je Mengeneinheit.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Pachtfalls, rechtlich qualifizierter Bestände/Mengen und vergleichbarer Bewertung.

Positive Mehrmenge des Holzeinschlags gegenüber ordnungsgemäß zulässiger Menge mit qualifiziertem Wert je gleicher Mengeneinheit multiplizieren

wert ist exakter EUR-Bruch. Bei Inventardifferenz positiv=Pächter zahlt Verpächter, negativ=umgekehrte Richtung; Holzwertersatz nichtnegativ.

Nur §596a Absatz3 Satz2. Mengen beziehen sich auf denselben rechtlich maßgeblichen Nutzungsumfang, Zeitraum und dieselbe Holzeinheit/-qualität; zulässige ordnungsgemäße Nutzung und Wert extern qualifizieren. Bei verschiedenen Sortimenten oder Wertstufen getrennte überschneidungsfreie Positionen rechnen, keine pauschale Preisannahme. Weiterer Schaden gesondert ohne Doppelzählung. Nicht Ernte-/Holzwertersatz für noch nicht getrennte Früchte nach Absatz1–3Satz1.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_596a_T0005

```python
from bgbcalc import pacht_holzmehrnutzung_wertersatz
pacht_holzmehrnutzung_wertersatz(
    eingeschlagene_holzmenge='120',
    ordnungsgemaess_zulaessige_holzmenge='100',
    wert_je_mengeneinheit='50',
    einordnungsnachweis='Qualifizierter Mehrholzeinschlag bei vergleichbaren Mengen/Sortimenten und Werten.',
)
```

## pacht_inventar_ausgleichsdifferenz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `uebernommener_gesamtschaetzwert_zu_endpreisen`: Nichtnegativer exakter Dezimalwert/Bruch; Inventarwerte in EUR zu einheitlichen Endpreisen, Holzmengen in identischer Einheit/Qualität, Einheitswert in EUR je Mengeneinheit. Bei entsprechender Anwendung590III beide Bestände zum rechtlich maßgeblichen Zwischenabrechnungszeitpunkt bewerten; Endpreise bezeichnet dann diesen gemeinsamen Zeitpunkt.
- `zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen`: Nichtnegativer exakter Dezimalwert/Bruch; Inventarwerte in EUR zu einheitlichen Endpreisen, Holzmengen in identischer Einheit/Qualität, Einheitswert in EUR je Mengeneinheit. Bei entsprechender Anwendung590III beide Bestände zum rechtlich maßgeblichen Zwischenabrechnungszeitpunkt bewerten; Endpreise bezeichnet dann diesen gemeinsamen Zeitpunkt.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Pachtfalls, rechtlich qualifizierter Bestände/Mengen und vergleichbarer Bewertung.

Gesamtschätzwert des übernommenen Inventars minus Gesamtschätzwert des zurückzugewährenden Inventars, beide zu Preisen bei Pachtende

wert ist exakter EUR-Bruch. Bei Inventardifferenz positiv=Pächter zahlt Verpächter, negativ=umgekehrte Richtung; Holzwertersatz nichtnegativ.

§582a Absatz3 bei qualifizierter Inventarübernahme/-rückgewähr zum Schätzwert; entsprechend §590 Absatz3 bei qualifizierter wesentlicher Inventarverminderung während der Pachtzeit ohne gesetzliche Verwendungsausnahme. Im letzteren Fall sind Endpreise die einheitlichen Preise des rechtlich maßgeblichen Zwischenabrechnungszeitpunkts; der zweite Bestand ist das dort verbleibende Inventar, nicht ein erfundener künftiger Rückgabebestand. Positives Ergebnis bezeichnet Ausgleich vom Pächter an Verpächter, negatives Ergebnis den Betrag mit umgekehrter Richtung, null keinen Wertausgleich. Beide Inventarbestände mit Preisen desselben maßgeblichen Abrechnungszeitpunkts bewerten, nicht historische Anfangspreise gegen aktuelle Endpreise. Rechtlich wirksam abgelehnte überflüssige/überwertige Stücke zuvor aus dem zurückzugewährenden Bestand ausschließen. Keine Inventarbewertung, Eigentumsentscheidung oder zusätzliche Schadensersatzrechnung.

Nichtnegative Eingangswerte; exakte vorzeichenbehaftete Ausgleichsdifferenz im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_582a_T0007, BGB_582a_T0008, BGB_590_T0008

```python
from bgbcalc import pacht_inventar_ausgleichsdifferenz
pacht_inventar_ausgleichsdifferenz(
    uebernommener_gesamtschaetzwert_zu_endpreisen='1000',
    zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen='800',
    einordnungsnachweis='Qualifiziertes Inventar; beide Bestände zu Preisen bei Pachtende, abgelehnte Stücke bereinigt.',
)
```
