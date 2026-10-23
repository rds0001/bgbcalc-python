<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_abhaengige_nebenleistung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `hauptanspruch_letzter_tag`: ISO-Datum0001..9999 des rechtlich maßgeblichen letzten Tages vor Verjährung des Hauptanspruchs, einschließlich aller für ihn geltenden Fristveränderungen. Nicht bloß seine unmodifizierte Grundfrist.
- `nebenleistung_eigener_letzter_tag`: ISO-Datum0001..9999 des rechtlich maßgeblichen letzten Tages vor der eigenen Verjährung dieser Nebenleistung, unabhängig von der zusätzlichen Grenze§217. Frühere eigene Verjährung bleibt erhalten.
- `nebenleistung_abhaengig`: Wahrheitswert der rechtlichen Abhängigkeit der konkreten Nebenleistung vom bezeichneten Hauptanspruch im Sinne§217. Nicht jede andere Forderung zwischen denselben Parteien ist abhängig. FALSE ergibt NICHT_ANWENDBAR.
- `fristnachweis`: Nichtleere Beschreibung der rechtlichen Abhängigkeit und beider vollständig bestimmten Fristläufe. Hemmungen/Neubeginne je Anspruch korrekt berücksichtigen, nicht erst nach Auswahl dieses Minimums pauschal addieren.

Bei abhängiger Nebenleistung früheren letzten Tag aus Hauptanspruchsverjährung und eigener Nebenleistungsverjährung wählen.

wert ist ISO-Datum des maßgeblichen letzten unverjährten Tages der abhängigen Nebenleistung. Ohne Abhängigkeit NICHT_ANWENDBAR/null.

Nur Kombination zweier zuvor rechtlich bestimmter Fristgrenzen. Keine automatische Abhängigkeit, Einredeerhebung oder Berechnung der einzelnen Fristläufe. Frühere eigene Nebenleistungsverjährung nicht auf späteren Haupttermin verlängern.

ISO-Daten0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_217_T0001

```python
from bgbcalc import verjaehrung_abhaengige_nebenleistung
verjaehrung_abhaengige_nebenleistung(
    hauptanspruch_letzter_tag='2024-12-31',
    nebenleistung_eigener_letzter_tag='2024-12-31',
    nebenleistung_abhaengig=True,
    fristnachweis='Synthetisch abschließend bestimmte eigenständige Fristläufe und rechtliche Abhängigkeit.',
)
```

## verjaehrung_aufrechnung_zurueckbehaltung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `letzter_tag_vor_verjaehrung`: ISO-Datum0001..9999 des rechtlich maßgeblichen letzten unverjährten Tages zum Tagesschluss. Alle einschlägigen Hemmungen, Ablaufhemmungen, Neubeginne und gegebenenfalls Werktagsverschiebungen zuvor bestimmen; keine ungeprüfte Grundfrist.
- `erstmals_ausuebbar_am`: ISO-Datum0001..9999, an dem das ausgewählte Recht erstmals rechtlich ausgeübt werden konnte. Bei Aufrechnung erstmalige geeignete Gegenüberstellung nach allen Voraussetzungen, nicht bloß Entstehung der eigenen Forderung. Taggenaue rechtliche Normalisierung; untertägige Besonderheiten gesondert.
- `rechtsart`: Auswahl aufrechnung oder zurueckbehaltung. Bei Zurückbehaltung maßgeblichen Zeitpunkt erstmaliger Leistungsverweigerungsmöglichkeit eingeben, nicht automatisch Aufrechnungslage übernehmen.
- `einordnungsnachweis`: Nichtleere Beschreibung des Anspruchs, abschließend bestimmten Verjährungstags und rechtlich ersten Ausübbarkeitszeitpunkts des ausgewählten Rechts. Weitere Ausschlüsse separat.

Prüfen, ob erstmalige rechtliche Ausübbarkeit spätestens am letzten unverjährten Tag lag. Dann schließt spätere Verjährung das gewählte Recht nach§215 nicht aus.

wert ist Wahrheitswert: TRUE erfüllt zeitliche Erhaltungsbedingung§215. FALSE ist keine umfassende Entscheidung über andere Rechtsgrundlagen.

Nur gesetzliches Erhaltungsprivileg, keine Prüfung aller Aufrechnungsvoraussetzungen oder sonstiger Zurückbehaltungsausschlüsse. Kein Wiederaufleben eines bereits vor erster Ausübbarkeit verjährten Anspruchs durch diese Funktion.

ISO-Daten0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_215_T0001

```python
from bgbcalc import verjaehrung_aufrechnung_zurueckbehaltung
verjaehrung_aufrechnung_zurueckbehaltung(
    letzter_tag_vor_verjaehrung='2025-12-31',
    erstmals_ausuebbar_am='2025-12-30',
    rechtsart='aufrechnung',
    einordnungsnachweis='Synthetisch abschließend bestimmte Verjährung und erstmalige rechtliche Ausübbarkeit.',
)
```
