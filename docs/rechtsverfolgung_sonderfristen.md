<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## rechtsverfolgung_sondergrundfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristfall`: eilverfahren_zustellung_204, behoerdliche_vorentscheidung_204, gerichtsstandsbestimmung_204 oder verbandsunterlassung_zustellung_204a.
- `ereignis_am`: ISO-Datum des für den ausgewählten Fall gesetzlich maßgeblichen Ereignisses; Zuordnung im Nachweis belegen.
- `einordnungsnachweis`: Nichtleerer Nachweis von Fall, Fristauslöser und rechtlich erforderlichen gesonderten Fristkorrekturen.

Gesetzlich ausgewählte Ein- oder Dreimonats-Ereignisgrundfrist mit vorhandenem Kalenderkern berechnen.

wert.rechnerisches_fristende alsYYYY-MM-DD vor gesonderten Korrekturen.

§204I9: maßgebliche Verkündung oder Zustellung an Gläubiger, danach Monatsfrist zur Zustellung an Schuldner.204I12: Erledigung des behördlichen Gesuchs, danach drei Monate für Klage/zulässigen Folgeantrag;204I13 entsprechend nach Erledigung des Gerichtsstandsbestimmungsgesuchs.204aI2: maßgebliche Verkündung oder Zustellung der einstweiligen Verfügung an Antragsteller, danach Monat zur Zustellung an Antragsgegner. Fristauslöser rechtlich vorqualifizieren, nicht Antragseinreichung oder Kenntnis frei einsetzen. Nur Grundfristen: entsprechende206/210/211-Korrekturen nach204III für die dort genannten204-Fälle zusätzlich, keine ungeprüfte Übertragung dieses Verweises auf204aI2.193 bei feststehender Anwendung gesondert. Keine automatische Hemmungs-/Rückwirkungsentscheidung, keine Berechnung aus dem KapMuG außerhalb desBGB.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_204_T0016, BGB_204_T0021, BGB_204_T0022, BGB_204_T0027, BGB_204a_T0010

```python
from bgbcalc import rechtsverfolgung_sondergrundfrist
rechtsverfolgung_sondergrundfrist(
    fristfall='eilverfahren_zustellung_204',
    ereignis_am='2024-01-31',
    einordnungsnachweis='§204I9: maßgebliche Verkündung oder Zustellung an Gläubiger, danach Monatsfrist zur Zustellung an Schuldner.204I12: Erledigung des behördlichen Gesuchs, danach drei Monate für Klage/zulässigen Folgeantrag;204I13 entsprechend nach Erledigung des Gerichtsstandsbestimmungsgesuchs.204aI2: maßgebliche Verkündung oder Zustellung der einstweiligen Verfügung an Antragsteller, danach Monat zur Zustellung an Antragsgegner. Fristauslöser rechtlich vorqualifizieren, nicht Antragseinreichung oder Kenntnis frei einsetzen. Nur Grundfristen: entsprechende206/210/211-Korrekturen nach204III für die dort genannten204-Fälle zusätzlich, keine ungeprüfte Übertragung dieses Verweises auf204aI2.193 bei feststehender Anwendung gesondert. Keine automatische Hemmungs-/Rückwirkungsentscheidung, keine Berechnung aus dem KapMuG außerhalb desBGB.',
)
```

## verbandsklage_hemmungsnachlauf

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `verfahrensende_am`: Optionales ISO-Datum der Rechtskraft beziehungsweise anderweitigen Beendigung des einschlägigen Verfahrens; kein bloßer Stillstand. Bei noch nicht eingetretenem Ereignis null.
- `teilnahmefall`: Expliziter Wahrheitswert, ob ein Teilnahmefall nach204aIII2 vorliegt.
- `teilnahmeende_am`: Nur im Teilnahmefall optionales ISO-Datum des tatsächlichen Teilnahmeendes, etwa wirksame Rücknahme der Anmeldung; andernfalls null.
- `einordnungsnachweis`: Nichtleerer Nachweis des204a-Verfahrens, Anwendbarkeit, qualifizierter Endereignisse und gegebenenfalls Teilnahmefall.

Frühestes einschlägiges Verfahrens-/Teilnahmeende bestimmen und sechsmonatigen Hemmungsnachlauf berechnen.

wert.rechnerisches_nachlaufende alsYYYY-MM-DD; kein Anspruchsverjährungsdatum.

§204aIII: sechsmonatiger Nachlauf ab rechtskräftiger Entscheidung/anderweitigem Verfahrensende entsprechend204II1; im qualifizierten Teilnahmefall auch ab Ende der Teilnahme, insbesondere Rücknahme der Registeranmeldung. Wenn beide einschlägigen Ereignisse feststehen, maßgeblich ist das frühere Nachlaufende. Kein Stillstand durch Nichtbetreiben als zusätzlicher204a-Auslöser: der Verweis nennt nur204II1. Teilnahmefall ausschließlich204aI1Nr3/4 oderII2, gegebenenfalls gleichgestellte UnternehmerIV; keine beliebige Nichtteilnahme bei Unterlassungsklage. Ohne bekanntes Endereignis kein fiktives Ende des laufenden Schutzes. Keine automatische Addition des Ergebnisses zur Verjährungsfrist: normierte tatsächliche Hemmungstage und209 gesondert berechnen.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_204_T0024, BGB_204a_T0020, BGB_204a_T0021, BGB_204a_T0022

```python
from bgbcalc import verbandsklage_hemmungsnachlauf
verbandsklage_hemmungsnachlauf(
    verfahrensende_am='2024-01-31',
    teilnahmefall=False,
    teilnahmeende_am=None,
    einordnungsnachweis='§204aIII: sechsmonatiger Nachlauf ab rechtskräftiger Entscheidung/anderweitigem Verfahrensende entsprechend204II1; im qualifizierten Teilnahmefall auch ab Ende der Teilnahme, insbesondere Rücknahme der Registeranmeldung. Wenn beide einschlägigen Ereignisse feststehen, maßgeblich ist das frühere Nachlaufende. Kein Stillstand durch Nichtbetreiben als zusätzlicher204a-Auslöser: der Verweis nennt nur204II1. Teilnahmefall ausschließlich204aI1Nr3/4 oderII2, gegebenenfalls gleichgestellte UnternehmerIV; keine beliebige Nichtteilnahme bei Unterlassungsklage. Ohne bekanntes Endereignis kein fiktives Ende des laufenden Schutzes. Keine automatische Addition des Ergebnisses zur Verjährungsfrist: normierte tatsächliche Hemmungstage und209 gesondert berechnen.',
)
```
