<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## kleinbetragsinstrument_betragsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `grenzfall`: einzelzahlung, ausgabenobergrenze, speicherobergrenze oder egeld_sperrausnahme.
- `massgeblicher_betrag`: Nichtnegativer EUR-Betrag: rechtlich vorgesehener Höchstbetrag des einzelnen Vorgangs, Ausgaben-/Speicherobergrenze oder maßgeblicher Instrument-/Kontowert für675iIII. Kein zufällig kleiner Umsatz anstelle einer Instrumentenobergrenze.
- `ausschliesslich_inland`: Nur Ausgaben-/Speicherobergrenze: expliziter Wahrheitswert, ob das Instrument ausschließlich für inländische Vorgänge genutzt werden kann. Sonst null.
- `einordnungsnachweis`: Nichtleerer Nachweis des Grenzfalls und maßgeblichen Betrags; übrige675i-Voraussetzungen separat.

Qualifizierte Instrumentenbeträge mit30,150oder200EUR vergleichen.

wert: betragsgrenze_euro und ueberschreitungsbetrag als EUR-Brüche, grenze_eingehalten als Wahrheitswert.

§675iI: Einzelzahlungslimit höchstens30EUR; Ausgaben-/Speicherobergrenze150EUR, nur bei ausschließlich möglichen inländischen Vorgängen200EUR. Maßgeblich ist die rechtlich vorgesehene Instrumentengrenze, nicht ein zufällig kleiner Einzelumsatz; Speicherbetrag darf die Grenze zu keiner Zeit überschreiten. Drei alternative Instrumentenwege, kein kumulatives Erfordernis aller Grenzen. egeld_sperrausnahme betrifft nur die200EUR-Wertgrenze675iIII; fehlende Sperrmöglichkeit und übrige Voraussetzungen separat. Kein automatischer Ausschluss sämtlicher Zahlungsdienste-Schutzregeln aus einem positiven Zahlenvergleich; Vereinbarungen und spezifische Bedingungen675iII/III prüfen.

Exakte EUR-Dezimaltexte oder Brüche nach NUMERIK.md; Kontostände vorzeichenbehaftet, Betragspositionen nichtnegativ. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675i_T0001, BGB_675i_T0002, BGB_675i_T0003, BGB_675i_T0004, BGB_675i_T0005, BGB_675i_T0006, BGB_675i_T0014, BGB_675i_T0015

```python
from bgbcalc import kleinbetragsinstrument_betragsgrenze
kleinbetragsinstrument_betragsgrenze(
    grenzfall='einzelzahlung',
    massgeblicher_betrag='30',
    ausschliesslich_inland=None,
    einordnungsnachweis='Qualifizierter Normfall mit widerspruchsfreier Betragszuordnung; Voraussetzungen und Einwendungen vorab festgestellt.',
)
```

## zahlung_kontoberichtigung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `regelfall`: nichtautorisiert_675u oder ausfuehrungsfehler_675y; Korrekturanspruch rechtlich festgestellt.
- `aktueller_kontostand`: Exakter EUR-Kontostand einschließlich bisheriger Teilkorrekturen; darf negativ sein.
- `fehlerhafte_belastung`: Nichtnegative ursprüngliche qualifizierte Fehlbelastung in EUR; keine doppelt enthaltenen Zusatzentgelte.
- `bereits_korrigierter_betrag`: Nichtnegative bereits im aktuellen Kontostand enthaltene Korrektur dieser Belastung, höchstens Fehlbelastung.
- `einordnungsnachweis`: Nichtleerer Nachweis der Fehlbelastung, Korrekturberechtigung und bereits enthaltenen Teilkorrekturen; weitere Wertstellungs-/Zinsfolgen separat.

Noch nicht korrigierten Fehlbelastungsbetrag zum aktuellen Kontostand addieren.

wert: noch_zu_korrigierender_betrag (nichtnegativ) und berichtigter_kontostand (vorzeichenbehaftet) als EUR-Brüche.

