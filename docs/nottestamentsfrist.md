<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## nottestament_grundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `errichtung_am`: ISO-Datum YYYY-MM-DD der rechtlich qualifizierten Nottestamentserrichtung2249/2250/2251.
- `einordnungsnachweis`: Nichtleerer Nachweis des Fristtatbestands. Ergebnis rohe Grundfrist, Hemmung2252II/UnterbrechungIII gesondert.

Drei Kalendermonate ab Errichtung als Ereignisfrist nach187/188.

wert ist ISO-Datum der rohen Dreimonatsgrundfrist.

Keine Hemmung2252II oder neue ReiseIII berücksichtigt. Kein Gültigkeitsurteil bei Fortleben/Tod/TodeserklärungIV. Keine automatische193-Verschiebung.

Kalenderdaten ISO YYYY-MM-DD im Bereich0001..9999, Pflichtwahrheitswerte und nichtleerer Nachweis. Fehlende Pflichteingabe EINGABE_FEHLT; ungültige Eingabe oder Datumsüberlauf EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2252_T0001

```python
from bgbcalc import nottestament_grundfrist
nottestament_grundfrist(
    errichtung_am='2024-01-31',
    einordnungsnachweis='Synthetisch qualifizierter Errichtungstag.',
)
```

## seetestament_reise_neustart

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriges_fristende`: ISO-Datum des bereits rechtlich korrigierten bisherigen Endes einschließlich aller bisherigen Hemmungen/Unterbrechungen.
- `neue_seereise_beginn`: ISO-Datum des Antritts einer neuen Seereise; bis einschließlich bisherigem Endtag rechtzeitig.
- `neue_seereise_ende`: ISO-Datum des Reiseendes, nicht vor Antritt. Ab diesem Ereignis neue volle Dreimonatsgrundfrist.
- `seetestament_nach_2251_qualifiziert`: Pflichtwahrheitswert zum rechtlich qualifizierten2251-Fall; FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis bisheriger Fristkorrekturen und neuer Seereise.

Bei2251 und Reisebeginn spätestens am bisherigen Fristendtag neue volle Dreimonatsgrundfrist ab Reiseende.

wert ist ISO-Datum der neuen rohen Grundfrist; bei fehlendem Tatbestand NICHT_ANWENDBAR mit NULL.

Verspäteter Antritt keine Wiederbelebung. Weitere Hemmung2252II/erneute Reisen extra. Keine Gültigkeitsentscheidung2252I/IV.

Kalenderdaten ISO YYYY-MM-DD im Bereich0001..9999, Pflichtwahrheitswerte und nichtleerer Nachweis. Fehlende Pflichteingabe EINGABE_FEHLT; ungültige Eingabe oder Datumsüberlauf EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2252_T0003

```python
from bgbcalc import seetestament_reise_neustart
seetestament_reise_neustart(
    bisheriges_fristende='2024-01-31',
    neue_seereise_beginn='2024-01-30',
    neue_seereise_ende='2024-02-20',
    seetestament_nach_2251_qualifiziert=True,
    einordnungsnachweis='Synthetisch korrigiertes bisheriges Fristende und neue Reise.',
)
```
