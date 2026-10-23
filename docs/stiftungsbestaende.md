<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## stiftung_grundstock_soll_ist_vergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `erforderlicher_erhaltungswert`: Rechtlich und nach zutreffendem Bewertungsmaßstab qualifizierter Sollwert des zu erhaltenden Grundstocks in Euro.
- `vorhandener_erhaltungswert`: Nach demselben Bewertungsmaßstab und Stichtag ermittelter vorhandener Grundstockwert in Euro.
- `einordnungsnachweis`: Nichtleerer Nachweis der83cI-Erhaltungsanforderung und vergleichbarer Bewertungen; Satzung, Landesrecht und zulässige vorübergehende Verbrauchsausnahmen bereits berücksichtigt.

Qualifizierten Erhaltungs-Sollwert und vorhandenen Grundstockwert vergleichen, Unterdeckung und Mehrbestand getrennt ausweisen.

wert.rechnerische_unterdeckung und rechnerischer_mehrbestand als exakte Eurobrüche; sollwert_erreicht als Wahrheitswert.

§83cI: ausschließlich numerischer Soll/Ist-Vergleich unter rechtlich qualifiziertem Erhaltungsmaßstab. Keine selbst erfundene Wahl zwischen nominaler, realer oder gegenständlicher Kapitalerhaltung, keine automatische Inflationsindexierung. Positiver Mehrbestand ist weder automatisch verwendbarer Umschichtungsgewinn noch ausschüttbarer Ertrag. Zulässiger Verbrauch und Wiederaufstockung83cII bleiben getrennt.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_83c_T0001, BGB_83c_T0002, BGB_83c_T0003

```python
from bgbcalc import stiftung_grundstock_soll_ist_vergleich
stiftung_grundstock_soll_ist_vergleich(
    erforderlicher_erhaltungswert='1000',
    vorhandener_erhaltungswert='900',
    einordnungsnachweis='§83cI: ausschließlich numerischer Soll/Ist-Vergleich unter rechtlich qualifiziertem Erhaltungsmaßstab. Keine selbst erfundene Wahl zwischen nominaler, realer oder gegenständlicher Kapitalerhaltung, keine automatische Inflationsindexierung. Positiver Mehrbestand ist weder automatisch verwendbarer Umschichtungsgewinn noch ausschüttbarer Ertrag. Zulässiger Verbrauch und Wiederaufstockung83cII bleiben getrennt.',
)
```

## stiftung_uebertragene_vermoegensbestaende

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `grundstock_uebernehmende_stiftung`: Qualifizierter Grundstockwert der übernehmenden Stiftung unmittelbar vor wirksamer Übertragung in Euro; bei neuer Stiftung ohne Anfangsbestand0.
- `sonstiges_vermoegen_uebernehmende_stiftung`: Qualifizierter sonstiger Vermögenswert der übernehmenden Stiftung vor Übertragung in Euro.
- `uebertragende_stiftungen`: Liste1..1000 mit genau stiftung_id, grundstockvermoegen, sonstiges_vermoegen; eindeutige Kennungen, nichtnegative Euro-Werte unter gemeinsamem Bewertungsmaßstab.
- `einordnungsnachweis`: Nichtleerer Nachweis wirksamer Zulegung/Zusammenlegung86c/86f, vollständiger überschneidungsfreier Bestände und gemeinsamer Bewertung; Mindestzahl einer Zusammenlegung rechtlich vorgeprüft.

Grundstock und sonstige Vermögensbestände wirksam übertragender Stiftungen getrennt zum Bestand der übernehmenden Stiftung addieren.

wert.grundstockvermoegen_nach_uebertragung, sonstiges_vermoegen_nach_uebertragung und gesamtvermoegen_nach_uebertragung als exakte Eurobrüche.

§86cI2/II und86fI/II: vollständig übertragene qualifizierte Vermögensbestände addieren, Grundstock getrennt als Grundstock fortführen. Kein mehrfaches Einrechnen schon in der übernehmenden Stiftung erfasster Übertragungen. Nichtnegative qualifizierte Vermögenswerte, keine automatische Saldierung von Verbindlichkeiten oder konzerninternen Forderungen, keine rechtliche Übertragungswirksamkeit/Neugründung. Genehmigung, Unanfechtbarkeit und Zahl übertragender Stiftungen bei Zusammenlegung gesondert; keine künstliche Umwidmung sonstigen Vermögens in Grundstock.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_86c_T0001, BGB_86c_T0002, BGB_86c_T0003, BGB_86c_T0004, BGB_86c_T0005, BGB_86f_T0001, BGB_86f_T0002

```python
from bgbcalc import stiftung_uebertragene_vermoegensbestaende
stiftung_uebertragene_vermoegensbestaende(
    grundstock_uebernehmende_stiftung='1000',
    sonstiges_vermoegen_uebernehmende_stiftung='100',
    uebertragende_stiftungen=[{'stiftung_id': 'A', 'grundstockvermoegen': '200', 'sonstiges_vermoegen': '20'}, {'stiftung_id': 'B', 'grundstockvermoegen': '300', 'sonstiges_vermoegen': '30'}],
    einordnungsnachweis='§86cI2/II und86fI/II: vollständig übertragene qualifizierte Vermögensbestände addieren, Grundstock getrennt als Grundstock fortführen. Kein mehrfaches Einrechnen schon in der übernehmenden Stiftung erfasster Übertragungen. Nichtnegative qualifizierte Vermögenswerte, keine automatische Saldierung von Verbindlichkeiten oder konzerninternen Forderungen, keine rechtliche Übertragungswirksamkeit/Neugründung. Genehmigung, Unanfechtbarkeit und Zahl übertragender Stiftungen bei Zusammenlegung gesondert; keine künstliche Umwidmung sonstigen Vermögens in Grundstock.',
)
```
