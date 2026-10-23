<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zahlungsauftrag_zugangstage

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugang_am`: Tatsächlicher qualifizierter Zugangstag beim Zahlungsdienstleister des Zahlers als ISO-Datum.
- `nach_annahmeschluss`: Expliziter Wahrheitswert: Zugang nach wirksam festgelegtem Annahmeschluss an einem Geschäftstag. Bei Terminauftrag FALSE.
- `vereinbarter_ausfuehrungstag_am`: Optionales qualifiziertes ISO-Ausführungsdatum nach675nII, nicht vor tatsächlichem Zugang; sonst null.
- `bankkalender`: Objekt mit genau erster_kalendertag, letzter_kalendertag (ISO-Daten) und geschaeftstage (unbenannte Liste1..10000 streng aufsteigender eindeutiger ISO-Daten innerhalb des Intervalls). Vollständiger Geschäftskalender des maßgeblichen Dienstleisters für den konkreten Zahlungsvorgang im angegebenen Intervall; keine Wochenendannahme. Die erforderlichen Vor-/Folgetage müssen enthalten sein.
- `kalendernachweis`: Nichtleerer Nachweis des Normfalls, tatsächlichen vollständigen Geschäftskalenders und der taggenau normalisierten Zugangs-/Terminbedingungen; Uhrzeiten, Annahmeschluss und Zeitzone extern qualifizieren.

Wirksamkeitszugang und für die Ausführungsfrist maßgeblichen Zugangstag getrennt bestimmen.

wert: wirksamkeitszugangstag und zugangstag_fuer_ausfuehrungsfrist als ISO-Daten; Annahmeschluss verschiebt nur letzteren.

§675n: Geschäftskalender des Zahlungsdienstleisters des Zahlers für den konkreten Vorgang vollständig im angegebenen Intervall vorgeben. Keine pauschale Werktags-/Feiertagskonvention. nach_annahmeschluss bedeutet nach einem wirksam festgelegten Zeitpunkt nahe Geschäftstagsende, nicht bloß außerhalb beliebiger Öffnungszeiten. Diese Verschiebung gilt nur für675sI, nicht pauschal für sämtliche Wirkungen des Zugangs. Bei vereinbartem Termin675nII diesen maßgeblichen Tag angeben, nach_annahmeschlussFALSE; tatsächlicher Zugang bleibt getrennt. Uhrzeiten, Zeitzonen und Intraday-Reihenfolge extern qualifizieren.

ISO-Kalenderdaten0001..9999; Geschäftstagsliste1..10000 mit ausdrücklichem Abdeckungsintervall. Fehlende Kalenderabdeckung ist ungültig, keine Extrapolation.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675n_T0001, BGB_675n_T0002, BGB_675n_T0003, BGB_675n_T0004, BGB_675n_T0005, BGB_675n_T0006

```python
from bgbcalc import zahlungsauftrag_zugangstage
zahlungsauftrag_zugangstage(
    zugang_am='2024-03-28',
    nach_annahmeschluss=False,
    vereinbarter_ausfuehrungstag_am=None,
    bankkalender={'erster_kalendertag': '2024-03-25', 'letzter_kalendertag': '2024-04-15', 'geschaeftstage': ['2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08', '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15']},
    kalendernachweis='Expliziter synthetischer Geschäftskalender, vollständig im Intervall; qualifizierter Normfall, keine Behauptung eines universellen Bankkalenders.',
)
```

## zahlung_ausfuehrungsfristende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugangstag_fuer_ausfuehrungsfrist`: Bereits nach675n qualifizierter Zugangsgeschäftstag für675sI als ISO-Datum; muss im Kalender Geschäftstag sein.
- `fristfall`: standard (1Geschäftstag), papier_verlaengerung (wirksam genutzte2Geschäftstage) oder ewr_nichteuro_vereinbart.
- `vereinbarte_geschaeftstage`: Nur ewr_nichteuro_vereinbart: ganze Zahl1..4 aus wirksamer Vereinbarung; sonst null. Kein weiterer Papiertag auf diese Frist.
- `bankkalender`: Objekt mit genau erster_kalendertag, letzter_kalendertag (ISO-Daten) und geschaeftstage (unbenannte Liste1..10000 streng aufsteigender eindeutiger ISO-Daten innerhalb des Intervalls). Vollständiger Geschäftskalender des maßgeblichen Dienstleisters für den konkreten Zahlungsvorgang im angegebenen Intervall; keine Wochenendannahme. Die erforderlichen Vor-/Folgetage müssen enthalten sein.
- `kalendernachweis`: Nichtleerer Nachweis des Normfalls, tatsächlichen vollständigen Geschäftskalenders und der taggenau normalisierten Zugangs-/Terminbedingungen; Uhrzeiten, Annahmeschluss und Zeitzone extern qualifizieren.

Ein-/Zweitagesregel oder vereinbarte EWR-Nicht-Euro-Frist bis vier Geschäftstage.

wert: anzahl_geschaeftstage und spaetester_eingangstag (Tagesende beim Empfängerdienstleister).

