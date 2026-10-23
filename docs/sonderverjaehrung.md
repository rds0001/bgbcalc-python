<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verjaehrung_besondere_grundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `anspruchsart`: Rechtlich geprüfte Auswahl grundstuecksanspruch (§196 einschließlich Gegenleistung), vorsaetzliche_personenverletzung (§197 Absatz1 Nummer1), herausgabeanspruch (Nummer2 einschließlich Hilfsansprüche), rechtskraeftig_festgestellt (Nummer3), vollstreckbarer_vergleich_urkunde (Nummer4), insolvenzfeststellung (Nummer5) oder zwangsvollstreckungskosten (Nummer6). Kein beliebiger Grundstücksbezug oder allgemeiner Vermögensschaden.
- `anspruchsbeginn_am`: ISO-Datum0001..9999 der rechtlichen Anspruchsentstehung; bei Unterlassung stattdessen maßgebliche Zuwiderhandlung (§199 Absatz5). Ereignistag wird nicht mitgezählt. Keine automatische Verschiebung zum Jahresschluss.
- `titelereignis_am`: ISO-Datum des rechtlich maßgeblichen Ereignisses nach§201: Rechtskraft, Errichtung vollstreckbaren Titels oder Feststellung im Insolvenzverfahren. Für Nummer3 bis6 Pflicht, sonst optional und bei Angabe ebenfalls validiert. Nicht vor Anspruchsentstehung beginnende Frist wird durch Maximum beider Daten bestimmt; bei Kostenansprüchen zutreffenden Titelbezug rechtlich prüfen.
- `kuenftig_wiederkehrende_leistung`: Wahrheitswert, ob der abgegrenzte Anspruch künftig fällige regelmäßig wiederkehrende Leistungen umfasst. Nur für§197 Absatz1 Nummer3 bis5 führt TRUE zur Ausnahme des Absatz2; bereits fällige Rückstände separat abgrenzen. Kein bloß regelmäßig gezahlter Betrag ohne entsprechende Anspruchsstruktur.
- `abweichende_sonderregel`: Wahrheitswert einer vorrangigen abweichenden Fristdauer oder Beginnregel. TRUE ergibt NICHT_ANWENDBAR. Insbesondere keine Anwendung bloß wegen scheinbarer Übereinstimmung mit einer Anspruchsart trotz Sondervorschrift.
- `einordnungsnachweis`: Nichtleere Beschreibung von Anspruchsgrundlage und -entstehung, Unterlassungsfall, Titelereignis sowie Abgrenzung bereits fälliger und künftiger wiederkehrender Leistungen.

§196 zehn Jahre,§197 dreißig Jahre. Grundsätzlich Anspruchsentstehung, bei Unterlassung Zuwiderhandlung. Bei§197 Absatz1 Nummer3 bis6 Maximum aus Anspruchs- und Titelereignisdatum. Künftig fällige wiederkehrende Leistungen der Nummer3 bis5 sowie abweichende Sonderregel führen aus dem Modell.

wert enthält fristdauer_jahre, fristbeginnereignis_am und rechnerischer_letzter_tag zum Tagesschluss. Bei NICHT_ANWENDBAR null. Ergebnisjahr muss0001..9999 sein.

Nur unmodifizierte Grundfrist. Regelmäßige Frist bei§197 Absatz2 separat nach§§195/199 prüfen; weder pauschal drei Jahre ab Titel noch automatisch verjährungsfrei. Hemmung, Ablaufhemmung, Neubeginn,§193 und konkurrierende Fristläufe gesondert.

ISO-Daten0001..9999; explizite Wahrheitswerte und nichtleerer Nachweis. Fehlende Pflichtwerte EINGABE_FEHLT; falsche Typen, unzulässige Auswahl oder Kalenderüberschreitung EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_196_T0001, BGB_197_T0001, BGB_197_T0002, BGB_197_T0003, BGB_197_T0004, BGB_197_T0005, BGB_197_T0006, BGB_197_T0007, BGB_197_T0008, BGB_199_T0011, BGB_200_T0001, BGB_200_T0002, BGB_201_T0001, BGB_201_T0002

```python
from bgbcalc import verjaehrung_besondere_grundfrist
verjaehrung_besondere_grundfrist(
    anspruchsart='grundstuecksanspruch',
    anspruchsbeginn_am='2024-02-29',
    titelereignis_am='2020-01-01',
    kuenftig_wiederkehrende_leistung=False,
    abweichende_sonderregel=False,
    einordnungsnachweis='Synthetischer rechtlich eingeordneter Anspruch und gesetzlicher Fristbeginn.',
)
```
