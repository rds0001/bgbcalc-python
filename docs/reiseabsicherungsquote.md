<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pauschalreise_absicherungsanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigener_leistungsanspruch`: Nichtnegativer exakter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt. Eigener Anspruch höchstens Gesamtansprüche desselben vollständigen Insolvenzleistungskreises, Vorjahresumsatz strikt unter drei Millionen EUR.
- `gesamtleistungsansprueche`: Nichtnegativer exakter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt. Eigener Anspruch höchstens Gesamtansprüche desselben vollständigen Insolvenzleistungskreises, Vorjahresumsatz strikt unter drei Millionen EUR.
- `jahresumsatz_veranstalter`: Nichtnegativer exakter EUR-Betrag als Dezimalzeichenfolge oder Bruchobjekt. Eigener Anspruch höchstens Gesamtansprüche desselben vollständigen Insolvenzleistungskreises, Vorjahresumsatz strikt unter drei Millionen EUR.
- `einordnungsnachweis`: Nichtleerer Nachweis qualifizierter Versicherung/Bankabsicherung nach §651r Absatz2 Satz2, wirksamer Ein-Million-EUR-Begrenzung je Insolvenz, gesetzlicher Vorjahresumsatzbasis und vollständig gleichbezogener Leistungsansprüche. Kein Reisesicherungsfonds.

Im qualifiziert vereinbarten Ein-Million-Euro-Deckelfall Einzelanspruch mit min(1, eine Million Euro geteilt durch Gesamtleistungsansprüche) multiplizieren

wert ist der quotierte eigene Leistungsanspruch in EUR als exaktes Bruchobjekt.

Nur §651r Absatz3 Satz3/4: qualifiziert wirksam vereinbarte Begrenzung auf genau eine Million EUR je Insolvenz bei Versicherer oder Kreditinstitut nach Absatz2 Satz2 und Vorjahresumsatz strikt unter drei Millionen EUR. Kein Deckel für Reisesicherungsfonds; größere freiwillige Deckungsgrenzen separat qualifizieren. Eigener und Gesamtanspruch betreffen denselben vollständigen Insolvenz-Leistungskreis nach Absatz1, nicht nur die gerade bekannten Anmeldungen; keine Doppelzählung. Gesamtanspruch mindestens Einzelanspruch. Null Gesamtansprüche ergeben null. Keine Bestimmung des versicherten Schadens oder Prüfung der Insolvenz.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651r_T0013, BGB_651r_T0014

```python
from bgbcalc import pauschalreise_absicherungsanteil
pauschalreise_absicherungsanteil(
    eigener_leistungsanspruch='1000',
    gesamtleistungsansprueche='2000000',
    jahresumsatz_veranstalter='2000000',
    einordnungsnachweis='Wirksamer Ein-Million-Deckel bei Versicherer; vollständige Ansprüche derselben Insolvenz.',
)
```
