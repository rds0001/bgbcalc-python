<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mieterbe_vorauszahlungsersparnis

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `vorausgezahlte_abschnittsmiete`: Vom verstorbenen Mieter gezahlte Miete für einen homogen bepreisten Abschnitt als nichtnegativer exakter Eurobetrag.
- `nach_tod_zugeordneter_anteil_zaehler`: Ganzzahliger Zähler0..Nenner des rechtlich dem Zeitraum nach dem Tod zugeordneten Mietanteils; keine automatische Tageseinteilung.
- `nach_tod_zugeordneter_anteil_nenner`: Positiver ganzzahliger Nenner des Anteils, höchstens9007199254740991.
- `einordnungsnachweis`: Nichtleerer Nachweis des Eintritts563 beziehungsweise Fortsetzung563a und dass genau der zugeordnete Anteil dem Empfänger als Ersparnis oder Erlangtes zugutekommt.

Qualifizierte Vorauszahlung mit dem vollständig ersparten/erlangten Mietanteil nach dem Tod multiplizieren.

wert als exakter Eurobruch mit zaehler und nenner.

§563bII: rechnerischer Erstattungsbetrag gegenüber dem Erben für den qualifizierten Fall, dass die vorausbezahlte Miete im angegebenen Anteil den nach dem Tod liegenden Zeitraum betrifft und den eingetretenen/fortsetzenden Personen vollständig zugutekommt. Der Tod beendet das Mietverhältnis hier nicht. Keine automatische Anwendung der547-Rückforderung gegen den Vermieter. Zeitanteil, tatsächliche Ersparnis/Erlangtes und Zahlungszuordnung vorqualifizieren; bei abweichendem Vorteil ist diese Anteilsrechnung nicht ausreichend. Unterschiedlich bepreiste Abschnitte getrennt berechnen, keine pauschalen30Monatstage. Keine automatische Aufteilung unter mehreren Erben oder mehreren Eingetretenen; keine Addition von Ersparnis und Erlangtem für denselben Vorteil.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_563b_T0003

```python
from bgbcalc import mieterbe_vorauszahlungsersparnis
mieterbe_vorauszahlungsersparnis(
    vorausgezahlte_abschnittsmiete='930',
    nach_tod_zugeordneter_anteil_zaehler=15,
    nach_tod_zugeordneter_anteil_nenner=31,
    einordnungsnachweis='§563bII: rechnerischer Erstattungsbetrag gegenüber dem Erben für den qualifizierten Fall, dass die vorausbezahlte Miete im angegebenen Anteil den nach dem Tod liegenden Zeitraum betrifft und den eingetretenen/fortsetzenden Personen vollständig zugutekommt. Der Tod beendet das Mietverhältnis hier nicht. Keine automatische Anwendung der547-Rückforderung gegen den Vermieter. Zeitanteil, tatsächliche Ersparnis/Erlangtes und Zahlungszuordnung vorqualifizieren; bei abweichendem Vorteil ist diese Anteilsrechnung nicht ausreichend. Unterschiedlich bepreiste Abschnitte getrennt berechnen, keine pauschalen30Monatstage. Keine automatische Aufteilung unter mehreren Erben oder mehreren Eingetretenen; keine Addition von Ersparnis und Erlangtem für denselben Vorteil.',
)
```
