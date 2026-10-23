<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gastschulaufenthalt_kuendigungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarter_reisepreis`: Nichtnegativer exakter vereinbarter EUR-Preis.
- `ersparte_aufwendungen`: Nichtnegative ersparte EUR-Aufwendungen, höchstens der vereinbarte Preis.
- `notwendige_mehrkosten`: Nichtnegative rechtlich zugeordnete notwendige Mehrkosten der Kündigungsmaßnahmen in EUR.
- `einordnungsnachweis`: Nichtleerer Nachweis des §651uIV-Falls; Kündigung nach §651l ausdrücklich ausgeschlossen.

Vereinbarten Reisepreis um ersparte Aufwendungen mindern und notwendige Mehrkosten hinzufügen.

wert ist der exakte EUR-Bruch.

Nur §651uIV außerhalb einer Kündigung nach §651l. Ersparnis und notwendige Mehrkosten rechtlich bewerten, ohne doppelte Kostenpositionen. Ergebnis ist der Anspruch vor bereits geleisteten Zahlungen, kein automatischer Zahlungssaldo. Bei Ersparnis über dem Preis ist dieser abgegrenzte Fall nicht modelliert; keine erfundene negative Preisforderung.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651u_T0009, BGB_651u_T0010, BGB_651u_T0011, BGB_651u_T0012, BGB_651u_T0013

```python
from bgbcalc import gastschulaufenthalt_kuendigungsbetrag
gastschulaufenthalt_kuendigungsbetrag(
    vereinbarter_reisepreis='1000',
    ersparte_aufwendungen='400',
    notwendige_mehrkosten='150',
    einordnungsnachweis='Nur §651uIV außerhalb einer Kündigung nach §651l. Ersparnis und notwendige Mehrkosten rechtlich bewerten, ohne doppelte Kostenpositionen. Ergebnis ist der Anspruch vor bereits geleisteten Zahlungen, kein automatischer Zahlungssaldo. Bei Ersparnis über dem Preis ist dieser abgegrenzte Fall nicht modelliert; keine erfundene negative Preisforderung.',
)
```

## pauschalreise_ereignisentschaedigung_anrechnen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anspruch_vor_anrechnung`: Nichtnegativer exakter EUR-Anspruch vor Anrechnung.
- `bereits_erhaltene_ereignisentschaedigung`: Nichtnegative tatsächlich erhaltene und rechtlich anrechenbare Entschädigung für dasselbe Ereignis; noch nicht anderswo angerechnet.
- `einordnungsnachweis`: Nichtleerer Nachweis einer konkreten Anrechnungsrichtung nach §651pIII; identisches Ereignis und rechtlich anrechenbare Leistung bestimmt.

Bereits erhaltene anrechenbare Ereignisentschädigung vom Anspruch abziehen, mindestens null.

wert ist der exakte EUR-Bruch.

§651pIII in einer ausdrücklich vorqualifizierten Anrechnungsrichtung. Externe Verordnungen/Übereinkünfte liefern den bewerteten Anspruch und die anrechenbare bereits erhaltene Zahlung; deren Berechnung wird hier nicht erfunden. Mehrere Anspruchspositionen vorab überschneidungsfrei zuordnen; dieselbe Entschädigung nicht mehrfach abziehen. Überschießende Entschädigung begründet hier keinen Rückzahlungsanspruch.

Nichtnegative Eingangswerte, exakter nichtnegativer EUR-Bruch im sicheren gemeinsamen Zahlenbereich.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651p_T0005, BGB_651p_T0006, BGB_651p_T0007, BGB_651p_T0008, BGB_651p_T0009, BGB_651p_T0010, BGB_651p_T0011

```python
from bgbcalc import pauschalreise_ereignisentschaedigung_anrechnen
pauschalreise_ereignisentschaedigung_anrechnen(
    anspruch_vor_anrechnung='100',
    bereits_erhaltene_ereignisentschaedigung='40',
    einordnungsnachweis='§651pIII in einer ausdrücklich vorqualifizierten Anrechnungsrichtung. Externe Verordnungen/Übereinkünfte liefern den bewerteten Anspruch und die anrechenbare bereits erhaltene Zahlung; deren Berechnung wird hier nicht erfunden. Mehrere Anspruchspositionen vorab überschneidungsfrei zuordnen; dieselbe Entschädigung nicht mehrfach abziehen. Überschießende Entschädigung begründet hier keinen Rückzahlungsanspruch.',
)
```
