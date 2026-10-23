<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pauschalreise_beendigung_preisabrechnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reiseleistungen`: Liste1..1000 mit genau leistung_id, preisanteil, gezahlter_anteil und leistungsstatus. Eindeutige IDs; exakte nichtnegative EUR-Werte; Zahlung höchstens Preis. Status erbracht, zur_beendigung_noch_zu_erbringen oder entfaellt.
- `einordnungsnachweis`: Nichtleerer Nachweis wirksamer651l-Kündigung und sachgerechter Preis-/Zahlungszuordnung, ohne Rückbeförderungsmehrkosten des Veranstalters.

Verbleibende/entfallene Preisanteile getrennt summieren; gezahlte entfallene Anteile erstatten; unbezahlte verbleibende Anteile getrennt ausweisen.

wert enthält vier exakte EUR-Brüche: verbleibender_preisanspruch, entfallender_preisanspruch, zu_erstattende_zahlungen, offene_zahlung_auf_verbleibenden_preis.

Keine Tagespauschale, automatische Aufrechnung, zusätzliche Minderung oder Schadensersatzrechnung. Zahlungen über Positionspreis gesondert.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651l_T0003, BGB_651l_T0004, BGB_651l_T0006

```python
from bgbcalc import pauschalreise_beendigung_preisabrechnung
pauschalreise_beendigung_preisabrechnung(
    reiseleistungen=[{'leistung_id': 'Flug', 'preisanteil': '300', 'gezahlter_anteil': '100', 'leistungsstatus': 'erbracht'}, {'leistung_id': 'Hotel', 'preisanteil': '600', 'gezahlter_anteil': '400', 'leistungsstatus': 'entfaellt'}, {'leistung_id': 'Rueckfahrt', 'preisanteil': '100', 'gezahlter_anteil': '0', 'leistungsstatus': 'zur_beendigung_noch_zu_erbringen'}],
    einordnungsnachweis='Qualifizierte651l-Kündigung; Vertragsanteile und Zahlungen getrennt, Rückbeförderungsmehrkosten nicht eingepreist.',
)
```
