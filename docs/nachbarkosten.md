<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## grenzbaum_beseitigungskosten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `beseitigungskosten`: Nichtnegative rechtlich berücksichtigungsfähige Beseitigungskosten in EUR für den betroffenen Grenzbaum/Grenzstrauch. Keine bereits von einer Seite getragenen Kosten nochmals addieren.
- `anderer_nachbar_verzichtet`: Wahrheitswert eines rechtlich wirksamen Verzichts des anderen Nachbarn auf sein Recht am Baum. Dann trägt der die Beseitigung verlangende Nachbar die Kosten allein. Bloß fehlendes Interesse, Schweigen oder Abwesenheit nicht automatisch Verzicht.
- `unersetzliches_grenzzeichen`: Wahrheitswert: Baum dient als Grenzzeichen und kann den Umständen nach nicht durch anderes zweckmäßiges Grenzzeichen ersetzt werden. TRUE schließt gesetzlichen Beseitigungsanspruch§923 Absatz2 aus; hier NICHT_ANWENDBAR.
- `grenzbaumregel_anwendbar`: Wahrheitswert des einschlägigen gesetzlichen Beseitigungsfalls§923 zwischen zwei Nachbargrundstücken. Auch Grenzstrauch gemäßAbsatz3. Grenzlage, sonstige Beschränkungen und keine vorrangige abweichende Kostenregelung zuvor prüfen; kein beliebiger Baum nahe Grenze.
- `kostennachweis`: Nichtleere Beschreibung der Grenzlage, des verlangenden und anderen Nachbarn, etwaigen Rechtsverzichts, Grenzzeichenfunktion und Beseitigungskosten. Freiwillige anderweitige Vereinbarungen separat.

Bei einschlägigem nicht wegen unersetzlichen Grenzzeichens ausgeschlossenen Beseitigungsfall Kosten grundsätzlichhälftig; bei Verzicht des anderen Nachbarn trägt Verlangender alles, anderer0.

wert enthält kosten_verlangender_nachbar und kosten_anderer_nachbar als exakte EUR-Brüche mit Summe der Gesamtkosten; ausgeschlossener gesetzlicher Fall ergibt NICHT_ANWENDBAR/null.

Kein gesetzlicher Beseitigungsanspruch bei unersetzlichem Grenzzeichen. Sonstige rechtliche/öffentlich-rechtliche Einschränkungen vorher prüfen; freiwillige andere Regelung außerhalb Modell. Eigentumserwerb mit Trennung und Früchteverteilung nicht Teil dieser Kostenoperation.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_923_T0002, BGB_923_T0003, BGB_923_T0004, BGB_923_T0005, BGB_923_T0006

```python
from bgbcalc import grenzbaum_beseitigungskosten
grenzbaum_beseitigungskosten(
    beseitigungskosten='100.01',
    anderer_nachbar_verzichtet=False,
    unersetzliches_grenzzeichen=False,
    grenzbaumregel_anwendbar=True,
    kostennachweis='Synthetischer gesetzlicher Grenzbaum-Beseitigungsfall und Kosten.',
)
```

## nachbarrecht_kostengleichanteil

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtkosten`: Nichtnegative rechtlich zu verteilende tatsächliche Gesamtkosten in EUR für Abmarkung beziehungsweise Unterhaltung der Grenzeinrichtung. Nicht Herstellung, beliebige Erneuerung oder andere Maßnahmen ungeprüft als Unterhaltung einordnen.
- `kostenart`: Auswahl abmarkung (§919 Absatz3) oder grenzeinrichtung_unterhaltung (§922 Satz2). Abmarkung meint gesetzlich einschlägige Grenzzeichenerrichtung/-wiederherstellung; landesrechtliche Verfahrensvorgaben zuvor prüfen.
- `beteiligtenzahl`: Ganze Zahl2..2^53-1 der beteiligten Kostenseiten. Bei Unterhaltung einer Einrichtung zwischen zwei Grundstücken genau2. Miteigentümer innerhalb einer Grundstücksseite nicht ungeprüft als zusätzliche Nachbarn zählen; interne Verteilung separat.
- `abweichendes_rechtsverhaeltnis`: Wahrheitswert einer rechtlich wirksamen abweichenden Kostenverteilung. TRUE führt aus gesetzlichem Gleichteilungsmodell; Ersatzquote nicht erfinden. Bei Abmarkung ausdrücklicher Vorbehalt§919 Absatz3.
- `gesetzlicher_kostenfall`: Wahrheitswert des rechtlich einschlägigen gesetzlichen Kostenfalls. Bei§922 gemeinschaftliche Benutzungsberechtigung an Einrichtung§921 erforderlich; nicht bloß Grenznähe. Andere spezielle Regelungen vorab prüfen.
- `kostennachweis`: Nichtleere Beschreibung von Maßnahme, rechtlichem Kostenfall, Kostenträgern/Grundstücksseiten, Kostenhöhe und gegebenenfalls abweichendem Rechtsverhältnis.

Gesetzlichen Kostenfall ohne abweichende Kostenverteilung auswählen. Gesamtkosten durch Zahl der beteiligten Kostenseiten teilen; bei Unterhaltung zwischen zwei Nachbargrundstücken genau zwei.

wert ist exakter EUR-Kostenanteil je gesetzlicher Kostenseite. Fehlender Kostenfall oder abweichende Verteilung ergibt NICHT_ANWENDBAR mit null.

Kein automatischer Abmarkungs-/Unterhaltungsanspruch und keine Aussage zum zulässigen Verfahren nach Landesrecht. Keine gleiche Verteilung auf sämtliche natürlichen Miteigentümer unabhängig von Grundstücksseiten. Abweichendes Rechtsverhältnis gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_919_T0001, BGB_919_T0002, BGB_919_T0003, BGB_922_T0001, BGB_922_T0002

```python
from bgbcalc import nachbarrecht_kostengleichanteil
nachbarrecht_kostengleichanteil(
    gesamtkosten='0',
    kostenart='abmarkung',
    beteiligtenzahl=2,
    abweichendes_rechtsverhaeltnis=False,
    gesetzlicher_kostenfall=True,
    kostennachweis='Synthetischer gesetzlicher Kostenfall mit zutreffenden Grundstücksseiten.',
)
```
