<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamthypothek_regress_restverteilung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `gesamthypothekenbetrag`: Nichtnegativer Gesamtbetrag vor dem hier betrachteten Teilübergang.
- `uebergegangener_regressbetrag`: Teilbetrag, der auf den persönlichen Schuldner übergeht; höchstens Gesamtbetrag.
- `grundstuecke`: Vollständige1172-Liste mit grundstueck_id, grundstueckswert, vorrangige_belastungen.
- `ersatzpflichtiges_grundstueck_id`: Das eine Grundstück des nach1174ersatzpflichtigen Eigentümers.
- `verteilungsmodell`: Zwingend ausdrücklich qualifiziert: restquotierung_mit_anteiliger_restzuweisung. Kein gesetzlicher Standard ohne rechtliche Prüfung.
- `methodennachweis`: 1174II-Teilübergang, positive Nettowertgewichte, Anrechnung nach Restquotierung und proportionale Zuweisung des freigewordenen Betrags an die übrigen Eigentümer rechtlich begründen.

Teilübergang abziehen,1174-Anrechnung auf Restquote ausführen und übrige Masse unter ausdrücklich vorgegebenem Modell den anderen Eigentümern proportional zuweisen.

Übergegangener Regress, Gemeinschaftsrestmasse, vollständige Eigentümerliste und expliziter nicht zugewiesener Restbetrag.

Bedingtes vollständiges Rechenmodell: Restmasse=Gesamtbetrag-Regressübergang.1172-Nettogewichte mit vorhandener positiver Nettowertmethode bestimmen.1174II-Anrechnung des Übergangs auf den quotierten Restanteil des ersatzpflichtigen Eigentümers durch vorhandenen Anrechnungskern. Verbleibende Restmasse proportional nach positiven Nettogewichten der übrigen Eigentümer verteilen. Dieses zusätzliche Zuweisungsmodell ist eine ausdrücklich zu qualifizierende Voraussetzung, keine aus dem Normwortlaut allein gesicherte generelle Auslegung. Ohne andere positive Gewichte bleibt der nicht zuweisbare Betrag sichtbar; keine künstliche Kopfquote oder Rückzuweisung entgegen der gewählten Anrechnung. Bei völlig fehlender positiver Nettowertbasis Eingabe ablehnen und separate Nettowertdiagnose verwenden. Summe Übergang+Eigentümeranteile+nichtzugewiesen=Gesamtbetrag.1176/1182-Rangschutz ist zusätzlich rechtlich zu beachten und wird nicht als allgemeiner ZVG-Verteilungsalgorithmus erfunden.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1172_T0001, BGB_1172_T0002, BGB_1172_T0003, BGB_1174_T0001, BGB_1174_T0002, BGB_1176_T0001, BGB_1182_T0001, BGB_1182_T0002

```python
from bgbcalc import gesamthypothek_regress_restverteilung
gesamthypothek_regress_restverteilung(
    gesamthypothekenbetrag='100',
    uebergegangener_regressbetrag='20',
    grundstuecke=[{'grundstueck_id': 'A', 'grundstueckswert': '100', 'vorrangige_belastungen': '0'}, {'grundstueck_id': 'B', 'grundstueckswert': '100', 'vorrangige_belastungen': '0'}],
    ersatzpflichtiges_grundstueck_id='A',
    verteilungsmodell='restquotierung_mit_anteiliger_restzuweisung',
    methodennachweis='Bedingtes vollständiges Rechenmodell: Restmasse=Gesamtbetrag-Regressübergang.1172-Nettogewichte mit vorhandener positiver Nettowertmethode bestimmen.1174II-Anrechnung des Übergangs auf den quotierten Restanteil des ersatzpflichtigen Eigentümers durch vorhandenen Anrechnungskern. Verbleibende Restmasse proportional nach positiven Nettogewichten der übrigen Eigentümer verteilen. Dieses zusätzliche Zuweisungsmodell ist eine ausdrücklich zu qualifizierende Voraussetzung, keine aus dem Normwortlaut allein gesicherte generelle Auslegung. Ohne andere positive Gewichte bleibt der nicht zuweisbare Betrag sichtbar; keine künstliche Kopfquote oder Rückzuweisung entgegen der gewählten Anrechnung. Bei völlig fehlender positiver Nettowertbasis Eingabe ablehnen und separate Nettowertdiagnose verwenden. Summe Übergang+Eigentümeranteile+nichtzugewiesen=Gesamtbetrag.1176/1182-Rangschutz ist zusätzlich rechtlich zu beachten und wird nicht als allgemeiner ZVG-Verteilungsalgorithmus erfunden.',
)
```
