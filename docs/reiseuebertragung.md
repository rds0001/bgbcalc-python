<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## reiseuebertragung_mehrkostenbetrag

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `tatsaechliche_mehrkosten`: Nachweislich durch Eintritt des Dritten tatsächlich entstandene zusätzliche Kosten in Euro; kein Reisepreis, keine bloße Pauschale.
- `angemessener_hoechstbetrag`: Rechtlich bewerteter angemessener Höchstbetrag für genau dieselben Mehrkosten in Euro; keine erfundene Tarifgrenze.
- `einordnungsnachweis`: Nichtleerer Nachweis von tatsächlichem Eintritt, Kausalität, Angemessenheit und betragsmäßigem Nachweis651eIV.

Tatsächlich entstandene Übertragungsmehrkosten auf rechtlich angemessenen Höchstbetrag begrenzen.

wert als exakter nichtnegativer Eurobruch mit zaehler und nenner.

§651eIII2/IV: nur kleinere Zahl aus tatsächlichen nachgewiesenen Mehrkosten und rechtlich angemessener Betragsgrenze. Keine Gebührentabelle oder automatische Angemessenheitsprüfung. Reisepreis nicht nochmals als Mehrkosten zählen. Gesamtschuld von Reisendem und Drittem rechtlich vorausgesetzt; Betrag nicht verdoppeln und nicht automatisch nach Köpfen aufteilen. Andere Zahlungs-/Erfüllungsvorgänge separat.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651e_T0004, BGB_651e_T0005, BGB_651e_T0006

```python
from bgbcalc import reiseuebertragung_mehrkostenbetrag
reiseuebertragung_mehrkostenbetrag(
    tatsaechliche_mehrkosten='120',
    angemessener_hoechstbetrag='80',
    einordnungsnachweis='§651eIII2/IV: nur kleinere Zahl aus tatsächlichen nachgewiesenen Mehrkosten und rechtlich angemessener Betragsgrenze. Keine Gebührentabelle oder automatische Angemessenheitsprüfung. Reisepreis nicht nochmals als Mehrkosten zählen. Gesamtschuld von Reisendem und Drittem rechtlich vorausgesetzt; Betrag nicht verdoppeln und nicht automatisch nach Köpfen aufteilen. Andere Zahlungs-/Erfüllungsvorgänge separat.',
)
```

## reiseuebertragung_siebentagevergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `reisebeginn_am`: Rechtlich auf Kalendertag normalisierter ReisebeginnYYYY-MM-DD.
- `erklaerungszugang_am`: Rechtlich auf Kalendertag normalisierter Zugang der Erklärung beim VeranstalterYYYY-MM-DD, nicht Absendedatum.
- `einordnungsnachweis`: Nichtleerer Nachweis des651eI-Falls und der rechtlich zutreffenden taggenauen Normalisierung einschließlich gegebenenfalls relevanter Uhrzeiten/Zeitzonen.

Taggenau qualifizierten Abstand zwischen tatsächlichem Erklärungszugang und Reisebeginn bestimmen und mit sieben Kalendertagen vergleichen.

wert.kalendertage_vorlauf als vorzeichenbehaftete ganze Zahl und wert.mindestens_sieben_kalendertage als Wahrheitswert.

§651eI2: nur Anzahl der qualifizierten Kalendertage zwischen Zugang und Reisebeginn und Vergleich mit sieben Tagen. Erreichen ist rechnerischer Nachweis der gesetzlichen Siebentage-Sicherheitsgrenze im taggenau qualifizierten Fall. Unterschreiten bedeutet nicht automatisch Unwirksamkeit oder Verspätung: angemessene kürzere Frist nachSatz1 bleibt rechtlich zu prüfen. Dauerhafter Datenträger, tatsächlicher Zugang und Eignung des Dritten extern. Keine pauschale Umrechnung in168Stunden, keine automatische Feiertagsverschiebung und kein untertägiges Zugangs-/Reisebeginnurteil.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651e_T0001, BGB_651e_T0002

```python
from bgbcalc import reiseuebertragung_siebentagevergleich
reiseuebertragung_siebentagevergleich(
    reisebeginn_am='2024-03-10',
    erklaerungszugang_am='2024-03-03',
    einordnungsnachweis='§651eI2: nur Anzahl der qualifizierten Kalendertage zwischen Zugang und Reisebeginn und Vergleich mit sieben Tagen. Erreichen ist rechnerischer Nachweis der gesetzlichen Siebentage-Sicherheitsgrenze im taggenau qualifizierten Fall. Unterschreiten bedeutet nicht automatisch Unwirksamkeit oder Verspätung: angemessene kürzere Frist nachSatz1 bleibt rechtlich zu prüfen. Dauerhafter Datenträger, tatsächlicher Zugang und Eignung des Dritten extern. Keine pauschale Umrechnung in168Stunden, keine automatische Feiertagsverschiebung und kein untertägiges Zugangs-/Reisebeginnurteil.',
)
```
