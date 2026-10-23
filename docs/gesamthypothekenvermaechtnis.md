<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamthypothekenvermaechtnis_befriedigungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schuldbetrag`: Nichtnegative volle betrachtete Hypothekenschuld in EUR. Nicht vorab um Drittberichtigung kürzen; Fälle§2166 Absatz2 sind hier ausdrücklich außerhalb Modell.
- `grundstuecke`: Liste2..1000 aller mit derselben Hypothek haftenden Grundstücke. Genau grundstueck_id (nichtleer eindeutig), grundstueckswert und vorrangige_belastungen (nichtnegative EUR). Werte gemäß§2166 Absatz1 Satz2 bei Eigentumsübergang, bei verschiedenen Übergangszeitpunkten Vergleichsbasis rechtlich bestimmen. Nur im Rang vorgehende Belastungen abziehen, nicht betrachtete Gesamthypothek.
- `vermachtes_grundstueck_id`: ID des vermachten Grundstücks aus vollständiger Liste; nur dessen interne Befriedigungspflicht wird berechnet.
- `schuld_nach_2166_qualifiziert`: Expliziter Wahrheitswert: eigene Schuld des Erblassers oder Schuld, zu deren Berichtigung er dem Schuldner verpflichtet war, Nachlassgrundstücksvermächtnis und sonstige Grundvoraussetzungen§2166 qualifiziert.
- `zweifelsregel_anwendbar`: Expliziter Wahrheitswert der einschlägigen Zweifelsregel ohne abweichenden Erblasserwillen.
- `hoechstbetragshypothek`: Expliziter Wahrheitswert zur Hypothek§1190; TRUE schließt Anwendung aus.
- `alle_mithaftenden_grundstuecke_im_nachlass`: Expliziter Wahrheitswert, dass sämtliche mithaftenden Grundstücke zur Erbschaft gehören und vollständig aufgeführt sind. FALSE ergibt NICHT_ANWENDBAR.
- `drittberichtigung_nach_2166_absatz_2`: Expliziter Wahrheitswert des Drittberichtigungsfalls§2166 Absatz2. TRUE ergibt NICHT_ANWENDBAR; Verteilungs-/Drittleistungsreihenfolge wird hier nicht erfunden.
- `bewertungsnachweis`: Nichtleere Herkunft und rechtliche Einordnung von Schuldbetrag, sämtlichen Grundstückswerten, Stichtag, Ranglasten und Anwendungsbereich.

Je Grundstück positive Wertdeckung nach rangvorrangigen Lasten berechnen. Vermachten bereinigten Wert durch bereinigten Gesamtwert teilen; volle Schuld proportional verteilen und zusätzlich auf eigene Wertdeckung begrenzen. Bei Gesamtdeckung0 Befriedigung0 ohne fingierte0/0-Quote.

wert enthält bereinigte_grundstueckswerte, bereinigter_gesamtwert, verteilungsquote, anteilige_schuld, befriedigungsbetrag. Bei Gesamtdeckung0 sind Quote und anteilige Schuld NULL, Befriedigungsbetrag0.

Keine Drittberichtigung§2166II; kein Nichtnachlassgrundstück, keine Höchstbetragshypothek oder Gesamtgrund-/Rentenschuld. Nur interne Verpflichtung gegenüber Erben, keine Begrenzung dinglicher Gläubigerrechte. Keine erfundene Bewertungs-/Fälligkeitsregel.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2167_T0001, BGB_2167_T0002, BGB_2166_T0001, BGB_2166_T0002, BGB_2166_T0004

```python
from bgbcalc import gesamthypothekenvermaechtnis_befriedigungsbetrag
gesamthypothekenvermaechtnis_befriedigungsbetrag(
    schuldbetrag='0',
    grundstuecke=[{'grundstueck_id': 'A', 'grundstueckswert': '100', 'vorrangige_belastungen': '40'}, {'grundstueck_id': 'B', 'grundstueckswert': '200', 'vorrangige_belastungen': '80'}],
    vermachtes_grundstueck_id='A',
    schuld_nach_2166_qualifiziert=True,
    zweifelsregel_anwendbar=True,
    hoechstbetragshypothek=False,
    alle_mithaftenden_grundstuecke_im_nachlass=True,
    drittberichtigung_nach_2166_absatz_2=False,
    bewertungsnachweis='Synthetisch qualifizierte Gesamthypothek auf vollständigem Nachlassgrundstückskreis, Vergleichswerte und Ranglasten bei Eigentumsübergang.',
)
```
