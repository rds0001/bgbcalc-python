<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## fruechte_gewinnungskostenersatz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ordnungsgemaesse_gewinnungskosten`: Nichtnegativer in EUR bewerteter Teil tatsächlich auf die Gewinnung der konkreten Früchte verwendeter Kosten, der einer ordnungsmäßigen Wirtschaft entspricht. Ungeeignete/übermäßige/andere Kosten vorab ausscheiden; kein bloßes Gesamtbudget.
- `wert_der_fruechte`: Nichtnegativer rechtlich maßgeblicher Wert der betreffenden herauszugebenden Früchte in EUR, gleicher Bezugsfall wie Gewinnungskosten. Keine automatische Sachverständigenbewertung.
- `herausgabepflicht_fruechte`: Expliziter Wahrheitswert einer Pflicht zur Herausgabe der betreffenden Früchte. FALSE ergibt NICHT_ANWENDBAR für§102; andere Kostenersatzgrundlagen nicht beurteilt.
- `kostennachweis`: Nichtleere Beschreibung der tatsächlich verwendeten und rechtlich qualifizierten Gewinnungskosten, des Fruchtwerts und der Herausgabepflicht.

Bei Herausgabepflicht: Ersatz=min(ordnungsmäßige verwendete Gewinnungskosten,Fruchtwert). Sonst NICHT_ANWENDBAR.

wert ist exakter EUR-Kostenersatz, höchstens Fruchtwert. Ohne Herausgabepflicht null und NICHT_ANWENDBAR.

Kein Kostenersatz für beliebige Aufwendungen und keine automatische Rechtfertigung aller eingegebenen Kosten. Nur§102 im konkret abgegrenzten Fall.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_102_T0001

```python
from bgbcalc import fruechte_gewinnungskostenersatz
fruechte_gewinnungskostenersatz(
    ordnungsgemaesse_gewinnungskosten='0',
    wert_der_fruechte='0',
    herausgabepflicht_fruechte=True,
    kostennachweis='Synthetische ordnungsmäßige tatsächliche Gewinnungskosten und herauszugebende Früchte.',
)
```

## fruechte_lasten_betragszuordnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zuordnungsart`: Auswahl natuerliche_fruechte (Erzeugnisse/Bestandteile nach§99 Absatz1, auch als Rechtsfrüchte), sonstige_fruechte, regelmaessige_fruechte (einschließlich Gebrauchs-/Fruchtgenussvergütung, Zinsen, Gewinnanteile und sonstiger regelmäßig wiederkehrender Erträge), sonstige_lasten oder regelmaessige_lasten. Rechtliche Einordnung vorab.
- `gesamtbetrag`: Nichtnegativer in EUR bewerteter Gesamtbetrag der konkret abgegrenzten Früchte oder Lasten für den Bezugszeitraum. Bei Naturfrüchten monetärer Wert der betroffenen Stücke; keine Eigentumsübertragung durch die Berechnung. Bei wechselnden Ertragssätzen abschnittsweise zutreffende Bezugsbeträge verwenden.
- `massgebliches_ereignis_im_zeitraum`: Wahrheitswert: bei natürlichen Früchten Trennung während Berechtigung, bei sonstigen Früchten Fälligkeit während Berechtigung, bei sonstigen Lasten rechtlich zu entrichten während Lastentragungspflicht. Bei regelmäßigen Kategorien typgültig erforderlich, aber ohne Einfluss: deren Anteil folgt der Dauer, nicht dem einzelnen Fälligkeitstag.
- `zeitanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bestimmten Daueranteils, höchstens2^53-1 und höchstens Nenner. Bei regelmäßigen Kategorien Pflicht; sonst optional zusammen mit Nenner. Ein freiwillig angegebenes Paar wird ebenfalls validiert.
- `zeitanteil_nenner`: Positive ganze Bezugsdauer im gleichen Maßstab wie Zähler, höchstens2^53-1. Keine automatische365-Tage-Konvention oder Gleichverteilung wechselnder Erträge. Bei nicht regelmäßiger Kategorie können beide Anteilsfelder None/NULL sein.
- `abweichende_bestimmung`: Wahrheitswert einer rechtlich maßgeblichen abweichenden Bestimmung. TRUE ergibt NICHT_ANWENDBAR für den gesetzlichen Zuordnungsmaßstab; alternative Aufteilung gesondert.
- `zuordnungsnachweis`: Nichtleere Beschreibung der Frucht-/Lastenart, rechtlichen Berechtigungs-/Pflichtdauer, des maßgeblichen Ereignisses und gegebenenfalls konsistenten Daueranteils. Keine ungeprüfte Auswahl allein nach Zahlungstag.

Regelmäßige Früchte/Lasten: Gesamtbetrag×Daueranteil. Natürliche Früchte nach Trennung, andere nicht regelmäßige Früchte nach Fälligkeit, nicht regelmäßige Lasten nach Entrichtungspflicht: Betrag vollständig oder0 je Ereigniszuordnung. Abweichende Bestimmung führt aus Standardmodell.

wert ist exakter EUR-Anteil; Ereignis außerhalb Zeitraum ergibt BERECHNET mit0/1, abweichende Bestimmung NICHT_ANWENDBAR mit null.

Berechtigungs-/Pflichtzeitraum und rechtlich maßgebliches Ereignis extern eingeordnet; kein automatischer Schluss aus tatsächlichem Zahlungsdatum. Zeitanteil0..1, keine pauschale Kalenderkonvention. Nur Geldwertzuordnung, keine abschließende Übertragung konkreter Sachen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_99_T0001, BGB_99_T0002, BGB_99_T0003, BGB_101_T0001, BGB_101_T0002, BGB_101_T0003, BGB_103_T0001

```python
from bgbcalc import fruechte_lasten_betragszuordnung
fruechte_lasten_betragszuordnung(
    zuordnungsart='natuerliche_fruechte',
    gesamtbetrag='1200',
    massgebliches_ereignis_im_zeitraum=False,
    zeitanteil_zaehler=0,
    zeitanteil_nenner=3,
    abweichende_bestimmung=False,
    zuordnungsnachweis='Synthetische rechtlich bestimmte Zuordnung und gleichmäßig bepreiste Bezugsdauer.',
)
```
