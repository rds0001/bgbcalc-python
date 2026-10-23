<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## widerruf_fristenden_zusammenfuehren

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `regelfristende_am`: Rechtlich qualifiziertes RegelfristendeYYYY-MM-DD nach gegebenenfalls erforderlicher Kalenderkorrektur. NULL/None ausdrücklich, wenn noch kein berechenbares Regelfristende vorliegt.
- `hoechstfristende_am`: Anwendbares qualifiziertes HöchstfristendeYYYY-MM-DD nach gegebenenfalls erforderlicher Kalenderkorrektur; NULL/None ausdrücklich, wenn kein solches berechenbares Ende vorliegt.
- `einordnungsnachweis`: Nichtleerer Nachweis der Enddaten einschließlich nötiger Kalenderkorrekturen und Bedeutung eventuell fehlender Daten. BeideNULL bedeuten keine berechenbare zeitliche Endgrenze, keinen automatischen Bestand eines Widerrufsrechts.

Früheres von Regelfristende und anwendbarem Höchstfristende bestimmen; fehlende berechenbare Enden ausdrücklich ausweisen.

wert: rechnerisch_bestimmbares_endeYYYY-MM-DD oderNULL, regelfristende_vorhanden und hoechstfristende_vorhanden als Wahrheitswerte.

Nur zeitliche Kombination rechtlich vorqualifizierter Enddaten355/356–356f. Vorher gegebenenfalls einschlägige Kalenderkorrekturen wie193 für das jeweilige Ende vornehmen; rohe Fristdaten nicht ungeprüft als endgültige Erklärungstermine verwenden. NULL/None bedeutet ausdrücklich kein vorliegendes berechenbares Ende dieses Typs, nicht stillschweigend erfüllte Anfangsvoraussetzungen oder eine pauschale unbegrenzte Widerrufsmöglichkeit. Sind beide EndenNULL, bleibt das ErgebnisdatumNULL. Bei noch nicht begonnener Regelfrist kann eine qualifizierte Höchstfrist dennoch maßgeblich sein. Frühzeitiges Erlöschen, Anwendungsbereich, Form und rechtzeitige Absendung gesondert.

Strikte ISO-Daten0001..9999; ausdrückliche Ereignislisten und optionale qualifizierte Enddaten gemäß Parametervertrag.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_355_T0001, BGB_355_T0002, BGB_355_T0003, BGB_355_T0004, BGB_355_T0005, BGB_355_T0006, BGB_355_T0007, BGB_355_T0008, BGB_355_T0009, BGB_355_T0010, BGB_355_T0011, BGB_356_T0001, BGB_356_T0002, BGB_356_T0003, BGB_356_T0004, BGB_356_T0005, BGB_356_T0006, BGB_356_T0007, BGB_356_T0008, BGB_356_T0009, BGB_356_T0010, BGB_356_T0011, BGB_356_T0012, BGB_356_T0013, BGB_356_T0014, BGB_356_T0015, BGB_356_T0016, BGB_356_T0017, BGB_356_T0018, BGB_356_T0019, BGB_356_T0020, BGB_356_T0021, BGB_356_T0022, BGB_356_T0023, BGB_356_T0024, BGB_356_T0025, BGB_356_T0026, BGB_356_T0027, BGB_356_T0028, BGB_356b_T0001, BGB_356b_T0002, BGB_356b_T0003, BGB_356b_T0004, BGB_356c_T0001, BGB_356c_T0002, BGB_356c_T0003, BGB_356c_T0004, BGB_356c_T0005, BGB_356c_T0006, BGB_356c_T0007, BGB_356c_T0008, BGB_356c_T0009, BGB_356d_T0001, BGB_356d_T0002, BGB_356d_T0003, BGB_356e_T0001, BGB_356e_T0002, BGB_356f_T0001, BGB_356f_T0002

