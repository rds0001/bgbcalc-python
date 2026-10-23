<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verwendungsersatz_erloeschensfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `herausgabe_am`: ISO-Datum0001..9999 der rechtlich maßgeblichen Herausgabe an Eigentümer. Nicht bloß Aufforderung oder Besitzverlust an Dritten.
- `grundstueck`: Wahrheitswert: herausgegebene Sache ist Grundstück (sechs Monate), sonst ein Monat.
- `massgebliches_fristende`: ISO-Datum des rechtlich maßgeblichen letzten Tages einschließlich gesondert ermittelter zulässiger Fristkorrekturen, insbesondere§1002 Absatz2 mit§§206/210/211. Mindestens rechnerische Grundfrist; Verlängerung belegen, nicht frei wählen.
- `prueftag`: ISO-Datum der Prüfung nach Abschluss dieses Tages; frühestens Herausgabetag.
- `gerichtliche_geltendmachung_am`: Optionales ISO-Datum der wirksamen gerichtlichen Geltendmachung dieses Anspruchs, spätestens Prüftag. NULL bedeutet bis Prüftag nicht eingetreten, nicht unbekannt. Auch vor Herausgabe möglich. Keine bloße außergerichtliche Mahnung.
- `genehmigung_verwendungen_am`: Optionales ISO-Datum der rechtlich wirksamen Genehmigung dieser Verwendungen durch Eigentümer, spätestens Prüftag; auch vor Herausgabe möglich. NULL bedeutet nicht eingetreten, nicht ungeklärt.
- `anspruch_unterliegt_1002`: Wahrheitswert des geprüften Anspruchs- und Herausgaberegimes§1002. FALSE ergibt NICHT_ANWENDBAR; keine Aussage zum Erlöschen anderer Ansprüche.
- `einordnungsnachweis`: Nichtleere Begründung von Herausgabe, Sachtyp, Anspruchsregime, maßgeblichem Fristende samt Korrekturen sowie gerichtlicher Geltendmachung und Genehmigung.

Grundfrist ab Herausgabe: Grundstück sechs Monate, sonst ein Monat. Nach maßgeblichem Fristende erlischt Anspruch, wenn weder rechtzeitige gerichtliche Geltendmachung noch Genehmigung vorliegt.

wert enthält rechnerisches_fristende als ISO-Datum und gerichtliche_geltendmachung_rechtzeitig, genehmigung_rechtzeitig, anspruch_nach_1002_erloschen als Wahrheitswerte. Bei fehlendem Anwendungsbereich NICHT_ANWENDBAR/null.

§§206/210/211 werden entsprechend angewandt, aber ihre Korrekturen hier als belegtes Fristende eingegeben. Anspruchsgrund/Betrag/Fälligkeit§1001 separat; verspätete Genehmigung begründet nicht automatisch Wiederaufleben.

ISO-Daten und berechnete Grenzen0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1002_T0001, BGB_1002_T0002

```python
from bgbcalc import verwendungsersatz_erloeschensfrist
verwendungsersatz_erloeschensfrist(
    herausgabe_am='2030-01-31',
    grundstueck=False,
    massgebliches_fristende='2030-02-28',
    prueftag='2030-04-01',
    gerichtliche_geltendmachung_am=None,
    genehmigung_verwendungen_am=None,
    anspruch_unterliegt_1002=True,
    einordnungsnachweis='Synthetisch qualifizierte Herausgabe und Ereignisse; keine Korrektur der Grundfrist.',
)
```
