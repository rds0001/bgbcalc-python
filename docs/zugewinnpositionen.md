<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## zugewinn_anfangsvermoegen_positionssumme

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anfangsaktivvermoegen`: Nichtnegativer rechtlich bewerteter Aktivwert des Anfangsvermögens in EUR, keine Verbindlichkeiten vorab abgezogen.
- `anfangsverbindlichkeiten`: Nichtnegative zugehörige Anfangsverbindlichkeiten in EUR, auch über Aktivhöhe abzuziehen.
- `privilegierte_erwerbe`: Liste1..10000 qualifizierter Erwerbe nach§1374II, je genau erwerbswert und zugehoerige_verbindlichkeiten als nichtnegative EUR. Keine Einkünfte, keine Doppelzuordnung. Keine Erwerbe durch eine Nullposition0/0 ausdrücken.
- `bewertungsnachweis`: Nichtleerer Nachweis der Privilegierung, maßgeblicher Werte/Verbindlichkeiten und konsistenter gegebenenfalls erforderlicher Kaufkraftanpassung; keine automatische Indexierung.

Anfangsnetto=Aktiva−Schulden; jeder Nettoerwerb=Erwerbswert−zugehörige Schulden; Anfangsvermögenssumme=Anfangsnetto+Summe Nettoerwerbe. Keine Nullkappung.

wert enthält urspruengliches_nettoanfangsvermoegen, nettoerwerbe in Eingabereihenfolge, hinzuzurechnende_nettoerwerbssumme und anfangsvermoegenssumme als auch negative EUR-Brüche.

§1374III verlangt ausdrücklich Schuldenabzug auch über die Vermögenshöhe hinaus; ursprünglicher Nettowert, einzelne Nettoerwerbe und Gesamtsumme können negativ sein. Nur rechtlich privilegierte Erwerbe nachAbsatz2 eingeben: von Todes wegen/vorweggenommenes Erbrecht/Schenkung/Ausstattung, nach Güterstandseintritt und nicht den Umständen nach Einkünfte. Anfangsschulden und Erwerbsverbindlichkeiten nicht doppelt zuordnen. Werte und zugehörige Verbindlichkeiten nach rechtlich maßgeblichen Bewertungszeitpunkten und konsistenter gegebenenfalls bereits erforderlicher Kaufkraftanpassung vorqualifizieren; keine automatische Indexierung oder Bewertung nach§1376. Keine Erwerbe durch eine Nullposition mit Erwerbswert0 und Verbindlichkeiten0 ausdrücken. Keine automatische Privilegierungs-/Einkünfteentscheidung, keine§1380-Anrechnung und kein abschließender Zugewinnausgleich.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1374_T0001, BGB_1374_T0002, BGB_1374_T0003

```python
from bgbcalc import zugewinn_anfangsvermoegen_positionssumme
zugewinn_anfangsvermoegen_positionssumme(
    anfangsaktivvermoegen='100',
    anfangsverbindlichkeiten='20',
    privilegierte_erwerbe=[{'erwerbswert': '50', 'zugehoerige_verbindlichkeiten': '10'}, {'erwerbswert': '30', 'zugehoerige_verbindlichkeiten': '5'}],
    bewertungsnachweis='Qualifizierte privilegierte Erwerbe, Werte/Schulden ohne Doppelzählung und auf rechtlich konsistenter Bewertungsbasis.',
)
```

## zugewinn_endvermoegen_positionssumme

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `endaktivvermoegen`: Nichtnegative rechtlich bewertete Endaktiva in EUR ohne vorab abgezogene Verbindlichkeiten.
- `endverbindlichkeiten`: Nichtnegative zugehörige Endverbindlichkeiten in EUR, auch über Aktiva hinaus abzuziehen.
- `bezugsstichtag_am`: Rechtlich maßgeblicher ISO-Bezugsstichtag für§1375III-Zehnjahresgrenze, einschließlich einschlägiger§1384/1387-Zuordnung vorqualifiziert.
- `vermoegensminderungen`: Liste1..10000 rechtlich qualifizierter tatsächlicher Minderungen nach Güterstandseintritt, je genau minderung_id(eindeutig), betrag(nichtnegative EUR), eingetreten_am(ISO≤Stichtag), minderungsart(unentgeltliche_zuwendung/verschwendung/benachteiligung), einverstaendnis_anderer(echter Wahrheitswert). Keine Minderungen als Nullposition zum Stichtag vorgeben.
- `bewertungsnachweis`: Nichtleerer Nachweis der Tatbestandsqualifikation, tatsächlicher Minderungsbeträge, Werte/Stichtage und gegebenenfalls Kaufkraftanpassung. Keine frei gewählte Einverständniswirkung fürNummer3.

Nettoendvermögen=Aktiva−Schulden. Minderungen mindestens10Kalenderjahre vor Bezugsstichtag ausschließen. Bei Zuwendung/Verschwendung auch bei Einverständnis ausschließen. Übrige qualifizierte Minderungsbeträge zum Nettoendvermögen addieren.

wert enthält nettoendvermoegen (auch negativ), hinzurechnungspositionen mit ID/Betrag, hinzurechnungssumme und endvermoegenssumme (auch negativ).

§1375IbisIII. Tatsächlichen Vermögensminderungsbetrag nach Eintritt des Güterstands und dessen Wert rechtlich qualifizieren, nicht ungeprüft Ausgaben-/Schenkungsbruttobetrag. Einwilligungs-/Einverständnisausschluss nachAbsatz3 gilt ausdrücklich für unentgeltliche Zuwendung und Verschwendung; eine als Nummer3 qualifizierte Benachteiligung wird nicht allein wegen dieses Eingabeflags ausgeschlossen. Qualifikation nachNummer3 muss einschließlich relevanter Umstände bereits belastbar sein. Mindestens zehn Jahre schließt Gleichheit ein; vorhandener Kalenderkern, keine3650-Tage-Pauschale. Bezugsstichtag für die konkrete§1375III-Berechnung rechtlich bestimmen, einschließlich einschlägiger Stichtagsregeln§1384/1387; keine freie Wahl. Minderungen/Schulden nicht mehrfach erfassen, überschneidende Tatbestände einmal. Endschulden dürfen Endaktiva übersteigen. Keine automatische Beweislastentscheidung, Bewertungs-/Kaufkraftanpassung oder Prüfung einer Benachteiligungsabsicht. Keine Minderungen durch eine Nullposition zum Bezugsstichtag ausdrücken. §1380-Sonderanrechnung und eingreifende Haftungsgrenzen nicht gelöst.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1375_T0001, BGB_1375_T0002, BGB_1375_T0003, BGB_1375_T0004, BGB_1375_T0005, BGB_1375_T0006, BGB_1375_T0008

```python
from bgbcalc import zugewinn_endvermoegen_positionssumme
zugewinn_endvermoegen_positionssumme(
    endaktivvermoegen='100',
    endverbindlichkeiten='20',
    bezugsstichtag_am='2030-01-01',
    vermoegensminderungen=[{'minderung_id': 'A', 'betrag': '30', 'eingetreten_am': '2029-01-01', 'minderungsart': 'unentgeltliche_zuwendung', 'einverstaendnis_anderer': False}, {'minderung_id': 'B', 'betrag': '20', 'eingetreten_am': '2028-01-01', 'minderungsart': 'verschwendung', 'einverstaendnis_anderer': False}],
    bewertungsnachweis='Tatsächliche Minderungen nach Güterstandseintritt, Tatbestand und Bewertungs-/Bezugsstichtag rechtlich qualifiziert.',
)
```
