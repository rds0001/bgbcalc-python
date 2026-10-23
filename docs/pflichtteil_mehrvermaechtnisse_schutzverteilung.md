<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteil_mehrvermaechtnisse_schutzverteilung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `erwerbswert_vor_vermaechtnissen`: Erwerbswert nach sonstigen einschlägigen Verbindlichkeiten, vor diesen Beschwerungen/Pflichtteilslast.
- `gesamte_pflichtteilslast`: Gesamtlast auf gleicher Wertgrundlage, höchstens Erwerbswert.
- `anderweitig_getragene_last_2323`: Rechtlich nach2320–2322anderweitig getragene Last, höchstens Gesamtlast.
- `vermaechtnisse`: Liste1..1000: beschwerung_id, vermaechtniswert, pflichtteilsschutzwert, rang. Kleinere Rangzahl bedeutet rechtlich vorrangige Beschwerung; Kürzung nachrangiger zuerst.
- `erbenschutz_anwendbar`: Ob2318III-Schutz des Erben rechtlich anwendbar ist.
- `eigener_pflichtteilswert`: Eigener Pflichtteilswert, bei fehlendem Erbenschutz zwingend0; Schutz höchstens vorbestehender Erwerbsrest.
- `konkurrenzmodell`: Zwingend rechtlich begründet: erbe_vorrangig oder bedachte_vorrangig.
- `methodennachweis`: Gemeinsame2318-Lastbasis, Einzelwerte/Schutzrechte,2189-Ränge und konkrete Schutzkonkurrenz rechtlich qualifizieren. Gleicher Rang proportional nach Beschwerungswerten; keine2324-Sondergewichte.

Gemeinsame Pflichtteilskürzung und zusätzlichen Erbenschutz in getrennten Rangstufen unter individuellen Schutzgrenzen verteilen.

Je Beschwerung Kürzung/Rest; rechnerischer Erbenrest und ungedeckter qualifizierter Erbenschutz.

Bedingtes Mehrbeschwerungsmodell2318/2189/2323: anderweitigeLast zuerst abziehen. Grundkürzung je Beschwerung anteiligLast*V_i/Erwerb, höchstens positiver Überschuss über individuellen Schutzwert; gemeinsame Grundkürzung rangweise auf nachrangige Beschwerungen zuerst verteilen, innerhalb eines Rangs wertproportional mit Obergrenzen. Zusätzlichen Erbenschutzbedarf zunächst vollständig aus noch ungeschützten Beschwerungsanteilen decken. Nur bei ausdrücklich qualifiziertem Erbenvorrang darf danach verbleibender Bedarf in geschützte Anteile eingreifen; Bedachtenvorrang lässt diesen Fehlbetrag offen. Keine vorbestehende Unterdeckung auf eigenen Pflichtteil auffüllen: SchutzErbe höchstens Erwerb-SummeV, SchutzBedachter höchstensV_i. Rang-/Schutzhierarchie ist eine zwingende rechtliche Modellvoraussetzung, keine allgemeine Lösung aller Auslegungsstreitigkeiten. Negative rechnerische Erbenreste sind offen ausgewiesene Belastung, kein automatisch neuer Anspruch. Keine automatischeGeldforderung beiSachvermächtnissen, keine doppelte Gesamtlastausübung pro Vermächtnis.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2189_T0001, BGB_2318_T0001, BGB_2318_T0002, BGB_2318_T0003, BGB_2318_T0004, BGB_2323_T0001

```python
from bgbcalc import pflichtteil_mehrvermaechtnisse_schutzverteilung
pflichtteil_mehrvermaechtnisse_schutzverteilung(
    erwerbswert_vor_vermaechtnissen='100',
    gesamte_pflichtteilslast='30',
    anderweitig_getragene_last_2323='0',
    vermaechtnisse=[{'beschwerung_id': 'A', 'vermaechtniswert': '60', 'pflichtteilsschutzwert': '50', 'rang': 1}, {'beschwerung_id': 'B', 'vermaechtniswert': '20', 'pflichtteilsschutzwert': '0', 'rang': 1}],
    erbenschutz_anwendbar=False,
    eigener_pflichtteilswert='0',
    konkurrenzmodell='bedachte_vorrangig',
    methodennachweis='Bedingtes Mehrbeschwerungsmodell2318/2189/2323: anderweitigeLast zuerst abziehen. Grundkürzung je Beschwerung anteiligLast*V_i/Erwerb, höchstens positiver Überschuss über individuellen Schutzwert; gemeinsame Grundkürzung rangweise auf nachrangige Beschwerungen zuerst verteilen, innerhalb eines Rangs wertproportional mit Obergrenzen. Zusätzlichen Erbenschutzbedarf zunächst vollständig aus noch ungeschützten Beschwerungsanteilen decken. Nur bei ausdrücklich qualifiziertem Erbenvorrang darf danach verbleibender Bedarf in geschützte Anteile eingreifen; Bedachtenvorrang lässt diesen Fehlbetrag offen. Keine vorbestehende Unterdeckung auf eigenen Pflichtteil auffüllen: SchutzErbe höchstens Erwerb-SummeV, SchutzBedachter höchstensV_i. Rang-/Schutzhierarchie ist eine zwingende rechtliche Modellvoraussetzung, keine allgemeine Lösung aller Auslegungsstreitigkeiten. Negative rechnerische Erbenreste sind offen ausgewiesene Belastung, kein automatisch neuer Anspruch. Keine automatischeGeldforderung beiSachvermächtnissen, keine doppelte Gesamtlastausübung pro Vermächtnis.',
)
```
