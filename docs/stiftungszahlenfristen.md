<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## stiftung_uebergang_bekanntmachungsfristen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wirkungen_am`: ISO-Datum des Eintritts der Wirkungen§86f, regelmäßig Unanfechtbarkeit der Genehmigung/Entscheidung; keine bloße Vertragsunterzeichnung.
- `veroeffentlichung_am`: ISO-Datum der tatsächlichen ordnungsgemäßen Bundesanzeigerveröffentlichung ab Wirkungsereignis. Auch verspätete Veröffentlichung mit tatsächlichem Datum eingeben, nicht auf Sollfrist zurückdatieren.
- `einordnungsnachweis`: Nichtleere rechtliche Begründung von Wirkungsereignis und ordnungsgemäßer Bekanntmachung einschließlich Gläubigerhinweis.

Wirkungsdatum+1 Monat für Veröffentlichung; tatsächliche Veröffentlichung+2 Tage für Bewirkung; Bewirkung+6 Monate für Gläubigeranmeldung.

wert enthält rechnerisches_bekanntmachungsfristende, bekanntmachung_bewirkt_mit_ablauf, rechnerisches_anmeldefristende.

Grundfristen, ohne automatische Kalenderkorrekturen oder Sicherungsberechtigungsprüfung. Bewirkung am Tagesende.

ISO-Daten und berechnete Grenzen0001..9999; Anzahl als Ganzzahl0..2^53-1; nichtleerer Nachweis beim Fristmodell.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_86g_T0001, BGB_86g_T0002, BGB_86g_T0003, BGB_86h_T0001, BGB_86h_T0002, BGB_86h_T0003

```python
from bgbcalc import stiftung_uebergang_bekanntmachungsfristen
stiftung_uebergang_bekanntmachungsfristen(
    wirkungen_am='2030-01-31',
    veroeffentlichung_am='2030-02-28',
    einordnungsnachweis='Qualifizierte Unanfechtbarkeit und Veröffentlichung mit Gläubigerhinweis.',
)
```

## stiftung_zusammenlegung_mindestzahl

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anzahl_uebertragender_stiftungen`: Ganzzahl0..2^53-1 rechtlich bestimmter übertragender Stiftungen; neue übernehmende Stiftung nicht mitzählen.

Zahl übertragender Stiftungen mindestens2.

wert enthält mindestzahl=2 und mindestzahl_erreicht.

Nur numerische Voraussetzung, keine Zulässigkeit/Genehmigung und keine qualitative Prüfung der Nummern1bis3.

ISO-Daten und berechnete Grenzen0001..9999; Anzahl als Ganzzahl0..2^53-1; nichtleerer Nachweis beim Fristmodell.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_86a_T0001

```python
from bgbcalc import stiftung_zusammenlegung_mindestzahl
stiftung_zusammenlegung_mindestzahl(
    anzahl_uebertragender_stiftungen=0,
)
```
