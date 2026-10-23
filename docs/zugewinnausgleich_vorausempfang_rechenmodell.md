<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zugewinnausgleich_vorausempfang_rechenmodell

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `ehegatten`: Objekt mit a und b; jeweils vermoegensdifferenz (vorzeichenbehaftet, vor1373Nullbegrenzung), endnettovermoegen (vorzeichenbehaftet), illoyale_hinzurechnung (nichtnegativ). Bewertungen rechtlich vergleichbar.
- `vorausempfaenge`: Liste0..1000: richtung (a_an_b/b_an_a), hinzurechnungswert, herausrechnungswert, anrechnungswert. Dieselbe wirtschaftliche Zuwendung einmal; verschiedene rechtlich qualifizierte Werte dürfen auseinanderfallen.
- `nullbegrenzungsfolge`: Zwingend: zugewinn_vor_korrektur oder vermoegenskorrektur_vor_nullgrenze.
- `haftungsgrenzenfolge`: Zwingend: haftungsgrenze_vor_anrechnung oder haftungsgrenze_nach_anrechnung.
- `methodennachweis`: Rechtsgrund und zulässige Bewertung/Anrechnung jeder Zuwendung, wechselseitige Behandlung sowie Reihenfolge von Nullgrenze und Haftungsgrenze begründen.

Getrennte Richtungsrechnungen mit tatsächlichen Vermögensdifferenzen, bewerteten Vorausempfängen und ausdrücklich vorgegebener Null-/Haftungsgrenzenfolge ausführen.

Beide bedingten Richtungsrechnungen mit Zwischenschritten und vorzeichenbehafteter rechnerischer Differenz; keine automatische Aufrechnung.

Bedingte Erweiterung des vorhandenen einseitigen1380-Grundmodells: je Anspruchsrichtung die zugehörigen Vorausempfänge summieren, Geberbasis um Hinzurechnung erhöhen und Empfängerbasis um Herausrechnung vermindern. Zwingend gewählte Nullbegrenzungsfolge bestimmt, ob ursprüngliche Vermögensdifferenzen schon vor dieser Korrektur bei0begrenzt werden oder erst die korrigierten Differenzen. Positive halbe Differenz berechnen;1378II-Haftungsgrenze=max(Endnettovermögen+illoyaleHinzurechnung,0) selbst berechnen. Haftungsgrenze gemäß gewählter Folge vor oder nach der auf0begrenzten Anrechnung anwenden. Beide Richtungsrechnungen separat ausweisen, einschließlich Gegenrichtung ohne einschlägigen Empfang. Gegenseitige Empfänge werden in diesem ausdrücklich qualifizierten Modell getrennt nach Richtung behandelt; kein unbelegtes automatisches Saldieren der Zuwendungswerte. Rechnerischer Saldo der beiden Ergebnisse ist nur Vergleichswert, keine automatische Aufrechnung oder rechtliche Feststellung zweier Ansprüche. Reihenfolge/reziproke Behandlung/verschiedene Wertansätze rechtlich nicht allgemein bestätigt; keine Standardwahl. Kein negativer Rückforderungsanspruch allein aus überhöhter Anrechnung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1373_T0001, BGB_1378_T0001, BGB_1378_T0002, BGB_1378_T0003, BGB_1378_T0004, BGB_1378_T0005, BGB_1378_T0006, BGB_1378_T0007, BGB_1380_T0001, BGB_1380_T0002, BGB_1380_T0003, BGB_1380_T0004

```python
from bgbcalc import zugewinnausgleich_vorausempfang_rechenmodell
zugewinnausgleich_vorausempfang_rechenmodell(
    ehegatten={'a': {'vermoegensdifferenz': '80', 'endnettovermoegen': '100', 'illoyale_hinzurechnung': '0'}, 'b': {'vermoegensdifferenz': '20', 'endnettovermoegen': '100', 'illoyale_hinzurechnung': '0'}},
    vorausempfaenge=[{'richtung': 'a_an_b', 'hinzurechnungswert': '10', 'herausrechnungswert': '10', 'anrechnungswert': '10'}],
    nullbegrenzungsfolge='zugewinn_vor_korrektur',
    haftungsgrenzenfolge='haftungsgrenze_vor_anrechnung',
    methodennachweis='Bedingte Erweiterung des vorhandenen einseitigen1380-Grundmodells: je Anspruchsrichtung die zugehörigen Vorausempfänge summieren, Geberbasis um Hinzurechnung erhöhen und Empfängerbasis um Herausrechnung vermindern. Zwingend gewählte Nullbegrenzungsfolge bestimmt, ob ursprüngliche Vermögensdifferenzen schon vor dieser Korrektur bei0begrenzt werden oder erst die korrigierten Differenzen. Positive halbe Differenz berechnen;1378II-Haftungsgrenze=max(Endnettovermögen+illoyaleHinzurechnung,0) selbst berechnen. Haftungsgrenze gemäß gewählter Folge vor oder nach der auf0begrenzten Anrechnung anwenden. Beide Richtungsrechnungen separat ausweisen, einschließlich Gegenrichtung ohne einschlägigen Empfang. Gegenseitige Empfänge werden in diesem ausdrücklich qualifizierten Modell getrennt nach Richtung behandelt; kein unbelegtes automatisches Saldieren der Zuwendungswerte. Rechnerischer Saldo der beiden Ergebnisse ist nur Vergleichswert, keine automatische Aufrechnung oder rechtliche Feststellung zweier Ansprüche. Reihenfolge/reziproke Behandlung/verschiedene Wertansätze rechtlich nicht allgemein bestätigt; keine Standardwahl. Kein negativer Rückforderungsanspruch allein aus überhöhter Anrechnung.',
)
```
