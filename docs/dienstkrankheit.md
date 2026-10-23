<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dienst_krankenfuersorge_zeitraum

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erkrankungsbeginn_am`: ISO-Datum0001..9999 des rechtlich maßgeblichen Beginns der konkreten Erkrankung während des Dienstverhältnisses. Keine ungeprüfte Zusammenfassung verschiedener Krankheitsfälle.
- `beginnart`: Auswahl tagesbeginn bei mitzuzählendem ersten Krankheitstag ab Tagesbeginn oder ereignis bei rechtlich einschlägigem Ereignisbeginn. Untertägige Tatsachen vorab rechtlich einordnen.
- `dienstverhaeltnis_ende_am`: ISO-Datum0001..9999 des rechtlich letzten Diensttags einschließlich, mindestens Erkrankungsbeginn. NULL/None bedeutet im betrachteten Zeitraum fortbestehendes Dienstverhältnis ohne früheren feststehenden Endtag; kein unbekanntes Ende fiktiv ersetzen.
- `dauerndes_hauptdienstverhaeltnis`: Wahrheitswert: dauerndes Dienstverhältnis, das Erwerbstätigkeit des Verpflichteten vollständig oder hauptsächlich in Anspruch nimmt. Dauernd/hauptsächlich rechtlich beurteilen, keine erfundene feste Wochenstundengrenze.
- `in_haeusliche_gemeinschaft_aufgenommen`: Wahrheitswert der Aufnahme in die häusliche Gemeinschaft des Dienstberechtigten. Bloßer Arbeitsort im Haushalt ist nicht ungeprüft ausreichend.
- `erkrankung_vorsaetzlich_oder_grob_fahrlaessig`: Wahrheitswert der vorsätzlichen oder grob fahrlässigen Herbeiführung der konkreten Erkrankung durch Dienstverpflichteten; einfache Fahrlässigkeit nicht gleichsetzen.
- `versicherung_oder_oeffentliche_krankenpflege`: Wahrheitswert, dass für gerade erforderliche Verpflegung und ärztliche Behandlung durch Versicherung oder öffentliche Krankenpflege Vorsorge getroffen ist. Nicht jede beliebige Versicherung genügt; dann tritt diese Verpflichtung nicht ein.
- `krankheitskuendigung_626_durch_dienstberechtigten`: Wahrheitswert, dass das angegebene Dienstende gerade durch Kündigung des Dienstberechtigten nach§626 wegen der Erkrankung herbeigeführt wurde. Nur dann Dienstende für Fürsorgegrenze außer Betracht lassen.
- `einordnungsnachweis`: Nichtleere Begründung von Dienst-/Wohnverhältnissen, Erkrankung/Beginnart, Verschulden, anderweitiger Vorsorge und gegebenenfalls genauer Kündigungsursache.

Qualifizierter Dienst-/Haushaltsfall ohne schweren Eigenverursachungs- oder Vorsorgeausschluss: Sechswochengrenze. Früheres Dienstende begrenzt, außer gerade krankheitsbedingter§626-Kündigung durch Dienstberechtigten.

wert enthält sechswochengrenze und fuersorge_spaetestens_bis als ISO-Daten. Ohne gesetzlichen Tatbestand NICHT_ANWENDBAR/null.

Nur Höchstdauer erforderlicher Fürsorge; Genesung/Erforderlichkeitswegfall kann früher enden. Keine allgemeine Entgeltfortzahlung. Taggenaues Modell, keine automatische§193-Verlängerung.

ISO-Daten und berechnete Grenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_617_T0001, BGB_617_T0004, BGB_617_T0005

```python
from bgbcalc import dienst_krankenfuersorge_zeitraum
dienst_krankenfuersorge_zeitraum(
    erkrankungsbeginn_am='2024-02-29',
    beginnart='tagesbeginn',
    dienstverhaeltnis_ende_am='2024-03-15',
    dauerndes_hauptdienstverhaeltnis=True,
    in_haeusliche_gemeinschaft_aufgenommen=True,
    erkrankung_vorsaetzlich_oder_grob_fahrlaessig=False,
    versicherung_oder_oeffentliche_krankenpflege=False,
    krankheitskuendigung_626_durch_dienstberechtigten=False,
    einordnungsnachweis='Synthetisch qualifizierter häuslicher Dienstfall mit belegter Erkrankung und rechtlichen Ausschluss-/Kündigungstatbeständen.',
)
```

## dienst_krankheitskosten_anrechnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verguetung_erkrankungszeit`: Nichtnegative exakte EUR-Zahl als Dezimalzeichenfolge oder Bruchobjekt der für den konkreten Erkrankungszeitraum tatsächlich geschuldeten Vergütung. Anspruch und Zeitraum vorher bestimmen, keine allgemeine Entgeltfortzahlung aus§617 ableiten.
- `anrechenbare_fuersorgekosten`: Nichtnegative exakte EUR-Zahl rechtlich anrechenbarer Kosten erforderlicher Verpflegung/ärztlicher Behandlung nach§617 im zugehörigen Zeitraum; keine unbereinigten Gesamtkosten oder schon anderweitig gedeckten Ausgaben.
- `kostenanrechnung_nach_617_zulaessig`: Wahrheitswert, dass die besondere Kostenanrechnung§617 Absatz1 Satz3 für diesen Dienst-/Fürsorgefall zulässig ist; Fürsorgevoraussetzungen und entgegenstehende Regeln vorab prüfen. FALSE ergibt NICHT_ANWENDBAR.
- `anrechnung_ausgeuebt`: Wahrheitswert der rechtlich ausgeübten Anrechnung. Gesetzliches Können ist keine automatische Lohnkürzung; bei FALSE Anrechnung0 und volle eingegebene Vergütung verbleibend.
- `kostennachweis`: Nichtleere Beschreibung der tatsächlichen/erforderlichen Kosten, deckungsgleichen Vergütungsperiode, konsistenten Brutto-/Nettobasis und Ausübung der Anrechnung. Keine Doppelanrechnung.

Zulässige ausgeübte Anrechnung=min(qualifizierte Kosten, zugehörige Vergütung); verbleibende Vergütung=Vergütung−Anrechnung. Ohne Ausübung Anrechnung0.

wert enthält angerechnete_kosten und verbleibende_verguetung als exakte EUR-Brüche. Ohne Anwendbarkeit NICHT_ANWENDBAR/null.

Keine negative Vergütung oder eigenständige Erstattungspflicht aus übersteigenden Kosten; andere Rechtsgrundlagen separat. Anspruch auf Vergütung und Zulässigkeit der Fürsorgekosten vorab rechtlich bestimmen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_617_T0003

```python
from bgbcalc import dienst_krankheitskosten_anrechnung
dienst_krankheitskosten_anrechnung(
    verguetung_erkrankungszeit='0',
    anrechenbare_fuersorgekosten='0',
    kostenanrechnung_nach_617_zulaessig=True,
    anrechnung_ausgeuebt=False,
    kostennachweis='Synthetisch zugehörige Vergütung und erforderliche anrechenbare Fürsorgekosten ohne Doppelanrechnung.',
)
```
