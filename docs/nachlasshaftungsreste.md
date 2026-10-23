<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## nacherbe_haftungsmasse

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erlangter_erbschaftswert_ohne_vorerbenansprueche`: Nichtnegativer EUR-Wert des Erlangten ohne separat genannte Vorerbenansprüche.
- `anspruchswert_gegen_vorerben`: Nichtnegativer rechtlich/wirtschaftlich bewerteter EUR-Wert der Ansprüche gegen Vorerben als solchen. Nicht doppelt bereits erfüllte Ansprüche erfassen.
- `bewertungsnachweis`: Nichtleerer Nachweis der überschneidungsfreien2144I-Massenbestandteile.

Erlangten Erbschaftswert und überschneidungsfreie Vorerbenansprüche summieren.

wert ist zusammengerechneter EUR-Massenwert als exakter Bruch.

Numerische Masse, keine automatische Haftungsbeschränkung/Rangentscheidung oder Insolvenzbewertung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2144_T0001

```python
from bgbcalc import nacherbe_haftungsmasse
nacherbe_haftungsmasse(
    erlangter_erbschaftswert_ohne_vorerbenansprueche='80',
    anspruchswert_gegen_vorerben='20',
    bewertungsnachweis='Synthetische getrennte Massenbestandteile.',
)
```

## nachlassglaeubiger_restdeckung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `haftungsmasse_vor_bindungen`: Nichtnegativer rechtlich bewerteter EUR-Haftungswert vor angegebenen Bindungen;1973II bereicherungsrechtlich korrigiert,1991 Verantwortlichkeitskorrekturen berücksichtigt.
- `vorrangig_gebundener_betrag`: Nichtnegative Summe rechtlich vorrangiger Bindungen, einschließlich ggf.bereits befriedigter oder gleichstehend rechtskräftig zuerkannter Beträge. Nicht doppelt von bereits bereinigter Masse abziehen. Keine willkürliche Gleichrangpräferenz.
- `forderungsbetrag`: Nichtnegative rechtlich festgestellte einzelne Forderung.
- `haftungsfall`: ausgeschlossener_glaeubiger_1973, spaetglaeubiger_1974, duerftigkeit_1990 oder vermaechtnisueberschuldung_1992.
- `rang_und_einrede_qualifiziert`: Pflichtwahrheitswert: einschlägige Einrede und Rang/Bindung rechtlich vorqualifiziert.1973I2-Grundvorrang samt Vorleistungs-Ausnahme,1974II/1991IV-Insolvenzrang ausdrücklich berücksichtigen. FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der Masse, Bindungen, individuellen Forderung und Rangqualifikation.

FreieMasse=max(Masse−vorrangigeBindungen,0);Deckung=min(Forderung,freieMasse);Restforderung=Forderung−Deckung.

wert enthält freie_haftungsmasse, gedeckter_forderungsteil und nicht_gedeckter_forderungsteil als exakte EUR-Brüche.

Keine automatische InsO-Rangordnung oder Gleichrangquote. Forderung erlischt nicht, keine automatische Sachherausgabe-Geldpflicht.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1973_T0001, BGB_1973_T0002, BGB_1973_T0003, BGB_1973_T0005, BGB_1974_T0003, BGB_1990_T0001, BGB_1991_T0003, BGB_1991_T0004, BGB_1992_T0001

```python
from bgbcalc import nachlassglaeubiger_restdeckung
nachlassglaeubiger_restdeckung(
    haftungsmasse_vor_bindungen='100',
    vorrangig_gebundener_betrag='70',
    forderungsbetrag='50',
    haftungsfall='ausgeschlossener_glaeubiger_1973',
    rang_und_einrede_qualifiziert=True,
    bewertungsnachweis='Synthetisch qualifizierte Masse und Ränge.',
)
```

## vorerbe_verbleibende_haftung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlassschuld`: Nichtnegative rechtlich bestimmte EUR-Nachlassschuld.
- `rechtlich_vom_nacherben_getragener_schuldteil`: Nichtnegativer rechtlicher Haftungsteil des Nacherben, höchstens Schuld. Nicht Zahlungsfähigkeit/erlangbare Zahlung verwenden.
- `schuld_im_innenverhaeltnis_vorerbe`: Pflichtwahrheitswert: gesamte hier betrachtete Schuld fällt im Innenverhältnis dem Vorerben zur Last; gemischte Schuld vorher aufteilen.
- `vorerbe_unbeschraenkt_haftend`: Pflichtwahrheitswert: bei TRUE keine Kappung auf Vorerbenmasse.
- `fuer_forderung_verfuegbare_vorerbenmasse`: Nichtnegativer dem Vorerben aus Erbschaft gebührender und nach qualifizierten Rang-/Bindungsregeln für diese Forderung verfügbarer EUR-Wert. Nicht pauschal eigenes Vermögen.
- `nacherbfall_qualifiziert`: Pflichtwahrheitswert des eingetretenen Nacherbfalls und2145-Anwendungsfalls; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis rechtlicher Nacherbenhaftung, Innenlast und verfügbarer Masse.

Ohne eigene Innenlast Schuld minus rechtlicher Nacherbenhaftung; sonst volle Schuld. Unbeschränkte Haftung voll, beschränkte Haftung höchstens verfügbare Masse.

wert enthält verbleibende_haftung_vor_massenbegrenzung, befriedigungsbetrag_nach_massenbegrenzung und wegen_massenbegrenzung_nicht_gedeckter_teil als exakte EUR-Brüche.

Rechtliche Nacherbenhaftung nicht mit bloßer Nichtzahlung/Insolvenz des Nacherben verwechseln. Keine Doppeladdition eigener Innenlast; Rang-/Massenabgrenzung vorqualifiziert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2145_T0001, BGB_2145_T0002, BGB_2145_T0003, BGB_2145_T0004

```python
from bgbcalc import vorerbe_verbleibende_haftung
vorerbe_verbleibende_haftung(
    nachlassschuld='100',
    rechtlich_vom_nacherben_getragener_schuldteil='60',
    schuld_im_innenverhaeltnis_vorerbe=False,
    vorerbe_unbeschraenkt_haftend=False,
    fuer_forderung_verfuegbare_vorerbenmasse='30',
    nacherbfall_qualifiziert=True,
    bewertungsnachweis='Synthetische rechtliche Resthaftung.',
)
```
