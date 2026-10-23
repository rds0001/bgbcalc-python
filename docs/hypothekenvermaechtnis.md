<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothekenvermaechtnis_befriedigungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `schuldbetrag`: Nichtnegative Höhe der betrachteten hypothekarisch gesicherten Schuld; exakte EUR-Zeichenfolge oder Bruch.
- `grundstueckswert`: Rechtlich bewerteter Grundstückswert im Zeitpunkt des Eigentumsübergangs auf Vermächtnisnehmer, vor Abzug rangvorrangiger Belastungen.
- `vorrangige_belastungen`: Rechtlich bewertete Summe nur der betrachteten Hypothek im Rang vorgehender Belastungen; Hypothek selbst nicht erneut abziehen.
- `vom_dritten_erlangbarer_betrag`: Nichtnegative Berichtigung dieser Schuld, die der Erbe von einem gegenüber dem Erblasser zur Berichtigung verpflichteten Dritten erlangen kann; höchstens schuldbetrag. Ohne solchen Dritten null, nicht unbekannt. Nicht bloß tatsächlich bereits gezahlter Betrag.
- `schuld_nach_2166_qualifiziert`: Wahrheitswert: vermachtes Grundstück gehört zur Erbschaft, Hypothek für eigene Schuld des Erblassers oder Schuld, zu deren Berichtigung er dem Schuldner gegenüber verpflichtet war.
- `zweifelsregel_anwendbar`: Wahrheitswert: keine maßgebliche abweichende Erblasseranordnung; gesetzliche Zweifelsregel einschlägig.
- `hoechstbetragshypothek`: Wahrheitswert: Hypothek§1190; TRUE führt gemäß§2166 Absatz3 NICHT_ANWENDBAR.
- `weitere_grundstuecke_mithaftend`: Wahrheitswert: weitere Grundstücke haften für dieselbe Schuld; TRUE außerhalb dieses Einzelgrundstücksmodells. §2167/2168 nicht durch unqualifizierten Wertansatz ersetzen.
- `bewertungsnachweis`: Nichtleere Begründung der Schuld, Bewertung, Rangfolge und vom Erben erlangbaren Drittberichtigung.

Deckung=max(Grundstückswert minus vorrangige Belastungen,0). Verbleibende Schuld=Schuld minus erlangbare Drittberichtigung. Interne Befriedigungsverpflichtung=min(Deckung, verbleibende Schuld).

wert enthält bereinigter_grundstueckswert, schuld_nach_drittberichtigung und befriedigungsbetrag als exakte EUR-Brüche.

Keine dingliche Haftungsbegrenzung oder Fälligkeitsbestimmung. Nur Einzelgrundstück; Mehrgrundstücksquoten§2167 und Gesamtgrundschuld§2168 außerhalb. Höchstbetragshypothek ausgeschlossen. Bewertung/Erblasserwille qualifiziert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2166_T0001, BGB_2166_T0002, BGB_2166_T0003, BGB_2166_T0004

```python
from bgbcalc import hypothekenvermaechtnis_befriedigungsbetrag
hypothekenvermaechtnis_befriedigungsbetrag(
    schuldbetrag='100',
    grundstueckswert='80',
    vorrangige_belastungen='30',
    vom_dritten_erlangbarer_betrag='0',
    schuld_nach_2166_qualifiziert=True,
    zweifelsregel_anwendbar=True,
    hoechstbetragshypothek=False,
    weitere_grundstuecke_mithaftend=False,
    bewertungsnachweis='Synthetisch qualifiziertes Einzelgrundstück, Rangwerte bei Eigentumsübergang und erlangbare Drittberichtigung.',
)
```
