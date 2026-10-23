<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## grundbuch_betraglicher_rangumfang

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `rechtsbetrag`: Gesamter bewerteter Betrag des betroffenen Rechts auf derselben Grundlage wie Rangumfang.
- `bezifferter_rangumfang`: Rechtlich bezifferter Umfang der Rangänderung/des Vorbehalts oder des vormerkungsgesicherten Anspruchs; keine ungeprüfte Nominaladdition von Hauptforderung/Zinsen/Kosten.
- `rangfall`: rangvereinbarung_880, rangvorbehalt_881 oder vormerkungsumfang_883.
- `einordnungsnachweis`: Wirksamkeit, betragsgleiche Komponenten und gesetzlicher Schutz anderer Rechte vorqualifizieren. Dieser Baustein verteilt keinen Versteigerungserlös und legt keine Rangvereinbarung aus.

Bezifferten Rangumfang auf Rechtsbetrag begrenzen und beide nicht erfassten Restgrößen getrennt ausweisen.

Erfasster/nicht erfasster Rechtsteil und ungenutzter Rangrahmen; kein Erlösverteilungsplan.

Nur numerische Aufteilung eines ausdrücklich bezifferten Rangumfangs: erfasster Teil=min(Rechtsbetrag,Rangumfang), übriger Rechtsteil=Rechtsbetrag-erfassterTeil, ungenutzter Rahmen=Rangumfang-erfassterTeil.880Vschützt Zwischenrechte;881IVschränkt den Vorbehalt bei zusätzlicher Beeinträchtigung ein;883IIbegrenzt relative Unwirksamkeit auf Anspruchsbeeinträchtigung. Diese Vorschriften liefern keine allgemeine gesetzliche Geldverteilungsformel allein aus Nominalbeträgen. Rechtliche Eintragung/Auslegung und Wirkungen auf fremde Rechte sind vorqualifiziert, kein automatischer vollständiger Rangtausch oder selbst erfundene ZVG-Erlösverteilung.883IIImaßgeblicheVormerkungseintragung mit vorhandenem879-Paarvergleich verwendbar. Rechte mit nicht vergleichbaren Zins-/Nebenleistungsbestandteilen nicht in eine einzige Zahl pressen, sondern rechtlich sachgerechte Komponenten getrennt rechnen. Keine künstliche transitive Gesamtranggruppe aus einzelnen879-Vergleichen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_880_T0001, BGB_880_T0002, BGB_880_T0003, BGB_880_T0004, BGB_880_T0005, BGB_880_T0006, BGB_880_T0007, BGB_881_T0001, BGB_881_T0002, BGB_881_T0003, BGB_881_T0004, BGB_883_T0001, BGB_883_T0002, BGB_883_T0003, BGB_883_T0004, BGB_883_T0005

```python
from bgbcalc import grundbuch_betraglicher_rangumfang
grundbuch_betraglicher_rangumfang(
    rechtsbetrag='120',
    bezifferter_rangumfang='100',
    rangfall='rangvorbehalt_881',
    einordnungsnachweis='Nur numerische Aufteilung eines ausdrücklich bezifferten Rangumfangs: erfasster Teil=min(Rechtsbetrag,Rangumfang), übriger Rechtsteil=Rechtsbetrag-erfassterTeil, ungenutzter Rahmen=Rangumfang-erfassterTeil.880Vschützt Zwischenrechte;881IVschränkt den Vorbehalt bei zusätzlicher Beeinträchtigung ein;883IIbegrenzt relative Unwirksamkeit auf Anspruchsbeeinträchtigung. Diese Vorschriften liefern keine allgemeine gesetzliche Geldverteilungsformel allein aus Nominalbeträgen. Rechtliche Eintragung/Auslegung und Wirkungen auf fremde Rechte sind vorqualifiziert, kein automatischer vollständiger Rangtausch oder selbst erfundene ZVG-Erlösverteilung.883IIImaßgeblicheVormerkungseintragung mit vorhandenem879-Paarvergleich verwendbar. Rechte mit nicht vergleichbaren Zins-/Nebenleistungsbestandteilen nicht in eine einzige Zahl pressen, sondern rechtlich sachgerechte Komponenten getrennt rechnen. Keine künstliche transitive Gesamtranggruppe aus einzelnen879-Vergleichen.',
)
```
