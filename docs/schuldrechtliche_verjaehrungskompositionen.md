<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## delikt_restbereicherung_verjaehrungsgrundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anspruch_entstanden_am`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `verletzungsereignis_am`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anspruchsfalls und beider maßgeblicher Ereignisse; Hemmung/Korrekturen separat.

Früheres Ende aus Entstehung des Restbereicherungsanspruchs plus zehn Jahre und Verletzungshandlung/sonstigem auslösendem Ereignis plus dreißig Jahre

wert enthält beide Teilfristenden und verknüpftes Ende; bei Grundfristfunktionen verknuepftes_grundfristende, beim Nachlauf verknuepftes_fristende; alle letzten eingeschlossenen Tage bisTagesablauf.

Nur§852 Restbereicherung nach deliktischem Erlangen auf Kosten des Verletzten, keine allgemeine Schadensersatzverjährung oder Anspruchshöhe. Maßgebliches auslösendes Ereignis rechtlich qualifizieren; Entstehung nicht vor Ereignis. Kenntnis ist hier kein Beginnparameter. Herausgabeumfang nachBereicherungsrecht gesondert. Nur Grundfristen vor Hemmung/Ablaufhemmung/Neubeginn/Feiertagskorrekturen.

ISO-Daten und Ergebnisse0001..9999;852EntstehungnichtvorVerletzungsereignis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_852_T0001, BGB_852_T0002

```python
from bgbcalc import delikt_restbereicherung_verjaehrungsgrundfrist
delikt_restbereicherung_verjaehrungsgrundfrist(
    anspruch_entstanden_am='2028-02-29',
    verletzungsereignis_am='2000-02-29',
    einordnungsnachweis='Qualifizierter852RestbereicherungsanspruchundEreignisse.',
)
```

## lieferantenregress_verjaehrungsgrundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ablieferung_am`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `kaeuferanspruch_erfuellt_am`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anspruchsfalls und beider maßgeblicher Ereignisse; Hemmung/Korrekturen separat.

Späteres Ende aus Ablieferung plus zwei Jahre und Erfüllung des Käuferanspruchs plus zwei Monate

wert enthält beide Teilfristenden und verknüpftes Ende; bei Grundfristfunktionen verknuepftes_grundfristende, beim Nachlauf verknuepftes_fristende; alle letzten eingeschlossenen Tage bisTagesablauf.

Nur§445b Absatz1/2 für qualifizierten Lieferantenregress beim Mangel einer neu hergestellten Sache. Keine historische Fünfjahreskappung. Käuferanspruchserfüllung muss rechtlich bestimmt sein; mehrere Ansprüche/Teilbefriedigungen separat qualifizieren. Nicht digitale Vertriebskette327u. Verjährung anderer437-Ansprüche kann andereGrundfrist haben: hier ausdrücklich zweijährige445a-Aufwendungsersatzgrundfrist. Nur Grundfristen vor Hemmung/Ablaufhemmung/Neubeginn/Feiertagskorrekturen.

ISO-Daten und Ergebnisse0001..9999;852EntstehungnichtvorVerletzungsereignis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_445b_T0001, BGB_445b_T0002

```python
from bgbcalc import lieferantenregress_verjaehrungsgrundfrist
lieferantenregress_verjaehrungsgrundfrist(
    ablieferung_am='2028-02-29',
    kaeuferanspruch_erfuellt_am='2030-01-31',
    einordnungsnachweis='Qualifizierter445aAufwendungsersatzregress.',
)
```

## lieferantenregress_verjaehrungsnachlauf

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriges_fristende`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `kaeuferanspruch_erfuellt_am`: Rechtlich maßgebliches ISO-Datum0001..9999 des benannten Ereignisses; kein bloßes Kenntnis-/Anzeigedatum.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Anspruchsfalls und beider maßgeblicher Ereignisse; Hemmung/Korrekturen separat.

Maximum aus separat bestimmter konkreter Anspruchsfrist und Käuferanspruchserfüllung+2Monate.

wert enthält beide Teilfristenden und verknüpftes Ende; bei Grundfristfunktionen verknuepftes_grundfristende, beim Nachlauf verknuepftes_fristende; alle letzten eingeschlossenen Tage bisTagesablauf.

437-/445a-Anspruchsfrist bereits separat bestimmt; keine pauschaleZweijahresfrist, keine historischeFünfjahreskappung. EigeneKorrekturen/Ereignisqualifikationgesondert. Nur Grundfristen vor Hemmung/Ablaufhemmung/Neubeginn/Feiertagskorrekturen.

ISO-Daten und Ergebnisse0001..9999;852EntstehungnichtvorVerletzungsereignis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_445b_T0002, BGB_445b_T0003

```python
from bgbcalc import lieferantenregress_verjaehrungsnachlauf
lieferantenregress_verjaehrungsnachlauf(
    bisheriges_fristende='2033-02-28',
    kaeuferanspruch_erfuellt_am='2033-01-31',
    einordnungsnachweis='Qualifizierter437-AnspruchundseparatbestimmteGrundfrist.',
)
```
