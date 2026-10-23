<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## bienenschwarm_eigentumsquoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `eigentuemer_schwaerme`: Unbenannte Liste mit2..1000 Einträgen, jeweils genau eigentuemer_id (nichtleere eindeutige Zeichenfolge) und verfolgte_schwaerme (positive ganze Zahl bis2^53-1). Auch Gesamtsumme höchstens2^53-1. Pro Eigentümer zusammenfassen. Nur ausgezogene, vereinigte, eigentumserhaltend nach§961 verfolgte Schwärme zählen; keine Bienenzahlen, Gewichte oder Werte. Einzelberechtigter und vorbestehendes Miteigentum eines Schwarms außerhalb dieses Modells.
- `ausgezogene_schwaerme_vereinigt`: Wahrheitswert der Vereinigung der ausgezogenen Schwärme der erfassten berechtigten Eigentümer. Bloß benachbarte getrennte Schwärme erfüllen den Tatbestand nicht.
- `gesamtschwarm_eingefangen`: Wahrheitswert, dass der vereinigte Gesamtschwarm eingefangen ist. Vorheriges bloßes Verfolgen allein nicht mit abgeschlossenem Erwerb gleichsetzen.
- `einzug_in_fremde_besetzte_wohnung`: Wahrheitswert des Sonderfalls§964 einer fremden bereits besetzten Bienenwohnung. TRUE ergibt hier NICHT_ANWENDBAR; dessen andere Eigentumsfolge nicht als§963-Quote berechnen.
- `einordnungsnachweis`: Nichtleere Begründung von Eigentümerzuordnung, eigentumserhaltender Verfolgung, Anzahl jedes Schwarms, Vereinigung/Einfangen und Abgrenzung§964.

Bei vereinigtem eingefangenem Gesamtschwarm außerhalb§964: verfolgte Schwarmzahl jedes berechtigten Eigentümers durch Gesamtzahl teilen.

wert ist Liste in Eingabereihenfolge mit eigentuemer_id und eigentumsquote als exaktem dimensionslosem Bruch; Summe1. Ohne Tatbestand NICHT_ANWENDBAR/null.

Keine Wert-/Bienenzahlgewichtung. Eigentumsverlust durch fehlende/aufgegebene Verfolgung§961 vorab einordnen; keine komplette Eigentumskette. Einzelberechtigter und Miteigentum einzelner Schwärme nicht in diesem Modell.

Nichtleere Personenkennungen, explizite Wahrheitswerte und Nachweis; bei Schwärmen2..1000 Eigentümer, positive ganze Schwarmzahlen und Gesamtsumme höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_961_T0001, BGB_963_T0001, BGB_964_T0001, BGB_964_T0002

```python
from bgbcalc import bienenschwarm_eigentumsquoten
bienenschwarm_eigentumsquoten(
    eigentuemer_schwaerme=[{'eigentuemer_id': 'A', 'verfolgte_schwaerme': 2}, {'eigentuemer_id': 'B', 'verfolgte_schwaerme': 1}],
    ausgezogene_schwaerme_vereinigt=True,
    gesamtschwarm_eingefangen=True,
    einzug_in_fremde_besetzte_wohnung=False,
    einordnungsnachweis='Synthetisch verschiedene Eigentümer mit rechtzeitig fortgeführter Verfolgung ihrer vereinigten Schwärme.',
)
```

## schatzfund_eigentumsquoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `entdecker_id`: Nichtleere Zeichenfolge des einen rechtlich bestimmten Entdeckers. Mehrere Entdecker oder dienst-/auftragsbezogene Zuordnungsfragen gesondert lösen; keine beliebige erste meldende Person einsetzen.
- `eigentuemer_verbergende_sache_id`: Nichtleere Zeichenfolge des einen Alleineigentümers der Sache, in der Schatz verborgen war. Nicht bloßer Besitzer oder Grundstücksnachbar. Bei Identität mit Entdecker werden beide Hälften zu1 vereinigt; Miteigentum der verbergenden Sache außerhalb dieses Modells.
- `qualifizierter_schatz`: Wahrheitswert, dass Sache so lange verborgen lag, dass ihr Eigentümer nicht mehr zu ermitteln ist. Unbekannter Eigentümer eines gewöhnlichen Funds allein genügt nicht.
- `entdeckt_und_infolge_entdeckung_besitzgenommen`: Wahrheitswert, dass Entdeckung und infolgedessen Besitzergreifung eingetreten sind. Bloße Vermutung eines Schatzes oder Meldung ohne Besitzergreifung nicht gleichsetzen.
- `abweichendes_landesrecht`: Wahrheitswert, dass am konkreten Fundort abweichende landesrechtliche Erwerbsregel, insbesondere Schatzregal, einschlägig ist. Dann NICHT_ANWENDBAR; FALSE nur nach rechtlicher Orts-/Sachprüfung, keine automatische Annahme für archäologische Funde.
- `einordnungsnachweis`: Nichtleere Begründung von Schatzcharakter, Entdeckung/Besitzergreifung, Personen-/Eigentümerzuordnung und Prüfung abweichenden Rechts am Fundort.

Im anwendbaren BGB-Schatzfundfall je Hälfte Entdecker und Eigentümer verbergender Sache; identische Person erhält beide Hälften zusammen.

wert ist Liste mit eigentuemer_id/eigentumsquote; unterschiedliche Personen je1/2, identische Person einmal1. Ohne Tatbestand oder bei abweichendem Landesrecht NICHT_ANWENDBAR/null.

Nur ein Entdecker/ein Alleineigentümer. Landesrechtliche Schatzregale oder besondere Zuordnung können ausschließen; keine automatische Prüfung externer Rechtsquellen. Quoten begründen keinen Finderlohn oder Geldanspruch.

Nichtleere Personenkennungen, explizite Wahrheitswerte und Nachweis; bei Schwärmen2..1000 Eigentümer, positive ganze Schwarmzahlen und Gesamtsumme höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_984_T0001

```python
from bgbcalc import schatzfund_eigentumsquoten
schatzfund_eigentumsquoten(
    entdecker_id='A',
    eigentuemer_verbergende_sache_id='A',
    qualifizierter_schatz=True,
    entdeckt_und_infolge_entdeckung_besitzgenommen=True,
    abweichendes_landesrecht=False,
    einordnungsnachweis='Synthetisch geprüfter BGB-Schatzfund ohne abweichendes Landesrecht, ein Entdecker und ein Alleineigentümer.',
)
```
