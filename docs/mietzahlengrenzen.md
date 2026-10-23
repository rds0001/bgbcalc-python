<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mietspiegel_einwohnerschwelle

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `einwohnerzahl`: Nichtnegative ganze Anzahl im gemeinsamen exakten Zahlenbereich.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Gemeindeeinwohnerzahl strikt mit50000 vergleichen.

wert enthält einwohnergrenze, grenze_ueberschritten. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur numerische Schwelle nach558cIV2; rechtlich maßgebliche Einwohnerzahl der betreffenden Gemeinde vorgeben. Genau50000 erfüllt die strikte Überschreitung nicht. Unterhalb der Schwelle kann weiterhin ein Bedürfnis nachAbsatz4Satz1 bestehen; keine allgemeine Befreiung von Aufgaben und keine automatische Mietspiegelerstellung.

Nichtnegative Eingaben; Kostendifferenz kann negativ sein. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558c_T0001, BGB_558c_T0002, BGB_558c_T0003, BGB_558c_T0004, BGB_558c_T0005, BGB_558c_T0006, BGB_558c_T0007

```python
from bgbcalc import mietspiegel_einwohnerschwelle
mietspiegel_einwohnerschwelle(
    einwohnerzahl=0,
    einordnungsnachweis='Nur numerische Schwelle nach558cIV2; rechtlich maßgebliche Einwohnerzahl der betreffenden Gemeinde vorgeben. Genau50000 erfüllt die strikte Überschreitung nicht. Unterhalb der Schwelle kann weiterhin ein Bedürfnis nachAbsatz4Satz1 bestehen; keine allgemeine Befreiung von Aufgaben und keine automatische Mietspiegelerstellung.',
)
```

## mietspiegel_spanneneinordnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `spannengrenze_unten`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `spannengrenze_oben`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `verlangte_miete`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Verlangte Miete einschließlich der Grenzen mit qualifizierter Mietspiegelspanne vergleichen.

wert enthält innerhalb_der_spanne, unterhalb_unterschreitungsbetrag, oberhalb_ueberschreitungsbetrag. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur numerischer Spannenvergleich nach558aIV1; gleiche Miet-/Flächeneinheit und gleicher Zeitraum für alle drei Werte. Keine automatische Auswahl der Vergleichsmerkmale, kein Beweis endgültiger ortsüblicher Vergleichsmiete und keine Prüfung der vollständigen Mieterhöhungsberechtigung nach558. Unter- und Obergrenze zählen mit; keine automatische Erhöhung einer unter der Spanne verlangten Miete.

Nichtnegative Eingaben; Kostendifferenz kann negativ sein. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558a_T0001, BGB_558a_T0002, BGB_558a_T0003, BGB_558a_T0004, BGB_558a_T0005, BGB_558a_T0006, BGB_558a_T0007, BGB_558a_T0008, BGB_558a_T0009, BGB_558a_T0010

```python
from bgbcalc import mietspiegel_spanneneinordnung
mietspiegel_spanneneinordnung(
    spannengrenze_unten='5',
    spannengrenze_oben='10',
    verlangte_miete='5',
    einordnungsnachweis='Nur numerischer Spannenvergleich nach558aIV1; gleiche Miet-/Flächeneinheit und gleicher Zeitraum für alle drei Werte. Keine automatische Auswahl der Vergleichsmerkmale, kein Beweis endgültiger ortsüblicher Vergleichsmiete und keine Prüfung der vollständigen Mieterhöhungsberechtigung nach558. Unter- und Obergrenze zählen mit; keine automatische Erhöhung einer unter der Spanne verlangten Miete.',
)
```

