<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betriebskosten_grundfristende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fristfall`: abrechnung oder einwendungen nach556III. Fristauslöser für den gewählten Fall ausdrücklich bestimmen.
- `bezugsdatum`: ISO-DatumYYYY-MM-DD: bei abrechnung letzter Tag des maßgeblichen Abrechnungszeitraums; bei einwendungen rechtlich bestimmter Zugangstag der ordnungsgemäßen Abrechnung. Nicht Erstellungs- oder Absendedatum.
- `fristberechnung`: Rechtlich begründet ausgewählte Variante: taggenau_zwoelf_monate oder ende_zwoelfter_kalendermonat. Pflichtparameter ohne Standardwert; kein freies Wahlrecht zur Fristverlängerung.
- `einordnungsnachweis`: Nichtleerer Nachweis des556III-Falls, Fristauslösers und der rechtlichen Grundlage für die ausgewählte Berechnungsweise; Ausnahmen wegen fehlenden Vertretenmüssens sowie193 separat.

Zwölfmonatige Ereignisfrist nach187/188 berechnen; nur bei ausdrücklich ausgewählter Monatsendevariante auf den letzten Kalendertag dieses Zielmonats setzen.

wert.rechnerisches_fristende alsYYYY-MM-DD; Ergebnis der ausgewählten Variante vor etwaiger193-Korrektur.

§556III: zwei explizite Berechnungsweisen ohne automatische Auslegungsentscheidung. LGFrankfurt(Oder)20.11.2012,16S47/12 befürwortet Monatsende192 und dokumentiert die gegenteilige taggenaue Berechnung der Vorinstanz. Hieraus folgt keine Behauptung einer heute universell verbindlichen Auslegung; Auswahl rechtlich belegen. Grundfrist ohne193-Wochenend-/Feiertagskorrektur; diese bei feststehender Anwendbarkeit mit vorhandenem Kalenderkern nachführen. Kein automatischer Ausschluss von Nachforderung oder Einwendung: ordnungsgemäße Abrechnung, Zugang, Vertretenmüssen und Sonderfälle gesondert. Jährliche Abrechnungspflicht ist nicht identisch mit dem anschließenden Mitteilungszeitraum.

Kalenderdaten0001..9999 einschließlich Grenz- und Folgedaten; keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003, BGB_192_T0001, BGB_556_T0008, BGB_556_T0009, BGB_556_T0010, BGB_556_T0011, BGB_556_T0012, BGB_556_T0013

```python
from bgbcalc import betriebskosten_grundfristende
betriebskosten_grundfristende(
    fristfall='abrechnung',
    bezugsdatum='2010-10-08',
    fristberechnung='taggenau_zwoelf_monate',
    einordnungsnachweis='§556III: zwei explizite Berechnungsweisen ohne automatische Auslegungsentscheidung. LGFrankfurt(Oder)20.11.2012,16S47/12 befürwortet Monatsende192 und dokumentiert die gegenteilige taggenaue Berechnung der Vorinstanz. Hieraus folgt keine Behauptung einer heute universell verbindlichen Auslegung; Auswahl rechtlich belegen. Grundfrist ohne193-Wochenend-/Feiertagskorrektur; diese bei feststehender Anwendbarkeit mit vorhandenem Kalenderkern nachführen. Kein automatischer Ausschluss von Nachforderung oder Einwendung: ordnungsgemäße Abrechnung, Zugang, Vertretenmüssen und Sonderfälle gesondert. Jährliche Abrechnungspflicht ist nicht identisch mit dem anschließenden Mitteilungszeitraum.',
)
```
