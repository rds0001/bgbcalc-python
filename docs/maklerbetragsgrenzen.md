<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## makler_anderer_partei_hoechstbelastung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `qualifizierter_gesamtmaklerlohn`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; einheitliche Kostenbasis ohne Doppelzählung. Erlass höchstens bisheriger Maklerlohn je Partei.
- `einordnungsnachweis`: Nichtleerer Nachweis des §656b-Verbraucher-/Immobilienfalls und wirksamer qualifizierter Maklerlohn-/Erlassbasis.

Gesamtmaklerlohn durch zwei teilen als maximale auf andere Vertragspartei abwälzbare Belastung

wert ist die Höchstbelastung der anderen Partei oder verbleibender gleicher Maklerlohn je Partei in EUR als exakter Bruch.

Nur §656d bei einem Maklervertrag mit einer Partei eines Wohnungs-/Einfamilienhauskaufs und Verbrauchereigenschaft des Käufers nach §656b. Gesamtmaklerlohn ist die rechtlich wirksame einheitliche Kostenbasis beider Parteien nach qualifizierten Ermäßigungen/Erlassen; keine Zusammenzählung zusätzlicher identischer Forderungen. Ergebnis nur Belastungsobergrenze; überschreitende Vereinbarung wird nicht automatisch auf Hälfte reduziert. Fälligkeit verlangt Zahlung und Nachweis nach Satz2; kein automatischer Fälligkeitseintritt.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_656d_T0001

```python
from bgbcalc import makler_anderer_partei_hoechstbelastung
makler_anderer_partei_hoechstbelastung(
    qualifizierter_gesamtmaklerlohn='6000',
    einordnungsnachweis='Qualifizierter656d-Fall mit Verbraucher-Käufer.',
)
```

## makler_gleichwirkender_erlass_restbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriger_gleicher_maklerlohn_je_partei`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; einheitliche Kostenbasis ohne Doppelzählung. Erlass höchstens bisheriger Maklerlohn je Partei.
- `qualifizierter_erlassbetrag`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; einheitliche Kostenbasis ohne Doppelzählung. Erlass höchstens bisheriger Maklerlohn je Partei.
- `einordnungsnachweis`: Nichtleerer Nachweis des §656b-Verbraucher-/Immobilienfalls und wirksamer qualifizierter Maklerlohn-/Erlassbasis.

Von bisherigem gleichen Maklerlohn je Partei den qualifizierten gleichwirkenden Erlassbetrag abziehen

wert ist die Höchstbelastung der anderen Partei oder verbleibender gleicher Maklerlohn je Partei in EUR als exakter Bruch.

Nur §656c Absatz1 Satz3/4 bei zuvor wirksam gleich hohen Maklerlohnpflichten beider Parteien und Verbraucher-Käufer nach §656b; erlassene Geldsumme wirkt spiegelbildlich auf jeweils gleiche Pflicht. Erlassbetrag höchstens ursprünglicher je-Partei-Betrag. Bei verschiedenen/mehrfachen Erlassen deren rechtliche Wechselwirkung zuerst qualifizieren, nicht mehrfach denselben Erlass abziehen. Keine Heilung anfänglich ungleicher/unwirksamer Verpflichtungen; keine automatische Erstattung bereits gezahlter Provisionen. Entsprechende Anwendung nach §656d Absatz2 nur bei fachlich qualifizierter gleichartiger Berechnungsbasis.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_656c_T0003

```python
from bgbcalc import makler_gleichwirkender_erlass_restbetrag
makler_gleichwirkender_erlass_restbetrag(
    bisheriger_gleicher_maklerlohn_je_partei='3000',
    qualifizierter_erlassbetrag='500',
    einordnungsnachweis='Wirksam gleiche Ausgangsprovisionen und qualifizierter gleichwirkender Erlass.',
)
```
