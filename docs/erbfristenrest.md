<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbrecht_weitere_grundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristart`: erbrechtsnachweis_1965 (3Monate), nachlassverwaltung_1981 (2Jahre), erbteilvorkauf_2034 (2Monate), glaeubigeranmeldung_2061 (6Monate). Nur der rechtlich einschlägige gesetzliche Fristentyp.
- `fristbeginnereignis_am`: ISO-Datum des qualifizierten Anfangsereignisses:1965 Ablauf öffentliche Anmeldungsfrist oder ohne öffentliche Aufforderung gerichtliche Nachweisaufforderung;1981 Annahme;2034 Empfang ausreichender Vertragsmitteilung469;2061 letzte erforderliche Veröffentlichung. Keine pauschale Ersatzwahl Erbfall/Kaufvertrag.
- `einordnungsnachweis`: Nichtleerer Nachweis zu Fristart, gesetzlichem Anwendungsfall und maßgeblichem Anfangsereignis.

Gesetzliche3-/2-/6Monats- oder2Jahresfrist auswählen und als Ereignisfrist berechnen.

wert enthält grundfristende, anzahl und einheit der gesetzlichen Frist.

Nur Grundfrist, kein Wirksamkeits-/Zulässigkeitsentscheid und keine automatische Hemmung/Feiertagskorrektur.2061-Haftungsquote getrennt.

ISO-Daten und berechnete Grenzen0001..9999, feste Auswahlwerte, nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1965_T0003, BGB_1965_T0004, BGB_1981_T0003, BGB_2034_T0002, BGB_469_T0003, BGB_469_T0004, BGB_2061_T0001, BGB_2061_T0004

```python
from bgbcalc import erbrecht_weitere_grundfrist
erbrecht_weitere_grundfrist(
    fristart='erbrechtsnachweis_1965',
    fristbeginnereignis_am='2030-01-31',
    einordnungsnachweis='Synthetisch qualifizierter gesetzlicher Fristbeginn.',
)
```

## inventarfrist_erbentod_mindestende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriges_fristende`: ISO-Enddatum der Inventarfrist oder Zweiwochenantragsfrist1996II, rechtlich inklusive bereits einschlägiger Korrekturen. Nicht die absolute Jahresgrenze.
- `erbe_gestorben_am`: ISO-Todestag des Erben. Ereignis am bisherigen Endtag liegt vor Tagesablauf; Tod danach erzeugt keine Wiederbelebung.
- `ausschlagungsfristende_erbeserbe`: ISO-Enddatum der für die Erbschaft des verstorbenen Erben maßgeblichen Ausschlagungsfrist des betrachteten Erbeserben, frühestens Tod. Bei mehreren Personen gesondert qualifizieren.
- `einordnungsnachweis`: Nichtleerer Nachweis der Fristart, bisherigen Korrekturen, Erbentods und maßgeblichen Ausschlagungsfrist.

Bei Tod bis zum letzten Tag der laufenden Frist: Maximum aus bestehendem und einschlägigem Ausschlagungsende, sonst unverändertes bestehendes Ende.

wert enthält massgebliches_fristende.

Nicht absolute1996II-Jahresgrenze verlängern; keine Addition, keine Wiederbelebung abgelaufener Frist oder ungeprüfte gemeinsame Frist mehrerer Erbeserben.

ISO-Daten und berechnete Grenzen0001..9999, feste Auswahlwerte, nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1998_T0001

```python
from bgbcalc import inventarfrist_erbentod_mindestende
inventarfrist_erbentod_mindestende(
    bisheriges_fristende='2030-06-30',
    erbe_gestorben_am='2030-06-01',
    ausschlagungsfristende_erbeserbe='2030-07-13',
    einordnungsnachweis='Synthetische einschlägige Inventar-/Ausschlagungsfrist.',
)
```

## totgeglaubter_verjaehrung_mindestende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriges_verjaehrungsende`: ISO-Enddatum des Anspruchs ohne die zusätzliche2031-Mindestgrenze, rechtlich bestimmt.
- `kenntnis_todesannahme_am`: ISO-Datum der relevanten Kenntnis der tatsächlich lebenden betroffenen Person von ihrer falschen Todeserklärung/Todeszeitfeststellung oder sonst unrichtigen Todesannahme.
- `einordnungsnachweis`: Nichtleerer Nachweis des2031-Anwendungsfalls, relevanten Kenntnisses und Fortlebens der Person über den betrachteten Zeitraum. Fälle mit Tod währenddessen gesondert.

Einjährige Ereignisfrist ab relevanter Kenntnis; späteres Ende aus bisheriger Verjährung und einjährigem Mindestende.

wert enthält einjaehriges_mindestende und massgebliches_verjaehrungsende.

Nur fortlebende betroffene Person; Tod während des Zeitraums außerhalb Modell. Keine pauschale neue Verjährung oder Jahresendregel; weitere Korrekturen/Einrede getrennt.

ISO-Daten und berechnete Grenzen0001..9999, feste Auswahlwerte, nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2031_T0002, BGB_2031_T0003

```python
from bgbcalc import totgeglaubter_verjaehrung_mindestende
totgeglaubter_verjaehrung_mindestende(
    bisheriges_verjaehrungsende='2030-12-31',
    kenntnis_todesannahme_am='2030-06-15',
    einordnungsnachweis='Synthetischer2031-Fall, betroffene Person lebt fort.',
)
```
