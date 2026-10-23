<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## besitz_nutzungswerte_im_haftungszeitraum

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `haftungsbeginn_utc`: Rechtlich maßgeblicher Beginn der Nutzungsverantwortlichkeit als ausreichend genauer UTC-SekundenzeitpunktYYYY-MM-DDTHH:MM:SSZ.
- `beginn_eingeschlossen`: Wahrheitswert: Beginn gehört zum qualifizierten Haftungszeitraum.987 nach Eintritt und990 von Erwerb/Kenntnis zeitlich rechtlich zutreffend normalisieren.
- `abrechnungsende_utc`: Letzter eingeschlossener UTC-Sekundenzeitpunkt der vollständig bekannten Abrechnung.
- `nutzungen`: Liste0..1000 mit genau nutzung_id, nutzungszeitpunkt_utc, nutzungsart (gezogen oder schuldhaft_nichtgezogen), nutzungswert(EUR). Pro Position eigener nachgewiesener Wert, keine doppelt gezählten tatsächlich/unterlassenen Nutzungen.
- `einordnungsnachweis`: Nichtleerer Nachweis des987/990/991I-Falls, Beginn-/Endeinschlusses, rechtlich zutreffenden Nutzungszeitpunkts und Wertes; für nichtgezogene Nutzungen ordnungsgemäße Wirtschaft und Verschulden vorqualifiziert.

Qualifizierte Nutzungspositionen im maßgeblichen Haftungszeitraum auswählen und Werte nach gezogener und schuldhaft nicht gezogener Nutzung getrennt summieren.

wert.gezogener_nutzungswert, schuldhaft_nichtgezogener_nutzungswert und gesamter_nutzungswert als exakte Eurobrüche; beruecksichtigte_nutzung_ids als Liste in Eingabereihenfolge.

§§987/990,gegebenenfalls991I: qualifizierte Nutzungspositionen nach Haftungszeitraum auswählen, tatsächlich gezogene und schuldhaft nicht gezogene Werte getrennt summieren. Anwendungsfall, gegebenenfalls kumulative Verantwortlichkeit mittelbaren Besitzers991I, Bewertungsmaßstab und zeitliche Zuordnung extern. Keine automatische Bösgläubigkeit, Rechtshängigkeit oder Verschuldensentscheidung. Mehrtägige Nutzungsabschnitte an Haftungsgrenzen vorher rechtlich zutreffend aufteilen; kein pauschales Abstellen auf Buchungs-/Zahlungstag. UTC-Sekunden nur bei ausreichend genauer Normalisierung, keine Subsekunden abschneiden. Werte in Euro begründen keinen automatischen Geldersatz statt Naturherausgabe.988/993-Bereicherung und weitergehende Verzugshaftung gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_987_T0001, BGB_987_T0002, BGB_990_T0001, BGB_990_T0002, BGB_991_T0001

```python
from bgbcalc import besitz_nutzungswerte_im_haftungszeitraum
besitz_nutzungswerte_im_haftungszeitraum(
    haftungsbeginn_utc='2024-01-01T10:00:00Z',
    beginn_eingeschlossen=False,
    abrechnungsende_utc='2024-01-02T12:00:00Z',
    nutzungen=[{'nutzung_id': 'vorher', 'nutzungszeitpunkt_utc': '2024-01-01T09:59:59Z', 'nutzungsart': 'gezogen', 'nutzungswert': '500'}, {'nutzung_id': 'grenze', 'nutzungszeitpunkt_utc': '2024-01-01T10:00:00Z', 'nutzungsart': 'gezogen', 'nutzungswert': '20'}, {'nutzung_id': 'spaeter', 'nutzungszeitpunkt_utc': '2024-01-01T10:00:01Z', 'nutzungsart': 'gezogen', 'nutzungswert': '30'}, {'nutzung_id': 'unterlassen', 'nutzungszeitpunkt_utc': '2024-01-02T12:00:00Z', 'nutzungsart': 'schuldhaft_nichtgezogen', 'nutzungswert': '40'}, {'nutzung_id': 'danach', 'nutzungszeitpunkt_utc': '2024-01-02T12:00:01Z', 'nutzungsart': 'gezogen', 'nutzungswert': '600'}],
    einordnungsnachweis='§§987/990,gegebenenfalls991I: qualifizierte Nutzungspositionen nach Haftungszeitraum auswählen, tatsächlich gezogene und schuldhaft nicht gezogene Werte getrennt summieren. Anwendungsfall, gegebenenfalls kumulative Verantwortlichkeit mittelbaren Besitzers991I, Bewertungsmaßstab und zeitliche Zuordnung extern. Keine automatische Bösgläubigkeit, Rechtshängigkeit oder Verschuldensentscheidung. Mehrtägige Nutzungsabschnitte an Haftungsgrenzen vorher rechtlich zutreffend aufteilen; kein pauschales Abstellen auf Buchungs-/Zahlungstag. UTC-Sekunden nur bei ausreichend genauer Normalisierung, keine Subsekunden abschneiden. Werte in Euro begründen keinen automatischen Geldersatz statt Naturherausgabe.988/993-Bereicherung und weitergehende Verzugshaftung gesondert.',
)
```