§675u beziehungsweise675yI/II/IV: isolierte rechnerische Rückgängigmachung der qualifizierten Fehlbelastung. Aktueller Kontostand darf negativ sein und muss bereits_korrigierter_betrag bereits enthalten; andere Kontobewegungen bleiben unberührt. Kein mehrfaches Erstatten derselben Belastung. Anspruchsvoraussetzungen, Haftungsausnahmen und675u-Betrugsverdachtsfall extern klären. Wertstellung, gesonderte Entgelte/Zinsen675yVI und Folgeschäden675z separat; diese Rechnung allein bildet noch keine vollständige rückwirkende Kontorekonstruktion.

Exakte EUR-Dezimaltexte oder Brüche nach NUMERIK.md; Kontostände vorzeichenbehaftet, Betragspositionen nichtnegativ. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675u_T0001, BGB_675u_T0002, BGB_675u_T0003, BGB_675u_T0004, BGB_675u_T0005, BGB_675y_T0001, BGB_675y_T0002, BGB_675y_T0003, BGB_675y_T0004, BGB_675y_T0005, BGB_675y_T0006, BGB_675y_T0007, BGB_675y_T0008, BGB_675y_T0013, BGB_675y_T0014, BGB_675y_T0015, BGB_675y_T0016

```python
from bgbcalc import zahlung_kontoberichtigung
zahlung_kontoberichtigung(
    regelfall='nichtautorisiert_675u',
    aktueller_kontostand='-200',
    fehlerhafte_belastung='100',
    bereits_korrigierter_betrag='20',
    einordnungsnachweis='Qualifizierter Normfall mit widerspruchsfreier Betragszuordnung; Voraussetzungen und Einwendungen vorab festgestellt.',
)
```

## zahlung_sonstiger_schadenbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `begrenzbarer_schaden`: Nichtnegativer EUR-Schaden außerhalb675y, der rechtlich einer wirksamen Haftungsbegrenzung unterliegen darf.
- `nicht_begrenzbarer_schaden`: Nichtnegativer EUR-Anteil außerhalb675y, für den keine Begrenzung gilt, etwa Zinsschaden, Vorsatz/grobe Fahrlässigkeit oder besonders übernommene Gefahr; ohne Überschneidung mit begrenzbarem Anteil.
- `vereinbarte_haftungsgrenze`: Optionaler wirksam vereinbarter EUR-Höchstbetrag mindestens12500; null bedeutet keine Begrenzungsvereinbarung und damit keine automatische Kappung.
- `einordnungsnachweis`: Nichtleerer Nachweis675z, der haftungsrechtlichen Zuordnung, Ausschlüsse und gegebenenfalls wirksamen Vereinbarung.

Qualifizierten sonstigen Zahlungsschaden begrenzen und nicht begrenzbare Anteile ungekürzt addieren.

wert: exakter EUR-Bruch des begrenzten und ungekürzten sonstigen Schadens zusammen.

§675z: nur sonstiger Schaden außerhalb bereits von675y erfasster Ansprüche. Keine Doppelzählung mit Zahlungsbetrag, Entgelten oder Zinsen nach675y. Vereinbarte Grenze optional; null bedeutet keine Begrenzungsvereinbarung, nicht automatisch12500EUR. Vorsatz, grobe Fahrlässigkeit, Zinsschaden und besonders übernommene Gefahren dürfen nicht in den begrenzbaren Anteil eingehen. Bei insgesamt vorsätzlicher/grob fahrlässiger Ausführung gesamten qualifizierten Schaden als nicht begrenzbar zuordnen. Wirksamkeit der Vereinbarung, Haftungszurechnung, fehlerhafte Kundenkennung und Sonderrecht extern bestimmen.

Exakte EUR-Dezimaltexte oder Brüche nach NUMERIK.md; Kontostände vorzeichenbehaftet, Betragspositionen nichtnegativ. Keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675z_T0001, BGB_675z_T0002, BGB_675z_T0003, BGB_675z_T0004, BGB_675z_T0005, BGB_675z_T0006

```python
from bgbcalc import zahlung_sonstiger_schadenbetrag
zahlung_sonstiger_schadenbetrag(
    begrenzbarer_schaden='20000',
    nicht_begrenzbarer_schaden='500',
    vereinbarte_haftungsgrenze='12500',
    einordnungsnachweis='Qualifizierter Normfall mit widerspruchsfreier Betragszuordnung; Voraussetzungen und Einwendungen vorab festgestellt.',
)
```
