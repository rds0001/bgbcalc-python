<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteil_getrennter_zuwendungs_leistungsausgleich

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gruppennachlass`: Nichtnegative vollständige hypothetische gesetzliche Ausgleichungsgruppenmasse.
- `miterben`: Liste wie erbteilung_getrennter_zuwendungs_leistungsausgleich: person_id,relative_erbquote,ausgleichungswert_zuwendungen,leistungs_ausgleichsbetrag. Getrennte positive Zuwendungs-/Leistungsempfänger.
- `berechtigter_id`: ID des Pflichtteilsberechtigten innerhalb der hypothetischen Gruppe.
- `zugleich_anrechenbarer_zuwendungswert`: Nichtnegativer zugleich2315-anrechenbarer Anteil des eigenen bereits enthaltenen Ausgleichungswertes; gleicheBewertungsbasis.
- `hinterlassener_erbteilwert`: Rechtlich maßgeblicher nichtnegativer Wert, beiEnterbung0.
- `fall_nach_2316_qualifiziert`: Pflichtwahrheitswert des2316-Falls einschließlich getrennterEmpfänger,Leistungsvorwegabzug,Erbverzichtsausschluss undAusstattungsschutz;FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis gerade dieser rechtlichenReihenfolge undWertungen; keinefreieMethodenwahl.

Getrennten2055/2056/2057a-Kern anwenden; individuellenhypothetischenErbteil halbieren; zugleichanrechenbarenZuwendungswert nurhalbabziehen,mindestens0;positivenMehrbetrag gegenüberHinterlassenschaft bilden.

HypothetischerErbteil,PflichtteilvorDoppelanrechnung,halberAnrechnungswert,Pflichtteilswert undMehrbetrag exakt.

ZugleichLeistenderZuwendungsempfänger NICHT_ANWENDBAR. Keinezusätzlichenreinen2315-Zuwendungen,keine2325/2327Ergänzung. QualifizierteReihenfolge erforderlich.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2316_T0001, BGB_2316_T0003, BGB_2316_T0005

```python
from bgbcalc import pflichtteil_getrennter_zuwendungs_leistungsausgleich
pflichtteil_getrennter_zuwendungs_leistungsausgleich(
    gruppennachlass='100',
    miterben=[{'person_id': 'A', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '300', 'leistungs_ausgleichsbetrag': '0'}, {'person_id': 'B', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '20'}, {'person_id': 'C', 'relative_erbquote': {'zaehler': '1', 'nenner': '3'}, 'ausgleichungswert_zuwendungen': '0', 'leistungs_ausgleichsbetrag': '0'}],
    berechtigter_id='B',
    zugleich_anrechenbarer_zuwendungswert='0',
    hinterlassener_erbteilwert='10',
    fall_nach_2316_qualifiziert=True,
    bewertungsnachweis='HypothetischegesetzlicheGruppe,A NichtleistenderÜberempfänger,BLeistender; getrennteEmpfängerundReihenfolgequalifiziert.',
)
```
