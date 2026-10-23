<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteil_gemischter_ausgleich_mit_anrechnung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `gruppennachlass`: Rechtlich auf Ausgleichungsgruppe entfallender Nachlass vor zusätzlicher2315-Hinzurechnung.
- `miterben`: Vollständige Ausgleichungsgruppe nach Vertrag des gemischten Überempfangskerns.
- `berechtigter_id`: Kennung des konkret berechneten Pflichtteilsberechtigten in der hypothetischen Gruppe.
- `gruppenquote_am_gesamtnachlass`: Positive gesetzliche Quote der gesamten Ausgleichungsgruppe am Gesamtnachlass, höchstens1; relative Miterbenquoten bleiben auf die Gruppe bezogen.
- `zugleich_anrechenbarer_zuwendungswert`: Bereits in eigener2055-Zuwendung enthaltener zugleich2315-anrechenbarer Wert auf identischer Bewertungsbasis, höchstens eigener Zuwendungswert.
- `reiner_anrechnungswert_2315`: Zusätzliche eigene2315-Zuwendung ohne2050-Ausgleichspflicht, nicht bereits in Gruppenpositionen enthalten.
- `hinterlassener_erbteilwert`: Für2316IImaßgeblicher tatsächlich hinterlassener Wert;0bei Enterbung.
- `ausgleichungsmodell`: Zwingend rechtlich begründetes Modell des gemischten Überempfangskerns.
- `methodennachweis`: 2316-Anwendbarkeit, Gruppe/Gruppequote, identische Doppelanrechnungswerte und vorgelagerte2315-Hinzurechnung der zusätzlichen Zuwendung ausdrücklich rechtlich qualifizieren; keine automatische Rechtsauslegung.

Reine2315-Zuwendung anteilig zur hypothetischen Gruppenmasse addieren, gemischtes Modell berechnen, Anteil halbieren und getrennte Anrechnungen abziehen.

Hypothetische Gruppenmasse/Erbteil, halber Grundwert/Doppelabzug, positiver Pflichtteil und Mehrbetrag.

Bedingte2316/2315-Komposition: reine eigene2315-Zuwendung mit gesetzlicher Gruppenquote zur Gruppenmasse hinzufügen; vorhandenen ausdrücklich ausgewählten2055/2056/2057a-Kern auf hypothetische Masse anwenden. Eigenen hypothetischen gesetzlichen Anteil halbieren; zugleich ausgleichungspflichtige2315-Zuwendung nach2316IVnur halb, zusätzliche reine2315-Zuwendung vollständig abziehen; positiver Rest und2316II-Mehrbetrag. Gruppenquote verhindert volle Hinzurechnung zur Teilgruppe bei weiteren gesetzlichen Erben. Kein doppelt erfasstes Geschenk, keine automatische Bewertung/Kaufkraftbereinigung. Kombination und Reihenfolge sind rechtliche Modellvoraussetzungen, insbesondere zugleich leistende Überempfänger bleiben keine automatisch gelöste Auslegungsfrage. Unterschiedliche Wertansätze derselben Doppelzuwendung und2325/2327-Ergänzung separat. Rechtlicher Gruppenausschluss durch Erbverzicht und Ausstattungsschutz2316IIIvorqualifiziert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2055_T0001, BGB_2055_T0002, BGB_2055_T0003, BGB_2056_T0001, BGB_2056_T0002, BGB_2057a_T0001, BGB_2057a_T0002, BGB_2057a_T0003, BGB_2057a_T0004, BGB_2057a_T0005, BGB_2057a_T0006, BGB_2057a_T0007, BGB_2315_T0001, BGB_2315_T0002, BGB_2315_T0003, BGB_2315_T0004, BGB_2316_T0001, BGB_2316_T0002, BGB_2316_T0003, BGB_2316_T0004, BGB_2316_T0005

```python
from bgbcalc import pflichtteil_gemischter_ausgleich_mit_anrechnung
pflichtteil_gemischter_ausgleich_mit_anrechnung(
    gruppennachlass='100',
    miterben=[{'person_id': 'A', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '150', 'leistungs_ausgleichsbetrag': '50'}, {'person_id': 'B', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '0'}, {'person_id': 'C', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '0'}],
    berechtigter_id='A',
    gruppenquote_am_gesamtnachlass='1',
    zugleich_anrechenbarer_zuwendungswert='0',
    reiner_anrechnungswert_2315='0',
    hinterlassener_erbteilwert='0',
    ausgleichungsmodell='leistungsvorwegabzug_mit_fortgeltung',
    methodennachweis='Bedingte2316/2315-Komposition: reine eigene2315-Zuwendung mit gesetzlicher Gruppenquote zur Gruppenmasse hinzufügen; vorhandenen ausdrücklich ausgewählten2055/2056/2057a-Kern auf hypothetische Masse anwenden. Eigenen hypothetischen gesetzlichen Anteil halbieren; zugleich ausgleichungspflichtige2315-Zuwendung nach2316IVnur halb, zusätzliche reine2315-Zuwendung vollständig abziehen; positiver Rest und2316II-Mehrbetrag. Gruppenquote verhindert volle Hinzurechnung zur Teilgruppe bei weiteren gesetzlichen Erben. Kein doppelt erfasstes Geschenk, keine automatische Bewertung/Kaufkraftbereinigung. Kombination und Reihenfolge sind rechtliche Modellvoraussetzungen, insbesondere zugleich leistende Überempfänger bleiben keine automatisch gelöste Auslegungsfrage. Unterschiedliche Wertansätze derselben Doppelzuwendung und2325/2327-Ergänzung separat. Rechtlicher Gruppenausschluss durch Erbverzicht und Ausstattungsschutz2316IIIvorqualifiziert.',
)
```
