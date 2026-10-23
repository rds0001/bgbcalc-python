<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbraucherdarlehen_zinsschadensgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesondert_verbuchte_verzugszinsen`: Nichtnegative exakte unveränderte Zinsschuldbasis nach497II als EUR-Dezimalzeichenfolge/Bruch.
- `nachgewiesener_zinsschaden`: Rechtlich qualifiziert nachgewiesener Schaden desselben Zeitabschnitts in EUR, nichtnegativ und exakt.
- `zeitanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des belegten Jahresanteils.
- `zeitanteil_nenner`: Positive ganze Zahl als Nenner des belegten Jahresanteils.
- `zeitanteil_nachweis`: Nichtleerer Nachweis des Zeitraums und der rechtlich maßgeblichen Zeitkonvention.
- `einordnungsnachweis`: Nichtleerer Nachweis des497II-Zinsschadensfalls; kein Immobiliardarlehen, keine automatische Verzinsung von Zinsen.

Nachgewiesenen Schaden auf gesonderte Zinsschuld mal4Prozent mal qualifiziertem Jahresanteil begrenzen; vorhandenen gesetzlichen Zinskern verwenden.

wert ist der begrenzte nachgewiesene Zinsschaden in EUR als exakter Bruch.

Nur §497 Absatz2 Satz2 in Verbindung mit §289 Satz2 für Allgemein-Verbraucherdarlehen; Immobiliar-Verbraucherdarlehen nach Absatz4 ausgenommen. Grundlage sind qualifiziert gesondert verbuchte nach Verzugseintritt anfallende Zinsen, keine gesamte Darlehensrestschuld und kein automatischer Zinseszins. Ein einheitlicher Schadens-/Jahresanteilsabschnitt mit unveränderter Zinsschuldbasis; bei laufend anfallenden Zinsen Teilabschnitte separat qualifizieren, keine Verzinsung vor Entstehung. Nachgewiesener Schaden und Anspruchsvoraussetzungen extern; der Vierprozentbetrag begrenzt nur den Schaden. Jahresanteil aus belegter Zeitkonvention, keine automatische365- oder360-Tage-Annahme.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_497_T0004

```python
from bgbcalc import verbraucherdarlehen_zinsschadensgrenze
verbraucherdarlehen_zinsschadensgrenze(
    gesondert_verbuchte_verzugszinsen='1000',
    nachgewiesener_zinsschaden='50',
    zeitanteil_zaehler=1,
    zeitanteil_nenner=2,
    zeitanteil_nachweis='Ein rechtlich belegtes halbes Jahr bei unveränderter Zinsschuld.',
    einordnungsnachweis='Allgemein-Verbraucherdarlehen, qualifizierter nachgewiesener497II-Zinsschaden.',
)
```
