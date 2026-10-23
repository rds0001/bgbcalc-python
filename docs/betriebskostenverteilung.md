<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betriebskosten_umstellung_mietherabsetzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisherige_zeitraummiete`: Nichtnegativer exakter qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruch; Miete und Kosten gleiche Zeiteinheit, enthaltener Kostenanteil höchstens Miete.
- `bisher_enthaltener_kostenanteil`: Nichtnegativer exakter qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruch; Miete und Kosten gleiche Zeiteinheit, enthaltener Kostenanteil höchstens Miete.
- `einordnungsnachweis`: Nichtleerer Nachweis rechtlich zutreffenden556a-Umlagemaßstabs/Kostenkreises bzw. zulässiger Umstellung und bisherigen Kostenanteils.

Bisherige Miete um bislang enthaltene künftig gesondert umgelegte Betriebskosten herabsetzen.

wert enthält je Position Quote/Wohnungsbetrag und Gesamtsumme oder den herabgesetzten Mietbetrag; exakte EUR-/Quotenbrüche.

Nur §556a Absatz2 Satz3 nach qualifiziert zulässiger Umstellung der Umlage erfassten Verbrauchs/Verursachung. Kostenanteil und Miete gleiche Zeiteinheit, nicht Jahreskosten unmittelbar von Monatsmiete abziehen. Nur bisher tatsächlich in der Miete enthaltenen künftig gesonderten Anteil abziehen, keine Schätzung durch Bibliothek. Textform, rechtzeitige Erklärung vor Abrechnungsbeginn und Wirksamkeit gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556a_T0005

```python
from bgbcalc import betriebskosten_umstellung_mietherabsetzung
betriebskosten_umstellung_mietherabsetzung(
    bisherige_zeitraummiete='1000',
    bisher_enthaltener_kostenanteil='150',
    einordnungsnachweis='Zulässige Umstellung, bisher enthaltener Kostenanteil derselben Periode künftig separat.',
)
```

## betriebskosten_wohnungsanteile

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kostenpositionen`: Liste1..1000 eindeutige position_id, gesamtkosten, wohnungsbezugswert, gesamtbezugswert und umlagemassstab wohnflaeche/verbrauch/verursachung/vereinbarung/wohnungseigentum. Exakte nichtnegative Werte; Gesamtbezugswert positiv und mindestens Wohnungswert; je Position gleiche Einheit/Abrechnungsbasis.
- `einordnungsnachweis`: Nichtleerer Nachweis rechtlich zutreffenden556a-Umlagemaßstabs/Kostenkreises bzw. zulässiger Umstellung und bisherigen Kostenanteils.

Je Betriebskostenposition qualifizierten Bezugsanteil berechnen und Wohnungsbeträge summieren.

wert enthält je Position Quote/Wohnungsbetrag und Gesamtsumme oder den herabgesetzten Mietbetrag; exakte EUR-/Quotenbrüche.

Nur §556a mit bereits rechtlich qualifiziertem Umlagemaßstab und umlagefähigen Kosten. Vorrang abweichender Vorschriften/Vereinbarungen, erfasster Verbräuche/Verursachung sowie besonderer WEG-Verteilung rechtlich bestimmen; unbilligen WEG-Schlüssel nicht ungeprüft übernehmen. Bezugswerte je Position müssen denselben vollständigen Abrechnungskreis und Zeitraum betreffen. Einheiten können zwischen Positionen verschieden sein, innerhalb einer Position identisch. Verbrauchsabhängige Mischschlüssel in disjunkte Kostenkomponenten aufteilen, keine Doppelzählung. Keine Bestimmung der Kostenumlagefähigkeit, Messwertschätzung, Leerstands-/Nutzerwechselzuordnung oder Heizkosten-Sondervorschriften.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556a_T0001, BGB_556a_T0002, BGB_556a_T0006, BGB_556a_T0007

```python
from bgbcalc import betriebskosten_wohnungsanteile
betriebskosten_wohnungsanteile(
    kostenpositionen=[{'position_id': 'Flaeche', 'gesamtkosten': '1000', 'wohnungsbezugswert': '30', 'gesamtbezugswert': '100', 'umlagemassstab': 'wohnflaeche'}, {'position_id': 'Verbrauch', 'gesamtkosten': '900', 'wohnungsbezugswert': '20', 'gesamtbezugswert': '100', 'umlagemassstab': 'verbrauch'}],
    einordnungsnachweis='Qualifizierte umlagefähige Kosten nach unterschiedlichen passenden556a-Schlüsseln ohne Überschneidung.',
)
```
