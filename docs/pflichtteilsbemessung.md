<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsnachlass_positionssumme

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlasspositionen`: Liste0..1000 eindeutiger Positionen mit genau position_id (nichtleer), betrag (nichtnegativer exakter EUR-Wert), vermoegensseite (aktiv/passiv), ansatzart (unbedingt/aufloesend_offen/aufschiebend_offen/ungewiss_oder_unsicher). Vollständig, überschneidungsfrei und rechtlich qualifiziert. Nur erste zwei Ansatzarten zählen.
- `ehegattenvoraus_wert`: Nichtnegativer exakter Vorauswert, bereits in Aktiva enthalten und dort noch nicht abgezogen.
- `berechtigter_abkoemmling_oder_elternteil`: Pflichtwahrheitswert: nur bei TRUE Voraus nach2311I2 abziehen.
- `bewertungsnachweis`: Nichtleerer Nachweis rechtlicher Qualifizierung, Ansatzarten und gleicher maßgeblicher Bewertungsgrundlage. Geeigneter Ertragswert2312 darf qualifizierter Bewertungsinput sein.

Berücksichtigte Aktiv-/Passivpositionen getrennt addieren; Passiva und ggf.Voraus abziehen; negative Nettobasis erhalten.

wert enthält beruecksichtigte_aktiva, beruecksichtigte_passiva, abgezogener_ehegattenvoraus und vorzeichenbehafteten pflichtteilsnachlass als exakte EUR-Brüche.

Keine automatische Bewertung oder rechtliche Bedingungsprüfung; nach Bedingungseintritt Positionen neu qualifizieren. Keine Pflichtteilsquote, Kapitalisierung oder Zahlungsanspruch.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2311_T0001, BGB_2311_T0002, BGB_2313_T0001, BGB_2313_T0002, BGB_2313_T0004

```python
from bgbcalc import pflichtteilsnachlass_positionssumme
pflichtteilsnachlass_positionssumme(
    nachlasspositionen=[{'position_id': 'A', 'betrag': '100', 'vermoegensseite': 'aktiv', 'ansatzart': 'unbedingt'}, {'position_id': 'B', 'betrag': '20', 'vermoegensseite': 'aktiv', 'ansatzart': 'aufloesend_offen'}, {'position_id': 'C', 'betrag': '30', 'vermoegensseite': 'passiv', 'ansatzart': 'unbedingt'}, {'position_id': 'D', 'betrag': '1000', 'vermoegensseite': 'aktiv', 'ansatzart': 'aufschiebend_offen'}, {'position_id': 'E', 'betrag': '1000', 'vermoegensseite': 'passiv', 'ansatzart': 'ungewiss_oder_unsicher'}],
    ehegattenvoraus_wert='10',
    berechtigter_abkoemmling_oder_elternteil=True,
    bewertungsnachweis='Synthetisch rechtlich qualifizierte Stichtagspositionen.',
)
```

## pflichtteil_bemessungsausgleich

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `frueherer_pflichtteilsnachlass`: Vorzeichenbehaftete exakte EUR-Nettobasis vor Neubemessung.
- `neuer_pflichtteilsnachlass`: Vorzeichenbehaftete exakte EUR-Nettobasis nach rechtlich qualifizierter Neubemessung2313, gleicher Bewertungsmaßstab.
- `gesetzliche_erbquote_zaehler`: Ganzzahlig0..Nenner, Zähler unveränderter gesetzlicher Erbquote.
- `gesetzliche_erbquote_nenner`: Positiver ganzzahliger Nenner bis2^53−1.
- `grundmodell_ohne_anrechnung_qualifiziert`: Pflichtwahrheitswert: Neubemessung2313 bei unveränderter Quote ohne2315/2316/2325 oder Vermächtnisanrechnung; FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis geänderter Positionen und unveränderter Bewertungsgrundlage.

Beide Nettobasen jeweils mindestens null mit halber gesetzlicher Erbquote multiplizieren; neuer minus früherer Pflichtteilswert.

wert enthält frueherer_pflichtteilswert, neuer_pflichtteilswert und vorzeichenbehaftete ausgleichsdifferenz als exakte EUR-Brüche.

Nur Grundmodell; keine automatischen Zahlungs-/Rückzahlungsansprüche, Vorleistungen/Einwendungen separat. Keine anderen Anrechnungsregime.

Nachlassbasen als vorzeichenbehaftete Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2313_T0003, BGB_2313_T0004, BGB_2303_T0002

```python
from bgbcalc import pflichtteil_bemessungsausgleich
pflichtteil_bemessungsausgleich(
    frueherer_pflichtteilsnachlass='100',
    neuer_pflichtteilsnachlass='140',
    gesetzliche_erbquote_zaehler=1,
    gesetzliche_erbquote_nenner=2,
    grundmodell_ohne_anrechnung_qualifiziert=True,
    bewertungsnachweis='Synthetische Neubemessung wegen Bedingungseintritt.',
)
```
