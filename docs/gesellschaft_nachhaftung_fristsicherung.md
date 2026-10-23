<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_nachhaftung_fristsicherung

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `nachhaftungsfrist_letzter_tag`: Bereits aus Kenntnis/Registereintrag und erforderlichen204/206/210/211-Korrekturen berechneter letzter Fristtag.
- `faelligkeit_am`: Rechtlich maßgeblicher Fälligkeitstag der betrachteten Altverbindlichkeit.
- `sicherungsereignisse`: Liste0..1000 mit genau ereignis_id,art,datum,rueckwirkend_unwirksam_212. art:feststellung_197,gerichtliche_vollstreckung,behoerdliche_vollstreckung,vollstreckungsantrag,verwaltungsakt_oeffentlich_rechtlich,schriftliches_anerkenntnis. Zeitpunkte und jeweilige rechtliche Eignung vorqualifiziert.212-Rückwirkung nur für Vollstreckung/Antrag zulässig.
- `einordnungsnachweis`: 728b-Fall: bis zum Ausscheiden begründete Verbindlichkeit, bei Schadensersatz vorherige Pflichtverletzung, richtig berechnete Frist, wirksame einschlägige Sicherungsakte und212II/III-Rückwirkung vorqualifizieren.

Fälligkeit und qualifizierte Sicherungszeitpunkte gegen unveränderte korrigierte Nachhaftungsfrist vergleichen;212II/III-rückwirkend unwirksame Vollstreckungsakte ausschließen.

Unveränderter Nachhaftungsfristtag, Fälligkeitsmerkmal, rechtzeitige wirksame Sicherungskennungen und kombinierte Zeitkopplung.

728bI/II: Fälligkeit bis einschließlich letztem Fristtag und mindestens ein rechtlich geeigneter rechtzeitiger Sicherungsakt; schriftliches Anerkenntnis ersetzt in qualifiziertem Umfang Feststellung. Vollstreckungsakte/Anträge mit rechtlich feststehender212II/III-Rückwirkung zählen nicht. Kein pauschaler212I-Neubeginn: der übergebene korrigierte Nachhaftungsfristtag bleibt unverändert.212-Rückwirkung ist Rechtsbewertung, keine neue Fristdauer. Bei teilweise wirksamem Anerkenntnis oder nur teilweise gesicherter Forderung vorher sachlich in Forderungsteile trennen; kein volles Anerkenntnis vortäuschen. Gerichtliche/behördliche Vollstreckung, Titel nach197Absatz1Nummer3–5und öffentlich-rechtlicher Verwaltungsakt müssen zum konkreten Anspruch passen. Funktion berechnet Zeitkopplung, keinen vollständigen Haftungstatbestand. Untertägige Grenzprobleme vorab qualifizieren.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_212_T0001, BGB_212_T0002, BGB_212_T0003, BGB_212_T0004, BGB_212_T0005, BGB_728b_T0001, BGB_728b_T0002, BGB_728b_T0003, BGB_728b_T0004, BGB_728b_T0005, BGB_728b_T0006, BGB_728b_T0007

```python
from bgbcalc import gesellschaft_nachhaftung_fristsicherung
gesellschaft_nachhaftung_fristsicherung(
    nachhaftungsfrist_letzter_tag='2025-01-31',
    faelligkeit_am='2025-01-31',
    sicherungsereignisse=[{'ereignis_id': 'V', 'art': 'vollstreckungsantrag', 'datum': '2025-01-31', 'rueckwirkend_unwirksam_212': False}],
    einordnungsnachweis='728bI/II: Fälligkeit bis einschließlich letztem Fristtag und mindestens ein rechtlich geeigneter rechtzeitiger Sicherungsakt; schriftliches Anerkenntnis ersetzt in qualifiziertem Umfang Feststellung. Vollstreckungsakte/Anträge mit rechtlich feststehender212II/III-Rückwirkung zählen nicht. Kein pauschaler212I-Neubeginn: der übergebene korrigierte Nachhaftungsfristtag bleibt unverändert.212-Rückwirkung ist Rechtsbewertung, keine neue Fristdauer. Bei teilweise wirksamem Anerkenntnis oder nur teilweise gesicherter Forderung vorher sachlich in Forderungsteile trennen; kein volles Anerkenntnis vortäuschen. Gerichtliche/behördliche Vollstreckung, Titel nach197Absatz1Nummer3–5und öffentlich-rechtlicher Verwaltungsakt müssen zum konkreten Anspruch passen. Funktion berechnet Zeitkopplung, keinen vollständigen Haftungstatbestand. Untertägige Grenzprobleme vorab qualifizieren.',
)
```
