<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zahlung_beanstandungsfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `belastung_am`: Tag der nicht autorisierten/fehlerhaften Kontobelastung.
- `ordnungsgemaesse_unterrichtung_am`: Tag der vollstaendigen qualifizierten248EGBGB-Unterrichtung; None/NULL wenn noch nicht erfolgt. Nicht blosse Kenntnis des Nutzers.
- `beanstandung_am`: Tag der tatsaechlichen Unterrichtung des verpflichteten Zahlungsdienstleisters durch den Nutzer.
- `einordnungsnachweis`: 676bII/IVAnwendbarkeit, rechtlich vollstaendige Unterrichtung und richtiger Empfaenger vorqualifizieren. Grundfrist ohne gegebenenfalls erforderliche193-Korrektur.

Spaeteren qualifizierten Belastungs-/Unterrichtungstag bestimmen,13Monatsgrundfrist berechnen und Beanstandung vergleichen; bei fehlender Unterrichtung kein Fristende erfinden.

Optionaler Fristbeginn, Grundfristende und einschliesslicher Zeitvergleich; ohne Unterrichtung alle drei None/NULL.

§676bII/IV:13Monate ab Belastung, bei spaeterer ordnungsgemaesser Unterrichtung erst ab dieser; vollstaendig fehlende Unterrichtung startet keinen fiktiven Fristlauf. Fehlendes Fristende ist keine Behauptung unbegrenzter Anspruchsdauer: allgemeine Verjaehrung und unverzuegliche Meldung676bI bleiben getrennt. Fristende nach187I/188, kein pauschales390Tage-Fenster. Beanstandung vor spaeterer formeller Unterrichtung kann die Ausschlussfrist bereits wahren.676bIII/Vunverschuldete Verhinderung bei dort genannten anderen Anspruechen ist qualitative Ausnahme ohne feste weitere Tageszahl; keine automatische6Monatsverlaengerung oder erfundenes Nachfristende.676cHaftungsausschluesse sind qualitative Tatbestaende ohne zusaetzliche feste Rechenregel.193gegebenenfalls mit bestehendem Kern nach rechtlicher Qualifikation, keine automatische Verschiebung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_676b_T0001, BGB_676b_T0002, BGB_676b_T0003, BGB_676b_T0004, BGB_676b_T0005, BGB_676b_T0006, BGB_676b_T0007, BGB_676b_T0008, BGB_676b_T0009, BGB_676c_T0001, BGB_676c_T0002, BGB_676c_T0003

```python
from bgbcalc import zahlung_beanstandungsfrist
zahlung_beanstandungsfrist(
    belastung_am='2024-01-31',
    ordnungsgemaesse_unterrichtung_am='2024-01-31',
    beanstandung_am='2025-02-28',
    einordnungsnachweis='§676bII/IV:13Monate ab Belastung, bei spaeterer ordnungsgemaesser Unterrichtung erst ab dieser; vollstaendig fehlende Unterrichtung startet keinen fiktiven Fristlauf. Fehlendes Fristende ist keine Behauptung unbegrenzter Anspruchsdauer: allgemeine Verjaehrung und unverzuegliche Meldung676bI bleiben getrennt. Fristende nach187I/188, kein pauschales390Tage-Fenster. Beanstandung vor spaeterer formeller Unterrichtung kann die Ausschlussfrist bereits wahren.676bIII/Vunverschuldete Verhinderung bei dort genannten anderen Anspruechen ist qualitative Ausnahme ohne feste weitere Tageszahl; keine automatische6Monatsverlaengerung oder erfundenes Nachfristende.676cHaftungsausschluesse sind qualitative Tatbestaende ohne zusaetzliche feste Rechenregel.193gegebenenfalls mit bestehendem Kern nach rechtlicher Qualifikation, keine automatische Verschiebung.',
)
```
