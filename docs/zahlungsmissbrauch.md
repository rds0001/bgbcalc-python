<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zahlungsmissbrauch_zahlerhaftungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schadensbetrag`: Nichtnegativer exakter EUR-Schaden derselben rechtlichen Haftungseinheit als Dezimalzeichenfolge oder Bruchobjekt.
- `betruegerische_absicht`: Expliziter Wahrheitswert für den rechtlich qualifizierten Tatbestand des §675v; keine automatische Verschuldens-/Authentifizierungsprüfung.
- `qualifizierte_pflichtverletzung`: Expliziter Wahrheitswert für den rechtlich qualifizierten Tatbestand des §675v; keine automatische Verschuldens-/Authentifizierungsprüfung.
- `ausschluss_absatz_2`: Expliziter Wahrheitswert für den rechtlich qualifizierten Tatbestand des §675v; keine automatische Verschuldens-/Authentifizierungsprüfung.
- `ausschluss_absatz_4_oder_5`: Expliziter Wahrheitswert für den rechtlich qualifizierten Tatbestand des §675v; keine automatische Verschuldens-/Authentifizierungsprüfung.
- `einordnungsnachweis`: Nichtleerer Nachweis des Anwendungsfalls und qualifizierter Betrugs-/Pflichtverletzungs-/Ausschlusstatbestände; Absatz4/5-Grundtatbestand vor Betrugsausnahme.

Betrug voller Schaden; sonst Absatz4/5 null; sonst qualifizierte Pflichtverletzung voller Schaden; sonst Absatz2 null; sonst min(Schaden,50EUR).

wert ist der Zahlerhaftungsbetrag in EUR als exaktes Bruchobjekt.

Nur §675v im qualifizierten Anwendungsbereich nicht autorisierter Zahlungsvorgänge/Zahlungsinstrumente. Betrug und qualifizierte vorsätzliche/grob fahrlässige kausale Pflichtverletzung nach Absatz3 getrennt bewerten. Absatz2 betrifft unbemerkbaren Missbrauch bzw. dienstleisterseitigen Verlust; Absatz4/5 betrifft qualifiziert fehlende starke Authentifizierung oder nach Anzeige entstandene Schäden bzw. fehlende Anzeigemöglichkeit. Ausschlussflag Absatz4/5 bezeichnet den Grundtatbestand vor Betrugsausnahme. Schaden muss derselben rechtlich einheitlichen Haftungseinheit angehören;50EUR nicht automatisch je Einzelbuchung erneut ausschöpfen. Keine automatische Betrugs-/Verschuldensbeurteilung, Kontokorrektur nach §675u oder Haftung des Zahlungsempfängers.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675v_T0001, BGB_675v_T0002, BGB_675v_T0005, BGB_675v_T0010, BGB_675v_T0013, BGB_675v_T0015, BGB_675v_T0016, BGB_675v_T0017

```python
from bgbcalc import zahlungsmissbrauch_zahlerhaftungsbetrag
zahlungsmissbrauch_zahlerhaftungsbetrag(
    schadensbetrag='1000',
    betruegerische_absicht=False,
    qualifizierte_pflichtverletzung=False,
    ausschluss_absatz_2=False,
    ausschluss_absatz_4_oder_5=False,
    einordnungsnachweis='Qualifizierter675v-Grundfall und einheitlicher Schaden.',
)
```
