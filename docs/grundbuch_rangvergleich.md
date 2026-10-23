<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## grundbuch_rangpaarvergleich

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `erstes_recht`: Objekt mit genau recht_id, abteilung (einheitliche nichtleere Kennung), eintragungsposition (positive ganze tatsächliche Reihenfolgenummer innerhalb der Abteilung) und eintragungstagYYYY-MM-DD.
- `zweites_recht`: Zweites verschiedenes wirksam eingetragenes Grundstücksrecht mit denselben Feldern; dasselbe belastete Grundstück.
- `einordnungsnachweis`: Nichtleerer Nachweis der879I/II-Grundregel, wirksamer Rechte und tatsächlicher Eintragungsdaten/Positionen. Keine eingetragene abweichende Rangbestimmung879III, keine nachträgliche Rangänderung.

Zwei Grundstücksrechte nach abteilungsabhängigem Eintragungsmaßstab paarweise vergleichen.

wert.rangvergleich:-1 erstes Recht vorrangig,0gleichrangig,+1zweites Recht vorrangig; vergleichsmassstab eintragungsreihenfolge oder eintragungstag.

§879I/II: in derselben Grundbuchabteilung tatsächliche Reihenfolge der Eintragungen vergleichen; in verschiedenen Abteilungen angegebenen Eintragungstag vergleichen, bei gleichem Tag Gleichrang. Zeitpunkt einer späteren dinglichen Einigung ersetzt den Eintragungsmaßstab nicht. Position ist wirkliche Reihenfolge, nicht ungeprüft laufende Nummer eines Rechts oder Antragsnummer. Nur Paarvergleich: bei mehreren Rechten keine transitive globale Ranggruppe aus einzelnen Gleichrangvergleichen erfinden. Abweichende eingetragene Rangbestimmung,880Rangänderung,881Vorbehalt,883Vormerkung und Verwertungsbeträge gesondert. Gleiche Position verschiedener Rechte derselben Abteilung wird mangels eindeutig qualifizierter Reihenfolge nicht angenommen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_879_T0001, BGB_879_T0002, BGB_879_T0003

```python
from bgbcalc import grundbuch_rangpaarvergleich
grundbuch_rangpaarvergleich(
    erstes_recht={'recht_id': 'A', 'abteilung': 'II', 'eintragungsposition': 1, 'eintragungstag': '2024-01-02'},
    zweites_recht={'recht_id': 'B', 'abteilung': 'II', 'eintragungsposition': 2, 'eintragungstag': '2024-01-03'},
    einordnungsnachweis='§879I/II: in derselben Grundbuchabteilung tatsächliche Reihenfolge der Eintragungen vergleichen; in verschiedenen Abteilungen angegebenen Eintragungstag vergleichen, bei gleichem Tag Gleichrang. Zeitpunkt einer späteren dinglichen Einigung ersetzt den Eintragungsmaßstab nicht. Position ist wirkliche Reihenfolge, nicht ungeprüft laufende Nummer eines Rechts oder Antragsnummer. Nur Paarvergleich: bei mehreren Rechten keine transitive globale Ranggruppe aus einzelnen Gleichrangvergleichen erfinden. Abweichende eingetragene Rangbestimmung,880Rangänderung,881Vorbehalt,883Vormerkung und Verwertungsbeträge gesondert. Gleiche Position verschiedener Rechte derselben Abteilung wird mangels eindeutig qualifizierter Reihenfolge nicht angenommen.',
)
```
