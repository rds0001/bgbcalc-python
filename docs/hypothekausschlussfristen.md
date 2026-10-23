<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_glaeubigerausschluss_grenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `letzte_eintragung_am`: ISO-Datum der letzten sich auf die Hypothek beziehenden Eintragung, nicht beliebiger späterer Grundbuchvorgang.
- `letztes_fristwirksames_anerkenntnis_am`: Optionales ISO-Datum des letzten innerhalb eines noch laufenden Fristlaufs wirksamen Anerkenntnisses212I1. Gegebenenfalls mehrfache vorausgehende Neubeginne rechtlich bereits geprüft; spätes Anerkenntnis nach abgelaufener Frist nicht als Neubeginn erfinden. Ohne solches Ereignis ausdrücklich null.
- `kalendertag_zahlung_am`: Optionaler rechtlich bestimmter kalendarischer Zahlungstag der Forderung; Fristbeginn nicht vor dessen Ablauf. Bei keiner kalendermäßig bestimmten Zahlungszeit ausdrücklich null.
- `inhaberschuldverschreibung`: Expliziter Wahrheitswert zum zusätzlichen Fall1188II.
- `vorlegungsfristende_am`: Bei1188II bereits vollständig berechneter letzter Tag der einschlägigen801-Vorlegungsfrist, einschließlich Urkundenabweichungen und Hemmung. Sonst null.
- `fristgemaesse_vorlegung_oder_klage`: Nur bei1188II ausdrücklicher Wahrheitswert: Schuldverschreibung innerhalb der Vorlegungsfrist vorgelegt oder Anspruch gerichtlich geltend gemacht? Sonst null.
- `verjaehrungsende_am`: Nur bei1188II und fristgemäßer Vorlegung/Klage: bereits vollständig berechneter letzter Verjährungstag, einschließlich einschlägiger Hemmung/Neubeginn. Sonst null.
- `einordnungsnachweis`: Nichtleerer Nachweis von1170, wirksamen Beginn-/Neubeginnereignissen und gegebenenfalls1188II/801-Zusatzgrenzen. Gläubigerunbekanntheit und Aufgebotsvoraussetzungen gesondert.

Spätesten qualifizierten1170-Bezugstag bestimmen und zehnjährige Ereignisfrist berechnen; im1188II-Fall zusätzliche Vorlegungs-/Verjährungsgrenzen als Maximum berücksichtigen, ersten Folgetag ausgeben.

wert: grundfristende_1170, kombinierte_zeitgrenze und erster_tag_nach_zeitgrenzen alsYYYY-MM-DD. Reine Zeitrechnung, kein automatisches Ausschließungsurteil.

§1170I/1188II: nur zeitlicher Grundrahmen für Gläubigerausschluss, kein Ausschließungsbeschluss oder automatischer Eigentumserwerb. Zahlungstag wirkt als früheste Fristbeginnschranke; nicht zusätzlich zehn Jahre nach bereits berechnetem Fristende addieren. Anerkenntnis als letzten rechtlich wirksamen Neubeginn vorqualifizieren; frühere Anerkenntnisse vor späterer maßgeblicher Eintragung ändern deren späteren Beginn nicht. Keine automatische Ermittlung beliebiger Anerkenntnisketten. Bei1188II muss Vorlegungsfrist verstrichen sein; nach fristgemäßer Vorlegung/Klage zusätzlich Verjährung abwarten. Zusatzfristen müssen bereits vollständig gerechnet sein. Ergebnis vor etwaigen weiteren rechtlich festgestellten Korrekturen des1170-Grundlaufs; keine pauschale193-Verschiebung. Keine Prüfung der Unbekanntheit des Gläubigers, des Aufgebotsverfahrens oder der Voraussetzungen des Eigentumserwerbs1170II.

Kalenderdaten0001..9999 einschließlich Grenz- und Folgedaten; keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1170_T0001, BGB_1170_T0002, BGB_1188_T0002, BGB_1188_T0003

```python
from bgbcalc import hypothek_glaeubigerausschluss_grenze
hypothek_glaeubigerausschluss_grenze(
    letzte_eintragung_am='2000-01-31',
    letztes_fristwirksames_anerkenntnis_am=None,
    kalendertag_zahlung_am=None,
    inhaberschuldverschreibung=False,
    vorlegungsfristende_am=None,
    fristgemaesse_vorlegung_oder_klage=None,
    verjaehrungsende_am=None,
    einordnungsnachweis='§1170I/1188II: nur zeitlicher Grundrahmen für Gläubigerausschluss, kein Ausschließungsbeschluss oder automatischer Eigentumserwerb. Zahlungstag wirkt als früheste Fristbeginnschranke; nicht zusätzlich zehn Jahre nach bereits berechnetem Fristende addieren. Anerkenntnis als letzten rechtlich wirksamen Neubeginn vorqualifizieren; frühere Anerkenntnisse vor späterer maßgeblicher Eintragung ändern deren späteren Beginn nicht. Keine automatische Ermittlung beliebiger Anerkenntnisketten. Bei1188II muss Vorlegungsfrist verstrichen sein; nach fristgemäßer Vorlegung/Klage zusätzlich Verjährung abwarten. Zusatzfristen müssen bereits vollständig gerechnet sein. Ergebnis vor etwaigen weiteren rechtlich festgestellten Korrekturen des1170-Grundlaufs; keine pauschale193-Verschiebung. Keine Prüfung der Unbekanntheit des Gläubigers, des Aufgebotsverfahrens oder der Voraussetzungen des Eigentumserwerbs1170II.',
)
```
