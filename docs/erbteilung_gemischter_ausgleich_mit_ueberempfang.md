<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbteilung_gemischter_ausgleich_mit_ueberempfang

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `gruppennachlass`: Nichtnegativer Nachlass der vollständigen Ausgleichungsgruppe.
- `miterben`: Wie im gemischten Kern: person_id, relative_erbquote, ausgleichungswert_zuwendungen und leistungs_ausgleichsbetrag; Quoten summieren zu1, Leistungen höchstens Gruppennachlass.
- `ausgleichungsmodell`: Zwingend rechtlich begründet: leistungsvorwegabzug_mit_fortgeltung oder gemeinsame_neuberechnung_ohne_ausgeschiedene. Beide sind bedingte Rechenmodelle, keine automatische BGB-Auslegung.
- `methodennachweis`: Konkrete rechtliche Behandlung zugleich leistender Überempfänger einschließlich Fortbestand/Ausscheiden des Leistungsbetrags ausdrücklich begründen; Billigkeitsbeträge und Gruppe vorqualifizieren.

Zwingend gewähltes kombiniertes Ausgleichungsmodell unter Wiederverwendung vorhandener Validierung/2056-Rechnung berechnen; keine automatische Auslegung.

Ausdrücklich gewähltes Modell, ausgeschiedene Personen und nichtnegative Zuteilungen mit SummeGruppennachlass.

2055/2056/2057a-Rechenkonkurrenz bei zugleich Leistenden und Überempfängern: keine allgemeine juristische Lösung aus ungeprüfter Iteration behaupten. Bedingtes Vorwegmodell zieht sämtliche qualifizierten Leistungen ab, verwendet vorhandene2056-Zuwendungsausscheidung und fügt individuelle Leistungen auch ausgeschiedenen Zuwendungsempfängern wieder hinzu. Bedingtes gemeinsames Modell berechnet je aktiver Gruppe q_i/Summeq*(N-SummeL+SummeZ)-Z_i+L_i; negative Endbeträge scheiden mit Quote,Zuwendung und Leistungsposition aus, Gruppe wird neu berechnet. Diese Behandlung muss im konkreten Fall rechtlich vorgegeben sein, nicht aus einem bloßen negativen Zwischenergebnis als Rechtsfolge erfunden werden. Beide Modelle erhalten die SummeN und erzeugen keine Rückzahlung aus negativem Erbteil. Leistungen sind billig bemessene Eingaben, keine erfundene Pflegevergütung. Keine2315-Anrechnung, Pflichtteilsergänzung oder automatische rechtliche Auswahl.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2055_T0001, BGB_2055_T0002, BGB_2055_T0003, BGB_2056_T0001, BGB_2056_T0002, BGB_2057a_T0001, BGB_2057a_T0002, BGB_2057a_T0003, BGB_2057a_T0004, BGB_2057a_T0005, BGB_2057a_T0006, BGB_2057a_T0007

```python
from bgbcalc import erbteilung_gemischter_ausgleich_mit_ueberempfang
erbteilung_gemischter_ausgleich_mit_ueberempfang(
    gruppennachlass='100',
    miterben=[{'person_id': 'A', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '150', 'leistungs_ausgleichsbetrag': '50'}, {'person_id': 'B', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '0'}, {'person_id': 'C', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '0'}],
    ausgleichungsmodell='leistungsvorwegabzug_mit_fortgeltung',
    methodennachweis='2055/2056/2057a-Rechenkonkurrenz bei zugleich Leistenden und Überempfängern: keine allgemeine juristische Lösung aus ungeprüfter Iteration behaupten. Bedingtes Vorwegmodell zieht sämtliche qualifizierten Leistungen ab, verwendet vorhandene2056-Zuwendungsausscheidung und fügt individuelle Leistungen auch ausgeschiedenen Zuwendungsempfängern wieder hinzu. Bedingtes gemeinsames Modell berechnet je aktiver Gruppe q_i/Summeq*(N-SummeL+SummeZ)-Z_i+L_i; negative Endbeträge scheiden mit Quote,Zuwendung und Leistungsposition aus, Gruppe wird neu berechnet. Diese Behandlung muss im konkreten Fall rechtlich vorgegeben sein, nicht aus einem bloßen negativen Zwischenergebnis als Rechtsfolge erfunden werden. Beide Modelle erhalten die SummeN und erzeugen keine Rückzahlung aus negativem Erbteil. Leistungen sind billig bemessene Eingaben, keine erfundene Pflegevergütung. Keine2315-Anrechnung, Pflichtteilsergänzung oder automatische rechtliche Auswahl.',
)
```
