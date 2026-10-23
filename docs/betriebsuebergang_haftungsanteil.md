<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betriebsuebergang_bisheriger_arbeitgeber_haftungsbetrag

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `betriebsuebergang_am`: Qualifizierter Tag des BetriebsübergangsYYYY-MM-DD.
- `faellig_am`: Rechtlich maßgeblicher FälligkeitstagYYYY-MM-DD der schon vor Übergang entstandenen Verpflichtung.
- `nach_uebergang_faellig`: Wahrheitswert zur zeitlichen Reihenfolge; bei identischem Kalendertag nach tatsächlichem Zeitpunkt rechtlich qualifizieren.
- `verpflichtungsbetrag`: Nichtnegativer BetragEUR dieser abgegrenzten Verpflichtung.
- `abgelaufene_bemessungseinheiten`: Nichtnegative exakte Zahl rechtlich maßgeblicher, bis zum Übergang abgelaufener Bemessungseinheiten.
- `gesamte_bemessungseinheiten`: Positive exakte Zahl derselben Bemessungseinheit im vollständigen Bemessungszeitraum; keine pauschale360/365Tage-Annahme.
- `einordnungsnachweis`: Nichtleerer Nachweis613aII: wirksamer Betriebsübergang, Verpflichtung vor Übergang entstanden,613aIII-Ausnahme ausgeschlossen, Fälligkeitsreihenfolge und Bemessungszeitanteil qualifiziert.

Fälligkeitszeitgrenze und zeitanteiligen Haftungsumfang des bisherigen Arbeitgebers berechnen.

wert.einjahresgrenze_letzter_tag alsDatum und haftungsbetrag_bisheriger_arbeitgeber alsEurobruch.

§613aII: Vor Übergang fällige qualifizierte Verpflichtung in voller Höhe; später fällige nur bis zur gesetzlichen Einjahresgrenze und im Verhältnis des bereits abgelaufenen zum gesamten Bemessungszeitraum. Fristende nach187I/188; Datumsgleichheit zum letzten Tag gilt nur bei rechtlich qualifizierter Fälligkeit vor dessen Ablauf. Ausgabe ist Umfang der gesamtschuldnerischen Haftung des bisherigen Arbeitgebers; keine hälftige Aufteilung und kein zusätzlicher Anspruch neben dem Gesamtbetrag. Übrige Haftungsgrundlagen und Innenausgleich nicht entschieden. Beide Zeiteinheiten auch im Vollhaftungsfall angeben; keine automatische Bewertung oder zeitliche Entstehung der Verpflichtung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_613a_T0005, BGB_613a_T0006

```python
from bgbcalc import betriebsuebergang_bisheriger_arbeitgeber_haftungsbetrag
betriebsuebergang_bisheriger_arbeitgeber_haftungsbetrag(
    betriebsuebergang_am='2024-07-01',
    faellig_am='2024-12-31',
    nach_uebergang_faellig=True,
    verpflichtungsbetrag='1200',
    abgelaufene_bemessungseinheiten='6',
    gesamte_bemessungseinheiten='12',
    einordnungsnachweis='§613aII: Vor Übergang fällige qualifizierte Verpflichtung in voller Höhe; später fällige nur bis zur gesetzlichen Einjahresgrenze und im Verhältnis des bereits abgelaufenen zum gesamten Bemessungszeitraum. Fristende nach187I/188; Datumsgleichheit zum letzten Tag gilt nur bei rechtlich qualifizierter Fälligkeit vor dessen Ablauf. Ausgabe ist Umfang der gesamtschuldnerischen Haftung des bisherigen Arbeitgebers; keine hälftige Aufteilung und kein zusätzlicher Anspruch neben dem Gesamtbetrag. Übrige Haftungsgrundlagen und Innenausgleich nicht entschieden. Beide Zeiteinheiten auch im Vollhaftungsfall angeben; keine automatische Bewertung oder zeitliche Entstehung der Verpflichtung.',
)
```
