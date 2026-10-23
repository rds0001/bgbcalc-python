<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbraucher_entgeltkostenvergleich

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbartes_entgelt`: Nichtnegatives vereinbartes Entgelt in EUR für die konkrete Nutzung.
- `massgebliche_kosten`: Nichtnegative rechtlich qualifizierte Kosten dieser Zahlungsmittelnutzung für den Unternehmer oder das Entgelt für bloße Telekommunikationsnutzung. Konsistente Abrechnungseinheit.
- `regelfall`: zahlungsmittel_312a_absatz_4 oder vertragsanruf_312a_absatz_5.
- `vergleich_anwendbar`: Bestätigung des Kostenvergleichs-Anwendungsfalls. Keine Bestätigung, dass alle übrigen Zulässigkeitsvoraussetzungen erfüllt sind. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleerer Nachweis der Entgelte, tatsächlichen Kostenbasis, Abrechnungseinheit und Fallwahl.

Positive Differenz des vereinbarten Entgelts gegenüber maßgeblichen Kosten; strikte Kostenüberschreitung.

wert: kostenobergrenze und entgeltueberhang als EUR-Brüche, kostengrenze_ueberschritten als Wahrheitswert.

KEIN auf Kostengrenze reduzierter Zahlungsanspruch; überschreitende Vereinbarung ist unwirksam. Gängige zumutbare unentgeltliche Zahlungsmöglichkeit und speziellere Entgeltverbote nicht automatisch geprüft. Telekommunikations-Erstattungsanspruch gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_312a_T0008, BGB_312a_T0009, BGB_312a_T0010, BGB_312a_T0011, BGB_312a_T0012, BGB_312a_T0013

```python
from bgbcalc import verbraucher_entgeltkostenvergleich
verbraucher_entgeltkostenvergleich(
    vereinbartes_entgelt='10',
    massgebliche_kosten='3',
    regelfall='zahlungsmittel_312a_absatz_4',
    vergleich_anwendbar=True,
    einordnungsnachweis='Synthetischer Entgelt-/Kostenvergleich für einheitliche Nutzung.',
)
```

## verbraucher_informierte_nebenkosten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kostenpositionen`: Liste bis1000 eindeutiger Objekte mit position_id, nichtnegativem EUR-betrag und Wahrheitswert ordnungsgemaess_informiert. Nur rechtlich zugehörige und sonst beanspruchbare Positionen; bei teilweiser Information rechtlich zutreffend aufteilen.
- `regelfall`: praesenz_312a_absatz_2 oder fernabsatz_aussergeschaeftlich_312e; gesetzlichen Anwendungsbereich vorher qualifizieren.
- `kostenregel_anwendbar`: Explizite Bestätigung des Kostenregel-Anwendungsfalls ohne speziellere Ausschlüsse; FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Herkunft/Begründung von Positionen, Vereinbarung, Kostenhöhe und gesetzeskonformer Information.

Ordnungsgemäß informierte zugehörige Kosten auswählen und exakt addieren.

wert ist Summe der eingeschlossenen Kosten in EUR; leer oder vollständig ausgeschlossen ergibt0.

Keine neue qualitative Informationsprüfung.312a Absatz2 ausgenommen Fernabsatz/außergeschäftliche/Finanzdienstleistungsverträge. Hauptpreis und andere Entgeltverbote separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_312a_T0004, BGB_312a_T0005, BGB_312e_T0001

```python
from bgbcalc import verbraucher_informierte_nebenkosten
verbraucher_informierte_nebenkosten(
    kostenpositionen=[{'position_id': 'a', 'betrag': '10', 'ordnungsgemaess_informiert': True}, {'position_id': 'b', 'betrag': '20', 'ordnungsgemaess_informiert': False}, {'position_id': 'c', 'betrag': '0.25', 'ordnungsgemaess_informiert': True}],
    regelfall='praesenz_312a_absatz_2',
    kostenregel_anwendbar=True,
    einordnungsnachweis='Synthetische qualifizierte Kosten, Information gemäß einschlägigem EGBGB-Verweis.',
)
```
