<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## landpacht_verzug_zeit_und_terminvergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `verzugsbeginn_am`: Rechtlich qualifizierter Beginn des fortdauernden erheblichen PachtverzugsYYYY-MM-DD, nicht ungeprüft gleich Fälligkeit.
- `beginnart`: ereignis oder tagesbeginn nach rechtlicher Qualifikation des Beginns der Verzugslaufzeit.
- `prueftag`: KalendertagYYYY-MM-DD für Vergleich mit abgelaufener Dreimonatszeit.
- `rueckstaendige_terminnummern`: Liste0..1000 positiver eindeutiger ganzer Nummern aus dem vollständigen chronologisch fortlaufend nummerierten Pachtzahlungskalender. Jede genannte Rate rechtlich in Verzug mit Pacht oder nicht unerheblichem Teil; ausgelassene Nummern sind nicht qualifiziert rückständig.
- `einordnungsnachweis`: Nichtleerer Nachweis594eII, kontinuierlichem maßgeblichem Verzug, Zeitnormalisierung und vollständiger Terminfolge. Einordnung Zahlungsabschnitte kürzer als ein Jahr und übrige Kündigungsvoraussetzungen extern.

Dreimonats-Verzugslaufzeit streng vergleichen und aufeinanderfolgende qualifiziert rückständige Pachtzahlungstermine zählen.

wert.dreimonatszeitraum_letzter_tag als Datum, laenger_als_drei_monate als Wahrheitswert, laengste_rueckstandsfolge als ganze Zahl, mindestens_zwei_aufeinanderfolgende_termine als Wahrheitswert.

§594eII: Ende einer qualifizierten Dreimonats-Verzugslaufzeit und strenges Überschreiten am Prüftag berechnen; daneben längste lückenlos aufeinanderfolgende Folge qualifiziert rückständiger Zahlungstermine zählen und mit2vergleichen. Keine erfundene Euro-/Prozentgrenze für nicht unerheblichen Teil. Beide numerischen Teilprüfungen getrennt ausgegeben; rechtliche Fallzuordnung nach Zahlungsabschnitt sowie deren Zusammenspiel und Kündigung nicht automatisch entschieden. Terminnummern müssen dem vollständigen Kalender entsprechen, keine nachträgliche Neunummerierung nur rückständiger Raten. Kein künstlicher Neustart/Stillstand des Verzugs bei unbekannten Zahlungsvorgängen; Fristbeginn und kontinuierlicher Verlauf vorqualifiziert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_594e_T0002, BGB_594e_T0003

```python
from bgbcalc import landpacht_verzug_zeit_und_terminvergleich
landpacht_verzug_zeit_und_terminvergleich(
    verzugsbeginn_am='2024-01-01',
    beginnart='tagesbeginn',
    prueftag='2024-04-01',
    rueckstaendige_terminnummern=[1, 2],
    einordnungsnachweis='§594eII: Ende einer qualifizierten Dreimonats-Verzugslaufzeit und strenges Überschreiten am Prüftag berechnen; daneben längste lückenlos aufeinanderfolgende Folge qualifiziert rückständiger Zahlungstermine zählen und mit2vergleichen. Keine erfundene Euro-/Prozentgrenze für nicht unerheblichen Teil. Beide numerischen Teilprüfungen getrennt ausgegeben; rechtliche Fallzuordnung nach Zahlungsabschnitt sowie deren Zusammenspiel und Kündigung nicht automatisch entschieden. Terminnummern müssen dem vollständigen Kalender entsprechen, keine nachträgliche Neunummerierung nur rückständiger Raten. Kein künstlicher Neustart/Stillstand des Verzugs bei unbekannten Zahlungsvorgängen; Fristbeginn und kontinuierlicher Verlauf vorqualifiziert.',
)
```
