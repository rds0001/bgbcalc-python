<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## anerkennung_fuenfjahresfrist_mit_hemmung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristausloesung_am`: Qualifizierte Registereintragung oder gesetzlich gleichgestellte Beurkundung1598II als EreignistagYYYY-MM-DD.
- `ruecknahmezeitraeume`: Liste höchstens1000 abgeschlossener, auf eingeschlossene Kalendertage normalisierter rechtlich wirksamer Rücknahme-Hemmungsintervalle mit genau erster_tag und letzter_tag.
- `aufschiebende_wirkung_zeitraeume`: Liste höchstens1000 abgeschlossener, auf eingeschlossene Kalendertage normalisierter Intervalle gerichtlich angeordneter aufschiebender Wirkung80V VwGO mit genau erster_tag und letzter_tag. Leere Liste bedeutet festgestellt keine.
- `einordnungsnachweis`: Nichtleerer Nachweis des1598II-Fristbeginns, Rücknahme mit unrichtig gewordener Eintragung und der vollständigen qualifizierten Hemmungs-/Ausnahmeintervalle.

Fünfjahresfrist berechnen; gerichtlich angeordnete aufschiebende Wirkungszeiten aus Rücknahmehemmung ausschneiden und verbleibende Hemmungstage vereinigt berücksichtigen.

wert.grundfrist_letzter_tag und rechnerischer_letzter_tag alsYYYY-MM-DD; beruecksichtigte_hemmungstage als ganze Zahl.

§1598II: Fünfjahresgrundlauf ab qualifiziertem Register-/Beurkundungsereignis. Von den abgeschlossenen qualifizierten Rücknahmeintervallen die Intervalle angeordneter aufschiebender Wirkung abziehen; verbleibende Tage vereinigen und nicht mitzählen. Bloße Rechtsbehelfseinlegung ist keine automatische aufschiebende Wirkung. Alle Intervalle müssen rechtlich taggenau normalisiert sein; offene oder unbekannte Enden nicht durch erfundene Daten ersetzen. Eine nach bereits abgeschlossenem Fristlauf eintretende Rücknahme setzt keine neue Frist in Gang. Keine automatische Anerkennungswirksamkeit, Ausländerbehördenentscheidung oder Feiertagsverschiebung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1598_T0003, BGB_1598_T0004, BGB_1598_T0005, BGB_1598_T0006, BGB_1598_T0007, BGB_1598_T0008

```python
from bgbcalc import anerkennung_fuenfjahresfrist_mit_hemmung
anerkennung_fuenfjahresfrist_mit_hemmung(
    fristausloesung_am='2020-01-01',
    ruecknahmezeitraeume=[{'erster_tag': '2021-03-01', 'letzter_tag': '2021-03-31'}],
    aufschiebende_wirkung_zeitraeume=[],
    einordnungsnachweis='§1598II: Fünfjahresgrundlauf ab qualifiziertem Register-/Beurkundungsereignis. Von den abgeschlossenen qualifizierten Rücknahmeintervallen die Intervalle angeordneter aufschiebender Wirkung abziehen; verbleibende Tage vereinigen und nicht mitzählen. Bloße Rechtsbehelfseinlegung ist keine automatische aufschiebende Wirkung. Alle Intervalle müssen rechtlich taggenau normalisiert sein; offene oder unbekannte Enden nicht durch erfundene Daten ersetzen. Eine nach bereits abgeschlossenem Fristlauf eintretende Rücknahme setzt keine neue Frist in Gang. Keine automatische Anerkennungswirksamkeit, Ausländerbehördenentscheidung oder Feiertagsverschiebung.',
)
```
