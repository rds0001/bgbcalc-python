<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## modernisierung_haerteeinwand_beginnvergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `mitteilungseingang_utc`: Rechtlich qualifizierter tatsaechlicher Mitteilungszugang als sekundengenauer UTC-Zeitpunkt.
- `massnahmenbeginn_utc`: Tatsaechlicher rechtlich massgeblicher Beginn der Modernisierung als sekundengenauer UTC-Zeitpunkt.
- `einordnungsnachweis`: Anwendbarkeit555dIV2 beziehungsweiseV2 auf wirtschaftliche Haerte qualifizieren. BeiIV unverschuldete Verhinderung und unverzuegliche Mitteilung mit Gruenden, beiV fehlenden Form-/Fristhinweis gesondert feststellen.

Mitteilungszugang mit tatsaechlichem Massnahmenbeginn einschliesslich Grenzzeitpunkt vergleichen.

Ein Zeitgrenzenvergleich, keine vollstaendige Haerteberuecksichtigungsentscheidung.

§555dIV2/V2: wirtschaftliche Haerte spaetestens bis zum Beginn der Modernisierung mitteilen. Zeitvergleich einschliesslich des Beginnzeitpunkts; keine pauschale Frist bis Tagesende, wenn Arbeiten schon morgens beginnen. Ausschliesslich diese zusaetzliche aeusserste Zeitgrenze. Der regulaere Monatsendtermin555dIII wird durch miete_erklaerungs_monatsendtermin berechnet; ordnungsgemaesse Ankuendigung, Hinweis-/Formausnahmen und unverschuldete unverzuegliche Nachholung sind rechtliche Voraussetzungen ohne feste zusaetzliche BGB-Tageszahl. Keine fixe Frist fuer unverzueglich erfinden und keine Uebertragung der wirtschaftlichen Ausschlussgrenze auf jeden Duldungshaertegrund. UTC-Zeitpunkte vorab normalisieren; keine lokalen Zeitzonen raten.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_555d_T0006, BGB_555d_T0007, BGB_555d_T0008, BGB_555d_T0009

```python
from bgbcalc import modernisierung_haerteeinwand_beginnvergleich
modernisierung_haerteeinwand_beginnvergleich(
    mitteilungseingang_utc='2026-05-01T07:59:59Z',
    massnahmenbeginn_utc='2026-05-01T08:00:00Z',
    einordnungsnachweis='§555dIV2/V2: wirtschaftliche Haerte spaetestens bis zum Beginn der Modernisierung mitteilen. Zeitvergleich einschliesslich des Beginnzeitpunkts; keine pauschale Frist bis Tagesende, wenn Arbeiten schon morgens beginnen. Ausschliesslich diese zusaetzliche aeusserste Zeitgrenze. Der regulaere Monatsendtermin555dIII wird durch miete_erklaerungs_monatsendtermin berechnet; ordnungsgemaesse Ankuendigung, Hinweis-/Formausnahmen und unverschuldete unverzuegliche Nachholung sind rechtliche Voraussetzungen ohne feste zusaetzliche BGB-Tageszahl. Keine fixe Frist fuer unverzueglich erfinden und keine Uebertragung der wirtschaftlichen Ausschlussgrenze auf jeden Duldungshaertegrund. UTC-Zeitpunkte vorab normalisieren; keine lokalen Zeitzonen raten.',
)
```
