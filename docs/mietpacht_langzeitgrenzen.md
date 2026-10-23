<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## landpacht_fortsetzungsdauergrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `pachtbeginn_am`: Vertraglicher Beginn des laufenden PachtverhältnissesYYYY-MM-DD zum Tagesbeginn; nicht Beginn nur der zuletzt verlangten Verlängerung.
- `vereinbartes_pachtende_am`: Vertraglich vereinbartes EndeYYYY-MM-DD einschließlich Endtag, nicht vor Beginn.
- `pachtart`: Genau betrieb_oder_kultiviertes_moor_oedland (auch Zupachtung, durch die ein Betrieb entsteht) oder anderes_grundstueck; rechtlich qualifiziert.
- `einordnungsnachweis`: Nichtleerer Nachweis von Pachtart, ursprünglichem Beginn des laufenden Pachtverhältnisses und vertraglicher Dauer. Weitere Fortsetzungsvoraussetzungen595 und gerichtliche Abwägung gesondert.

Zwölf- beziehungsweise Achtzehnjahresgrenze ab Beginn des laufenden Pachtverhältnisses berechnen und vereinbarte Dauer damit vergleichen.

wert: dauergrenze_jahre12oder18, gerichtlicher_hoechstterminYYYY-MM-DD, vereinbarte_dauer_erreicht_grenze als Wahrheitswert.

§595III3/VI:18Jahre für Betriebspacht, betriebsbildende Zupachtung oder vom Pächter kultiviertes Moor-/Ödland, sonst12Jahre. Vereinbarte Dauer mindestens dieser Länge ist eine numerische Ausschlussgrenze nachIII3; keine alleinige Entscheidung über alle Fortsetzungsgründe. Gerichtliche Fortsetzung nachVI höchstens bis zum ausgegebenen Termin, gerechnet ab Beginn des laufenden Pachtverhältnisses, nicht je Verlängerung neu. Weitere Ausschlussgründe, angemessene kürzere Dauer, Teilflächen und Bedingungen extern qualifizieren. Ende einschließlich Endtag; keine193Verschiebung.

Kalenderbereich0001..9999 und ausdrücklich qualifizierte Dauer; keine automatische Feiertagsverschiebung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_595_T0001, BGB_595_T0002, BGB_595_T0003, BGB_595_T0004, BGB_595_T0005, BGB_595_T0006, BGB_595_T0007, BGB_595_T0008, BGB_595_T0009, BGB_595_T0010, BGB_595_T0011, BGB_595_T0012, BGB_595_T0013, BGB_595_T0014, BGB_595_T0015, BGB_595_T0016, BGB_595_T0017, BGB_595_T0018, BGB_595_T0019, BGB_595_T0020, BGB_595_T0021, BGB_595_T0022

```python
from bgbcalc import landpacht_fortsetzungsdauergrenze
landpacht_fortsetzungsdauergrenze(
    pachtbeginn_am='2024-01-01',
    vereinbartes_pachtende_am='2035-12-30',
    pachtart='anderes_grundstueck',
    einordnungsnachweis='§595III3/VI:18Jahre für Betriebspacht, betriebsbildende Zupachtung oder vom Pächter kultiviertes Moor-/Ödland, sonst12Jahre. Vereinbarte Dauer mindestens dieser Länge ist eine numerische Ausschlussgrenze nachIII3; keine alleinige Entscheidung über alle Fortsetzungsgründe. Gerichtliche Fortsetzung nachVI höchstens bis zum ausgegebenen Termin, gerechnet ab Beginn des laufenden Pachtverhältnisses, nicht je Verlängerung neu. Weitere Ausschlussgründe, angemessene kürzere Dauer, Teilflächen und Bedingungen extern qualifizieren. Ende einschließlich Endtag; keine193Verschiebung.',
)
```

## wohnraum_umwandlung_sperrfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `massgeblicher_erwerb_am`: Rechtlich maßgeblicher Tag der Veräußerung beziehungsweise Belastung577aI/IaYYYY-MM-DD. Nicht ungeprüft Datum des Kaufvertrags; maßgeblichen Erwerbsvorgang extern bestimmen.
- `sperrfrist_monate`: Ganze Zahl36..120: gesetzliche Grunddauer36Monate oder tatsächlich einschlägige längere landesrechtliche Dauer bis120Monate. Keine automatische Suche einer örtlichen Rechtsverordnung.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten577a-Falls, maßgeblichen Erwerbsvorgangs und einschlägiger Dauer. Ausnahmen und räumlich/zeitlich geltende Verordnung vorqualifizieren.

Qualifizierte Sperrfrist von36bis120Monaten ab maßgeblichem Erwerb berechnen und ersten Tag nach Fristablauf ausweisen.

wert: sperrfristende und erster_tag_nach_sperrfrist alsYYYY-MM-DD.

§577aI/Ia/II/IIa: nur Ende der qualifizierten Kündigungsbeschränkung. Bei späterer Begründung von Wohnungseigentum nachVeräußerung/BelastungIa läuft die Frist bereits ab dem VorgangIa, nicht erneut ab Umwandlung. Nach Ablauf kann erst diese Sperre entfallen; keine automatische Kündigungsberechtigung, kein Mietende und keine Verkürzung gesetzlicher Kündigungsfristen. Einschlägige verlängerte Dauer ausdrücklich eingeben; nicht pauschal zehn Jahre für sämtliche Orte. Keine193Verschiebung, da Schutzzeitraum.

Kalenderbereich0001..9999 und ausdrücklich qualifizierte Dauer; keine automatische Feiertagsverschiebung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_577a_T0001, BGB_577a_T0002, BGB_577a_T0003, BGB_577a_T0004, BGB_577a_T0005, BGB_577a_T0006, BGB_577a_T0007, BGB_577a_T0008, BGB_577a_T0009

```python
from bgbcalc import wohnraum_umwandlung_sperrfrist
wohnraum_umwandlung_sperrfrist(
    massgeblicher_erwerb_am='2024-02-29',
    sperrfrist_monate=36,
    einordnungsnachweis='§577aI/Ia/II/IIa: nur Ende der qualifizierten Kündigungsbeschränkung. Bei späterer Begründung von Wohnungseigentum nachVeräußerung/BelastungIa läuft die Frist bereits ab dem VorgangIa, nicht erneut ab Umwandlung. Nach Ablauf kann erst diese Sperre entfallen; keine automatische Kündigungsberechtigung, kein Mietende und keine Verkürzung gesetzlicher Kündigungsfristen. Einschlägige verlängerte Dauer ausdrücklich eingeben; nicht pauschal zehn Jahre für sämtliche Orte. Keine193Verschiebung, da Schutzzeitraum.',
)
```
