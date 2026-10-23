<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fortsetzung_rechnerische_schlussbilanz

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `bereinigte_restmasse`: Nichtnegative sonstige Restmasse nach vorrangigen Verbindlichkeiten und Rueckbehalten; ohne gesonderte Ersatz-/Anrechnungsposten und ohne bereits abgeflossene Abfindungen.
- `ersatzschuld_ehegatte`: Rechtlich festgestellte, bewertete Ersatzschuld des ueberlebenden Ehegatten.
- `anrechnung_abkoemmlinge`: Qualifizierte Anrechnungsposten1498/1500 der Abkoemmlingsseite; keine erneut angesetzten bereits gedeckten Betraege.
- `gezahlte_abfindungen`: Tatsaechlich aus Gesamtgut gezahlte einrechenbare Abfindungen1501 beziehungsweise Ausschlussbetraege1511III.
- `bilanznachweis`: Rechtliche Zuordnung, Bewertung, fehlende Doppelanrechnung und Fehlen einer abweichenden1501II-Vereinbarung belegen.

Qualifizierte Bilanzposten addieren, halbieren und seitengerecht anrechnen; persoenliche ueberschiessende Ersatzpflicht nur beim ueberlebenden Ehegatten ausweisen.

Exakte Rechenmasse, Halbteil, vorzeichenbehaftete Seitensalden und ausschliesslich1498/1476II2 betreffende persoenliche Restersatzpflichten.

Rechnerische Verbindung1498/1476 mit1500/1501: Restmasse plus beide qualifizierten Anrechnungsposten plus tatsaechlich gezahlte Abfindungen halbieren; eigene Lasten jeweils auf die betreffende Haelfte anrechnen. Negative Abkoemmlingssalden begruenden nach1498 gerade keine ueberschiessende persoenliche1476II2-Ersatzpflicht. Nur die ueberschiessende Ersatzschuld des ueberlebenden Ehegatten wird als solche ausgewiesen. Positive Salden sind rechnerische Bilanzpositionen, keine Zusage realisierbarer oder sofort faelliger Barauszahlung; gegenstaendliche Haftung, Deckung, Bewertung und Uneinbringlichkeit gesondert bestimmen. Personenverteilung1503I, Vorempfaenge1503II und ausschliesslich Beguenstigte treffende Lasten1503III/1511III2 anschliessend ohne Doppelabzug normgerecht verbinden. Keine automatische Anrechnung aller Lasten proportional auf jeden Abkoemmling. Keine abschliessende Abwicklung beliebiger Insolvenz-/Haftungskonstellationen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1476_T0001, BGB_1476_T0002, BGB_1476_T0003, BGB_1498_T0001, BGB_1498_T0002, BGB_1500_T0001, BGB_1500_T0002, BGB_1501_T0001, BGB_1501_T0002, BGB_1501_T0003

```python
from bgbcalc import fortsetzung_rechnerische_schlussbilanz
fortsetzung_rechnerische_schlussbilanz(
    bereinigte_restmasse='1000',
    ersatzschuld_ehegatte='100',
    anrechnung_abkoemmlinge='50',
    gezahlte_abfindungen='50',
    bilanznachweis='Rechnerische Verbindung1498/1476 mit1500/1501: Restmasse plus beide qualifizierten Anrechnungsposten plus tatsaechlich gezahlte Abfindungen halbieren; eigene Lasten jeweils auf die betreffende Haelfte anrechnen. Negative Abkoemmlingssalden begruenden nach1498 gerade keine ueberschiessende persoenliche1476II2-Ersatzpflicht. Nur die ueberschiessende Ersatzschuld des ueberlebenden Ehegatten wird als solche ausgewiesen. Positive Salden sind rechnerische Bilanzpositionen, keine Zusage realisierbarer oder sofort faelliger Barauszahlung; gegenstaendliche Haftung, Deckung, Bewertung und Uneinbringlichkeit gesondert bestimmen. Personenverteilung1503I, Vorempfaenge1503II und ausschliesslich Beguenstigte treffende Lasten1503III/1511III2 anschliessend ohne Doppelabzug normgerecht verbinden. Keine automatische Anrechnung aller Lasten proportional auf jeden Abkoemmling. Keine abschliessende Abwicklung beliebiger Insolvenz-/Haftungskonstellationen.',
)
```
