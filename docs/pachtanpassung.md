<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## landpacht_anpassung_zeitgrenzen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `pachtbeginn_am`: Rechtlich maßgeblicher Beginn des Pachtverhältnisses YYYY-MM-DD.
- `letzte_aenderung_wirksam_am`: Optionaler Tag der letzten rechtlich wirksamen Änderung der Vertragsleistungen; sonst null. Nicht vor Pachtbeginn.
- `beginnart`: ereignis oder tagesbeginn für den maßgeblichen Beginn der Zweijahreswartezeit rechtlich bestimmen.
- `naturereignis_ausnahme`: Wahr nur bei vorqualifiziertem Ausnahmefall des593II2; sonst falsch.
- `aenderungsverlangen_am`: Tag der Erklärung des Änderungsverlangens YYYY-MM-DD.
- `pachtjahr_beginn_am`: Beginn des rechtlich maßgeblichen Pachtjahres, in dem das Verlangen erklärt wird.
- `pachtjahr_ende_am`: Letzter Tag dieses Pachtjahres; keine automatische Gleichsetzung mit Kalenderjahr.
- `einordnungsnachweis`: Nichtleerer Nachweis der gesetzlichen Anwendbarkeit, Fristbeginnart, Pachtjahresgrenzen und gegebenenfalls Naturereignisausnahme.

Zweijahreswartezeit und Ausnahme rechnerisch verknüpfen, Erklärungstag vergleichen und Rückwirkungsgrenze des zugeordneten Pachtjahres ausweisen.

wert mit erster_tag_nach_wartezeit (bei gesetzlicher Ausnahme null), rechnerische_rueckwirkungsgrenze als Datum und wartezeit_eingehalten als Wahrheitswert.

§593II/III: Zweijahreswartezeit ab Beginn beziehungsweise letzter wirksamer Vertragsleistungsänderung, außer qualifiziertem verwüstendem Naturereignis ohne üblichen Versicherungsschutz. Beginnart rechtlich bestimmen; beim Tagesbeginn1.Juli2022 endet die Wartezeit30.Juni2024, erster Folgetag1.Juli2024. Ausgewiesene Rückwirkungsgrenze ist der Beginn des Pachtjahres des tatsächlichen Verlangens, nicht automatisch der Erklärungstag oder Kalenderjahresbeginn. Eine rechnerisch verfrühte Erklärung wird weder verschoben noch als wirksam bestätigt. Grundlegende Verhältnisänderung, grobes Missverhältnis, Ausschlüsse und konkrete neue Vertragsleistung bleiben extern qualifiziert. Keine Änderung der Pachtdauer, kein automatisch berechneter angemessener Pachtzins; weitere gerichtliche/vertragliche Wirkungen separat.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_593_T0003, BGB_593_T0004, BGB_593_T0005

```python
from bgbcalc import landpacht_anpassung_zeitgrenzen
landpacht_anpassung_zeitgrenzen(
    pachtbeginn_am='2022-07-01',
    letzte_aenderung_wirksam_am=None,
    beginnart='tagesbeginn',
    naturereignis_ausnahme=False,
    aenderungsverlangen_am='2024-07-01',
    pachtjahr_beginn_am='2024-07-01',
    pachtjahr_ende_am='2025-06-30',
    einordnungsnachweis='§593II/III: Zweijahreswartezeit ab Beginn beziehungsweise letzter wirksamer Vertragsleistungsänderung, außer qualifiziertem verwüstendem Naturereignis ohne üblichen Versicherungsschutz. Beginnart rechtlich bestimmen; beim Tagesbeginn1.Juli2022 endet die Wartezeit30.Juni2024, erster Folgetag1.Juli2024. Ausgewiesene Rückwirkungsgrenze ist der Beginn des Pachtjahres des tatsächlichen Verlangens, nicht automatisch der Erklärungstag oder Kalenderjahresbeginn. Eine rechnerisch verfrühte Erklärung wird weder verschoben noch als wirksam bestätigt. Grundlegende Verhältnisänderung, grobes Missverhältnis, Ausschlüsse und konkrete neue Vertragsleistung bleiben extern qualifiziert. Keine Änderung der Pachtdauer, kein automatisch berechneter angemessener Pachtzins; weitere gerichtliche/vertragliche Wirkungen separat.',
)
```