```python
from bgbcalc import widerruf_fristenden_zusammenfuehren
widerruf_fristenden_zusammenfuehren(
    regelfristende_am='2024-02-14',
    hoechstfristende_am='2025-02-14',
    einordnungsnachweis='Nur zeitliche Kombination rechtlich vorqualifizierter Enddaten355/356–356f. Vorher gegebenenfalls einschlägige Kalenderkorrekturen wie193 für das jeweilige Ende vornehmen; rohe Fristdaten nicht ungeprüft als endgültige Erklärungstermine verwenden. NULL/None bedeutet ausdrücklich kein vorliegendes berechenbares Ende dieses Typs, nicht stillschweigend erfüllte Anfangsvoraussetzungen oder eine pauschale unbegrenzte Widerrufsmöglichkeit. Sind beide EndenNULL, bleibt das ErgebnisdatumNULL. Bei noch nicht begonnener Regelfrist kann eine qualifizierte Höchstfrist dennoch maßgeblich sein. Frühzeitiges Erlöschen, Anwendungsbereich, Form und rechtzeitige Absendung gesondert.',
)
```

## widerruf_hoechstfristende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristfall`: Genau fernabsatz_aussergeschaeftlich_356, immobiliardarlehen_356b, teilzeitwohnrecht_informationen_356c, teilzeitwohnrecht_belehrung_356c, ratenlieferung_356d, verbraucherbau_356e oder unentgeltliches_darlehen_356f. Nur rechtlich anwendbare Höchstfrist wählen. Zusätzlich unentgeltliches_darlehen_ohne_unterrichtung_356f ausschließlich bei tatsächlich vollständig fehlender Unterrichtung.
- `bezugsereignistage`: Unbenannte Liste von genau einem oder zweiYYYY-MM-DD gemäß Fall:356 ein maßgeblicher Grundtag356II/355II2;356b zwei Tage Vertragsschluss und Urkundenzeitpunkt356bI;356c zwei Tage Vertrags-/Vorvertragsabschluss und Urkundenerhalt;356d/e ein Tag Vertragsschluss;356f zwei Tage Vertragsschluss und Unterrichtung. Beide Ereignisse müssen feststehen; gleiche Tage wiederholen, nicht fiktiv ergänzen. Ausnahme: unentgeltliches_darlehen_ohne_unterrichtung_356f genau ein tatsächlicher Vertragsschlusstag, keine fiktive Unterrichtung.
- `einordnungsnachweis`: Nichtleerer Nachweis gesetzlicher Höchstfrist, Informations-/Belehrungsfall und Bezugsereignisse. Bei356-Finanzdienstleistung ohne erforderliche Widerrufsbelehrung keine12Monats-Höchstfrist einsetzen; bei356c-Mangel beider Informationsarten Belehrungsfall12Monate wählen.

Gesetzlichen Höchstfristbezug als spätesten Bezugstag wählen, drei oder zwölf Monate und danach14Tage addieren.

wert: massgeblicher_bezugstagYYYY-MM-DD, hoechstfrist_monate3oder12 und hoechstfristende_ohne_kalenderkorrekturYYYY-MM-DD.

Feste lokale Fassung:356IV zwölfMonate+14Tage ab356II/355II2, nicht ab verspäteter Belehrung; bei Finanzdienstleistungen Ausnahme fehlender Belehrung356IV2 beachten, dann diesen Höchstfristfall nicht anwenden.356bII nur Immobiliardarlehen: späterer Vertragsschluss/Urkundenzeitpunkt356bI; keine pauschale Höchstfrist für Allgemeindarlehen.356c: späterer Vertrags-/Vorvertragsabschluss und Urkundenerhalt; dreiMonate+14Tage bei Informations-/Formblattmangel, zwölfMonate+14Tage bei Belehrungsmangel, letzterer auch bei beidem maßgeblich. Bei Urkunde bereits zum Abschluss denselben Tag zweimal angeben.356d/e: ein Bezugstag Vertragsschluss.356f: Bei tatsächlich erteilter Unterrichtung späteren Vertragsschluss/Unterrichtung verwenden, beide Tage müssen feststehen. Bei vollständig ausgebliebener Unterrichtung ausdrücklich unentgeltliches_darlehen_ohne_unterrichtung_356f wählen: nur tatsächlicher Vertragsschlusstag, zwölfMonate+14Tage. Dies ist keine fiktive Unterrichtung und startet keine14Tage-Regelfrist. Belegt durchBT-Drs18/7584S.141zur inhaltsgleichen früheren356d-Regelung. Vollständig fehlende Unterrichtung von unbekannter Informationslage unterscheiden. Ein bereits erloschenes Recht wird durch spätere Information nicht automatisch wiederbelebt; den Zwei-Ereignisfall nicht ungeprüft dafür verwenden. Regelwiderrufsfrist, frühzeitiges Erlöschen und gegebenenfalls193-Korrektur separat; Monatsanteil nicht eigenständig vor Addition der14Tage verschieben.

