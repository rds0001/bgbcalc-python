<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_zinserweiterungsrahmen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisheriger_zinssatz`: Nichtnegativer exakter Prozentwert als Dezimalzeichenfolge/Bruchobjekt:5 bedeutet5Prozent; unverzinslich0.
- `vorgesehener_zinssatz`: Nichtnegativer exakter neuer Prozentwert derselben Forderung;5 bedeutet5Prozent.
- `einordnungsnachweis`: Nichtleere rechtliche Begründung der hypothekarisch gesicherten Forderung und Zinssätze; Änderungswirksamkeit separat.

Spielraum=max(5-bisheriger Zinssatz,0) Prozentpunkte; echte Erhöhung liegt bei bisher<neu<=5.

wert enthält erweiterungsspielraum_prozentpunkte als exakten Bruch, zinssatz_wird_erhoeht und erhoehung_innerhalb_fuenfprozentrahmen.

Nur numerischer zustimmungsfreier Erweiterungsrahmen1119I, keine gesamte Änderungswirksamkeit. Keine Gleichsetzung mit gesetzlichem Zinssatz.

Kalenderdaten/Ergebnisse0001..9999; Prozentwerte nichtnegative Dezimalzeichenfolge/exaktes Bruchobjekt, sichere Zwischenwerte höchstens2^53-1; Nachweis nichtleer.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1119_T0001

```python
from bgbcalc import hypothek_zinserweiterungsrahmen
hypothek_zinserweiterungsrahmen(
    bisheriger_zinssatz='0',
    vorgesehener_zinssatz='5',
    einordnungsnachweis='Qualifizierte Forderungszinssätze in Prozent.',
)
```

## verjaehrung_vereinbarungsobergrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesetzlicher_verjaehrungsbeginn`: Rechtlich maßgebliches ISO-Datum des gesetzlichen Verjährungsbeginns, nicht Vertragsabschluss oder vereinbart verschobener Beginn.
- `vereinbartes_fristende`: ISO-Datum des vereinbarten letzten Fristtags einschließlich, nicht vor angegebenem Beginn.
- `beginnart`: ereignis oder tagesbeginn nach rechtlicher Bestimmung des gesetzlichen Beginns. Bei Jahresschluss das Schlussdatum mit ereignis eingeben.
- `einordnungsnachweis`: Nichtleere Begründung des gesetzlichen Beginns/Beginnart und der zu prüfenden Verjährungsvereinbarung.

Gesetzlicher Beginn+30 Jahre; vereinbartes Ende höchstens diese Grenze.

wert enthält dreissigjahres_vereinbarungsgrenze und vereinbartes_ende_innerhalb_grenze.

Nur quantitative Obergrenze202II; Vorsatzverbot202I/andere Unwirksamkeit separat. Keine automatische Heilung/Kürzung einer unzulässigen Vereinbarung; kein vollständiger Verjährungsablauf.

Kalenderdaten/Ergebnisse0001..9999; Prozentwerte nichtnegative Dezimalzeichenfolge/exaktes Bruchobjekt, sichere Zwischenwerte höchstens2^53-1; Nachweis nichtleer.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_202_T0001, BGB_202_T0002

```python
from bgbcalc import verjaehrung_vereinbarungsobergrenze
verjaehrung_vereinbarungsobergrenze(
    gesetzlicher_verjaehrungsbeginn='2028-02-29',
    vereinbartes_fristende='2058-02-28',
    beginnart='ereignis',
    einordnungsnachweis='Qualifizierter gesetzlicher Beginn und vorgeschlagenes Ende.',
)
```
