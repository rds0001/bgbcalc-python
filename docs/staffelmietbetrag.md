<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## staffelmiete_aufsteigende_betragsgrenzen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `staffeln`: Chronologische Liste2..1000 gültiger, mindestens jahresabständiger und vertraglich nicht sinkender Mietstaffeln. Je genau staffelbeginn_am, vereinbarte_monatsmiete, zulaessige_monatsmiete_ohne_vorstaffelschutz. Letztere an dem nach557aIV maßgeblichen Stichtag rechtlich qualifiziert.
- `einordnungsnachweis`: Nichtleerer Nachweis von vollständiger gültiger Staffelvereinbarung, Anwendung556d–g und zutreffenden individuellen Höchstbeträgen einschließlich Auskunftslage556g. Keine ausgelassenen Vorstaffeln.

Für eine vollständige aufsteigende gültige Staffelfolge individuelle Mietgrenzen und Schutz der zuvor wirksam begründeten Miethöhe fortschreiben.

wert als Liste je Staffel: staffelbeginn_am sowie rechnerische_monatsgrenze, rechnerische_monatsmiete und monatlicher_ueberhoehungsbetrag als exakte Eurobrüche.

§557aIV in Verbindung556gI2: für jede aufsteigende gültige Staffel Höchstbetrag mit der zuvor wirksam begründeten Miethöhe vergleichen; höhere geschützte Vormietstaffel erhalten, vereinbarte Monatsmiete auf diesen Höchstbetrag begrenzen. Nur rechtlich qualifizierte, vollständig geordnete und nicht sinkende Vereinbarungsbeträge; absteigende/neu verhandelte Folgen benötigen gesonderte Bewertung. Anfängliche Überhöhung wird nicht als geschützte Vorstaffelmiete fortgeschrieben. Die Höchstbeträge müssen556d–g einschließlich relevanter Vormiete/Modernisierung/Auskunft und bei Folgestaffeln Zeitpunkt der ersten Fälligkeit bereits korrekt berücksichtigen. Keine automatische10%-Bewertung aus unqualifizierter Vergleichsmiete. Fehlende Jahresabstände führen zu Eingabefehler für diese vorqualifizierte gültige Folge; keine automatische Ersatzvereinbarung. Rückforderung, Rüge, Verjährung, Kündigungsausschluss und Rundung gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_557a_T0006, BGB_557a_T0007, BGB_557a_T0008, BGB_556g_T0001, BGB_556g_T0002, BGB_556g_T0003, BGB_556g_T0004

```python
from bgbcalc import staffelmiete_aufsteigende_betragsgrenzen
staffelmiete_aufsteigende_betragsgrenzen(
    staffeln=[{'staffelbeginn_am': '2024-01-01', 'vereinbarte_monatsmiete': '1000', 'zulaessige_monatsmiete_ohne_vorstaffelschutz': '900'}, {'staffelbeginn_am': '2025-01-01', 'vereinbarte_monatsmiete': '1100', 'zulaessige_monatsmiete_ohne_vorstaffelschutz': '800'}],
    einordnungsnachweis='§557aIV in Verbindung556gI2: für jede aufsteigende gültige Staffel Höchstbetrag mit der zuvor wirksam begründeten Miethöhe vergleichen; höhere geschützte Vormietstaffel erhalten, vereinbarte Monatsmiete auf diesen Höchstbetrag begrenzen. Nur rechtlich qualifizierte, vollständig geordnete und nicht sinkende Vereinbarungsbeträge; absteigende/neu verhandelte Folgen benötigen gesonderte Bewertung. Anfängliche Überhöhung wird nicht als geschützte Vorstaffelmiete fortgeschrieben. Die Höchstbeträge müssen556d–g einschließlich relevanter Vormiete/Modernisierung/Auskunft und bei Folgestaffeln Zeitpunkt der ersten Fälligkeit bereits korrekt berücksichtigen. Keine automatische10%-Bewertung aus unqualifizierter Vergleichsmiete. Fehlende Jahresabstände führen zu Eingabefehler für diese vorqualifizierte gültige Folge; keine automatische Ersatzvereinbarung. Rückforderung, Rüge, Verjährung, Kündigungsausschluss und Rundung gesondert.',
)
```
