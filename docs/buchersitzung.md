<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## buchersitzung_dreissigjahresfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eintragung_am`: ISO-Datum des rechtlich qualifizierten Beginns der fortbestehenden Eintragung für den betrachteten Berechtigten, spätestens Prüftag.
- `besitzbeginn_am`: ISO-Datum des qualifizierten Eigenbesitzbeginns; bei Absatz2 entsprechender besitzbezogener Zustand; spätestens Prüftag. Fremde/Vorgängerzeiten nicht ungeprüft einsetzen.
- `beginnart`: ereignis für Eintritt des gemeinsamen Vorliegens im Tagesverlauf, tagesbeginn nur wenn rechtlich bereits zu Beginn dieses Tages beide Voraussetzungen bestehen. Bezieht sich auf den späteren der beiden Beginntermine.
- `rechtsart`: eigentum oder anderes_besitzbezogenes_recht. Letzteres nur ein nach§900 Absatz2 zum Besitz berechtigendes oder besitzrechtlich geschütztes Recht; keine beliebige Grundbucheintragung.
- `korrigiertes_fristende`: Erforderliches rechtlich abschließend bestimmtes ISO-Fristende, mindestens rohe Dreißigjahresgrenze. Enthält Wirkung sämtlicher im konkreten Fall anwendbarer Hemmungen, besonders eingetragener Widerspruch§900 Absatz1 Satz3, und Ablaufregeln. Ohne Korrekturen rohe Grenze eingeben; unbekanntes Ende nicht durch Schätzung ersetzen.
- `prueftag`: ISO-Prüfdatum. Ergebnis gilt nach vollständigem Ablauf dieses Tages; genau am letzten Fristtag TRUE bedeutet erst mit dessen Ende.
- `zusammenhaengender_zeitraum_qualifiziert`: Expliziter Wahrheitswert: zusammenhängender, rechtlich qualifizierter Buchersitzungszeitraum des Eingetragenen, ursprünglich ohne das eingetragene Recht, mit erforderlichem Besitz und fortbestehender Eintragung. Keine anzurechnenden Vorgängerzeiten oder ungeklärten Unterbrechungen. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis zu Eintragung, Besitz/Rechtsart, Beginnart, Kontinuität sowie ausdrücklich der Herleitung des korrigierten Endes einschließlich Widerspruchs-/Hemmungslage.

Maximum aus Eintragungs- und qualifiziertem Besitzbeginn; dreißig Jahre gemäß gewählter Beginnart. Korrigiertes Ende darf rohe Grenze nicht unterschreiten. Prüftag am Tagesende mindestens korrigiertes Ende.

wert enthält gemeinsamer_beginn_am, dreissigjahresgrundfristende, massgebliches_fristende und frist_am_prueftag_abgelaufen. Fehlende Qualifikation NICHT_ANWENDBAR; kein endgültiger Rechtserwerbsausspruch.

Nur zusammenhängender qualifizierter Zeitraum; keine automatische Hemmungs-, Unterbrechungs-, Nachfolge-, Vermutungs- oder Erwerbsprüfung. Widerspruchs-Hemmung im qualifiziert korrigierten Datum; Rechtsrang Absatz2 Satz2 separat. Kein Übertragen des Gutglaubenserfordernisses§937 Absatz2.

ISO-Daten und berechnete Grenzen0001..9999, feste Auswahlwerte, expliziter Wahrheitswert und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_900_T0001, BGB_900_T0002, BGB_900_T0003, BGB_900_T0004

```python
from bgbcalc import buchersitzung_dreissigjahresfrist
buchersitzung_dreissigjahresfrist(
    eintragung_am='2000-01-31',
    besitzbeginn_am='2001-01-31',
    beginnart='ereignis',
    rechtsart='eigentum',
    korrigiertes_fristende='2031-01-31',
    prueftag='2031-01-30',
    zusammenhaengender_zeitraum_qualifiziert=True,
    einordnungsnachweis='Synthetisch zusammenhängender Zeitraum; keine Hemmung; rechtlich qualifizierte Beginnart.',
)
```
