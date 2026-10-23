<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## sonstige_miete_kuendigungstermin

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugang_kuendigung`: Rechtlich festgestellter Zugangstag als ISO-Datum.
- `fristfall`: tagesmiete, grundstueck_wochen, grundstueck_monate, gewerblich_unbebaut_monate, geschaeftsraeume oder beweglich_digital_laenger; Anwendungsbereich und Mietbemessungszeitraum qualifiziert.
- `qualifizierte_zugangsgrenze_am`: Qualifizierter erster Werktag der Zugangswoche beziehungsweise dritte Werktagsgrenze des Zugangsmonats oder Zugangsquartals. Örtliche Feiertags- und Zugangsregeln vorab berücksichtigen. Bei festen Tagesregeln null.
- `fristnachweis`: Nichtleerer Nachweis des gesetzlichen Fristfalls und der örtlich qualifizierten Zugangsschwelle.

Tagesmiete: Zugang plus1Tag. Wochenmiete: Samstag der Zugangswoche bei rechtzeitigem Zugang, sonst nächster Samstag. Monatsmiete: Ende des übernächsten Monats, bei verspätetem Zugang ein Monat später; gewerblich unbebaut auf nächstes Quartalsende aufrunden. Geschäftsräume: Ende des nächsten Quartals, bei verspätetem Zugang ein Quartal später. Bewegliche Sachen/digitale Produkte bei längerer Bemessung: Zugang plus3Tage.

wert: fruehester_beendigungstag, zugangsgrenze (bei Tagesregeln null), zugangsgrenze_eingehalten (bei Tagesregeln null).

Nur rechtlich qualifizierte gesetzliche Grundfälle580a, keine allgemeine Wohnraummietkündigung. tagesmiete umfasst580aI1/III1; grundstueck_wochen und grundstueck_monate jeweilsI2/I3, gewerblich_unbebaut_monate zusätzlich Quartalsbindung; geschaeftsraeume stetsAbsatz2; beweglich_digital_laenger Absatz3Nummer2. Bemessungszeitraum ist nicht automatisch Zahlungsrhythmus. Zugangsschwelle anhand einschlägiger örtlicher Werktags-/Feiertags- und Zugangsregeln ausdrücklich vorgeben; kein pauschaler Montag-bis-Freitag-Kalender. Feste Tagesregeln benötigen keine Werktagsschwelle. Beendigungstermine nicht nach193 verschieben. Absatz4 überträgt nurI3/II/III2 auf entsprechende außerordentliche Kündigung mit gesetzlicher Frist; Voraussetzungen extern qualifizieren. Befristung, abweichende Vereinbarungen und spezielle Verbrauchervertragsregeln für digitale Produkte gesondert.

Kalenderdaten0001..9999; keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_580a_T0001, BGB_580a_T0002, BGB_580a_T0003, BGB_580a_T0004, BGB_580a_T0005, BGB_580a_T0006, BGB_580a_T0007, BGB_580a_T0008, BGB_580a_T0009, BGB_580a_T0010

```python
from bgbcalc import sonstige_miete_kuendigungstermin
sonstige_miete_kuendigungstermin(
    zugang_kuendigung='2024-02-28',
    fristfall='tagesmiete',
    qualifizierte_zugangsgrenze_am=None,
    fristnachweis='Gesetzlicher Fall580a und örtliche Zugangsschwelle qualifiziert; kein abweichender Vertrag.',
)
```
