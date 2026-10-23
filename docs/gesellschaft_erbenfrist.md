<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_erbenrechtsfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `erbschaftskenntnis_am`: Kenntnis des Erbschaftsanfalls YYYY-MM-DD; nicht automatisch Todestag.
- `ablaufhemmung_mindestende_am`: Rechtlich vollständig bestimmtes210-Mindestende YYYY-MM-DD; null ausschließlich wenn keine wirksame210-Verlängerung besteht. Ungeklärten Schutz nicht als null behandeln.
- `ausschlagungsrecht_bei_dreimonatsablauf_noch_offen`: Expliziter Wahrheitswert für das bei Ablauf der gesetzlichen Dreimonatsgrundfrist noch bestehende Ausschlagungsrecht.
- `ausschlagungsfristende_am`: Nur bei noch offenem Ausschlagungsrecht dessen vollständig bestimmtes Ende YYYY-MM-DD; sonst null.
- `einordnungsnachweis`: Nichtleerer Nachweis des724III-Falls, Kenntnis,210-Behandlung und Ausschlagungsrechts einschließlich Hemmung und Verlustgründen.

Dreimonatsgrundfrist mit wirksamer210-Ablaufhemmung und noch offener Ausschlagungsfrist als spätestes Ende verknüpfen.

wert.dreimonatsgrundfristende und wert.rechnerisches_ausuebungsfristende alsYYYY-MM-DD.

§724III: Drei Monate ab Kenntnis des Erbschaftsanfalls, entsprechend210 bestimmtes Mindestende und gegebenenfalls späteres Ausschlagungsfristende als Maximum. Ob das Ausschlagungsrecht bei Ablauf der Dreimonatsgrundfrist noch besteht, separat rechtlich vorqualifizieren, nicht allein aus einem theoretischen Datum folgern.210-Mindestende mit vorhandener Ablaufhemmungsfunktion berechnen: die maßgebliche Frist beträgt drei Monate, daher210-Nachlauf grundsätzlich entsprechend kürzer als sechs Monate. Offene/ungeklärte Schutzereignisse nicht durch fiktives Enddatum oder null ersetzen. Keine automatische Annahme/Ausschlagung, Kommanditistenstellung, Kündigungswirksamkeit oder Haftungsbeschränkung nachAbsatz4. Keine pauschale Feiertagsverschiebung; gegebenenfalls weitere rechtliche Kalenderkorrektur separat.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_724_T0003, BGB_724_T0004, BGB_724_T0005, BGB_210_T0001, BGB_210_T0002, BGB_210_T0003

```python
from bgbcalc import gesellschaft_erbenrechtsfrist
gesellschaft_erbenrechtsfrist(
    erbschaftskenntnis_am='2024-01-31',
    ablaufhemmung_mindestende_am=None,
    ausschlagungsrecht_bei_dreimonatsablauf_noch_offen=False,
    ausschlagungsfristende_am=None,
    einordnungsnachweis='§724III: Drei Monate ab Kenntnis des Erbschaftsanfalls, entsprechend210 bestimmtes Mindestende und gegebenenfalls späteres Ausschlagungsfristende als Maximum. Ob das Ausschlagungsrecht bei Ablauf der Dreimonatsgrundfrist noch besteht, separat rechtlich vorqualifizieren, nicht allein aus einem theoretischen Datum folgern.210-Mindestende mit vorhandener Ablaufhemmungsfunktion berechnen: die maßgebliche Frist beträgt drei Monate, daher210-Nachlauf grundsätzlich entsprechend kürzer als sechs Monate. Offene/ungeklärte Schutzereignisse nicht durch fiktives Enddatum oder null ersetzen. Keine automatische Annahme/Ausschlagung, Kommanditistenstellung, Kündigungswirksamkeit oder Haftungsbeschränkung nachAbsatz4. Keine pauschale Feiertagsverschiebung; gegebenenfalls weitere rechtliche Kalenderkorrektur separat.',
)
```