§675sI: spätester Eingang beim Zahlungsdienstleister des Empfängers. standard=ein Geschäftstag; papier_verlaengerung=nur wirksam genutzte Verlängerung der Standardfrist um einen Geschäftstag. ewr_nichteuro_vereinbart=nur wirksame Vereinbarung von1bis4Geschäftstagen im einschlägigen EWR-Nicht-Euro-Fall; kein zusätzlicher Papiertag auf diese Vier-Tages-Frist. Qualifizierter Geschäftskalender und675n-Zugangstag vorgeben.675sII-Empfängerauslösung und Ausnahmen675sIII/675dVI separat; keine automatische Gutschrift-/Wertstellungsentscheidung.

ISO-Kalenderdaten0001..9999; Geschäftstagsliste1..10000 mit ausdrücklichem Abdeckungsintervall. Fehlende Kalenderabdeckung ist ungültig, keine Extrapolation.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675s_T0001, BGB_675s_T0002, BGB_675s_T0003

```python
from bgbcalc import zahlung_ausfuehrungsfristende
zahlung_ausfuehrungsfristende(
    zugangstag_fuer_ausfuehrungsfrist='2024-03-28',
    fristfall='standard',
    vereinbarte_geschaeftstage=None,
    bankkalender={'erster_kalendertag': '2024-03-25', 'letzter_kalendertag': '2024-04-15', 'geschaeftstage': ['2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08', '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15']},
    kalendernachweis='Expliziter synthetischer Geschäftskalender, vollständig im Intervall; qualifizierter Normfall, keine Behauptung eines universellen Bankkalenders.',
)
```

## zahlung_geschaeftstags_grenztermin

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristfall`: lastschrift_widerruf_675p, terminauftrag_widerruf_675p, nichtautorisiert_erstattung_675u, erstattung_entscheidung_675x oder bareinzahlung_nichtverbraucher_675t.
- `bezugstag_am`: Qualifizierter ISO-Bezugstag: vereinbarte Fälligkeit/Ausführung bei675p, früheste Anzeige/Kenntnis bei675u, Zugang des Erstattungsverlangens bei675x oder Entgegennahme der Bareinzahlung bei675t.
- `bankkalender`: Objekt mit genau erster_kalendertag, letzter_kalendertag (ISO-Daten) und geschaeftstage (unbenannte Liste1..10000 streng aufsteigender eindeutiger ISO-Daten innerhalb des Intervalls). Vollständiger Geschäftskalender des maßgeblichen Dienstleisters für den konkreten Zahlungsvorgang im angegebenen Intervall; keine Wochenendannahme. Die erforderlichen Vor-/Folgetage müssen enthalten sein.
- `kalendernachweis`: Nichtleerer Nachweis des Normfalls, tatsächlichen vollständigen Geschäftskalenders und der taggenau normalisierten Zugangs-/Terminbedingungen; Uhrzeiten, Annahmeschluss und Zeitzone extern qualifizieren.

Vortag, nächster Geschäftstag oder zehnter Geschäftstag im qualifizierten Zahlungsfall.

wert: rechnerischer_grenztermin als ISO-Datum, Tagesablauf.

675pII/III: letzter Geschäftstag vor vereinbarter Fälligkeit beziehungsweise vereinbartem Ausführungstag, nicht vor einem eigenständig verschobenen Termin; spätere Widerrufsvereinbarungen gesondert.675u: Bezugstag ist früheste maßgebliche Anzeige oder anderweitige Kenntnis, äußerste Erstattungs-/Kontokorrekturfrist, unverzüglich bleibt zusätzlich; qualifizierte Betrugsverdachtsausnahme außerhalb.675xV: zehn Geschäftstage nach Zugang des Erstattungsverlangens, Anspruch und Vier-/Achtwochenregeln getrennt.675tII: Nichtverbraucher-Bareinzahlung in Kontowährung, spätestens folgender Geschäftstag; Verbraucherregel unverzüglich nicht übertragen.675dVI-/Spezialausnahmen vorqualifizieren. Jeweils Kalender des verpflichteten Zahlungsdienstleisters für diesen Vorgang vollständig angeben. Ergebnis bezeichnet Tagesablauf; Uhrzeiten/Zeitzonen extern normalisieren.

ISO-Kalenderdaten0001..9999; Geschäftstagsliste1..10000 mit ausdrücklichem Abdeckungsintervall. Fehlende Kalenderabdeckung ist ungültig, keine Extrapolation.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_675p_T0002, BGB_675p_T0003, BGB_675p_T0004, BGB_675t_T0006, BGB_675t_T0007, BGB_675u_T0001, BGB_675u_T0002, BGB_675u_T0003, BGB_675u_T0004, BGB_675u_T0005, BGB_675x_T0009, BGB_675x_T0010, BGB_675x_T0011

```python
from bgbcalc import zahlung_geschaeftstags_grenztermin
zahlung_geschaeftstags_grenztermin(
    fristfall='lastschrift_widerruf_675p',
    bezugstag_am='2024-04-02',
    bankkalender={'erster_kalendertag': '2024-03-25', 'letzter_kalendertag': '2024-04-15', 'geschaeftstage': ['2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08', '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15']},
    kalendernachweis='Expliziter synthetischer Geschäftskalender, vollständig im Intervall; qualifizierter Normfall, keine Behauptung eines universellen Bankkalenders.',
)
```
