<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## digitalbeendigung_zeitanteilige_betraege

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarter_abschnittspreis`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Preis und Zahlung in EUR; Zeiteinheiten einheitlich und disjunkt, Gesamtzeit positiv. Zahlung proportional über den homogenen Preisabschnitt verteilt und höchstens Abschnittspreis.
- `gezahlter_abschnittspreis`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Preis und Zahlung in EUR; Zeiteinheiten einheitlich und disjunkt, Gesamtzeit positiv. Zahlung proportional über den homogenen Preisabschnitt verteilt und höchstens Abschnittspreis.
- `zeiteinheiten_gesamt`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Preis und Zahlung in EUR; Zeiteinheiten einheitlich und disjunkt, Gesamtzeit positiv. Zahlung proportional über den homogenen Preisabschnitt verteilt und höchstens Abschnittspreis.
- `zeiteinheiten_mangelhaft`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Preis und Zahlung in EUR; Zeiteinheiten einheitlich und disjunkt, Gesamtzeit positiv. Zahlung proportional über den homogenen Preisabschnitt verteilt und höchstens Abschnittspreis.
- `zeiteinheiten_nicht_mehr_zu_erbringen`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Preis und Zahlung in EUR; Zeiteinheiten einheitlich und disjunkt, Gesamtzeit positiv. Zahlung proportional über den homogenen Preisabschnitt verteilt und höchstens Abschnittspreis.
- `einordnungsnachweis`: Nichtleerer Nachweis der wirksamen Beendigung, Dauerbereitstellung, homogenen Bepreisung, proportionalen Zahlungszuordnung und disjunkten mangelhaften/entfallenden Zeitbereiche.

Disjunkte mangelhafte und künftig entfallende Zeiteinheiten addieren; durch Gesamtzeit teilen; Abschnittspreis und proportional zugeordneten Zahlungsbetrag mit Quote multiplizieren.

wert enthält entfallender_zeitanteil als Quote, erloschener_preisanteil und erstattungsbetrag in EUR, jeweils exakte Bruchobjekte.

Nur wirksame Beendigung dauerhafter digitaler Bereitstellung nach §327o Absatz2/3. Ein homogen bepreister Abschnitt mit proportional über dessen Zeit verteilter Zahlung. Mangelhafte Zeit nur bereits erbrachte Leistungen, zukünftige Zeit nur nicht mehr geschuldete Leistungen; disjunkt, vollständig qualifiziert. Ungleich bepreiste oder anders bezahlte Zeitbereiche getrennt rechnen; überlappende Mangelintervalle zuvor vereinigen. Keine automatische Mangelbeurteilung, Vertragsbeendigung, Zahlungszuordnung, Berechnung von Wertersatz oder Frist. Ergebnis erloschener_preisanteil ist gesamter entfallener Preis einschließlich bereits bezahlten Teils, keine zusätzliche offene Forderung. Überzahlungen über Abschnittspreis gesondert behandeln.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_327o_T0004, BGB_327o_T0005, BGB_327o_T0006

```python
from bgbcalc import digitalbeendigung_zeitanteilige_betraege
digitalbeendigung_zeitanteilige_betraege(
    vereinbarter_abschnittspreis='120',
    gezahlter_abschnittspreis='60',
    zeiteinheiten_gesamt='12',
    zeiteinheiten_mangelhaft='2',
    zeiteinheiten_nicht_mehr_zu_erbringen='4',
    einordnungsnachweis='Homogener Abschnitt; proportionale Teilzahlung; disjunkte qualifizierte Zeiten.',
)
```
