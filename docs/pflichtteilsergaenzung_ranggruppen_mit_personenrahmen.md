<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_ranggruppen_mit_personenrahmen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fehlbetrag`: Nichtnegativer rechtlich bestimmter Ergänzungsfehlbetrag.
- `schenkungsgruppen`: Liste1..1000; je Person und Zeitpunkt genau eine Gruppe: beschenkter_id, schenkungsrang, schenkungswert, einzelhaftungsgrenze. Höherer Rang=spätere Schenkung, gleicher Rang=qualifiziert gleichzeitig. Mehrere Geschenke derselben Person am selben Zeitpunkt vorab als rechtlich einheitliche Gruppe erfassen.
- `personenrahmen`: Liste: beschenkter_id, gemeinsame_haftungsgrenze. Genau alle Empfänger; rechtliche Grenze für diesen Anspruch, nicht bloße Zahlungsfähigkeit.
- `kuerzungsmethode`: Zwingend rechtlich qualifiziert: anteilige_kuerzung_ohne_umverteilung oder begrenzte_umverteilung. Keine automatische Rechtsentscheidung bei Sonderkürzungen.
- `methodennachweis`: Zeitordnung, Schenkungswerte, rechtliche Einzel-/Personengrenzen und Behandlung von Kürzungen innerhalb einer Gleichzeitigkeitsgruppe ausdrücklich begründen.

Chronologische Gruppen mit gleichzeitig wertproportionaler Verteilung und ausdrücklich qualifizierter Kappungsmethode unter einmaligen Personenrahmen abarbeiten.

Gruppenanteile in Eingabereihenfolge, verbleibende Personenrahmen und ungedeckter Fehlbetrag; keine automatische rechtliche Methodenwahl.

Bedingte arithmetische2329III-Komposition: spätere Gruppen zuerst; gleichzeitig nach Schenkungswerten. Individuelle Kapazität=min(Gruppengrenze,Schenkungswert,noch unverbrauchter Personenrahmen). Bei anteilige_kuerzung_ohne_umverteilung erst Wertquote am kleineren Betrag aus Restfehlbetrag/Gesamtgruppenwert und danach persönliche Kappung; bei begrenzte_umverteilung proportional mit Kappung und Neuverteilung auf übrige Gruppenmitglieder. Nur tatsächlich zugeordnete Beträge verbrauchen den gemeinsamen Personenrahmen; rechtlich nicht gedeckter Rest geht zum früheren Rang. Kein doppelter Personenrahmen über mehrere Ränge. Die beiden Methoden sind ausdrücklich bedingte Rechenmodelle, keine Behauptung, dass beide gesetzlich zulässig sind. Rechtsfrage zusätzlicher Kürzungen bei Gleichzeitigkeit bleibt vom Anwender anhand seines Falls zu entscheiden; bloße Insolvenz macht spätere Verpflichtung nicht automatisch unwirksam. Keine gewöhnliche Geldhaftung statt qualifizierter Sachherausgabe unterstellen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2329_T0001, BGB_2329_T0002, BGB_2329_T0003, BGB_2329_T0004

```python
from bgbcalc import pflichtteilsergaenzung_ranggruppen_mit_personenrahmen
pflichtteilsergaenzung_ranggruppen_mit_personenrahmen(
    fehlbetrag='100',
    schenkungsgruppen=[{'beschenkter_id': 'A', 'schenkungsrang': 2, 'schenkungswert': '60', 'einzelhaftungsgrenze': '60'}, {'beschenkter_id': 'B', 'schenkungsrang': 2, 'schenkungswert': '40', 'einzelhaftungsgrenze': '40'}, {'beschenkter_id': 'A', 'schenkungsrang': 1, 'schenkungswert': '100', 'einzelhaftungsgrenze': '100'}, {'beschenkter_id': 'C', 'schenkungsrang': 1, 'schenkungswert': '100', 'einzelhaftungsgrenze': '100'}],
    personenrahmen=[{'beschenkter_id': 'A', 'gemeinsame_haftungsgrenze': '30'}, {'beschenkter_id': 'B', 'gemeinsame_haftungsgrenze': '100'}, {'beschenkter_id': 'C', 'gemeinsame_haftungsgrenze': '100'}],
    kuerzungsmethode='anteilige_kuerzung_ohne_umverteilung',
    methodennachweis='Bedingte arithmetische2329III-Komposition: spätere Gruppen zuerst; gleichzeitig nach Schenkungswerten. Individuelle Kapazität=min(Gruppengrenze,Schenkungswert,noch unverbrauchter Personenrahmen). Bei anteilige_kuerzung_ohne_umverteilung erst Wertquote am kleineren Betrag aus Restfehlbetrag/Gesamtgruppenwert und danach persönliche Kappung; bei begrenzte_umverteilung proportional mit Kappung und Neuverteilung auf übrige Gruppenmitglieder. Nur tatsächlich zugeordnete Beträge verbrauchen den gemeinsamen Personenrahmen; rechtlich nicht gedeckter Rest geht zum früheren Rang. Kein doppelter Personenrahmen über mehrere Ränge. Die beiden Methoden sind ausdrücklich bedingte Rechenmodelle, keine Behauptung, dass beide gesetzlich zulässig sind. Rechtsfrage zusätzlicher Kürzungen bei Gleichzeitigkeit bleibt vom Anwender anhand seines Falls zu entscheiden; bloße Insolvenz macht spätere Verpflichtung nicht automatisch unwirksam. Keine gewöhnliche Geldhaftung statt qualifizierter Sachherausgabe unterstellen.',
)
```
