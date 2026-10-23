<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## schuldverschreibung_zahlungssperre_intervall

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `antrag_zahlungssperre_am`: Tag des rechtlich wirksamen Antrags auf die tatsächlich einschlägige Zahlungssperre; erster normalisierter Hemmungstag.
- `zahlungssperre_vor_verfahrenseinleitung`: Wahrheitswert des802Satz2-Sonderfalls vor Verfahrenseinleitung.
- `sechsmonatsfrist_letzter_tag`: Nur bei Sonderfall: aus Hindernisbeseitigung und206/210/211berechneter letzter Sechsmonatsfristtag. Sonst zwingend None/NULL.
- `einleitungsantrag_am`: Tatsächlich erfolgter rechtlich wirksamer Einleitungsantrag; None/NULL bedeutet bis Beobachtung nicht erfolgt, nicht unbekannt.
- `verfahren_erledigt_am`: Tatsächliche rechtlich maßgebliche Erledigung; None/NULL bedeutet bis Beobachtung nicht erfolgt, nicht bloß unbekannt.
- `beobachtung_bis`: Letzter betrachteter ganzer Tag; ohne feststehendes Ende nur beobachtetes Intervall, kein fiktiver endgültiger Fristablauf.
- `einordnungsnachweis`: 802Anwendbarkeit und wirksame Zahlungssperre, vollständige Antrags-/Erledigungsdaten und auf ganze Tage normalisierte Hemmung qualifizieren.

Tatsächliche Erledigung und gegebenenfalls unwahrte Sechsmonatsfrist vergleichen; frühestes bekanntes Hemmungsende oder ausdrücklich begrenztes Beobachtungsintervall bilden.

Optionales feststehendes Hemmungsende, Abschlussmerkmal und ein auf Beobachtung begrenztes Hemmungsintervall für209-Kern.

802: Beginn mit Zahlungssperrenantrag. Ende mit tatsächlicher Verfahrenserledigung; im qualifizierten Vorverfahren zusätzlich Ablauf der korrigierten Sechsmonatsfrist, sofern bis dahin kein wirksamer Einleitungsantrag gestellt war. Früheres Endereignis maßgeblich. Einleitungsantrag am letzten Fristtag wahrt; späterer Antrag belebt bereits beendete Hemmung nicht rückwirkend wieder. Bei laufender Hemmung nur bis Beobachtung rechnen und Abschluss ausdrücklich verneinen. Keine künstliche Verfahrenserledigung. Hemmung beeinflusst auch Beginn der Vorlegungsfrist; entsprechende Weiterrechnung mit209unter rechtlicher Qualifikation und ohne doppelte Tage. Sechsmonatsgrundfrist/206/210/211werden vorgelagert mit vorhandenen Kernen berechnet. Datumstage sind rechtlich normalisierte eingeschlossene Hemmungstage; untertägige Sonderfälle nicht pauschal runden.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_802_T0001, BGB_802_T0002, BGB_802_T0003

```python
from bgbcalc import schuldverschreibung_zahlungssperre_intervall
schuldverschreibung_zahlungssperre_intervall(
    antrag_zahlungssperre_am='2024-01-01',
    zahlungssperre_vor_verfahrenseinleitung=True,
    sechsmonatsfrist_letzter_tag='2024-07-01',
    einleitungsantrag_am=None,
    verfahren_erledigt_am=None,
    beobachtung_bis='2024-08-01',
    einordnungsnachweis='802: Beginn mit Zahlungssperrenantrag. Ende mit tatsächlicher Verfahrenserledigung; im qualifizierten Vorverfahren zusätzlich Ablauf der korrigierten Sechsmonatsfrist, sofern bis dahin kein wirksamer Einleitungsantrag gestellt war. Früheres Endereignis maßgeblich. Einleitungsantrag am letzten Fristtag wahrt; späterer Antrag belebt bereits beendete Hemmung nicht rückwirkend wieder. Bei laufender Hemmung nur bis Beobachtung rechnen und Abschluss ausdrücklich verneinen. Keine künstliche Verfahrenserledigung. Hemmung beeinflusst auch Beginn der Vorlegungsfrist; entsprechende Weiterrechnung mit209unter rechtlicher Qualifikation und ohne doppelte Tage. Sechsmonatsgrundfrist/206/210/211werden vorgelagert mit vorhandenen Kernen berechnet. Datumstage sind rechtlich normalisierte eingeschlossene Hemmungstage; untertägige Sonderfälle nicht pauschal runden.',
)
```
