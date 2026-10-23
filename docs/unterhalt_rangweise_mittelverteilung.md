<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## unterhalt_rangweise_mittelverteilung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `verfuegbare_mittel`: Fuer den einheitlichen Unterhaltszeitraum und diesen Pflichtigen rechtlich verfuegbare Gesamtmittel nach1603; nicht ungeprueft Bruttoeinkommen.
- `berechtigte`: 1..1000 eindeutige person_id mit rang1609 (1..7), ungedeckter_bedarf und positivem verteilungsgewicht; verwandtschaftsgrad nur beiRang7als positive Generationszahl ab2, sonst None/NULL. Rechtlich gleichrangige Bedarfs-/Mangelfallgewichte, nicht automatisch Kopfanteile.
- `verteilungsnachweis`: Einheitlicher Zeitraum/Pflichtiger, gesetzliche Rangzuordnung,1603I/II-Leistungsfaehigkeit und rechtlich zutreffende proportionale Verteilung innerhalb jedes Rangs samt Bedarfsgrenzen belegen.

Verfuegbare Mittel nach1609Raengen, innerhalb jedes Rangs nach qualifizierten Gewichten unter Bedarfsgrenzen verteilen und ungedeckten Rest ausweisen.

Personenweise Rang, zugeordneter Unterhalt und Restbedarf; Gesamtzuordnung und nicht verbrauchte Mittel.

§§1603/1609: qualifizierte verfuegbare Mittel rangweise verwenden. Rang1vor2usw.; innerhalb Rang7gehen naehere Verwandtschaftsgrade den ferneren vor. Innerhalb eines Rangs nach rechtlich begruendeten Gewichten proportional unter individuellen ungedeckten Bedarfsgrenzen mit vorhandenem begrenztem Quotenkern verteilen. Erst danach Restmittel an naechsten Rang. Keine Gleichverteilung nach Koepfen und keine erfundene Unterhaltstabelle/Selbstbehaltshoehe.1603IIgesteigerte Haftung bestimmt rechtlich verfuegbare Mittel und qualifizierte Mangelfallgewichte, kein vom BGB vorgegebener weiterer pauschaler Prozentsatz. Gewichte und Grenzen muessen fuer die gesamte jeweilige Rangverteilung gelten; rechtliche Neubewertung bei geaenderter Grundlage explizit erforderlich. Mehrere Pflichtige1606IIIund Ersatzhaftung1607/1608mit bestehenden Anteils-/Leistungsgrenzenkernen in rechtlich bestimmter Reihenfolge komponieren; keine automatische globale Familienmatrix oder Umdeutung eines ungedeckten Bedarfs in Anspruch gegen beliebige Dritte. Bereits anderweitig gedeckte Bedarfe/gebundene Mittel nicht doppelt verwenden. Keine automatische Bestimmung von Berechtigung, Rang, Leistungsfaehigkeit, Naturalleistung oder Tabellenbetrag.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1603_T0001, BGB_1603_T0002, BGB_1603_T0003, BGB_1603_T0004, BGB_1606_T0001, BGB_1606_T0002, BGB_1606_T0003, BGB_1606_T0004, BGB_1607_T0001, BGB_1607_T0002, BGB_1607_T0003, BGB_1607_T0004, BGB_1607_T0005, BGB_1607_T0006, BGB_1608_T0001, BGB_1608_T0002, BGB_1608_T0003, BGB_1608_T0004, BGB_1608_T0005, BGB_1609_T0001, BGB_1609_T0002, BGB_1609_T0003, BGB_1609_T0004, BGB_1609_T0005, BGB_1609_T0006, BGB_1609_T0007, BGB_1609_T0008

```python
from bgbcalc import unterhalt_rangweise_mittelverteilung
unterhalt_rangweise_mittelverteilung(
    verfuegbare_mittel='100',
    berechtigte=[{'person_id': 'A', 'rang1609': 1, 'ungedeckter_bedarf': '100', 'verteilungsgewicht': '1', 'verwandtschaftsgrad': None}, {'person_id': 'B', 'rang1609': 1, 'ungedeckter_bedarf': '300', 'verteilungsgewicht': '3', 'verwandtschaftsgrad': None}, {'person_id': 'C', 'rang1609': 2, 'ungedeckter_bedarf': '200', 'verteilungsgewicht': '1', 'verwandtschaftsgrad': None}],
    verteilungsnachweis='§§1603/1609: qualifizierte verfuegbare Mittel rangweise verwenden. Rang1vor2usw.; innerhalb Rang7gehen naehere Verwandtschaftsgrade den ferneren vor. Innerhalb eines Rangs nach rechtlich begruendeten Gewichten proportional unter individuellen ungedeckten Bedarfsgrenzen mit vorhandenem begrenztem Quotenkern verteilen. Erst danach Restmittel an naechsten Rang. Keine Gleichverteilung nach Koepfen und keine erfundene Unterhaltstabelle/Selbstbehaltshoehe.1603IIgesteigerte Haftung bestimmt rechtlich verfuegbare Mittel und qualifizierte Mangelfallgewichte, kein vom BGB vorgegebener weiterer pauschaler Prozentsatz. Gewichte und Grenzen muessen fuer die gesamte jeweilige Rangverteilung gelten; rechtliche Neubewertung bei geaenderter Grundlage explizit erforderlich. Mehrere Pflichtige1606IIIund Ersatzhaftung1607/1608mit bestehenden Anteils-/Leistungsgrenzenkernen in rechtlich bestimmter Reihenfolge komponieren; keine automatische globale Familienmatrix oder Umdeutung eines ungedeckten Bedarfs in Anspruch gegen beliebige Dritte. Bereits anderweitig gedeckte Bedarfe/gebundene Mittel nicht doppelt verwenden. Keine automatische Bestimmung von Berechtigung, Rang, Leistungsfaehigkeit, Naturalleistung oder Tabellenbetrag.',
)
```
