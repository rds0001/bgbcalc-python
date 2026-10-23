<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ankuendigung_vorlaufvergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vorlauffall`: modernisierung_555c, waermeumstellung_556c, mietaufrechnung_556b, zahlungsdienste_aenderung_675g, urlaubsprodukt_zahlung_486a gastschul_information_651u oder zahlung_vorabinformation_675x.
- `zugang_am`: ISO-Datum des tatsächlichen rechtlich maßgeblichen Zugangs einer vollständigen Erklärung/Information.
- `beabsichtigter_beginn_am`: ISO-Datum des Beginns der Maßnahme, Umstellung, Fälligkeit, Änderung oder Reise. Vorlauf muss vor Beginn dieses Tages vollständig abgelaufen sein; kein untertägiger Zeitpunkt.
- `einordnungsnachweis`: Nichtleere Qualifikation des gesetzlichen Vorlauffalls, des Zugangs und des Bezugsbeginns. Inhalt/Form/Adressat/Ausnahmen und zusätzliche Rechtsfolgen gesondert beurteilen.

Gesetzlichen Mindestvorlauf ab Zugang berechnen und Beginn nach vollständigem Fristablauf vergleichen.

wert.vorlauf_ablauf_am ist letzter eingeschlossener Fristtag, wert.fruehester_beginn_am der folgende Kalendertag; wert.vorlauf_eingehalten vergleicht den tatsächlichen geplanten Beginn mit dieser Mindestgrenze.

Mindestvorlauf ab tatsächlichem Zugang nach §§187I/188 vorwärts berechnen; der Zieltagesbeginn muss nach dem Ablaufdatum liegen. Nur kalendertäglicher Vorlauf, keine eigenständige qualitative Wirksamkeitsentscheidung und keine automatische Fristverschiebung nach§193. Bei verspäteter Ankündigung wird der tatsächlich beabsichtigte Beginn nicht automatisch geändert. §555cIV Bagatellausnahme, §556cI sonstige Umstellungsvoraussetzungen, §556bII zulässiger Forderungstyp und Textform, §675gII Zustimmung/Absätze3und4-Ausnahmen, §486a Zahlungsplan und §651uIII vollständige Information/angemessene Vorbereitung gesondert. §675xIII betrifft nur den Vierwochenvorlauf; direkte Zustimmung, wirksame Ausschlussvereinbarung und erforderliche Information sind gesonderte Voraussetzungen, kein automatischer Erstattungsausschluss. Untertägige Zeitpunktvereinbarungen sind nicht durch ein bloßes Datum abgebildet. Keine pauschale30-Tage-Monatsrechnung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_486a_T0001, BGB_486a_T0002, BGB_486a_T0003, BGB_486a_T0004, BGB_486a_T0005, BGB_555c_T0001, BGB_555c_T0002, BGB_555c_T0003, BGB_555c_T0004, BGB_555c_T0005, BGB_555c_T0006, BGB_555c_T0007, BGB_555c_T0008, BGB_555c_T0009, BGB_556b_T0001, BGB_556b_T0002, BGB_556b_T0003, BGB_556c_T0001, BGB_556c_T0002, BGB_556c_T0003, BGB_556c_T0004, BGB_556c_T0005, BGB_556c_T0006, BGB_556c_T0007, BGB_556c_T0008, BGB_651u_T0001, BGB_651u_T0002, BGB_651u_T0003, BGB_651u_T0004, BGB_651u_T0005, BGB_651u_T0006, BGB_651u_T0007, BGB_651u_T0008, BGB_651u_T0009, BGB_651u_T0010, BGB_651u_T0011, BGB_651u_T0012, BGB_651u_T0013, BGB_675g_T0001, BGB_675g_T0002, BGB_675g_T0003, BGB_675g_T0004, BGB_675g_T0005, BGB_675g_T0006, BGB_675g_T0007, BGB_675g_T0008, BGB_675x_T0001, BGB_675x_T0002, BGB_675x_T0003, BGB_675x_T0004, BGB_675x_T0005, BGB_675x_T0006, BGB_675x_T0007, BGB_675x_T0008, BGB_675x_T0009, BGB_675x_T0010, BGB_675x_T0011, BGB_675x_T0012, BGB_675x_T0013, BGB_675x_T0014

```python
from bgbcalc import ankuendigung_vorlaufvergleich
ankuendigung_vorlaufvergleich(
    vorlauffall='modernisierung_555c',
    zugang_am='2024-01-31',
    beabsichtigter_beginn_am='2024-05-01',
    einordnungsnachweis='Mindestvorlauf ab tatsächlichem Zugang nach §§187I/188 vorwärts berechnen; der Zieltagesbeginn muss nach dem Ablaufdatum liegen. Nur kalendertäglicher Vorlauf, keine eigenständige qualitative Wirksamkeitsentscheidung und keine automatische Fristverschiebung nach§193. Bei verspäteter Ankündigung wird der tatsächlich beabsichtigte Beginn nicht automatisch geändert. §555cIV Bagatellausnahme, §556cI sonstige Umstellungsvoraussetzungen, §556bII zulässiger Forderungstyp und Textform, §675gII Zustimmung/Absätze3und4-Ausnahmen, §486a Zahlungsplan und §651uIII vollständige Information/angemessene Vorbereitung gesondert. §675xIII betrifft nur den Vierwochenvorlauf; direkte Zustimmung, wirksame Ausschlussvereinbarung und erforderliche Information sind gesonderte Voraussetzungen, kein automatischer Erstattungsausschluss. Untertägige Zeitpunktvereinbarungen sind nicht durch ein bloßes Datum abgebildet. Keine pauschale30-Tage-Monatsrechnung.',
)
```
