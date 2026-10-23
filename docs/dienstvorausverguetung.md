<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dienstkuendigung_vorausverguetungsrueckzahlung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vorausverguetung`: Nichtnegativer exakter EUR-Betrag der tatsächlich vorausbezahlten Vergütung für den betrachteten Zeitraum.
- `zeitanteil_nach_kuendigung_zaehler`: Nichtnegative ganze Zahl des rechtlich bestimmten auf die spätere Zeit entfallenden Vergütungsanteils, höchstens Nenner und2^53-1.
- `zeitanteil_nach_kuendigung_nenner`: Positive ganze Bezugsgröße desselben vorausbezahlten Zeitraums, höchstens2^53-1. Vergütungskonvention und Kündigungszeitpunkt im Nachweis belegen.
- `kuendigungsumstand_nicht_zu_vertreten`: Expliziter Wahrheitswert: Kündigung erfolgt wegen eines vom Dienstverpflichteten nicht zu vertretenden Umstands; dann Bereicherungsrecht, andernfalls346.
- `abziehbare_entreicherung`: Nur im Bereicherungsfall nichtnegativer bereits rechtlich abzugsfähiger EUR-Betrag, höchstens vorausbezahlter Nachkündigungsanteil. Nullverlust ausdrücklich0. Im346-Fall null.
- `einordnungsnachweis`: Nichtleerer Nachweis des628I3-Falls, tatsächlich vorausbezahlten Zeitraums, Vergütungsanteils und rechtlich qualifizierter Rückabwicklung; nicht automatisch jede freie Kündigung gleichsetzen.

Vorauszahlung mit qualifiziertem Nachkündigungsanteil multiplizieren; nur im Bereicherungsfall rechtlich abzugsfähige Entreicherung abziehen.

wert: rechnerischer_vorausanteil und rechnerischer_rueckzahlungsbetrag als exakte EUR-Brüche.

§628I3 nach qualifizierter Kündigung626/627 nach Dienstbeginn: nur im Voraus entrichtete Vergütung für Zeit nach Kündigung. Anteil auf den tatsächlich vorausbezahlten Zeitraum beziehen, nicht blind auf gesamte Vertragsvergütung oder bisherige Leistungsquote. Teilbetrag nach der rechtlich einschlägigen Vergütungs-/Zeitkonvention bestimmen; keine universelle Dreißigtage- oder Jahreskonvention. Hat der Dienstverpflichtete den Kündigungsumstand nicht zu vertreten, gelten Bereicherungsvorschriften; abzugsfähige Entreicherung insbesondere unter Berücksichtigung818/819/820 rechtlich bestimmen. Im346-Fall keine818III-Entreicherung abziehen. Weitere Nutzungen, Wertersatz, frühere Leistungen und Interessenverlust628I1/2 sowie Kündigungsschaden628II separat; keine automatische Aufrechnung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_628_T0001, BGB_628_T0002, BGB_628_T0003

```python
from bgbcalc import dienstkuendigung_vorausverguetungsrueckzahlung
dienstkuendigung_vorausverguetungsrueckzahlung(
    vorausverguetung='1200',
    zeitanteil_nach_kuendigung_zaehler=1,
    zeitanteil_nach_kuendigung_nenner=3,
    kuendigungsumstand_nicht_zu_vertreten=False,
    abziehbare_entreicherung=None,
    einordnungsnachweis='§628I3 nach qualifizierter Kündigung626/627 nach Dienstbeginn: nur im Voraus entrichtete Vergütung für Zeit nach Kündigung. Anteil auf den tatsächlich vorausbezahlten Zeitraum beziehen, nicht blind auf gesamte Vertragsvergütung oder bisherige Leistungsquote. Teilbetrag nach der rechtlich einschlägigen Vergütungs-/Zeitkonvention bestimmen; keine universelle Dreißigtage- oder Jahreskonvention. Hat der Dienstverpflichtete den Kündigungsumstand nicht zu vertreten, gelten Bereicherungsvorschriften; abzugsfähige Entreicherung insbesondere unter Berücksichtigung818/819/820 rechtlich bestimmen. Im346-Fall keine818III-Entreicherung abziehen. Weitere Nutzungen, Wertersatz, frühere Leistungen und Interessenverlust628I1/2 sowie Kündigungsschaden628II separat; keine automatische Aufrechnung.',
)
```
