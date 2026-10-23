<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_mietverfuegung_zeitzuordnung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `beschlagnahme_am`: Qualifizierte Beschlagnahme zugunsten des HypothekengläubigersYYYY-MM-DD.
- `mietabschnitte`: Liste0..1000 überschneidungsfreier Abschnitte einer Miet-/Pachtforderung, je genau abschnitt_id, erster_miettag, letzter_miettag, verfuegungsbetrag(EUR). Vor der Beschlagnahme rechtlich erfolgte Verfügung vorausgesetzt. Grenzüberschreitende Abschnitte zuvor zutreffend aufteilen.
- `einordnungsnachweis`: Nichtleerer Nachweis des1124I/II-Falls, vorzeitiger Verfügung und identischer Forderungsgrundlage; Zeiträume betreffen die Miet-/Pachtzeit, nicht Zahlung oder Fälligkeit.

Vor Beschlagnahme verfügte Miet-/Pachtabschnittsbeträge nach gesetzlicher Monatsgrenze zeitlich auswählen und getrennt summieren.

wert.letzter_erfasster_miettag als Datum; betrag_im_zeitlichen_fenster und betrag_ausserhalb_des_zeitlichen_fensters als Eurobrüche; abschnitt_ids_im_zeitlichen_fenster in Eingabereihenfolge.

§1124II: vor Beschlagnahme erfolgte Verfügungen nach ihrem Miet-/Pachtzeitraum der Monatsgrenze zuordnen. Beschlagnahme bis einschließlich15.: Ende laufender Monat; nach15.: Ende Folgemonat. Beträge vollständig innerhalb/außerhalb getrennt summieren. Keine pauschale gleichmäßige Tagesaufteilung für einen grenzüberschreitenden Gesamtbetrag. Nur eine Forderungs-/Vertragsgrundlage je Aufruf; mehrere Verträge getrennt behandeln. Zeitliche Zuordnung setzt übrige1124-Voraussetzungen voraus und entscheidet keine sonstigen Wirksamkeitsfragen.1123-Jahresbefreiung sowie1126-Dreimonatsregel nicht durch diesen Monatsvergleich ersetzen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1124_T0001, BGB_1124_T0002, BGB_1124_T0003

```python
from bgbcalc import hypothek_mietverfuegung_zeitzuordnung
hypothek_mietverfuegung_zeitzuordnung(
    beschlagnahme_am='2024-01-15',
    mietabschnitte=[{'abschnitt_id': 'Januar', 'erster_miettag': '2024-01-01', 'letzter_miettag': '2024-01-31', 'verfuegungsbetrag': '100'}, {'abschnitt_id': 'Februar', 'erster_miettag': '2024-02-01', 'letzter_miettag': '2024-02-29', 'verfuegungsbetrag': '200'}, {'abschnitt_id': 'Maerz', 'erster_miettag': '2024-03-01', 'letzter_miettag': '2024-03-31', 'verfuegungsbetrag': '300'}],
    einordnungsnachweis='§1124II: vor Beschlagnahme erfolgte Verfügungen nach ihrem Miet-/Pachtzeitraum der Monatsgrenze zuordnen. Beschlagnahme bis einschließlich15.: Ende laufender Monat; nach15.: Ende Folgemonat. Beträge vollständig innerhalb/außerhalb getrennt summieren. Keine pauschale gleichmäßige Tagesaufteilung für einen grenzüberschreitenden Gesamtbetrag. Nur eine Forderungs-/Vertragsgrundlage je Aufruf; mehrere Verträge getrennt behandeln. Zeitliche Zuordnung setzt übrige1124-Voraussetzungen voraus und entscheidet keine sonstigen Wirksamkeitsfragen.1123-Jahresbefreiung sowie1126-Dreimonatsregel nicht durch diesen Monatsvergleich ersetzen.',
)
```
