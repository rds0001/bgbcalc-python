<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_liquidationsfehlbetrag_verteilen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fehlbetrag`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; gleiche Liquidationsabrechnung ohne Doppelzählung.
- `gesellschafter`: Vollständige Liste2..1000 Personen mit eindeutiger gesellschafter_id, nichtnegativem Gewinn-/Verlustanteil als exaktem Bruch/Dezimalwert (Summe1) und qualifiziertem einbringlicher_hoechstbetrag in EUR; letzterer ist tatsächlich/rechtlich erlangbarer Gesamtbetrag für diesen Fehlbetrag, keine frei gesetzte Haftungsgrenze.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Liquidationsfalls, qualifizierter Vermögens-/Verbindlichkeits-/Beitragswerte und gegebenenfalls Einbringlichkeitsgrenzen.

Fehlbetrag nach Quoten verteilen und qualifiziert uneinbringliche Teile proportional nachverteilen.

wert enthält EUR-Bruchobjekte für Liquidationsgrundbedarf/Überschuss/Fehlbetrag bzw. Verteilung mit Regelanteil, beibringbarem Betrag, zusätzlicher Ausfalllast, Gesamteinbringlichkeit und ungedecktem Fehlbetrag.

Nur §737 bei qualifiziertem Liquidationsfehlbetrag einschließlich Beitragsrückerstattungsbedarf. Einbringlicher Höchstbetrag bezeichnet rechtlich/tatsächlich festgestellten insgesamt noch erlangbaren Betrag für diesen Fehlbetrag, keine beliebige vertragliche Haftungsbegrenzung und keine bereits gezahlte Summe. Beträge auf gemeinsame Abrechnungsbasis bringen; Ausfälle bis zur Ausschöpfung der übrigen Grenzen proportional nachverteilen. Nullquote trägt keine rechnerische Ausfalllast. Uneinbringlicher Rest bleibt offen; kein Erlass und keine freie Beitragsrückzahlungsquote. Keine Feststellung der Insolvenz oder automatischer Vollstreckungsprognosen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_737_T0001, BGB_737_T0002

```python
from bgbcalc import gesellschaft_liquidationsfehlbetrag_verteilen
gesellschaft_liquidationsfehlbetrag_verteilen(
    fehlbetrag='120',
    gesellschafter=[{'gesellschafter_id': 'A', 'gewinn_verlust_anteil': {'zaehler': '1', 'nenner': '3'}, 'einbringlicher_hoechstbetrag': '1000'}, {'gesellschafter_id': 'B', 'gewinn_verlust_anteil': {'zaehler': '1', 'nenner': '3'}, 'einbringlicher_hoechstbetrag': '1000'}, {'gesellschafter_id': 'C', 'gewinn_verlust_anteil': {'zaehler': '1', 'nenner': '3'}, 'einbringlicher_hoechstbetrag': '1000'}],
    einordnungsnachweis='Vollständige Quoten und qualifiziert erlangbare Gesamtbeträge desselben Fehlbetrags.',
)
```

## gesellschaft_liquidationsgrundbetraege

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesellschaftsvermoegen`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; gleiche Liquidationsabrechnung ohne Doppelzählung.
- `zu_berichtigende_verbindlichkeiten`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; gleiche Liquidationsabrechnung ohne Doppelzählung.
- `erforderliche_rueckbehalte`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; gleiche Liquidationsabrechnung ohne Doppelzählung.
- `rueckzuerstattende_beitraege`: Nichtnegativer exakter rechtlich qualifizierter EUR-Betrag als Dezimalzeichenfolge/Bruchobjekt; gleiche Liquidationsabrechnung ohne Doppelzählung.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Liquidationsfalls, qualifizierter Vermögens-/Verbindlichkeits-/Beitragswerte und gegebenenfalls Einbringlichkeitsgrenzen.

Gläubiger- und Reservebedarf vor Beiträgen; Überschuss und gesamten Fehlbetrag berechnen.

wert enthält EUR-Bruchobjekte für Liquidationsgrundbedarf/Überschuss/Fehlbetrag bzw. Verteilung mit Regelanteil, beibringbarem Betrag, zusätzlicher Ausfalllast, Gesamteinbringlichkeit und ungedecktem Fehlbetrag.

§736d Absatz4–6/§737: tatsächlich verfügbares Liquidationsvermögen; fällige zu berichtigende Verbindlichkeiten und erforderliche Rückbehalte für nicht fällige/streitige Verbindlichkeiten überschneidungsfrei. Rückzuerstattende Beiträge sind rechtlich qualifiziert: Sachbeiträge zum Einbringungswert, Dienste/Nutzungsüberlassung im Zweifel kein Ersatz. Überschuss nach Gewinn-/Verlustquoten verteilen; Fehlbetrag nach §737 decken. Reicht Vermögen nicht, wird keine freie Quote für teilweise Beitragsrückerstattung oder Rangfolge unter Gläubigern erfunden. Kein Ersatz für Insolvenzprüfung, Bewertung von Sachbeiträgen oder Abrechnung bereits erfolgter Liquidationszahlungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_736d_T0006, BGB_736d_T0007, BGB_736d_T0008, BGB_736d_T0011, BGB_737_T0001

```python
from bgbcalc import gesellschaft_liquidationsgrundbetraege
gesellschaft_liquidationsgrundbetraege(
    gesellschaftsvermoegen='1000',
    zu_berichtigende_verbindlichkeiten='400',
    erforderliche_rueckbehalte='100',
    rueckzuerstattende_beitraege='200',
    einordnungsnachweis='Qualifizierte Liquidationswerte ohne Doppelzählung.',
)
```
