<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## inventarfrist_grundrahmen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zustellung_fristbeschluss_am`: ISO-Datum0001..9999 der wirksamen Zustellung des fristbestimmenden Beschlusses, nicht bloß Beschlussdatum.
- `annahme_erbschaft_am`: ISO-Datum der wirksamen Erbschaftsannahme; tatsächliche oder rechtlich zugerechnete Annahme qualifizieren. Nicht pauschal Erbfalltag. Nur Fall bereits feststehender Annahme.
- `bestimmtes_grundfristende`: ISO-Datum der gerichtlichen erstmaligen Grundfristgrenze, vergleichbar vor gesonderten Hemmungs-/Ablaufhemmungs- und Kalenderkorrekturen. Frühestens späterer Tag von Zustellung/Annahme.
- `erstmalige_inventarfrist`: Wahrheitswert: erstmalige Grundfristbestimmung, keine gerichtliche Verlängerung oder anderweitige Sonderfrist. FALSE ergibt NICHT_ANWENDBAR für diesen Sollrahmenvergleich.
- `einordnungsnachweis`: Nichtleere Begründung von Zustellung, wirksamer Annahme und Charakter der bestimmten Grundfrist.

Späteres Ereignis von Zustellung und Annahme als Beginn; ein und drei Monate berechnen und gerichtliches Grundende auf Einschluss in Sollrahmen prüfen.

wert enthält fristbeginnereignis_am, einmonatsgrenze, dreimonatsgrenze und bestimmtes_ende_im_sollrahmen. Außerhalb Erstbestimmung NICHT_ANWENDBAR/null.

Sollrahmen ist kein pauschales Wirksamkeitsurteil. Gerichtliche Verlängerung nicht auf drei Monate kappen. Ablaufhemmung§1997/210, Ehegatten§2008 und Kalenderkorrekturen separat.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1995_T0001, BGB_1995_T0002, BGB_1995_T0003, BGB_1995_T0004, BGB_1997_T0001

```python
from bgbcalc import inventarfrist_grundrahmen
inventarfrist_grundrahmen(
    zustellung_fristbeschluss_am='2030-01-31',
    annahme_erbschaft_am='2030-01-01',
    bestimmtes_grundfristende='2030-01-31',
    erstmalige_inventarfrist=True,
    einordnungsnachweis='Synthetisch erstmalige Grundfrist ohne Korrekturen; Zustellung und Annahme rechtlich bestimmt.',
)
```

## inventarfrist_neubestimmungsantrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `hindernis_beseitigt_am`: ISO-Datum0001..9999 der rechtlich maßgeblichen Beseitigung des unverschuldeten Hindernisses.
- `ende_zuerst_bestimmter_inventarfrist`: ISO-Datum des Endes der zuerst bestimmten Inventarfrist als Bezugsereignis der Jahresgrenze; nicht durch späteren Antrag beliebig erneuern.
- `massgebliches_zweiwochenfristende`: ISO-Datum des rechtlich maßgeblichen Zweiwochenendes einschließlich zulässiger Korrekturen und entsprechender Anwendung§210 über§1997. Mindestens berechnete Zweiwochengrundfrist; Verlängerung belegen.
- `massgebliche_jahreshoechstgrenze`: ISO-Datum der gesondert bestimmten Jahresgrenze einschließlich ausschließlich rechtlich zulässiger Kalenderkorrekturen. Mindestens rechnerische Jahresgrundgrenze. Verweisung§1997 auf§210 betrifft nicht diese Jahresgrenze; keine frei wählbare Verlängerung.
- `antrag_massgeblich_gestellt_am`: ISO-Datum des rechtlich maßgeblichen Antrags, nicht bloß Versand. In diesem Modell frühestens Hindernisbeseitigung.
- `unverschuldete_verhinderung`: Wahrheitswert: ohne Verschulden an rechtzeitiger Inventarerrichtung, gerechtfertigtem Verlängerungsantrag oder Einhaltung der Zweiwochenfrist verhindert (§1996 Absatz1). Keine automatische Verschuldensbewertung.
- `einordnungsnachweis`: Nichtleere Begründung von Hindernis/Beseitigung, zuerst bestimmter Frist, beiden korrigierten Grenzen und rechtlichem Antragstag.

Zwei Wochen nach Hindernisbeseitigung und ein Jahr nach Ende zuerst bestimmter Inventarfrist berechnen; qualifizierte Enden durch Minimum verbinden. Antrag bis Ende und unverschuldete Verhinderung getrennt prüfen.

wert enthält rechnerisches_zweiwochenfristende, jahreshoechstgrenze (rechnerisch), massgeblicher_letzter_antragstag sowie antragsfrist_eingehalten/verhinderung_und_frist_erfuellt. FALSE ist negatives Prüfergebnis, Status BERECHNET.

Keine automatische gerichtliche Neubestimmung; Anhörung Absatz3 gesondert. §210-Verweisung über§1997 betrifft Zweiwochenfrist, nicht Jahresgrenze. Keine freie Fristverlängerung oder Erneuerung durch weitere Anträge.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1996_T0001, BGB_1996_T0002, BGB_1996_T0003, BGB_1997_T0001

```python
from bgbcalc import inventarfrist_neubestimmungsantrag
inventarfrist_neubestimmungsantrag(
    hindernis_beseitigt_am='2030-12-20',
    ende_zuerst_bestimmter_inventarfrist='2030-01-01',
    massgebliches_zweiwochenfristende='2031-01-03',
    massgebliche_jahreshoechstgrenze='2031-01-01',
    antrag_massgeblich_gestellt_am='2030-12-20',
    unverschuldete_verhinderung=False,
    einordnungsnachweis='Synthetisch Ende zuerst bestimmter Frist und Hindernis qualifiziert; keine Korrekturen.',
)
```
