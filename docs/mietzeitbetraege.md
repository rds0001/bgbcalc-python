<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## miete_zeitanteiliger_minderungsbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `miete_des_abrechnungsabschnitts`: Nichtnegativer exakter Dezimalwert/Bruch; Mietbetrag in EUR, Gesamtminderungsquote und Zeitanteile zwischen0und1. Homogen bepreister disjunkter Abrechnungsabschnitt.
- `qualifizierte_gesamtminderungsquote`: Nichtnegativer exakter Dezimalwert/Bruch; Mietbetrag in EUR, Gesamtminderungsquote und Zeitanteile zwischen0und1. Homogen bepreister disjunkter Abrechnungsabschnitt.
- `beruecksichtigungsfaehiger_mangelzeitanteil`: Nichtnegativer exakter Dezimalwert/Bruch; Mietbetrag in EUR, Gesamtminderungsquote und Zeitanteile zwischen0und1. Homogen bepreister disjunkter Abrechnungsabschnitt.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten536-/547-Falls und der extern bestimmten Quote/Zeit-/Zahlungszuordnung. Keine gesetzlich ausgeschlossenen Mangelanteile oder unbekannten Bereicherungsfolgen einrechnen.

Miete des homogenen Abrechnungsabschnitts mit qualifizierter Gesamtminderungsquote und berücksichtigungsfähigem Mangelzeitanteil multiplizieren

wert ist der exakte Minderungs- oder Vorauszahlungsrückbetrag in EUR als Bruch.

Nur §536 bei rechtlich qualifizierter Mietminderung und homogener Mietpreis-/Minderungsbasis. Quote0..1 extern bestimmen; vollständige Gebrauchsunmöglichkeit gegebenenfalls1. Gleichzeitige Mängel zuerst zu rechtlich angemessener Gesamtquote zusammenführen, nicht einzelne Quoten blind addieren. Zeitanteil0..1 ohne unerhebliche/ausgeschlossene Beeinträchtigungen, insbesondere §536 Absatz1a und sonstige Ausschlüsse. Bei wechselnden Quoten/Mieten disjunkte Abschnitte getrennt berechnen. Keine Minderungstabelle, kein Marktwertverhältnis aus Kaufminderung, keine automatische Monatslänge oder Dreimonatsausnahmeberechnung.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_536_T0001, BGB_536_T0002

```python
from bgbcalc import miete_zeitanteiliger_minderungsbetrag
miete_zeitanteiliger_minderungsbetrag(
    miete_des_abrechnungsabschnitts='900',
    qualifizierte_gesamtminderungsquote='0.2',
    beruecksichtigungsfaehiger_mangelzeitanteil='0.5',
    einordnungsnachweis='Qualifizierte Gesamtminderung und berücksichtigungsfähige disjunkte Zeit bei homogener Miete.',
)
```

## mietvorauszahlung_zeitanteilige_rueckerstattung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vorausgezahlte_abschnittsmiete`: Nichtnegativer exakter Dezimalwert/Bruch; Mietbetrag in EUR, Gesamtminderungsquote und Zeitanteile zwischen0und1. Homogen bepreister disjunkter Abrechnungsabschnitt.
- `nach_beendigung_liegender_zeitanteil`: Nichtnegativer exakter Dezimalwert/Bruch; Mietbetrag in EUR, Gesamtminderungsquote und Zeitanteile zwischen0und1. Homogen bepreister disjunkter Abrechnungsabschnitt.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten536-/547-Falls und der extern bestimmten Quote/Zeit-/Zahlungszuordnung. Keine gesetzlich ausgeschlossenen Mangelanteile oder unbekannten Bereicherungsfolgen einrechnen.

Vorausgezahlte Miete eines homogen bepreisten Abschnitts mit dem nach Vertragsende liegenden Zeitanteil multiplizieren

wert ist der exakte Minderungs- oder Vorauszahlungsrückbetrag in EUR als Bruch.

Nur §547 Absatz1 Satz1 bei qualifiziert vom Vermieter zu vertretender Beendigung und einem gleichmäßig bepreisten Vorauszahlungsabschnitt. Zahlung muss gerade diesen Abschnitt betreffen; Zeitanteil0..1 rechtlich bestimmen. Unterschiedliche Preise/Zahlungszuordnungen abschnittsweise rechnen. Bei nicht zu vertretender Beendigung Bereicherungsrecht nach Satz2 gesondert, kein automatischer identischer Rückbetrag. Gesetzliche Zinsen ab jeweiligem Empfang mit vorhandenem Zinskern separat berechnen; keine automatische pauschale Verzinsung vor Eingang.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_547_T0001

```python
from bgbcalc import mietvorauszahlung_zeitanteilige_rueckerstattung
mietvorauszahlung_zeitanteilige_rueckerstattung(
    vorausgezahlte_abschnittsmiete='900',
    nach_beendigung_liegender_zeitanteil='0.5',
    einordnungsnachweis='Vom Vermieter zu vertretende Beendigung und eindeutiger homogener Vorauszahlungsabschnitt.',
)
```
