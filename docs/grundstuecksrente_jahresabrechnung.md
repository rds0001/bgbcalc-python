<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## grundstuecksrente_jahresabrechnung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `jahresrentenbetrag`: Rechtlich bewerteter nichtnegativer Jahresbetrag der Überbau-/Notwegrente in EUR.
- `rentenjahr_beginnt_am`: ISO-Datum des ersten eingeschlossenen Tages des rechtlich bestimmten Rentenjahrs; Regelzahlung jährlich im Voraus. Kein automatisch gewähltes Kalenderjahr.
- `berechtigungszeitraum_von`: Erster eingeschlossener ganzer Kalendertag der zuzuordnenden Berechtigung beziehungsweise Rentenpflicht im betrachteten Abrechnungsabschnitt.
- `berechtigungszeitraum_bis`: Letzter eingeschlossener ganzer Kalendertag dieses Abschnitts. Zeitraum darf über Rentenjahr hinausreichen; die Funktion berechnet die Schnittmenge. Bei Eigentumsübertragung nach§915II den rechtlich qualifizierten letzten Rententag vorgeben.
- `einordnungsnachweis`: Nichtleere Qualifikation von §§913/917, gegebenenfalls915II, und zeitanteiliger Zuordnung nach§101Nr2 nach tatsächlichen Kalendertagen. Untertägige Zeitanteile und abweichende wirksame Vereinbarungen nicht als ganze Tage ausgeben.

Rentenjahr ab Tagesbeginn bestimmen; Schnittmenge mit Berechtigungszeitraum zählen und Jahresbetrag nach tatsächlichen Tagen zuordnen.

wert enthält rentenjahr_endet_am, regel_vorauszahlung_am, tage_im_rentenjahr, zugeordnete_tage, jahresvorauszahlungsbetrag und zeitanteilig_zugeordneter_betrag. Geldwerte als exakte Brüche; keine automatische Zahlungssaldierung.

Gesetzlicher Jahresvorauszahlungsfall §§913II/917II; Jahresrentenhöhe und Ausgangstag rechtlich bestimmt. §101Nr2 zeitanteilige Zuordnung regelmäßig wiederkehrender Erträge bei begrenztem Bezugszeitraum; tatsächliche Kalendertage der Schnittmenge durch tatsächliche Tage des Rentenjahrs teilen. Kein pauschales365-Tage-Jahr und keine Übernahme der Sonderregel voller begonnener Leibrentenperioden aus§760. §915I Grundstückswert ist historische Bewertung, kein von der Bibliothek geschätzter Preis; bis zur rechtlich bestimmten Übertragung bleibt die Rentenpflicht nachII maßgeblich. Jahresvorauszahlungsbetrag und zugeordneter Zeitanteil getrennt: keine automatische Rückforderung bereits bezahlter Beträge oder doppelte zusätzliche Forderung. Andere Eigentümer getrennt mit überschneidungsfreien Berechtigungszeiten abrechnen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_101_T0001, BGB_101_T0002, BGB_101_T0003, BGB_913_T0001, BGB_913_T0002, BGB_915_T0001, BGB_915_T0002, BGB_915_T0003, BGB_917_T0001, BGB_917_T0002, BGB_917_T0003, BGB_917_T0004

```python
from bgbcalc import grundstuecksrente_jahresabrechnung
grundstuecksrente_jahresabrechnung(
    jahresrentenbetrag='366',
    rentenjahr_beginnt_am='2024-01-01',
    berechtigungszeitraum_von='2024-01-01',
    berechtigungszeitraum_bis='2024-12-31',
    einordnungsnachweis='Gesetzlicher Jahresvorauszahlungsfall §§913II/917II; Jahresrentenhöhe und Ausgangstag rechtlich bestimmt. §101Nr2 zeitanteilige Zuordnung regelmäßig wiederkehrender Erträge bei begrenztem Bezugszeitraum; tatsächliche Kalendertage der Schnittmenge durch tatsächliche Tage des Rentenjahrs teilen. Kein pauschales365-Tage-Jahr und keine Übernahme der Sonderregel voller begonnener Leibrentenperioden aus§760. §915I Grundstückswert ist historische Bewertung, kein von der Bibliothek geschätzter Preis; bis zur rechtlich bestimmten Übertragung bleibt die Rentenpflicht nachII maßgeblich. Jahresvorauszahlungsbetrag und zugeordneter Zeitanteil getrennt: keine automatische Rückforderung bereits bezahlter Beträge oder doppelte zusätzliche Forderung. Andere Eigentümer getrennt mit überschneidungsfreien Berechtigungszeiten abrechnen.',
)
```
