<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fremdwaehrung_eurobetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fremdwaehrungsbetrag`: Nichtnegativer Betrag einer bestimmten Fremdwährung; Währung und Zahlungsumstände im Bewertungsnachweis nennen.
- `eurokurs`: Strikt positiver maßgeblicher Eurobetrag für genau eine Einheit dieser Fremdwährung. Exakte Dezimalzeichenfolge oder Bruchobjekt, kein inverser Kurs.
- `eurozahlung_nach_244_zulaessig`: Explizite rechtliche Bestätigung des in der Abgrenzung beschriebenen Anwendungsfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Beschreibung von Herkunft, Zeitpunkt und rechtlicher Zuordnung aller Werte.

Fremdwährungsbetrag mit Euro je Einheit Fremdwährung multiplizieren.

wert ist der exakte Ergebnisbetrag in EUR, keine automatische Cent-Rundung.

Kurswert am Zahlungsort zur tatsächlichen Zahlungszeit als belegte Eingabe. Keine Onlinekurse, keine Umkehrung einer Fremdwährung-je-Euro-Notierung. Nur bei zulässiger Eurozahlung im Inland; ausdrücklich vereinbarte ausschließliche Fremdwährungszahlung ausgeschlossen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_244_T0001, BGB_244_T0002

```python
from bgbcalc import fremdwaehrung_eurobetrag
fremdwaehrung_eurobetrag(
    fremdwaehrungsbetrag='100',
    eurokurs='0.9',
    eurozahlung_nach_244_zulaessig=True,
    bewertungsnachweis='Synthetische qualifizierte Vergleichswerte; Fremdwährung USD, EUR/USD-Kurs am Ort und Zeitpunkt der Zahlung.',
)
```

## gelduebermittlung_umzugsmehrkosten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kosten_vor_verlegung`: Nichtnegativer exakt eingegebener Betrag; gemäß rechtlich qualifizierter Vergleichsbasis.
- `kosten_nach_verlegung`: Nichtnegativer exakt eingegebener Betrag; gleiche Vergleichs- und Bewertungsbasis.
- `kostenvergleich_nach_270_absatz_3_anwendbar`: Explizite rechtliche Bestätigung des in der Abgrenzung beschriebenen Anwendungsfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Beschreibung von Herkunft, Zeitpunkt und rechtlicher Zuordnung aller Werte.

Kosten nach Verlegung minus vergleichbare Kosten ohne Verlegung, mindestens null.

wert ist der exakte Ergebnisbetrag in EUR, keine automatische Cent-Rundung.

Nur kausale Mehrkosten der nach Entstehung des Schuldverhältnisses erfolgten Verlegung von Gläubigerwohnsitz oder maßgeblicher Niederlassung. Beträge unter ansonsten gleichen Bedingungen bestimmen; keine Übernahme der gesamten Übermittlungskosten oder Berechnung der Gefahrtragung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_270_T0003

```python
from bgbcalc import gelduebermittlung_umzugsmehrkosten
gelduebermittlung_umzugsmehrkosten(
    kosten_vor_verlegung='10',
    kosten_nach_verlegung='15',
    kostenvergleich_nach_270_absatz_3_anwendbar=True,
    bewertungsnachweis='Synthetische qualifizierte Vergleichswerte; Fremdwährung USD, EUR/USD-Kurs am Ort und Zeitpunkt der Zahlung.',
)
```

## leistungsbestimmung_durchschnittssumme

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bestimmte_summen`: Liste von2 bis1000 Objekten mit eindeutigem dritter_id und nichtnegativer summe in EUR. Sämtliche rechtlich maßgeblichen Bestimmungen vollständig angeben.
- `zweifelsregel_nach_317_anwendbar`: Fachlich geprüfte Anwendung der gesetzlichen Durchschnittsregel; FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der vollständigen Bestimmungen, ihrer Gültigkeit und einheitlichen Währung.

Summen sämtlicher bestimmender Dritter gleichgewichtet addieren und durch deren Anzahl teilen.

wert ist gleichgewichteter Durchschnitt als exakter EUR-Bruch, ohne Cent-Rundung.

Nur die Zweifelsregel für eine durch mehrere Dritte bestimmte Geldsumme in einheitlicher Währung EUR. Abweichende Vereinbarungen, rechtlich unwirksame Bestimmungen oder nichtmonetäre Leistungen nicht erfasst. Jede Person genau einmal einbeziehen; keine Mehrheitsabstimmung und keine Entfernung von Ausreißern.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_317_T0002

```python
from bgbcalc import leistungsbestimmung_durchschnittssumme
leistungsbestimmung_durchschnittssumme(
    bestimmte_summen=[{'dritter_id': '0', 'summe': '100'}, {'dritter_id': '1', 'summe': '200'}],
    zweifelsregel_nach_317_anwendbar=True,
    bewertungsnachweis='Synthetische vollständige Bestimmungen in EUR, gesetzliche Zweifelsregel.',
)
```

## schadensersatz_nach_ersatzherausgabe

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schadensersatz_vor_anrechnung`: Nichtnegativer exakt eingegebener Betrag; gemäß rechtlich qualifizierter Vergleichsbasis.
- `wert_des_erlangten_ersatzes`: Nichtnegativer exakt eingegebener Betrag; gleiche Vergleichs- und Bewertungsbasis.
- `ersatzrecht_nach_285_ausgeuebt`: Explizite rechtliche Bestätigung des in der Abgrenzung beschriebenen Anwendungsfalls. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Beschreibung von Herkunft, Zeitpunkt und rechtlicher Zuordnung aller Werte.

Schadensersatz statt der Leistung um den Wert des herausverlangten Ersatzes mindern, mindestens null.

wert ist der exakte Ergebnisbetrag in EUR, keine automatische Cent-Rundung.

Wirksamer Schadensersatzanspruch statt der Leistung und Ausübung des Rechts nach§285 Absatz1 fachlich vorgegeben. Ausgangsbetrag noch ohne diese Anrechnung. Keine Rückzahlungsforderung bei höherem Ersatzwert; Herausgabeanspruch und sonstige Anspruchsänderungen separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_285_T0001, BGB_285_T0002

```python
from bgbcalc import schadensersatz_nach_ersatzherausgabe
schadensersatz_nach_ersatzherausgabe(
    schadensersatz_vor_anrechnung='100',
    wert_des_erlangten_ersatzes='30',
    ersatzrecht_nach_285_ausgeuebt=True,
    bewertungsnachweis='Synthetische qualifizierte Vergleichswerte; Fremdwährung USD, EUR/USD-Kurs am Ort und Zeitpunkt der Zahlung.',
)
```