Strikte ISO-Daten0001..9999; ausdrückliche Ereignislisten und optionale qualifizierte Enddaten gemäß Parametervertrag.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_355_T0001, BGB_355_T0002, BGB_355_T0003, BGB_355_T0004, BGB_355_T0005, BGB_355_T0006, BGB_355_T0007, BGB_355_T0008, BGB_355_T0009, BGB_355_T0010, BGB_355_T0011, BGB_356_T0001, BGB_356_T0002, BGB_356_T0003, BGB_356_T0004, BGB_356_T0005, BGB_356_T0006, BGB_356_T0007, BGB_356_T0008, BGB_356_T0009, BGB_356_T0010, BGB_356_T0011, BGB_356_T0012, BGB_356_T0013, BGB_356_T0014, BGB_356_T0015, BGB_356_T0016, BGB_356_T0017, BGB_356_T0018, BGB_356_T0019, BGB_356_T0020, BGB_356_T0021, BGB_356_T0022, BGB_356_T0023, BGB_356_T0024, BGB_356_T0025, BGB_356_T0026, BGB_356_T0027, BGB_356_T0028, BGB_356b_T0001, BGB_356b_T0002, BGB_356b_T0003, BGB_356b_T0004, BGB_356c_T0001, BGB_356c_T0002, BGB_356c_T0003, BGB_356c_T0004, BGB_356c_T0005, BGB_356c_T0006, BGB_356c_T0007, BGB_356c_T0008, BGB_356c_T0009, BGB_356d_T0001, BGB_356d_T0002, BGB_356d_T0003, BGB_356e_T0001, BGB_356e_T0002, BGB_356f_T0001, BGB_356f_T0002

```python
from bgbcalc import widerruf_hoechstfristende
widerruf_hoechstfristende(
    fristfall='fernabsatz_aussergeschaeftlich_356',
    bezugsereignistage=['2024-01-31'],
    einordnungsnachweis='Feste lokale Fassung:356IV zwölfMonate+14Tage ab356II/355II2, nicht ab verspäteter Belehrung; bei Finanzdienstleistungen Ausnahme fehlender Belehrung356IV2 beachten, dann diesen Höchstfristfall nicht anwenden.356bII nur Immobiliardarlehen: späterer Vertragsschluss/Urkundenzeitpunkt356bI; keine pauschale Höchstfrist für Allgemeindarlehen.356c: späterer Vertrags-/Vorvertragsabschluss und Urkundenerhalt; dreiMonate+14Tage bei Informations-/Formblattmangel, zwölfMonate+14Tage bei Belehrungsmangel, letzterer auch bei beidem maßgeblich. Bei Urkunde bereits zum Abschluss denselben Tag zweimal angeben.356d/e: ein Bezugstag Vertragsschluss.356f: nach vorliegendem Wortlaut späterer Vertragsschluss/Unterrichtung; beide tatsächlich feststehenden Tage erforderlich, fehlende Unterrichtung nicht mit Vertragsschluss ersetzen. Keine automatisierte Bestimmung eines Höchstendes bei noch unbekanntem späterem Bezugsereignis. Regelwiderrufsfrist, frühzeitiges Erlöschen und gegebenenfalls193-Korrektur separat; Monatsanteil nicht eigenständig vor Addition der14Tage verschieben.',
)
```

## widerruf_regelfristende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristart`: Genau standard_vierzehn_tage nach355II oder darlehen_angabennachholung_monat nach356bII. Einmonatsfrist nicht auf andere Fälle verspäteter Unterrichtung übertragen.
- `erforderliche_ereignistage`: Unbenannte Liste1..10 tatsächlich eingetretener, rechtlich erforderlicher Anfangsereignisse alsYYYY-MM-DD. Alle einschlägigen Voraussetzungen vollständig erfassen; die Library bildet deren spätesten Tag. Bei noch fehlender Voraussetzung keine Fristberechnung mit erfundenem Datum; NULL in der Liste ist EINGABE_FEHLT.
- `einordnungsnachweis`: Nichtleerer Nachweis von gesetzlichem Fall und vollständiger Auswahl aller erforderlichen Anfangsvoraussetzungen, etwa Vertragsschluss, richtiger Warenempfang, Urkundenerhalt und ordnungsgemäßer Unterrichtung.

