<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## werkwohnung_kuendigungstermin

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristfall`: ersatzbedarf_576_1_1 oder arbeitsplatznaehe_576_1_2; übrige gesetzliche Voraussetzungen einschließlich beendetem Dienstverhältnis vorqualifiziert.
- `kuendigungszugang_am`: Tatsächlicher ZugangYYYY-MM-DD.
- `ueberlassungsbeginn_am`: Rechtlich anrechenbarer zusammenhängender Überlassungsbeginn am TagesbeginnYYYY-MM-DD.
- `qualifizierte_zugangsgrenze_am`: Rechtlich bestimmter letzter Zugangstag der Dritte-Werktag-Regel im ZugangsmonatYYYY-MM-DD; örtliche Kalenderqualifikation ausdrücklich vorgeben.
- `einordnungsnachweis`: Nichtleerer Nachweis von576I-Fall, Überlassungszeitraum, Wirksamkeit/Zugang und einschlägiger Werktagsgrenze.

Werkmietwohnungs-Sonderfrist nach qualifizierter Dritte-Werktag-Grenze und Zehnjahresvergleich zum Monatsendtermin berechnen.

wert.zehnjahreszeitraum_letzter_tag als Datum, weniger_als_zehn_jahre_am_zugang und zugangsgrenze_eingehalten als Wahrheitswerte; rechnerischer_sonderbeendigungstag als Datum oderNULL bei zeitlichem Ausschluss vonNummer1.

§576I: Nummer1 nur bei weniger als zehn Jahren Überlassung am Zugangstag; Nummer2 ohne diese Zehnjahresgrenze. Im qualifizierten Nummer1-Fall dritter Werktag zum Ende des übernächsten Monats, Nummer2 zum Ende des laufenden Monats. Bei Zugang nach Monatsgrenze verschiebt sich der früheste Termin um einen Monat. Zehnjahreszeitraum ab rechtlich qualifiziertem Tagesbeginn; intratägige Sonderfälle oder Unterbrechungen extern. Ist Nummer1 zeitlich ausgeschlossen, bleibt SonderterminNULL; daraus folgt keine generelle Unkündbarkeit und kein automatisch ersatzweise berechneter573c-Termin. Dienstverhältnis muss beendet und Ersatzbedarf/Arbeitsplatzbezug rechtlich festgestellt sein. Keine automatische Kündigungswirksamkeit, Widerspruchsentscheidung oder Feiertagsverschiebung des Mietendes.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_576_T0001, BGB_576_T0002, BGB_576_T0003

```python
from bgbcalc import werkwohnung_kuendigungstermin
werkwohnung_kuendigungstermin(
    fristfall='ersatzbedarf_576_1_1',
    kuendigungszugang_am='2024-01-04',
    ueberlassungsbeginn_am='2020-07-01',
    qualifizierte_zugangsgrenze_am='2024-01-04',
    einordnungsnachweis='§576I: Nummer1 nur bei weniger als zehn Jahren Überlassung am Zugangstag; Nummer2 ohne diese Zehnjahresgrenze. Im qualifizierten Nummer1-Fall dritter Werktag zum Ende des übernächsten Monats, Nummer2 zum Ende des laufenden Monats. Bei Zugang nach Monatsgrenze verschiebt sich der früheste Termin um einen Monat. Zehnjahreszeitraum ab rechtlich qualifiziertem Tagesbeginn; intratägige Sonderfälle oder Unterbrechungen extern. Ist Nummer1 zeitlich ausgeschlossen, bleibt SonderterminNULL; daraus folgt keine generelle Unkündbarkeit und kein automatisch ersatzweise berechneter573c-Termin. Dienstverhältnis muss beendet und Ersatzbedarf/Arbeitsplatzbezug rechtlich festgestellt sein. Keine automatische Kündigungswirksamkeit, Widerspruchsentscheidung oder Feiertagsverschiebung des Mietendes.',
)
```
