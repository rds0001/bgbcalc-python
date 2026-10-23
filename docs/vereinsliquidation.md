<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vereinsvermoegen_mitgliederanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verteilbarer_ueberschuss`: Nichtnegativer rechtlich verteilbarer Liquidationsüberschuss in EUR. Nicht ungeprüft Bruttovermögen oder bloßes Ergebnis einer Bestandsrechnung; Gläubigerbefriedigung, Sperrjahr und Sicherheiten separat erfüllen.
- `mitglieder_bei_aufloesung`: Positive ganze Zahl bis2^53-1 der zur Zeit der Auflösung beziehungsweise Entziehung der Rechtsfähigkeit vorhandenen maßgeblichen Mitglieder. Nicht einen späteren oder nur teilnehmenden Mitgliederkreis einsetzen.
- `anfallberechtigte_anderweitig_bestimmt`: Wahrheitswert einer rechtlich maßgeblichen anderen Bestimmung der Anfallberechtigten gemäß§45 Absätze1/2. TRUE schließt diese gesetzliche Gleichverteilung aus, ohne die andere Verteilung hier zu berechnen.
- `ausschliessliche_mitgliederinteressen`: Wahrheitswert, ob der Verein nach seiner Satzung ausschließlich den Interessen seiner Mitglieder diente. Nicht mit irgendeinem Mitgliedervorteil gleichsetzen. FALSE führt in dieser Funktion zu NICHT_ANWENDBAR; Fiskalanfall separat bestimmen.
- `verteilungsnachweis`: Nichtleere Beschreibung des verteilbaren Überschusses, maßgeblichen Mitgliederkreises, fehlender anderer Anfallbestimmung und satzungsmäßiger ausschließlicher Mitgliederinteressen.

Nur ohne anderweitige Anfallbestimmung und bei ausschließlichen Mitgliederinteressen: Überschuss geteilt durch maßgebliche Mitgliederzahl. Sonst NICHT_ANWENDBAR.

wert ist der exakte EUR-Anteil je maßgeblichem Mitglied; sonst null und NICHT_ANWENDBAR.

Keine fiktive Gleichverteilung im Fiskalfall oder bei anderer Anfallbestimmung. Tatsächliche Ausantwortungsreife wird nicht aus Zahlen allein abgeleitet. Bruchteile bleiben exakt, keine willkürliche Verteilung von Centresten.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_45_T0001, BGB_45_T0002, BGB_45_T0003, BGB_45_T0004

```python
from bgbcalc import vereinsvermoegen_mitgliederanteil
vereinsvermoegen_mitgliederanteil(
    verteilbarer_ueberschuss='1000',
    mitglieder_bei_aufloesung=1,
    anfallberechtigte_anderweitig_bestimmt=False,
    ausschliessliche_mitgliederinteressen=True,
    verteilungsnachweis='Synthetisch verteilbarer Überschuss und gesetzlicher Auffangfall.',
)
```

## vereins_liquidationssperrjahr

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erste_einrueckung`: ISO-Datum0001..9999 der maßgeblichen Einrückung beziehungsweise ersten Einrückung in das satzungsmäßige Veröffentlichungsblatt nach§50. Nicht das Auflösungsdatum oder eine spätere Wiederholung einsetzen.
- `bekanntmachung_ordnungsgemaess`: Expliziter Wahrheitswert zur gesetzeskonformen Bekanntmachung nach§50, insbesondere Inhalt mit Gläubigeraufforderung und maßgebliches Blatt. FALSE ergibt NICHT_ANWENDBAR. Keine automatische Inhaltsprüfung eines Textes.
- `bekanntmachungsnachweis`: Nichtleere Beschreibung/Beleg der Einrückung, ihrer Reihenfolge und ordnungsgemäßen Veröffentlichung. Besondere Mitteilungen an bekannte Gläubiger und spätere Verteilungsreife zusätzlich prüfen.

Bekanntmachung bewirkt mit Ablauf des zweiten Kalendertags nach erster Einrückung. Von diesem Ereignis ein Kalenderjahr nach§§187/188; Sperre bis dessen Tagesablauf. Erster Tag danach ist früheste kalenderseitige Grenze.

wert enthält bekanntmachung_bewirkt_mit_tagesablauf, sperrjahr_ende und fruehester_tag_nach_sperrjahr als ISO-Daten. NICHT_ANWENDBAR bei nicht bestätigter ordnungsgemäßer Bekanntmachung.

Nur Sperrjahrgrenze, kein umfassender Auszahlungstermin. Gläubigerbefriedigung, Hinterlegung/Sicherheiten, besondere Mitteilungen und Insolvenzpflichten bleiben getrennt. Keine pauschale§193-Verschiebung. Sämtliche Zwischendaten müssen0001..9999 bleiben.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_50_T0001, BGB_50_T0002, BGB_50_T0003, BGB_50_T0004, BGB_51_T0001, BGB_187_T0001, BGB_188_T0002, BGB_188_T0003

```python
from bgbcalc import vereins_liquidationssperrjahr
vereins_liquidationssperrjahr(
    erste_einrueckung='2026-01-01',
    bekanntmachung_ordnungsgemaess=True,
    bekanntmachungsnachweis='Synthetische erste Einrückung mit Gläubigeraufforderung im maßgeblichen Blatt.',
)
```

## vereins_liquidationsueberschuss

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verfuegbares_liquidationsvermoegen`: Nichtnegativer in EUR bestimmter verfügbarer Vermögensbestand für den konkreten Liquidationsstand, einschließlich bereits eingezogener Forderungen ohne Doppelzählung. Nicht verfügbare/streitige Werte nur nach rechtlicher Bewertung; keine automatische Gleichsetzung von Buchwert und verfügbarem Geld.
- `noch_zu_befriedigende_verbindlichkeiten`: Nichtnegative Summe in EUR aller zum gleichen Stand noch aus diesem Bestand zu befriedigenden Verbindlichkeiten einschließlich rechtlich zu berücksichtigender Liquidationslasten. Bereits bezahlte Verbindlichkeiten nicht erneut von bereits vermindertem Vermögen abziehen.
- `bestandsnachweis`: Nichtleere Beschreibung der zeitlich konsistenten und überschneidungsfreien Abgrenzung von verfügbarem Vermögen und offenen Verbindlichkeiten. Vollständigkeit, Hinterlegung, Sicherheiten und mögliche Insolvenzgründe separat prüfen.

Differenz=verfügbares Liquidationsvermögen minus noch zu befriedigende Verbindlichkeiten. Überschuss=max(Differenz,0); Fehlbetrag=max(-Differenz,0).

wert enthält ueberschuss und fehlbetrag als nichtnegative exakte EUR-Brüche. Positive Fehlbeträge nicht als negativer ausschüttbarer Anteil ausgeben.

Rechnerischer Bestand, keine Ausantwortungsreife. Tatsächliche Gläubigerbefriedigung, weitere Geschäfte, Sicherungen§52, Sperrjahr§51 und Insolvenzpflichten gesondert. Kein ungeprüftes Doppelzählen eingezogener Forderungen oder bereits bezahlter Schulden.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_49_T0001, BGB_49_T0003

```python
from bgbcalc import vereins_liquidationsueberschuss
vereins_liquidationsueberschuss(
    verfuegbares_liquidationsvermoegen='0',
    noch_zu_befriedigende_verbindlichkeiten='0',
    bestandsnachweis='Synthetischer konsistenter verfügbarer Bestand und offene Verbindlichkeiten.',
)
```
