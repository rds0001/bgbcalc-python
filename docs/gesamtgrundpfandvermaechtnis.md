<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamtgrundpfandvermaechtnis_fremdgrundstueck

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtbelastungsbetrag`: Nichtnegativer exakter, rechtlich bestimmter vergleichbarer EUR-Befriedigungsbetrag der Gesamtbelastung; keine ungeprüfte Kapitalisierung laufender Renten.
- `grundpfandart`: gesamtgrundschuld oder gesamtrentenschuld.
- `wert_vermachtes_grundstueck`: Nichtnegativer exakter EUR-Wert des vermachten Nachlassgrundstücks zum Eigentumsübergang.
- `vorrangige_lasten_vermachtes_grundstueck`: Nichtnegative exakte EUR-Belastungen, die der Gesamtbelastung am vermachten Grundstück im Rang vorgehen; betrachtete Gesamtbelastung nicht nochmals abziehen.
- `wert_fremdgrundstueck`: Nichtnegativer exakter vergleichbarer EUR-Wert des einzigen weiteren Grundstücks, das nicht zum Nachlass gehört, zum maßgeblichen Eigentumsübergang. Kompatibilitätsparameter: validiert,aber keinEinfluss auf2168II-Nachlassvergleichsquote.
- `vorrangige_lasten_fremdgrundstueck`: Nichtnegative exakte rangvorrangige EUR-Belastungen am Fremdgrundstück. Kompatibilitätsparameter: validiert,aber keinEinfluss auf2168II-Nachlassvergleichsquote.
- `erblasserpflicht_gegenueber_fremdeigentuemer`: Expliziter Wahrheitswert: Erblasser war im Erbfall gegenüber Eigentümer des Fremdgrundstücks oder dessen Rechtsvorgänger zur Befriedigung des Gläubigers verpflichtet. Bloße dingliche Mithaftung reicht nicht.
- `zweifelsregel_anwendbar`: Expliziter Wahrheitswert zur einschlägigen Zweifelsregel ohne abweichenden Erblasserwillen.
- `genau_zwei_grundstuecke_qualifiziert`: Expliziter Wahrheitswert: genau ein vermachtes Nachlassgrundstück und genau ein weiteres fremdes Grundstück mit identischer Gesamtbelastung; weitere Grundstücke außerhalb dieses Modells.
- `bewertungsnachweis`: Nichtleerer Nachweis zur Verpflichtung im Erbfall, Grundstückszuordnung, Werte-/Ranglastenlage beim Eigentumsübergang und vergleichbarer Geldbetragsbasis.

BereinigterEigenwert=max(Eigenwert−Vorrang,0); hier einzigesNachlassgrundstück, deshalbBefriedigung=min(Gesamtbetrag,bereinigterEigenwert).2167-Vergleichsgruppe umfasst nurNachlassgrundstücke,keineFremdwerte.

wert enthält bereinigter_wert_vermachtes_grundstueck, bereinigter_gesamtwert, wertquote, anteil_vor_wertbegrenzung und befriedigungsbetrag; negative Anwendbarkeit NULL. bereinigter_gesamtwert bezeichnet ausschließlichNachlasswertsumme, hierEigenwert; fremdeGrundstücke sind keineVergleichsmasse.

Nur2168Absatz2 mit genau einem vermachtenNachlassgrundstück und einem fremdenGrundstück. Erblasserpflicht imErbfall gegenüberFremdeigentümer/Rechtsvorgänger qualifizieren.2167 bezieht nurNachlassgrundstücke in Vergleichsgruppe ein: Fremdwerte mindern diese interneLast nicht. Hier einzigesNachlassgrundstück, deshalb Befriedigung=min(Gesamtbetrag,bereinigterEigenwert). bereinigter_gesamtwert ist alleinWertsumme derNachlassgrundstücke; wertquote beiEigenwertpositiv1,bei0NULL. Fremdwert-/Ranglastenparameter werden ausKompatibilitätsgründen validiert,aber nichtquotenbildend verwendet. Kein2166II-Drittleistungsabzug, keineAußenhaftungsbegrenzung, Rentenkapitalisierung oderFälligkeitsentscheidung. WeitereNachlassgrundstücke benötigen gesonderte2167-Quote.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2168_T0003, BGB_2166_T0001, BGB_2166_T0002, BGB_2167_T0001, BGB_2167_T0002

```python
from bgbcalc import gesamtgrundpfandvermaechtnis_fremdgrundstueck
gesamtgrundpfandvermaechtnis_fremdgrundstueck(
    gesamtbelastungsbetrag='800',
    grundpfandart='gesamtgrundschuld',
    wert_vermachtes_grundstueck='100',
    vorrangige_lasten_vermachtes_grundstueck='0',
    wert_fremdgrundstueck='300',
    vorrangige_lasten_fremdgrundstueck='0',
    erblasserpflicht_gegenueber_fremdeigentuemer=True,
    zweifelsregel_anwendbar=True,
    genau_zwei_grundstuecke_qualifiziert=True,
    bewertungsnachweis='Synthetische Erblasserpflicht im Erbfall gegenüber Fremdeigentümer und vergleichbare Werte.',
)
```

## gesamtgrundpfandvermaechtnis_nachlassanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtbelastungsbetrag`: Nichtnegativer exakter EUR-Bezugsbetrag der betrachteten Gesamtgrund-/Gesamtrentenschuld. Bei Rente rechtlich qualifizierter einheitlicher Zeitraum; keine automatische Kapitalisierung/Wahl der Ablösungssumme. Dieser Betrag wird proportional zugeordnet, nicht mit einer persönlichen Schuld verwechselt.
- `grundpfandart`: gesamtgrundschuld oder gesamtrentenschuld; keine Hypothek.
- `grundstuecke`: Vollständige Liste2..1000 mithaftender Grundstücke, je genau grundstueck_id (eindeutiger Text), grundstueckswert und vorrangige_belastungen (nichtnegative exakte EUR-Werte). Werte zum Eigentumsübergang auf Vermächtnisnehmer. Nur rangvorrangige Lasten, nicht die betrachtete Gesamtbelastung. Negative Wertdeckung wird null; Gesamtdeckung muss positiv sein.
- `vermachtes_grundstueck_id`: Nichtleere Kennung des einen vermachten Grundstücks in der vollständigen Liste.
- `ausschliesslich_nachlassgrundstuecke`: Expliziter Wahrheitswert: sämtliche mithaftenden Grundstücke gehören zum Nachlass. FALSE führt zu NICHT_ANWENDBAR, Absatz2 separat.
- `zweifelsregel_anwendbar`: Expliziter Wahrheitswert: keine abweichende maßgebliche Anordnung des Erblassers; rechtlich einschlägige Zweifelsregel.
- `bewertungsnachweis`: Nichtleerer Nachweis zu Eigentumsübergangszeitpunkt, Werten, Ranglasten, Grundpfandart und einheitlichem Betragsbezug.

