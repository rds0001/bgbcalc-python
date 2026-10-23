<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zahlungsdienste_entgeltabschnitt

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `abschnitt_von_utc`: Eingeschlossener Beginn des homogenen Entgeltabschnitts als sekundengenauer UTC-Zeitpunkt.
- `abschnitt_bis_utc`: Ausgeschlossene Endgrenze; strikt nach Beginn.
- `beendigung_utc`: Rechtlich wirksamer Beendigungszeitpunkt; Vertrag läuft bis zu dieser ausgeschlossenen Grenze.
- `abschnittsentgelt`: Regelmäßiges Entgelt für den gesamten Abschnitt, nichtnegativer exakter EUR-Wert.
- `vorausgezahltes_entgelt`: Bereits gezahltes Entgelt höchstens Abschnittsentgelt; proportional über diesen Abschnitt zugeordnet.
- `einordnungsnachweis`: Wirksame Kündigung, homogene Zeitbewertung, proportional zugeordnete Zahlung und UTC-Normalisierung belegen.

Halb offenen Entgeltabschnitt am Beendigungszeitpunkt schneiden; Zeitanteile exakt bestimmen und Entgelt sowie Vorauszahlung proportional abrechnen.

Sekunden insgesamt/bis Beendigung, exakter geschuldeter Zeitanteil und Entgeltbetrag sowie Erstattung des nach Beendigung zugeordneten Vorauszahlungsanteils.

§675hIII: Entgelt nur bis zur Beendigung; auf danach entfallende Zeit zugeordnete Vorauszahlung erstatten. Berechnung unter ausdrücklich rechtlich bestimmter gleichmäßiger Zeitbewertung in Sekunden; keine automatische Wahl einer Vertrags-/Tageskonvention. Abweichend bewertete Preisperioden getrennt normalisieren und abrechnen. Halb offene Intervalle verhindern doppelte Grenzsekunden. Standardbibliotheken und vorhandener UTC-Parser, keine neue Datumsbibliothek; keine stillschweigende Zeitzone oder Rundung von Subsekunden. Vertragswirksamkeit, zulässige Kündigungsfrist675hI/II und EntgeltverbotIV separat; kein Kündigungsentgelt ergänzen. Geschuldetes Entgelt und Rückerstattung nicht als zwei zusätzliche Ansprüche zusammenzählen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675h_T0001, BGB_675h_T0002, BGB_675h_T0003, BGB_675h_T0004, BGB_675h_T0005, BGB_675h_T0006, BGB_675h_T0007, BGB_675h_T0008

```python
from bgbcalc import zahlungsdienste_entgeltabschnitt
zahlungsdienste_entgeltabschnitt(
    abschnitt_von_utc='2024-02-01T00:00:00Z',
    abschnitt_bis_utc='2024-03-01T00:00:00Z',
    beendigung_utc='2024-02-15T12:00:00Z',
    abschnittsentgelt='29',
    vorausgezahltes_entgelt='29',
    einordnungsnachweis='§675hIII: Entgelt nur bis zur Beendigung; auf danach entfallende Zeit zugeordnete Vorauszahlung erstatten. Berechnung unter ausdrücklich rechtlich bestimmter gleichmäßiger Zeitbewertung in Sekunden; keine automatische Wahl einer Vertrags-/Tageskonvention. Abweichend bewertete Preisperioden getrennt normalisieren und abrechnen. Halb offene Intervalle verhindern doppelte Grenzsekunden. Standardbibliotheken und vorhandener UTC-Parser, keine neue Datumsbibliothek; keine stillschweigende Zeitzone oder Rundung von Subsekunden. Vertragswirksamkeit, zulässige Kündigungsfrist675hI/II und EntgeltverbotIV separat; kein Kündigungsentgelt ergänzen. Geschuldetes Entgelt und Rückerstattung nicht als zwei zusätzliche Ansprüche zusammenzählen.',
)
```
