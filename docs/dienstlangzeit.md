<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dienst_langzeitkuendigungsrahmen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `dienstbeginn_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Beginns des Dienstverhältnisses für Bindungs- und Fünfjahresprüfung. Nicht ungeprüft Datum der Unterschrift oder späteren Vertragsänderung verwenden.
- `beginnart`: Auswahl tagesbeginn bei mitzuzählendem ersten Diensttag ab Tagesbeginn oder ereignis bei rechtlich einschlägigem Ereignisbeginn. Rechtliche Einordnung§187 vorgeben.
- `lebenszeitvereinbarung`: Wahrheitswert einer Vereinbarung für die Lebenszeit einer Person. Maßgebliche Person/Bindung rechtlich bestimmen; gewöhnlicher unbefristeter Vertrag ist nicht automatisch Lebenszeitvereinbarung.
- `vereinbartes_dienstende_am`: ISO-Datum0001..9999 des vereinbarten letzten Diensttags einschließlich; ohne Lebenszeitvereinbarung erforderlich, mindestens Dienstbeginn. Bei Lebenszeitvereinbarung optional NULL/None; freiwilliges Datum wird validiert, ersetzt aber nicht die Lebenszeitprüfung.
- `kuendigungszugang_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Zugangs der Kündigung, mindestens Dienstbeginn. Noch vor Ablauf der fünf Jahre erklärte Kündigung wird nicht automatisch in spätere Erklärung umgedeutet.
- `kuendigung_durch_dienstverpflichteten`: Wahrheitswert, ob der Dienstverpflichtete kündigt. Das besondere Recht§624 steht nicht automatisch dem Dienstberechtigten zu.
- `regel_624_anwendbar`: Wahrheitswert der sachlichen/zeitlichen Anwendbarkeit des§624 im konkreten Dienstverhältnis, einschließlich konkurrierender Regeln. Dauer und Kündigungszeitpunkt werden zusätzlich berechnet. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung von Dienstbeginn, Beginnart, vereinbarter Dauer/Lebenszeit, noch bestehendem Dienstverhältnis, kündigender Person und Zugang. Frühere andere Beendigung gesondert prüfen.

Fünfjahreszeitraum und ersten Folgetag bestimmen. Lebenszeitvereinbarung oder vereinbartes Ende strikt nach Fünfjahresgrenze; Zugang frühestens am Folgetag während laufender Bindung durch Dienstverpflichteten. Dann sechsmonatiges rechnerisches Kündigungsfristende.

wert enthält fuenfjahreszeitraum_ende, fruehester_kuendigungstag als ISO-Daten, lange_bindung_erfuellt und kuendigung_nach_624_zeitlich_moeglich als Wahrheitswerte. rechnerisches_kuendigungsfristende ist ISO-Datum nur bei erfüllten geprüften Voraussetzungen, sonst null. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Genau fünf Jahre genügen nicht; früher Zugang wird nicht verschoben. Kein Aufschub eines früheren vertraglichen Endes auf das rechnerische Kündigungsfristende. Lebenszeitende/andere Beendigung sowie Erklärungsvoraussetzungen separat; keine automatische§193-Verlängerung.

ISO-Daten und berechnete Grenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis. Optionales Vertragsende nur bei Lebenszeitvereinbarung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_624_T0001, BGB_624_T0002

```python
from bgbcalc import dienst_langzeitkuendigungsrahmen
dienst_langzeitkuendigungsrahmen(
    dienstbeginn_am='2010-01-01',
    beginnart='tagesbeginn',
    lebenszeitvereinbarung=False,
    vereinbartes_dienstende_am='2014-12-31',
    kuendigungszugang_am='2014-12-31',
    kuendigung_durch_dienstverpflichteten=False,
    regel_624_anwendbar=True,
    einordnungsnachweis='Synthetische langfristige Bindung und tatsächlicher Kündigungszugang durch rechtlich bestimmte Person.',
)
```
