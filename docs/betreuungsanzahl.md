<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betreuungen_im_qualifizierten_zweijahresfenster

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `prueftag`: Maßgeblicher Tag YYYY-MM-DD.
- `rueckblick_erster_tag`: Rechtlich qualifizierter erster eingeschlossener Tag des Zweijahresrückblicks YYYY-MM-DD. Keine beliebige Dauer; Grenztag und untertägige Fälle müssen zuvor qualifiziert sein.
- `betreuungszeitraeume`: Liste0..1000 Zeiträume mit betreuungs_id und erster_tag und letzter_tag als eingeschlossene ISO-Tage. Laufende Betreuung mit letzter_tag gleich prueftag abschneiden; keine unbekannte Beendigung erfinden. Mehrere getrennte Zeiträume derselben Betreuung mit gleicher betreuungs_id angeben; diese Betreuung wird höchstens einmal gezählt. Keine Lücken durch Zusammenziehen überbrücken.
- `einordnungsnachweis`: Nichtleerer Nachweis1861II: qualifiziertes Zweijahresfenster und vollständige Betreuungshistorie einschließlich am Prüftag geführter Betreuungen, Identität der einzelnen Betreuungen und Tagesnormalisierung.

Eindeutige Betreuungen im qualifizierten Zweijahresfenster zählen und strikt mit eins vergleichen.

wert.beruecksichtigte_betreuungs_ids als Liste in Eingabereihenfolge, anzahl_betreuungen ganzzahlig und mehr_als_eine_betreuung als Wahrheitswert.

§1861II: Zahl unterschiedlicher Betreuungen zählen, die am Prüftag geführt werden oder das vorqualifizierte eingeschlossene Zweijahresfenster schneiden. Mehr als eine bedeutet strikt mindestens zwei; nicht Anzahl einzelner Tätigkeitstage oder unterschiedlicher Betreuer. Keine automatische Pflichtbefreiung oder Festlegung eines ungeklärten rückwärts zu berechnenden Grenztags. Nicht zusammenhängende Zeiträume derselben Betreuung werden getrennt auf Schnittmenge geprüft; gezählt wird die eindeutige Betreuung, nicht ihre Zeiträume.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1861_T0002, BGB_1861_T0003

```python
from bgbcalc import betreuungen_im_qualifizierten_zweijahresfenster
betreuungen_im_qualifizierten_zweijahresfenster(
    prueftag='2026-10-21',
    rueckblick_erster_tag='2024-10-22',
    betreuungszeitraeume=[{'betreuungs_id': 'A', 'erster_tag': '2020-01-01', 'letzter_tag': '2026-10-21'}, {'betreuungs_id': 'B', 'erster_tag': '2024-10-22', 'letzter_tag': '2024-10-22'}],
    einordnungsnachweis='§1861II: Zahl unterschiedlicher Betreuungen zählen, die am Prüftag geführt werden oder das vorqualifizierte eingeschlossene Zweijahresfenster schneiden. Mehr als eine bedeutet strikt mindestens zwei; nicht Anzahl einzelner Tätigkeitstage oder unterschiedlicher Betreuer. Keine automatische Pflichtbefreiung oder Festlegung eines ungeklärten rückwärts zu berechnenden Grenztags. Nicht zusammenhängende Zeiträume derselben Betreuung werden getrennt auf Schnittmenge geprüft; gezählt wird die eindeutige Betreuung, nicht ihre Zeiträume.',
)
```
