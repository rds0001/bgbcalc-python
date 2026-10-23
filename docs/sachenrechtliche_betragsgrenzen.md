<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## grundbuch_wertersatzgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wertersatz`: Nichtnegativer qualifizierter Wertersatz in EUR nach einschlägigen Versteigerungsvorschriften, vor Anwendung des konkreten Höchstbetrags.
- `eingetragener_hoechstbetrag`: Nichtnegativer wirksam eingetragener Höchstbetrag des Ersatzes in EUR.
- `hoechstbetrag_wirksam_bestimmt`: Expliziter Wahrheitswert des gesetzlichen Anwendungsbereichs§882 und wirksamer Eintragung; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Begründung von Ersatzwert, belastetem Recht, Eintragung und Höchstbetrag.

min(Wertersatz,eingetragener Höchstbetrag).

wert ist exakter gedeckelter EUR-Betrag, sonst null.

Keine Bewertung aus ZVG und kein Erlösverteilungsplan; Höchstbetrag schafft keinen Anspruch in voller Höhe.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_882_T0001, BGB_882_T0002

```python
from bgbcalc import grundbuch_wertersatzgrenze
grundbuch_wertersatzgrenze(
    wertersatz='100',
    eingetragener_hoechstbetrag='80',
    hoechstbetrag_wirksam_bestimmt=True,
    bewertungsnachweis='Qualifizierter Ersatzwert und eingetragener Höchstbetrag.',
)
```

## hoechstbetragshypothek_forderung_und_zinsen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `hauptforderung`: Nichtnegative qualifizierte Hauptforderung in EUR, ohne nochmals enthaltene Zinsen.
- `zinsen`: Nichtnegative gesondert rechtlich bestimmte Zinsen in EUR; Zinssatz und Laufzeit nicht in dieser Summenfunktion berechnet.
- `eingetragener_hoechstbetrag`: Nichtnegativer eingetragener Höchstbetrag in EUR, der Hauptforderung und Zinsen gemeinsam begrenzt.
- `hoechstbetragshypothek_anwendbar`: Expliziter Wahrheitswert zur rechtlichen Anwendbarkeit§1190 auf diese Forderung; FALSE NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung der Forderungs-/Zinsbeträge und wirksamen Höchstbetragshypothek.

Hauptforderung+Zinsen; gemeinsame Summe auf Höchstbetrag begrenzen; Überschuss als Differenz.

wert enthält forderung_mit_zinsen, durch_hoechstbetrag_erfasster_betrag, nicht_vom_hoechstbetrag_erfasster_anteil als exakte EUR-Brüche.

Nur Hauptforderung/Zinsen, sonstige Kosten und Nebenleistungen gesondert. Kein Erlös-/Rangplan, keine automatische Erlöschung übersteigender persönlicher Forderung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1190_T0001, BGB_1190_T0002, BGB_1190_T0003

```python
from bgbcalc import hoechstbetragshypothek_forderung_und_zinsen
hoechstbetragshypothek_forderung_und_zinsen(
    hauptforderung='90',
    zinsen='20',
    eingetragener_hoechstbetrag='100',
    hoechstbetragshypothek_anwendbar=True,
    einordnungsnachweis='Qualifizierte Hauptforderung und gesonderte Zinsen.',
)
```

## pfand_edelmetall_mindestpreis

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `angebotener_preis`: Nichtnegatives Gebot beziehungsweise angebotener Preis des freihändigen Ersatzverkaufs in EUR.
- `gold_oder_silberwert`: Nichtnegativer rechtlich maßgeblicher Gold-/Silberwert des Pfandes in EUR; keine automatische Marktpreis- oder Feingehaltsbewertung.
- `gold_oder_silbersache`: Expliziter Wahrheitswert des qualifizierten Edelmetallpfands im einschlägigen Verkaufsregime§1240; FALSE NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Begründung der Sache, Bewertung und des Verkaufsregimes einschließlich zulässiger Abweichungen.

Angebotener Preis>=Gold-/Silberwert; denselben Mindestwert für Zuschlag und freihändigen Ersatzverkauf anwenden.

wert enthält mindestpreis als EUR-Bruch und mindestpreis_erreicht.

Nur Preisuntergrenze, keine Gesamtzulässigkeit des Verkaufs, kein Preisabschlag bei fehlenden Geboten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1240_T0001, BGB_1240_T0002

```python
from bgbcalc import pfand_edelmetall_mindestpreis
pfand_edelmetall_mindestpreis(
    angebotener_preis='99.99',
    gold_oder_silberwert='100',
    gold_oder_silbersache=True,
    bewertungsnachweis='Qualifizierter Gold-/Silberwert und gesetzliches Verkaufsregime.',
)
```