## vergleichswohnungen_mindestzahl

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anzahl_vergleichswohnungen`: Nichtnegative ganze Anzahl im gemeinsamen exakten Zahlenbereich.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Anzahl qualifizierter Vergleichswohnungen mit drei vergleichen und fehlende Anzahl bestimmen.

wert enthält mindestzahl, fehlende_wohnungen, mindestzahl_erreicht. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur numerische Mindestzahl nach558aII Nummer4. Wohnungen müssen tatsächlich verschieden und rechtlich vergleichbar sein; Benennung und entsprechende Entgelte vorqualifizieren. Drei Wohnungen genügen als dieser Begründungsweg, entscheiden aber keine materielle Mieterhöhung. Kein Ersatz für notwendige Mietspiegelangaben nachAbsatz3.

Nichtnegative Eingaben; Kostendifferenz kann negativ sein. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558a_T0001, BGB_558a_T0002, BGB_558a_T0003, BGB_558a_T0004, BGB_558a_T0005, BGB_558a_T0006, BGB_558a_T0007, BGB_558a_T0008, BGB_558a_T0009, BGB_558a_T0010

```python
from bgbcalc import vergleichswohnungen_mindestzahl
vergleichswohnungen_mindestzahl(
    anzahl_vergleichswohnungen=0,
    einordnungsnachweis='Nur numerische Mindestzahl nach558aII Nummer4. Wohnungen müssen tatsächlich verschieden und rechtlich vergleichbar sein; Benennung und entsprechende Entgelte vorqualifizieren. Drei Wohnungen genügen als dieser Begründungsweg, entscheiden aber keine materielle Mieterhöhung. Kein Ersatz für notwendige Mietspiegelangaben nachAbsatz3.',
)
```

## waermelieferung_kosten_und_nutzungsgradgrenzen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `bisherige_betriebskosten`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `neue_waermelieferkosten`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `jahresnutzungsgrad_prozent`: Nichtnegativer exakter Dezimaltext/Bruch; Kosten/Miete in identischer Einheit und Periode, Jahresnutzungsgrad ausdrücklich in Prozentpunkten.
- `einordnungsnachweis`: Nichtleerer Nachweis zu maßgeblicher Vergleichsbasis und rechtlicher Einordnung; keine Gesamtentscheidung allein aus Zahlen.

Neue und bisherige Wärmekosten vergleichen; Jahresnutzungsgrad mit80Prozent vergleichen.

wert enthält kostendifferenz, kostenneutralitaetsgrenze_eingehalten, nutzungsgradgrenze_erreicht. Beträge als exakte Brüche, Anzahlen als Ganzzahlen, Vergleiche als Wahrheitswerte.

Nur numerische Teilbedingungen nach556cI. Kosten für denselben rechtlich maßgeblichen Vergleichszeitraum und Versorgungsumfang vorqualifizieren; keine eigenständige Berechnung nach externer Wärmelieferverordnung. Nutzungsgrad in Prozentpunkten,80 bedeutet80Prozent; keine automatische Bewertung der Anlage oder verbesserter Betriebsführung. Grenzwerte einschließlich Gleichheit. Ergebnis entscheidet nicht sämtliche Voraussetzungen der Kostenumlage; Ankündigung556cII separat.

Nichtnegative Eingaben; Kostendifferenz kann negativ sein. Keine automatische Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556c_T0001, BGB_556c_T0002, BGB_556c_T0003, BGB_556c_T0004, BGB_556c_T0005, BGB_556c_T0006, BGB_556c_T0007, BGB_556c_T0008

```python
from bgbcalc import waermelieferung_kosten_und_nutzungsgradgrenzen
waermelieferung_kosten_und_nutzungsgradgrenzen(
    bisherige_betriebskosten='100',
    neue_waermelieferkosten='100',
    jahresnutzungsgrad_prozent='80',
    einordnungsnachweis='Nur numerische Teilbedingungen nach556cI. Kosten für denselben rechtlich maßgeblichen Vergleichszeitraum und Versorgungsumfang vorqualifizieren; keine eigenständige Berechnung nach externer Wärmelieferverordnung. Nutzungsgrad in Prozentpunkten,80 bedeutet80Prozent; keine automatische Bewertung der Anlage oder verbesserter Betriebsführung. Grenzwerte einschließlich Gleichheit. Ergebnis entscheidet nicht sämtliche Voraussetzungen der Kostenumlage; Ankündigung556cII separat.',
)
```
