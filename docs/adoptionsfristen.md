<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## adoption_aufhebungsgrundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `annahme_am`: Rechtlich qualifiziertes ISO-Datum der Annahme als Ereignis für Dreijahresgrenze.
- `relativer_fristbeginn_am`: Rechtlich qualifiziertes ISO-Ereignisdatum des relativen Jahresbeginns nach§1762II a bis e; keine pauschale Gleichsetzung mit Annahmedatum oder Kenntnisdatum.
- `fristbeginnnachweis`: Nichtleerer Nachweis zu maßgeblichem relativen Beginn einschließlich Vertreterbezug/etwaigem vorausgehendem Fristablauf. Nur ungestörte Grundfristen.

Minimum aus relativem Beginn+1Jahr und Annahme+3Jahre; beide ungestörten Einzelgrenzen ausweisen.

wert enthält jahresgrundfristende, dreijahresgrundgrenze und antragsgrundfristende als ISO-Daten.

Nur ungestörte Grundfristen nach§1762II. Relativen Beginn nach Buchstaben a bis e einschließlich etwaiger Vertreterkenntnis oder Ablaufs der§1747II1-Frist rechtlich vorqualifizieren; nicht allgemein Kenntnis der Annahme einsetzen. §§206/210 und eine einschlägige§193-Korrektur sind hier nicht berechnet, insbesondere keine Behauptung absolut unkorrigierbarer Dreijahresfrist. Liegt relativer Beginn erst nach Dreijahresgrenze, bleibt das errechnete Grundende früher; daraus folgt kein automatisches Erlöschensurteil. Antragsberechtigung, Vertretung, Beurkundung und Aufhebungsgrund gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1762_T0005, BGB_1762_T0007, BGB_1762_T0008, BGB_1762_T0009, BGB_1762_T0010, BGB_1762_T0011, BGB_1762_T0012

```python
from bgbcalc import adoption_aufhebungsgrundfrist
adoption_aufhebungsgrundfrist(
    annahme_am='2030-01-15',
    relativer_fristbeginn_am='2030-03-01',
    fristbeginnnachweis='Rechtlich qualifizierter Beginn nach einschlägigem Buchstaben, kein Hemmungsfall.',
)
```

## adoption_ersetzungswartefrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `geburt_am`: ISO-Geburtsdatum des Kindes für Fünfmonatsmindestende.
- `belehrung_oder_erste_handlung_am`: Qualifiziertes ISO-Ereignisdatum der Belehrung oder bei gesetzlichem Ausnahmefall ersten einschlägigen Handlung des Jugendamts.
- `fristbeginnnachweis`: Nichtleerer Nachweis der einschlägigen Alternative und rechtlichen Qualifikation des Dreimonatsbeginns.

Dreimonatsfrist ab qualifiziertem Beginn, Fünfmonatsgrenze ab Geburt, Maximum beider Endtage.

wert enthält dreimonatsfristende, fuenfmonatsmindestende und wartefristende als ISO-Daten. Wartezeit läuft erst mit Ablauf des letzten Endtages ab.

§1748II betrifft Gleichgültigkeit ohne zugleich anhaltende gröbliche Pflichtverletzung. Beginn ist wirksame Belehrung oder im gesetzlich qualifizierten Ausnahmefall erste Handlung des Jugendamts zur Belehrung/Beratung oder Aufenthaltsermittlung. Beratung, Nachforschungen und Ausnahmevoraussetzungen vorqualifiziert. Ergebnisse sind Ablaufdaten; Ersetzung frühestens nach Ablauf, keine automatische Ersetzungsbefugnis. Keine§193-Verlängerung der bloßen Wartezeit. Andere Ersetzungsgründe nachAbsätzen1/3/4 nicht auf diese Wartezeit reduzieren.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1748_T0003, BGB_1748_T0004, BGB_1748_T0005

```python
from bgbcalc import adoption_ersetzungswartefrist
adoption_ersetzungswartefrist(
    geburt_am='2030-01-15',
    belehrung_oder_erste_handlung_am='2030-02-15',
    fristbeginnnachweis='Belehrung bzw. erste einschlägige Handlung rechtlich qualifiziert, keine Entscheidung über Ersetzung.',
)
```
