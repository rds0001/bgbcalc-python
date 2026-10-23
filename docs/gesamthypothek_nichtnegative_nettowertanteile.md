<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamthypothek_nichtnegative_nettowertanteile

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `zu_verteilender_hypothekenbetrag`: Nichtnegativer gemeinschaftlich zu verteilender Betrag nach1172/1175.
- `grundstuecke`: Liste1..1000: grundstueck_id, grundstueckswert, vorrangige_belastungen; dieselbe Wertgrundlage und vollständige Gemeinschaft.
- `gewichtsmethode`: Zwingend rechtlich qualifiziert: positive_nettowerte. Negative Rohdifferenz ergibt dabei Nullgewicht, keine negative dingliche Zuteilung.
- `verteilungsnachweis`: 1172II/1175-Anwendbarkeit und rechtliche Verwendung nichtnegativer Verwertungsgewichte ausdrücklich qualifizieren; keine abweichende Vereinbarung unterstellen.

Rohnettowerte und nichtnegative qualifizierte Gewichte bestimmen; vorhandenen Quotenkern nur bei positiver Gewichtssumme anwenden.

Rohnettowerte/Gewichte, Bestimmbarkeitsmerkmal und optionale vollständige Quotenverteilung.

Bedingte Nettowertrechnung: ursprünglichen Wert minus qualifizierte vorrangige Belastungen ausweisen; unter ausdrücklich vorgegebener Methode positive_nettowerte Verteilungsgewicht=max(Rohsaldo,0). Bestehenden1172-Quotenkern mit diesen abgeleiteten Gewichten verwenden, Vorrang nicht doppelt abziehen. Bei Gewichtssumme0keine Division/keine künstliche Kopfquote: quoten_bestimmbar=false, anteile=None/NULL; die Rohsalden bleiben ausgewiesen. Gesetzliche Vorschrift liefert für0/0keine feste Ersatzquote. Keine automatische Bewertung der Vorranglast, Verwertung oder rechtliche Freigabe des Nullgewichtsmodells in jedem Streitfall.1174-Regress und1176/1182-Rangschutz gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1172_T0001, BGB_1172_T0002, BGB_1172_T0003, BGB_1175_T0001, BGB_1175_T0002, BGB_1175_T0003

```python
from bgbcalc import gesamthypothek_nichtnegative_nettowertanteile
gesamthypothek_nichtnegative_nettowertanteile(
    zu_verteilender_hypothekenbetrag='100',
    grundstuecke=[{'grundstueck_id': 'A', 'grundstueckswert': '50', 'vorrangige_belastungen': '70'}, {'grundstueck_id': 'B', 'grundstueckswert': '100', 'vorrangige_belastungen': '20'}],
    gewichtsmethode='positive_nettowerte',
    verteilungsnachweis='Bedingte Nettowertrechnung: ursprünglichen Wert minus qualifizierte vorrangige Belastungen ausweisen; unter ausdrücklich vorgegebener Methode positive_nettowerte Verteilungsgewicht=max(Rohsaldo,0). Bestehenden1172-Quotenkern mit diesen abgeleiteten Gewichten verwenden, Vorrang nicht doppelt abziehen. Bei Gewichtssumme0keine Division/keine künstliche Kopfquote: quoten_bestimmbar=false, anteile=None/NULL; die Rohsalden bleiben ausgewiesen. Gesetzliche Vorschrift liefert für0/0keine feste Ersatzquote. Keine automatische Bewertung der Vorranglast, Verwertung oder rechtliche Freigabe des Nullgewichtsmodells in jedem Streitfall.1174-Regress und1176/1182-Rangschutz gesondert.',
)
```
