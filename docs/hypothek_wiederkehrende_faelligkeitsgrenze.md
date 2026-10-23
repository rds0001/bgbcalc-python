<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## hypothek_wiederkehrende_faelligkeitsgrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `beschlagnahme_am`: Rechtlich maßgeblicher Beschlagnahmetag.
- `faelligkeit_am`: Fälligkeit der einzelnen wiederkehrenden Leistung.
- `grenzmethode`: Zwingend rechtlich begründete Wahl: nach_ablauf_dreimonatsfrist oder ab_dreimonatsvergleichstag. Keine voreingestellte Auslegung des1126-Grenztags.
- `einordnungsnachweis`: Vor Beschlagnahme erfolgte Verfügung und1126-Anwendbarkeit sowie konkrete Grenztagsauslegung qualifizieren.

Drei Kalendermonate ab Beschlagnahme und Fälligkeitslage nach ausdrücklich gewählter Grenztagsmethode berechnen.

Dreimonatsvergleichstag, bedingtes zeitliches Unwirksamkeitsmerkmal und verwendete rechtliche Grenzmethode.

1126Satz3: Vorverfügung über wiederkehrende Leistung, keine Mietzeitraumprüfung nach1124II. Drei Kalendermonate mit bestehendem187/188-Kern rechnen, keine90Tage. Nach_ablauf_dreimonatsfrist vergleicht Fälligkeit streng nach dem letzten Fristtag; ab_dreimonatsvergleichstag bezieht diesen Vergleichstag ein. Die lokale Norm allein klärt die hier strittige Tagesgrenze nicht abschließend; verpflichtende Methodenwahl macht beide bedingten Rechnungen sichtbar, ohne eine allgemein verbindliche Grenztagsauslegung zu behaupten. Übrige rechtliche Unwirksamkeitsvoraussetzungen sind nicht Gegenstand dieser zeitlichen Rechnung. Keine193-Wochenendverschiebung einer Fälligkeitsabgrenzung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_187_T0001, BGB_187_T0002, BGB_187_T0003, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003, BGB_1126_T0001, BGB_1126_T0002, BGB_1126_T0003

```python
from bgbcalc import hypothek_wiederkehrende_faelligkeitsgrenze
hypothek_wiederkehrende_faelligkeitsgrenze(
    beschlagnahme_am='2024-01-15',
    faelligkeit_am='2024-04-15',
    grenzmethode='nach_ablauf_dreimonatsfrist',
    einordnungsnachweis='1126Satz3: Vorverfügung über wiederkehrende Leistung, keine Mietzeitraumprüfung nach1124II. Drei Kalendermonate mit bestehendem187/188-Kern rechnen, keine90Tage. Nach_ablauf_dreimonatsfrist vergleicht Fälligkeit streng nach dem letzten Fristtag; ab_dreimonatsvergleichstag bezieht diesen Vergleichstag ein. Die lokale Norm allein klärt die hier strittige Tagesgrenze nicht abschließend; verpflichtende Methodenwahl macht beide bedingten Rechnungen sichtbar, ohne eine allgemein verbindliche Grenztagsauslegung zu behaupten. Übrige rechtliche Unwirksamkeitsvoraussetzungen sind nicht Gegenstand dieser zeitlichen Rechnung. Keine193-Wochenendverschiebung einer Fälligkeitsabgrenzung.',
)
```
