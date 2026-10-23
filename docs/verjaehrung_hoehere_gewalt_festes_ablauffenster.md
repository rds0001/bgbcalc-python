<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_hoehere_gewalt_festes_ablauffenster

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristlauf_erster_tag`: Erster rechtlich maßgeblicher ganzer Fristlauftag.
- `fristende_ohne_diese_hemmung`: Endtag der ohne diese206-Hemmung maßgeblichen Frist; sonstige rechtlich relevante Korrekturen bereits überschneidungsfrei berücksichtigt.
- `verhinderungszeitraeume`: Liste0..10000 abgeschlossener Intervalle mit erster_verhinderter_tag und letzter_verhinderter_tag. Tatsächliche rechtlich qualifizierte Verhinderungstage, nicht schon zugeschnittene Hemmungssummen.
- `fenstermodell`: Ausschließlich fester_ablauf_ohne_206: ausdrücklich rechtlich qualifiziertes festes Sechsmonatsfenster vor dem ohne diese206-Hemmung maßgeblichen Ablauf. Kein stiller Standard oder dynamisches Modell.
- `monatsendregel`: nur_taggleiche_monate oder letzter_monatstag gemäß rueckwaertsfrist_kalendergrenze; Monatsend-Ersatzregel ausdrücklich rechtlich begründen.
- `methodennachweis`: Nichtleere rechtliche Begründung dieses festen Fenstermodells, der Monatsendregel und vollständig abgeschlossener Verhinderungen. Erstinstanzlicher Beleg allein begründet keine universelle Rechtsregel.

Festes rechtlich ausgewähltes Sechsmonatsfenster aus Ausgangsablauf berechnen, auf tatsächlichen Fristlauf begrenzen und bestehende206/209-Schnittmengenrechnung anwenden.

Berechneter erster/letzter Fenstertag, fortgeschriebener letzter Fristtag und berücksichtigte Hemmungstage; nur für ausdrücklich qualifiziertes festes Modell.

Bedingte vollständige206-Fensterarithmetik für das ausdrücklich gewählte feste Ablaufmodell. Sechs Kalendermonate vom Tagesende der Ausgangsfrist rückwärts, Fensterbeginn ist Grenztagesbeginn, frühestens erster Fristlauftag. Verhinderungsintervalle schneiden, Überschneidungen vereinigen und209-Tage fortschreiben. Kein vom Nutzer vorberechneter Fensterbeginn erforderlich. LGRegensburg18.6.2026,45O1916/24,Rn35–37 stützt im dortigen Fall Begrenzung auf festen Zeitraum bis zum Ablauf ohne206; keine Behauptung höchstrichterlicher oder universeller Freigabe. Keine automatische dynamische Fensterverschiebung; deren ursprüngliche Inventarbezeichnung war eine offene Hypothese, kein belegter gesetzlicher Algorithmus. Hindernisse außerhalb des festen Fensters werden in diesem Modell nicht erfasst. Ein fortdauerndes Hindernis ohne rechtlich feststehendes Ende erlaubt keinen endgültigen Ablauf. Weitere Hemmungen nicht doppelt zählen;210/211,Neubeginn und gegebenenfalls193 anschließend gesondert qualifizieren.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_206_T0001, BGB_209_T0001

```python
from bgbcalc import verjaehrung_hoehere_gewalt_festes_ablauffenster
verjaehrung_hoehere_gewalt_festes_ablauffenster(
    fristlauf_erster_tag='2022-01-01',
    fristende_ohne_diese_hemmung='2024-12-31',
    verhinderungszeitraeume=[{'erster_verhinderter_tag': '2024-06-25', 'letzter_verhinderter_tag': '2024-07-05'}],
    fenstermodell='fester_ablauf_ohne_206',
    monatsendregel='letzter_monatstag',
    methodennachweis='Bedingte vollständige206-Fensterarithmetik für das ausdrücklich gewählte feste Ablaufmodell. Sechs Kalendermonate vom Tagesende der Ausgangsfrist rückwärts, Fensterbeginn ist Grenztagesbeginn, frühestens erster Fristlauftag. Verhinderungsintervalle schneiden, Überschneidungen vereinigen und209-Tage fortschreiben. Kein vom Nutzer vorberechneter Fensterbeginn erforderlich. LGRegensburg18.6.2026,45O1916/24,Rn35–37 stützt im dortigen Fall Begrenzung auf festen Zeitraum bis zum Ablauf ohne206; keine Behauptung höchstrichterlicher oder universeller Freigabe. Keine automatische dynamische Fensterverschiebung; deren ursprüngliche Inventarbezeichnung war eine offene Hypothese, kein belegter gesetzlicher Algorithmus. Hindernisse außerhalb des festen Fensters werden in diesem Modell nicht erfasst. Ein fortdauerndes Hindernis ohne rechtlich feststehendes Ende erlaubt keinen endgültigen Ablauf. Weitere Hemmungen nicht doppelt zählen;210/211,Neubeginn und gegebenenfalls193 anschließend gesondert qualifizieren.',
)
```
