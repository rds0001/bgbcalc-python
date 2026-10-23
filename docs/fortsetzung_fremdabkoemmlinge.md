<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fortsetzung_nichtgemeinsame_abkoemmlinge_gesamtgut

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `teilungsfaehiges_gesamtgut`: Nichtnegativer Netto-Teilungswert des ursprünglichen Gesamtguts in EUR nach gesonderter Schuldenberichtigung, Rückbehalten und internen Ausgleichspositionen. Gesetzlicher hälftiger Teilungsfall nach §1476I.
- `erbquoten_nichtgemeinsamer_abkoemmlinge`: Liste0..1000 eindeutiger Objekte mit abkoemmling_id und erbquote. Rechtlich bestimmte Erbquoten am hypothetischen Nachlass ohne Fortsetzung; keine Quote am gesamten Gesamtgut. Summe höchstens1. Erbquoten können durch vorhandene Erbquotenfunktionen vorbereitet werden.
- `einordnungsnachweis`: Nichtleere Qualifikation von §1483II, gesetzlicher Halbteilung und vollständiger Liste der nichtgemeinschaftlichen Abkömmlinge; keine abweichende Teilungsregel.

Gesamtgut halbieren, nichtgemeinschaftliche Erbquoten auf Nachlasshälfte anwenden und Gesamtgutrest bestimmen.

wert enthält hypothetischer_nachlassanteil_gesamtgut, herauszurechnende_anteile mit abkoemmling_id/betrag, herauszurechnender_gesamtbetrag und verbleibendes_gesamtgut. Geldwerte als exakte EUR-Brüche.

§1483II: ursprünglichen, bereits bereinigten Gesamtgutwert hälftig dem hypothetischen Nachlass zuordnen; Erbquoten der nichtgemeinschaftlichen Abkömmlinge auf diese Hälfte anwenden und aus dem Gesamtgut herausrechnen. Nur Gesamtgutkomponente ihrer Erbteile; Sondergut/Vorbehaltsgut und sonstige Nachlasspositionen gesondert. Keine automatische Güterstands-, Abstammungs-, Erbquoten- oder Bewertungsentscheidung. Keine erneute Schuldenberichtigung bereits bereinigter Werte, kein negativer Nachlass und keine pauschale Kappung tatsächlicher Außenhaftung. Abweichende ehevertragliche Teilungsverhältnisse nicht mit Halbteilung vermischen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1483_T0004, BGB_1476_T0001

```python
from bgbcalc import fortsetzung_nichtgemeinsame_abkoemmlinge_gesamtgut
fortsetzung_nichtgemeinsame_abkoemmlinge_gesamtgut(
    teilungsfaehiges_gesamtgut='1000',
    erbquoten_nichtgemeinsamer_abkoemmlinge=[{'abkoemmling_id': 'A', 'erbquote': {'zaehler': '3', 'nenner': '8'}}],
    einordnungsnachweis='§1483II: ursprünglichen, bereits bereinigten Gesamtgutwert hälftig dem hypothetischen Nachlass zuordnen; Erbquoten der nichtgemeinschaftlichen Abkömmlinge auf diese Hälfte anwenden und aus dem Gesamtgut herausrechnen. Nur Gesamtgutkomponente ihrer Erbteile; Sondergut/Vorbehaltsgut und sonstige Nachlasspositionen gesondert. Keine automatische Güterstands-, Abstammungs-, Erbquoten- oder Bewertungsentscheidung. Keine erneute Schuldenberichtigung bereits bereinigter Werte, kein negativer Nachlass und keine pauschale Kappung tatsächlicher Außenhaftung. Abweichende ehevertragliche Teilungsverhältnisse nicht mit Halbteilung vermischen.',
)
```
