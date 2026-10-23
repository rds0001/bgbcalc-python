<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## erbschaftskauf_belastungswertminderung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `wert_ohne_belastung`: Nichtnegativer exakter EUR-Vergleichswert des Gegenstands ohne die untersuchte Belastung am rechtlich maßgeblichen Bewertungszeitpunkt.
- `wert_mit_belastung`: Nichtnegativer exakter EUR-Vergleichswert mit derselben Belastung, sonst gleiche Bewertungsannahmen/gleicher Zeitpunkt. Keine ungeprüfte Mischung historischer und aktueller Marktpreise.
- `unentgeltliche_belastung_vor_kauf_qualifiziert`: Expliziter Wahrheitswert: unentgeltliche Belastung des Erbschaftsgegenstands durch Verkäufer vor Abschluss des Erbschaftskaufs nach2375I. FALSE ergibt NICHT_ANWENDBAR.
- `kaeufer_kennt_belastung_beim_kauf`: Expliziter Wahrheitswert rechtlich maßgeblicher Kenntnis des Käufers bei Vertragsschluss; TRUE ergibt Ersatzbetrag null, rechnerische Wertminderung bleibt ausgewiesen.
- `bewertungsnachweis`: Nichtleerer Nachweis der vergleichbaren Werte, Belastung, Kaufzeit und Käuferkenntnis.

Positive Differenz Wert ohne minus Wert mit Belastung; bei Käuferkenntnis bei Kauf Ersatzbetrag null.

wert enthält wertminderung und ersatzbetrag als exakte EUR-Brüche; negative Anwendbarkeit NULL.

Nur unentgeltliche Vorbelastung2375I. Andere Ersatzgründe, Verbrauch/Veräußerung und Erbschaftsschenkung2385II separat. Keine Wertprognose oder pauschale historische Preisänderung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2375_T0001, BGB_2375_T0002

```python
from bgbcalc import erbschaftskauf_belastungswertminderung
erbschaftskauf_belastungswertminderung(
    wert_ohne_belastung='100',
    wert_mit_belastung='70',
    unentgeltliche_belastung_vor_kauf_qualifiziert=True,
    kaeufer_kennt_belastung_beim_kauf=False,
    bewertungsnachweis='Synthetisch vergleichbare Werte gleicher Bewertungszeitpunkt.',
)
```

## erbschaftskauf_verwendungsersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `notwendige_verwendungen_vor_kauf`: Nichtnegative exakte EUR-Summe notwendiger vom Verkäufer vor Kauf auf die Erbschaft gemachter Verwendungen, rechtlich qualifiziert.
- `andere_aufwendungen_vor_kauf`: Nichtnegative exakte EUR-Summe sonstiger Voraufwendungen, überschneidungsfrei zu notwendigen Verwendungen.
- `fortbestehende_wertsteigerung_beim_kauf`: Nichtnegativer exakter EUR-Wert der gerade durch diese anderen Aufwendungen verursachten und beim Verkauf noch vorhandenen Erbschaftswerterhöhung. Nicht gesamte Wertsteigerung aus anderen Ursachen.
- `aufwendungen_nach_2381_qualifiziert`: Expliziter Wahrheitswert des einschlägigen2381-Erstattungsfalls. Keine Nachkaufaufwendungen oder schon anderweitig doppelt erfassten Kosten; FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleerer Nachweis der Kostenabgrenzung, Kaufzeit und fortbestehenden aufwandsbedingten Wertsteigerung.

Notwendige Vorverwendungen voll; andere Aufwendungen auf Wertsteigerung bei Kauf begrenzen; beide Beträge addieren.

wert enthält ersatz_notwendiger_verwendungen, ersatz_anderer_aufwendungen und gesamter_verwendungsersatz als exakte EUR-Brüche.

Keine doppelte Erfassung notwendiger Kosten als andere Aufwendungen. Tilgungen2378 und Lasten/Nutzungen2379/2380 sowie Nachkaufkosten separat; keine erfundene Wertsteigerungsformel.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2381_T0001, BGB_2381_T0002

```python
from bgbcalc import erbschaftskauf_verwendungsersatz
erbschaftskauf_verwendungsersatz(
    notwendige_verwendungen_vor_kauf='20',
    andere_aufwendungen_vor_kauf='80',
    fortbestehende_wertsteigerung_beim_kauf='30',
    aufwendungen_nach_2381_qualifiziert=True,
    bewertungsnachweis='Synthetisch überschneidungsfrei abgegrenzte Voraufwendungen.',
)
```
