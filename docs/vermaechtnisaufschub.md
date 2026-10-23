<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vermaechtnis_dreissigjahresgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erbfall_am`: ISO-Datum des Erbfalls als Ereignisbeginn der dreißigjährigen Frist.
- `aufschubgrund`: Genau bedingung (aufschiebend), anfangstermin, zeugung (beim Erbfall noch nicht gezeugter Bedachter) oder persoenlichkeitsbestimmung (erst nach Erbfall bestimmende Tatsache). Je Aufruf ein rechtlich einschlägiger Grund; bei mehreren alle gesondert prüfen.
- `massgebliches_ereignis_am`: Optionales ISO-Datum tatsächlichen Bedingungs-/Termineintritts, Zeugung oder Bestimmungsereignisses je Grund. Bis Prüftag eingetreten; NULL bedeutet noch nicht eingetreten, nicht unbekannt. Bei Zeugung ausdrücklich nicht Geburt eingeben. Ereignis am Endtag gilt noch vor Ablauf um Tagesende. Zeugung/Bestimmung muss zeitlich nach Erbfall liegen; am gleichen Kalendertag Reihenfolge belegen.
- `prueftag`: ISO-Datum mindestens Erbfalltag; Prüfung zum Tagesende.
- `bestimmtes_personenereignis_angeordnet`: Wahrheitswert: Vermächtnis ist für bestimmtes Ereignis in Person gerade des Beschwerten oder Bedachten angeordnet (§2163 Absatz1 Nummer1); keine beliebige dritte Person.
- `ereignisperson_lebt_beim_erbfall`: Wahrheitswert, ob diese Ereignisperson beim Erbfall lebt. Lebenszeit bei späterem Prüftag ist nicht maßgeblich.
- `ereignisperson_juristische_person`: Wahrheitswert, ob Beschwerter/Bedachter, in dessen Person maßgebliches Ereignis eintreten soll, juristische Person ist; dann§2163 Absatz2 Dreißigjahresgrenze. Ohne entsprechende Ereignisperson FALSE, nicht unbekannt.
- `geschwistervermaechtnis_nach_2163`: Wahrheitswert des qualifizierten Sonderfalls Nummer2: Erbe, Nacherbe oder Vermächtnisnehmer für Geburt eines eigenen Bruders/einer eigenen Schwester zugunsten dieses Geschwisters beschwert. Keine beliebige Geschwisterzuwendung.
- `einordnungsnachweis`: Nichtleere rechtliche Begründung des Aufschubgrunds, Ereignisses einschließlich Zeugung versus Geburt sowie Personen-/Geschwisterausnahmen und etwaiger gleichdatierter Ereignisreihenfolge.

Dreißigjahresfrist ab Erbfall berechnen. Ohne maßgebliches Ereignis spätestens am Endtag führt Ablauf zur Unwirksamkeit aus geprüftem Grund, außer qualifizierte Ausnahme§2163. Personenereignis benötigt beim Erbfall lebende Person; juristische Ereignisperson verbleibt in Dreißigjahresgrenze.

wert enthält dreissigjahresfristende, frist_am_prueftag_abgelaufen, massgebliches_ereignis_rechtzeitig, ausnahme_nach_2163 und unwirksam_wegen_geprueften_aufschubgrundes. FALSE ist keine Aussage über Gesamtwirksamkeit.

Ein Aufschubgrund pro Aufruf; mehrere Gründe gesondert prüfen. Keine Gesamtwirksamkeitsprüfung, kein Anfall§§2177/2178 und keine Nacherbfolge§2109. Nach Ablauf eingetretenes Ereignis heilt Unwirksamkeit nicht. Zeugung, nicht Geburt, wahrt Frist bei§2162 Absatz2.

ISO-Daten und berechnete Grenzen0001..9999; explizite Wahrheitswerte, zulässiger Aufschubgrund und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2162_T0001, BGB_2162_T0002, BGB_2163_T0001, BGB_2163_T0002, BGB_2163_T0003, BGB_2163_T0004

```python
from bgbcalc import vermaechtnis_dreissigjahresgrenze
vermaechtnis_dreissigjahresgrenze(
    erbfall_am='2000-02-29',
    aufschubgrund='bedingung',
    massgebliches_ereignis_am=None,
    prueftag='2030-02-28',
    bestimmtes_personenereignis_angeordnet=False,
    ereignisperson_lebt_beim_erbfall=False,
    ereignisperson_juristische_person=False,
    geschwistervermaechtnis_nach_2163=False,
    einordnungsnachweis='Synthetisch qualifizierter einzelner Aufschubgrund, tatsächliches Ereignis und gesetzliche Ausnahmen.',
)
```