Nichtnegative bereinigte Grundstückswerte bilden; Wertquote des vermachten Grundstücks an Summe bestimmen; Gesamtbelastung mit dieser Quote multiplizieren.

wert enthält bereinigter_wert_vermachtes_grundstueck, bereinigter_gesamtwert, wertquote und zugeordneter_belastungsteil als exakte Brüche; negative Anwendbarkeit NULL.

§2168I verweist allein auf Wertbestimmung§2166I2. Kein zusätzlicher Grundstückswert-/persönlicher Schulddeckel, kein Drittleistungsabzug2166II. Kein Fremdgrundstücksfall oder dingliches Außenhaftungslimit.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2168_T0001, BGB_2168_T0002, BGB_2166_T0002

```python
from bgbcalc import gesamtgrundpfandvermaechtnis_nachlassanteil
gesamtgrundpfandvermaechtnis_nachlassanteil(
    gesamtbelastungsbetrag='800',
    grundpfandart='gesamtgrundschuld',
    grundstuecke=[{'grundstueck_id': 'A', 'grundstueckswert': '100', 'vorrangige_belastungen': '0'}, {'grundstueck_id': 'B', 'grundstueckswert': '300', 'vorrangige_belastungen': '0'}],
    vermachtes_grundstueck_id='A',
    ausschliesslich_nachlassgrundstuecke=True,
    zweifelsregel_anwendbar=True,
    bewertungsnachweis='Synthetische vergleichbare Werte bei Eigentumsübergang; Ranglasten geprüft.',
)
```
