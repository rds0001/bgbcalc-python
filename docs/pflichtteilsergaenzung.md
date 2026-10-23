<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_mehrhinterlassung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ergaenzungsbetrag_vor_mehrhinterlassung`: Nichtnegativer rechtlich bestimmter Ergänzungsbetrag in EUR vor Abzug der hier betrachteten Mehrhinterlassung. Nicht den gesamten ordentlichen Pflichtteil oder einen bereits nach§2326 gekürzten Betrag eingeben.
- `hinterlassener_wert`: Nichtnegativer rechtlich nach§2326 maßgeblicher Wert des dem Pflichtteilsberechtigten Hinterlassenen in EUR. Anzuerkennende Belastungen, Vermächtnisse und konkrete erbrechtliche Lage vorab zutreffend bewerten; kein beliebiger Bruttowert.
- `ordentlicher_pflichtteilswert`: Nichtnegativer Wert des ordentlichen Pflichtteils in EUR als Hälfte des maßgeblichen gesetzlichen Erbteils am tatsächlichen rechtlich bewerteten Nachlass. Kein bereits um Schenkungen ergänzter Pflichtteilswert.
- `bewertungsnachweis`: Nichtleere Beschreibung von ordentlichem Pflichtteil, Hinterlassung und Ergänzungsbetrag vor dieser Anrechnung auf konsistenter Bewertungsbasis. Weitere Anrechnungen separat und ohne Doppelzählung bestimmen.

Mehrhinterlassung=max(hinterlassener Wert−ordentlicher Pflichtteilswert,0). Verbleibende Ergänzung=max(Ergänzung vor dieser Anrechnung−Mehrhinterlassung,0).

wert enthält mehrhinterlassung, angerechneter_betrag (höchstens Ergänzungsbetrag) und verbleibende_ergaenzung als exakte EUR-Brüche.

Bloßes Hinterlassen des ordentlichen Pflichtteils schließt Ergänzung nicht aus. Nur Mehrwert darüber anrechnen. Eigengeschenke§2327, Erbenschutz§2328, Beschenktenhaftung§2329 und andere Anspruchsvoraussetzungen außerhalb dieser Operation.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2326_T0001, BGB_2326_T0002

```python
from bgbcalc import pflichtteilsergaenzung_mehrhinterlassung
pflichtteilsergaenzung_mehrhinterlassung(
    ergaenzungsbetrag_vor_mehrhinterlassung='0',
    hinterlassener_wert='0',
    ordentlicher_pflichtteilswert='0',
    bewertungsnachweis='Synthetisch konsistente ordentliche Pflichtteils- und Hinterlassungswerte.',
)
```

## pflichtteil_schenkungswert

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vergleichbarer_schenkungswert`: Nichtnegativer rechtlich bestimmter Schenkungswert in EUR aus dem Bewertungszeitpunkt der Schenkung, mit erforderlicher Wert-/Kaufkraftbereinigung für einen zulässigen Vergleich zum Erbfall. Belastungen und gegebenenfalls vorbehaltene Rechte fachlich bewerten. Kein ungeprüfter historischer Nominalwert.
- `wert_beim_erbfall`: Nichtnegativer rechtlich bestimmter Wert desselben Gegenstands zur Zeit des Erbfalls in EUR. Gleicher Bewertungsumfang und vergleichbarer Maßstab wie Schenkungswert. Bei verbrauchbarer Sache typgültig erforderlich, aber nicht maßgeblich.
- `verbrauchbare_sache`: Wahrheitswert der rechtlichen Einordnung nach§92: bewegliche Sache mit bestimmungsmäßigem Verbrauch/Veräußerung, einschließlich entsprechender Warenlager/Sachinbegriffe. Nicht bloß physische Abnutzbarkeit.
- `pflicht_oder_anstandsschenkung`: Wahrheitswert einer Schenkung zur Erfüllung sittlicher Pflicht oder einer auf den Anstand zu nehmenden Rücksicht gemäß§2330. TRUE ergibt NICHT_ANWENDBAR für diese Ergänzungsbewertung, nicht einen allgemeinen Wertnull der Sache.
- `bewertungsnachweis`: Nichtleere Beschreibung der Schenkung, beiden Bewertungszeitpunkte, vergleichbaren Wertansätze, etwaiger Bereinigung/Belastungen, Verbrauchbarkeit und Ausnahme§2330. Keine Schenkung an den Pflichtteilsberechtigten ungeprüft als Drittschenkung behandeln.

Verbrauchbare Sache: rechtlich vergleichbar bestimmter Schenkungswert. Sonst Minimum aus Schenkungs- und Erbfallwert. Pflicht-/Anstandsschenkung ausnehmen.

wert ist exakter EUR-Bewertungsansatz. Ausnahme§2330 ergibt NICHT_ANWENDBAR mit null.

Bewertungswahl vor Abschmelzung und Quotenberechnung; keine abschließende Pflichtteilsergänzung. Kein automatischer Verbraucherpreisindex oder Sachverständigenwert. Rechtlich erforderliche Preisbasis-/Belastungsbewertung als belegte Eingabe. Sonderfälle und weitere Anrechnungen separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_92_T0001, BGB_92_T0002, BGB_2325_T0002, BGB_2325_T0003, BGB_2330_T0001

```python
from bgbcalc import pflichtteil_schenkungswert
pflichtteil_schenkungswert(
    vergleichbarer_schenkungswert='0',
    wert_beim_erbfall='0',
    verbrauchbare_sache=False,
    pflicht_oder_anstandsschenkung=False,
    bewertungsnachweis='Synthetische vergleichbare rechtlich bestimmte Schenkungs-/Erbfallwerte.',
)
```
