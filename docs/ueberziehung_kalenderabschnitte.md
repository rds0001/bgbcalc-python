<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ueberziehung_kalenderabschnitte

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kontosaldoabschnitte`: 1..10000 vollstaendige lueckenlose Abschnitte mit erster_tag, letzter_tag (je einschliesslich) und ueberziehungsbetrag. Guthaben mit0einbeziehen.
- `bezugsbetrag`: 504aunveraenderte Kreditlinie;505gesamter qualifizierter Geldeingang der letzten drei Monate, nicht schon dessen Monatsdurchschnitt.
- `vergleichsregel`: kreditlinie_504a oder geduldete_ueberziehung_505.
- `einordnungsnachweis`: Vollstaendiger Beobachtungszeitraum, Tagesbeginn/-ende, rechtlich anwendbare zeitgewichtete Mittelung und Bezugsbetrag qualifizieren. Vierteljaehrlichen Rechnungsabschluss als Pruefstichtag gemaess504aI2/505II3 bestimmen.

Lueckenlose tatsaechliche Kalendertage je Kontosaldoabschnitt bestimmen, Kalender-Monatsgrenzen berechnen und vorhandenen Betragstage-Durchschnittskern verwenden.

Beobachtungsgrenzen, Ein-/Drei-/Sechsmonatsablaeufe und Dauerschwellen sowie vollstaendiges Ergebnis des bestehenden Durchschnittskerns.

§504aI/505II: tatsaechliche lueckenlose Tagesabschnitte sortieren, Ueberschneidungen/Luecken ablehnen, Dauer und Betragstage mit bestehendem Durchschnittskern rechnen. Kalendermonate nach187II/188: sechs Monate einschliesslich Ablauf, mehr als ein/drei Monate strikt nach jeweiligem Ablauf; keine180/90/30-Tage-Ersatzregel. Erste Nutzung und Ende als ganze rechtlich qualifizierte Tage, keine Rundung untertaegiger Ereignisse. Nullsaldoabschnitt bleibt in Mittelung enthalten und widerlegt ununterbrochene positive Ueberziehung. Bei vierteljaehrlichem Abschluss ist504aI2am jeweiligen Abschluss zu beurteilen;505II3nennt ausdruecklich die Informationsvoraussetzungen vonSatz1. Datum des bankvertraglichen Abschlusses vorgeben, nicht automatisch Kalenderquartal unterstellen. Die Berechnung am gewaehlten Beobachtungsende ersetzt keine gesetzliche Stichtagsqualifikation.505II2: Bezugsbetrag gesamter Geldeingang der letzten3Monate, Vergleichsgrenze dessen1/6; Bezugseingangsfenster rechtlich separat bestimmen. Veraenderliche Kreditlinie und andere Mittelungskonventionen nicht automatisch behandeln. Keine vollstaendige Beratungs-/Informationsentscheidung aus reinem Zahlenvergleich.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_504a_T0001, BGB_504a_T0002, BGB_504a_T0003, BGB_504a_T0004, BGB_505_T0003, BGB_505_T0004, BGB_505_T0005

```python
from bgbcalc import ueberziehung_kalenderabschnitte
ueberziehung_kalenderabschnitte(
    kontosaldoabschnitte=[{'erster_tag': '2024-01-01', 'letzter_tag': '2024-03-31', 'ueberziehungsbetrag': '80'}, {'erster_tag': '2024-04-01', 'letzter_tag': '2024-06-30', 'ueberziehungsbetrag': '100'}],
    bezugsbetrag='100',
    vergleichsregel='kreditlinie_504a',
    einordnungsnachweis='§504aI/505II: tatsaechliche lueckenlose Tagesabschnitte sortieren, Ueberschneidungen/Luecken ablehnen, Dauer und Betragstage mit bestehendem Durchschnittskern rechnen. Kalendermonate nach187II/188: sechs Monate einschliesslich Ablauf, mehr als ein/drei Monate strikt nach jeweiligem Ablauf; keine180/90/30-Tage-Ersatzregel. Erste Nutzung und Ende als ganze rechtlich qualifizierte Tage, keine Rundung untertaegiger Ereignisse. Nullsaldoabschnitt bleibt in Mittelung enthalten und widerlegt ununterbrochene positive Ueberziehung. Bei vierteljaehrlichem Abschluss ist504aI2am jeweiligen Abschluss zu beurteilen;505II3nennt ausdruecklich die Informationsvoraussetzungen vonSatz1. Datum des bankvertraglichen Abschlusses vorgeben, nicht automatisch Kalenderquartal unterstellen. Die Berechnung am gewaehlten Beobachtungsende ersetzt keine gesetzliche Stichtagsqualifikation.505II2: Bezugsbetrag gesamter Geldeingang der letzten3Monate, Vergleichsgrenze dessen1/6; Bezugseingangsfenster rechtlich separat bestimmen. Veraenderliche Kreditlinie und andere Mittelungskonventionen nicht automatisch behandeln. Keine vollstaendige Beratungs-/Informationsentscheidung aus reinem Zahlenvergleich.',
)
```