Spätesten Tag aller erforderlichen Anfangsvoraussetzungen wählen und14Tage oder einen Monat fortschreiben.

wert: massgeblicher_ereignistag und regelfristende_ohne_kalenderkorrektur alsYYYY-MM-DD.

§355II und356–356f:14Tage im qualifizierten Standardfall; ein Monat ausschließlich bei nachgeholten Angaben356bII. Liste muss sämtliche rechtlich erforderlichen eingetretenen Anfangsvoraussetzungen enthalten: je Norm insbesondere Vertrag/Vorvertrag, maßgeblicher Warenempfang, Vertragsurkunde, vollständige Informationen und Widerrufsbelehrung. Bei356II erste Ware bei regelmäßigen Lieferungen, letzte Ware/Teilsendung bei den anderen dort genannten Mehrlieferfällen rechtlich zutreffend auswählen.356cV gegebenenfalls maßgeblichen Teilzeit-Wohnrechtevertrag zugrunde legen. Solange eine erforderliche Voraussetzung fehlt, keine künstliche Ersatzdatierung eingeben. Kein automatischer Belehrungs-/Form-/Widerrufsrechtsentscheid; frühzeitiges Erlöschen356V/VI gesondert. Gesetzliche Höchstfristen und anwendbare193-Korrektur separat, rechtzeitige Absendung355I gesondert.

Strikte ISO-Daten0001..9999; ausdrückliche Ereignislisten und optionale qualifizierte Enddaten gemäß Parametervertrag.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_355_T0001, BGB_355_T0002, BGB_355_T0003, BGB_355_T0004, BGB_355_T0005, BGB_355_T0006, BGB_355_T0007, BGB_355_T0008, BGB_355_T0009, BGB_355_T0010, BGB_355_T0011, BGB_356_T0001, BGB_356_T0002, BGB_356_T0003, BGB_356_T0004, BGB_356_T0005, BGB_356_T0006, BGB_356_T0007, BGB_356_T0008, BGB_356_T0009, BGB_356_T0010, BGB_356_T0011, BGB_356_T0012, BGB_356_T0013, BGB_356_T0014, BGB_356_T0015, BGB_356_T0016, BGB_356_T0017, BGB_356_T0018, BGB_356_T0019, BGB_356_T0020, BGB_356_T0021, BGB_356_T0022, BGB_356_T0023, BGB_356_T0024, BGB_356_T0025, BGB_356_T0026, BGB_356_T0027, BGB_356_T0028, BGB_356b_T0001, BGB_356b_T0002, BGB_356b_T0003, BGB_356b_T0004, BGB_356c_T0001, BGB_356c_T0002, BGB_356c_T0003, BGB_356c_T0004, BGB_356c_T0005, BGB_356c_T0006, BGB_356c_T0007, BGB_356c_T0008, BGB_356c_T0009, BGB_356d_T0001, BGB_356d_T0002, BGB_356d_T0003, BGB_356e_T0001, BGB_356e_T0002, BGB_356f_T0001, BGB_356f_T0002

```python
from bgbcalc import widerruf_regelfristende
widerruf_regelfristende(
    fristart='standard_vierzehn_tage',
    erforderliche_ereignistage=['2024-01-31'],
    einordnungsnachweis='§355II und356–356f:14Tage im qualifizierten Standardfall; ein Monat ausschließlich bei nachgeholten Angaben356bII. Liste muss sämtliche rechtlich erforderlichen eingetretenen Anfangsvoraussetzungen enthalten: je Norm insbesondere Vertrag/Vorvertrag, maßgeblicher Warenempfang, Vertragsurkunde, vollständige Informationen und Widerrufsbelehrung. Bei356II erste Ware bei regelmäßigen Lieferungen, letzte Ware/Teilsendung bei den anderen dort genannten Mehrlieferfällen rechtlich zutreffend auswählen.356cV gegebenenfalls maßgeblichen Teilzeit-Wohnrechtevertrag zugrunde legen. Solange eine erforderliche Voraussetzung fehlt, keine künstliche Ersatzdatierung eingeben. Kein automatischer Belehrungs-/Form-/Widerrufsrechtsentscheid; frühzeitiges Erlöschen356V/VI gesondert. Gesetzliche Höchstfristen und anwendbare193-Korrektur separat, rechtzeitige Absendung355I gesondert.',
)
```
