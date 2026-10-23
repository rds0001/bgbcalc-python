<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## darlehensvermittlung_auslagenobergrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `entstandene_erforderliche_auslagen`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `vorab_mitgeteilter_hoechstbetrag`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `einordnungsnachweis`: Nichtleerer Nachweis des jeweiligen Darlehens-/Vermittlungs-/Teilzahlungsfalls und rechtlich qualifizierter Wert-, Kosten- oder Zinsgrundlage.

Qualifiziert vereinbarte entstandene erforderliche Vermittlerauslagen auf vorab mitgeteilten Höchstbetrag begrenzen

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur §655d Satz2/3: wirksame Vereinbarung über tatsächlich entstandene erforderliche Auslagen vorausgesetzt; nicht Maklervergütung oder Beratungsentgelt. Mitgeteilte Höhe/Höchstgrenze rechtlich bestimmen; bei getrennten Einzelkategorien jede passende Grenze separat anwenden, kein Austausch ungenutzter Grenzen ohne Rechtsgrundlage. Keine automatische Erforderlichkeits- oder Anspruchsprüfung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_655d_T0002, BGB_655d_T0003

```python
from bgbcalc import darlehensvermittlung_auslagenobergrenze
darlehensvermittlung_auslagenobergrenze(
    entstandene_erforderliche_auslagen='120',
    vorab_mitgeteilter_hoechstbetrag='100',
    einordnungsnachweis='Wirksame Auslagenvereinbarung und vorab mitgeteilte Kostengrenze.',
)
```

## darlehen_wertbeteiligungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `immobilienwert_bei_rueckzahlung`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `vertraglicher_wertanteil`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `einordnungsnachweis`: Nichtleerer Nachweis des jeweiligen Darlehens-/Vermittlungs-/Teilzahlungsfalls und rechtlich qualifizierter Wert-, Kosten- oder Zinsgrundlage.

Qualifizierten Immobilienwert bei Rückzahlung mit vertraglich festgelegter Wertbeteiligungsquote multiplizieren

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur Wertbeteiligungsdarlehen im Sinne §492b Absatz1 Nummer3. Immobilienwert für den maßgeblichen Rückzahlungszeitpunkt und vertraglichen Umfang extern bewerten; Quote als Jahres-unabhängiger Anteil (0.2=20Prozent), kein Zinssatz. Keine Bestimmung der Zulässigkeit des Kopplungsgeschäfts oder automatisches Hinzufügen einer ursprünglichen Darlehenssumme. Mehrere Rückzahlungen nach jeweils rechtlich bestimmtem Anteil/Umfang separat, keine Doppelzählung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_492b_T0009

```python
from bgbcalc import darlehen_wertbeteiligungsbetrag
darlehen_wertbeteiligungsbetrag(
    immobilienwert_bei_rueckzahlung='500000',
    vertraglicher_wertanteil='0.2',
    einordnungsnachweis='Qualifiziertes Wertbeteiligungsdarlehen und Immobilienwert bei Rückzahlung.',
)
```

## teilzahlung_gesamtbetragskorrektur

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vertraglicher_gesamtbetrag`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `angegebener_effektiver_jahreszins`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `tatsaechlicher_effektiver_jahreszins`: Nichtnegativer exakter qualifizierter Dezimalwert/Bruch; Beträge in EUR, vertragliche Wertbeteiligung/Zinsen als Quote (0.05=5Prozent).
- `einordnungsnachweis`: Nichtleerer Nachweis des jeweiligen Darlehens-/Vermittlungs-/Teilzahlungsfalls und rechtlich qualifizierter Wert-, Kosten- oder Zinsgrundlage.

Gesamtbetrag mit eins minus der absoluten Effektivzins-Unterangabe als Zinsquote multiplizieren

wert ist der exakt berechnete EUR-Betrag als Bruchobjekt.

Nur §507 Absatz2 letzter Satz bei qualifiziertem Teilzahlungsgeschäft und zu niedrig angegebenem Effektivzins. Eingaben als Jahresquoten,0.05=5Prozent. Beispielsweise Unterangabe8%-6%=2Prozentpunkte vermindert Gesamtbetrag um2Prozent. Nicht §494III-Sollzinskorrektur; nicht fehlende Zins-/Gesamtbetragsangabe. Sichere Rechendomäne: Unterangabe zwischen0und1 einschließlich; größere Differenzen erfordern gesonderte rechtliche Behandlung und werden nicht automatisch zu negativem Zahlungsanspruch. Tatsächlicher Effektivzins/Vertragsgesamtbetrag extern bestimmen; keine automatische Ratenneuberechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_507_T0007

```python
from bgbcalc import teilzahlung_gesamtbetragskorrektur
teilzahlung_gesamtbetragskorrektur(
    vertraglicher_gesamtbetrag='10000',
    angegebener_effektiver_jahreszins='0.06',
    tatsaechlicher_effektiver_jahreszins='0.08',
    einordnungsnachweis='Qualifiziertes Teilzahlungsgeschäft mit zwei Prozentpunkten Effektivzins-Unterangabe.',
)
```
