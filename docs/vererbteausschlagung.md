<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vererbte_ausschlagungsfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `tod_des_erben_am`: ISO-Datum0001..9999 des Todes des Erben, dem die erste Erbschaft bereits angefallen war; nicht Tod des ursprünglichen Erblassers.
- `bisheriges_ausschlagungsfristende`: ISO-Datum des bisher rechtlich maßgeblichen Endes für Ausschlagung der zuerst angefallenen Erbschaft einschließlich zulässiger Korrekturen.
- `ausschlagungsfristende_erbeserbschaft`: ISO-Datum des rechtlich maßgeblichen Endes der Ausschlagungsfrist für die Erbschaft des nun verstorbenen Erben, individuell für den betreffenden Erbeserben. Frühestens Tod des Erben. Kenntnis, Bekanntgabe und Korrekturen gesondert bestimmen.
- `ausschlagungsrecht_vererblich_vorhanden`: Wahrheitswert: das Ausschlagungsrecht war bei Tod vorhanden und vererblich, insbesondere nicht durch bereits wirksame Annahme/Ausschlagung ausgeschlossen. Zeitablauf wird zusätzlich anhand der Daten geprüft.
- `einordnungsnachweis`: Nichtleere Begründung beider Erbfälle, der individuellen Fristenden und des bei Tod vorhandenen Ausschlagungsrechts.

Bei vorhandenem vererblichem Ausschlagungsrecht und Tod spätestens am letzten Tag der bisherigen Frist: Maximum aus bisherigem Fristende und Fristende der Erbschaft des Erben.

wert ist ISO-Datum des Mindestendes nach§1952 Absatz2. Ohne Anwendungsbereich oder bei Tod nach bisherigem Fristende NICHT_ANWENDBAR/null.

Keine Addition, kein pauschaler Neubeginn ab Tod. Für mehrere Erbeserben individuell prüfen; Teilrechte§1952 Absatz3 nicht vollständig modelliert. Kenntnis-/Auslandsregeln und Hemmung der jeweiligen Frist separat.

ISO-Daten0001..9999, expliziter Wahrheitswert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1952_T0001, BGB_1952_T0002, BGB_1952_T0003

```python
from bgbcalc import vererbte_ausschlagungsfrist
vererbte_ausschlagungsfrist(
    tod_des_erben_am='2030-02-01',
    bisheriges_ausschlagungsfristende='2030-02-28',
    ausschlagungsfristende_erbeserbschaft='2030-03-01',
    ausschlagungsrecht_vererblich_vorhanden=True,
    einordnungsnachweis='Synthetische zwei Erbfälle mit individuell qualifizierten Fristenden.',
)
```
