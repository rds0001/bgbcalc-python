<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_vererbter_anteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesellschaftsanteil_zaehler`: Nichtnegative ganze Zahl des bisherigen Gesellschaftsanteils, höchstens Nenner und2^53-1.
- `gesellschaftsanteil_nenner`: Positive ganze Bezugsgröße des bisherigen Gesellschaftsanteils, höchstens2^53-1.
- `erbquote_zaehler`: Nichtnegative ganze Zahl der qualifizierten individuellen Erbquote, höchstens Nenner und2^53-1.
- `erbquote_nenner`: Positive ganze Bezugsgröße der Erbquote, höchstens2^53-1.
- `einordnungsnachweis`: Nichtleerer Nachweis der Fortsetzung mit Erben nach711II, des bisherigen Gesellschaftsanteils und der individuellen Erbquote.

Gesellschaftsanteil des Erblassers mit qualifizierter individueller Erbquote multiplizieren.

wert: dimensionsloser exakter Bruch des vererbten Gesellschaftsanteils.

§711II: qualifizierte gesellschaftsvertragliche Fortsetzung mit Erben und maßgebliche Erbquote vorausgesetzt. Bei mehreren Erben fällt jedem ein entsprechender Anteil zu; keine Umdeutung in einen einzigen ungeteilten Erbengemeinschaftsanteil. Für mehrere Einzelaufrufe müssen die verwendeten Erbquoten den Erbfall vollständig und ohne Doppelzählung abbilden. Kein EUR-Wert, keine Vertragsauslegung, kein Abfindungsanspruch und keine Berechnung der Erbquote selbst.

Exakte nichtnegative Anteile/Stimmgewichte beziehungsweise ganze Personenzahlen nach NUMERIK.md; Nenner positiv, Zustimmung höchstens Bezugsgröße. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_711_T0003, BGB_711_T0004, BGB_711_T0005

```python
from bgbcalc import gesellschaft_vererbter_anteil
gesellschaft_vererbter_anteil(
    gesellschaftsanteil_zaehler=1,
    gesellschaftsanteil_nenner=2,
    erbquote_zaehler=1,
    erbquote_nenner=3,
    einordnungsnachweis='Rechtlich qualifizierter Anteil beziehungsweise eindeutiger Stimm-/Personenkreis mit zutreffender Bezugsbasis; keine automatische Beschlusswirksamkeit.',
)
```

## gesellschaft_zustimmungsanzahl

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erforderliche_personenzahl`: Positive ganze Zahl erforderlicher verschiedener Personen im qualifizierten Zustimmungskreis, höchstens2^53-1.
- `zustimmende_personenzahl`: Nichtnegative ganze Zahl bereits wirksam zustimmender verschiedener Personen genau dieses Kreises, höchstens erforderliche Personenzahl.
- `einordnungsnachweis`: Nichtleerer Nachweis des maßgeblichen Personenkreises, gültiger Zustimmungen/Mitwirkung und rechtlicher Einordnung714/715II/720I; keine Doppelzählung.

Zahl noch fehlender Zustimmungen in einem rechtlich qualifizierten vollständigen Personenkreis bestimmen.

wert: fehlende_zustimmungen (ganze Zahl), alle_erforderlichen_zustimmungen_erfasst (Wahrheitswert).

Numerischer Vollständigkeitsvergleich714/715II beziehungsweise gemeinsam erforderlicher Mitwirkung720I. Personenkreis, Stimmberechtigung, Stimmverbote, wirksame Zustimmung/Mitwirkung und abweichender Gesellschaftsvertrag vorqualifizieren. Jede Person nur einmal zählen, Zustimmungen fremder Personen nicht hinzufügen. Bei714 alle Stimmberechtigten, nicht lediglich abgegebene Stimmen als Nenner. Ergebnis begründet allein weder einen wirksamen Beschluss noch eine wirksame Gesamtvertretung; für736V/736dI besondere Beteiligtenkreise nicht ungeprüft übernehmen.

Exakte nichtnegative Anteile/Stimmgewichte beziehungsweise ganze Personenzahlen nach NUMERIK.md; Nenner positiv, Zustimmung höchstens Bezugsgröße. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_714_T0001, BGB_715_T0002, BGB_715_T0003, BGB_720_T0001

```python
from bgbcalc import gesellschaft_zustimmungsanzahl
gesellschaft_zustimmungsanzahl(
    erforderliche_personenzahl=3,
    zustimmende_personenzahl=0,
    einordnungsnachweis='Rechtlich qualifizierter Anteil beziehungsweise eindeutiger Stimm-/Personenkreis mit zutreffender Bezugsbasis; keine automatische Beschlusswirksamkeit.',
)
```

## stimmgewichts_mehrheitsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `regelfall`: gesellschaft_aufloesung_732, gesellschaft_fortsetzung_734 oder gemeinschaft_verwaltung_745.
- `zustimmendes_stimmgewicht`: Nichtnegativer exakter Dezimaltext/Bruch des qualifizierten Zustimmungsgewichts in einheitlicher Stimm-/Anteilseinheit, höchstens Gesamtgewicht.
- `massgebliches_gesamtgewicht`: Strikt positives exaktes Gesamtgewicht. Bei732/734 maßgebliche abgegebene Stimmen; bei745 gesamte maßgebliche Gemeinschaftsanteile einschließlich nicht zustimmender/nicht abgegebener Anteile.
- `einordnungsnachweis`: Nichtleerer Nachweis des gesetzlichen Mehrheitsfalls, der passenden Stimmgewichtung/Nennerbasis und gegebenenfalls gesellschaftsvertraglicher Mehrheitsentscheidung.

Zustimmungsgewicht mit Dreiviertelmehrheit oder strikter Anteilsmehrheit vergleichen.

wert: zustimmungsquote, grenzquote als exakte Brüche, vergleich (mehr_als oder mindestens), mehrheitsgrenze_erreicht.

§732/734II: nur bei gesellschaftsvertraglicher Mehrheitsentscheidung; Nenner sind rechtlich maßgebliche abgegebene Stimmen, Stimmgewicht und Behandlung von Enthaltungen/Ungültigkeit vorqualifizieren. §745I: Mehrheit nach Größe sämtlicher maßgeblicher Gemeinschaftsanteile, nicht bloß nach Kopfzahl oder abgegebenen Stimmen; Nenner umfasst die gesamte Anteilsbasis. Keine automatische Beschlusswirksamkeit, Quorums-, Kompetenz- oder Vertragsprüfung.736V und736dI enthalten keine pauschale Dreiviertelregel und sind hier nicht einbezogen. Gleichheit genügt bei drei Vierteln, nicht bei der Hälfte.

Exakte nichtnegative Anteile/Stimmgewichte beziehungsweise ganze Personenzahlen nach NUMERIK.md; Nenner positiv, Zustimmung höchstens Bezugsgröße. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_732_T0001, BGB_734_T0002, BGB_745_T0001, BGB_745_T0002

```python
from bgbcalc import stimmgewichts_mehrheitsgrenze
stimmgewichts_mehrheitsgrenze(
    regelfall='gesellschaft_aufloesung_732',
    zustimmendes_stimmgewicht='0',
    massgebliches_gesamtgewicht='4',
    einordnungsnachweis='Rechtlich qualifizierter Anteil beziehungsweise eindeutiger Stimm-/Personenkreis mit zutreffender Bezugsbasis; keine automatische Beschlusswirksamkeit.',
)
```
