# Zinsen und Verzug

Beträge und Sätze werden exakt als Brüche mit Ganzzahlzeichenfolgen ausgegeben. Keine Rundung und keine automatischen Abrufe externer Zinssätze. Die Beispiele verwenden synthetische Werte.


## basiszinssatz_fortschreibung

Neuer Basiszinssatz = bisheriger Basiszinssatz + neuer Bezugszinssatz - bisheriger Bezugszinssatz. Anpassung nur zum 1. Januar oder 1. Juli; keine Rundung oder automatische Nulluntergrenze.

Keine Behauptung eines aktuellen amtlichen Basiszinssatzes; 3,62 Prozent aus dem Normtext ist kein zeitlos geltender Satz. Bezugswerte müssen genau die maßgeblichen Hauptrefinanzierungsoperationen und vorherigen Anpassungsstand bezeichnen.


Eingaben:


- `bisheriger_basiszinssatz_prozent`: Bisheriger Basiszinssatz als Dezimalzeichenfolge in Prozent pro Jahr.

- `bisheriger_bezugszinssatz_prozent`: Bezugszinssatz des vorherigen Anpassungsstands als Dezimalzeichenfolge in Prozent.

- `neuer_bezugszinssatz_prozent`: Maßgeblicher neuer Hauptrefinanzierungszinssatz als Dezimalzeichenfolge in Prozent.

- `anpassungsdatum`: ISO-Datum der Anpassung, ausschließlich 1. Januar oder 1. Juli.

- `quellenangabe`: Nichtleerer Beleg der vorgegebenen Bezugsgrößen und ihrer zeitlichen Zuordnung.


## gesetzliche_zinsen

Kapital * Jahreszinssatz/100 * angegebener Jahresanteil. Jahreszinssatz 4 Prozent, außer ausdrücklich abweichende wirksame Bestimmung als Eingabe. Während eines vollständig im Gläubigerverzug liegenden Zeitanteils kein Zinsanspruch aus dieser Regel (NICHT_ANWENDBAR).

Verzinsungspflicht aus Gesetz/Rechtsgeschäft muss bereits feststehen; Funktion begründet sie nicht. Keine universelle 30/360-/365-Tage-Annahme und kein Zinseszins; Zeitanteile mit geändertem Satz, Kapital oder Gläubigerverzug getrennt berechnen.


Eingaben:


- `kapital`: Nichtnegative Dezimalzeichenfolge des zu verzinsenden Kapitals in EUR.

- `zeitanteil_zaehler`: Nichtnegative ganze Zahl im ausdrücklich ermittelten Jahresanteil.

- `zeitanteil_nenner`: Positive ganze Zahl als Nenner des Jahresanteils.

- `zeitanteil_nachweis`: Nichtleere Beschreibung von Zeitraum und maßgeblicher Zeitkonvention. Keine automatische 30/360- oder 365-Tage-Annahme.

- `glaeubigerverzug`: Expliziter Wahrheitswert: liegt der gesamte eingegebene Zeitraum im Gläubigerverzug?

- `abweichender_zinssatz_prozent`: Optionaler wirksam abweichender Jahreszinssatz als Dezimalzeichenfolge in Prozent; sonst None für 4 Prozent.


## verzugszinsen

Grundsatz Basiszins+5 Prozentpunkte; bei Entgeltforderung ohne Verbraucherbeteiligung +9. Verbraucherdarlehen nach § 497 Abs. 1 +5, Immobiliar-Verbraucherdarlehen +2,5. Höherer Zinssatz aus anderem Rechtsgrund nur im allgemeinen Zweig über max auswählen. Zinsbetrag=Kapital*Jahreszinssatz/100*Jahresanteil. Keine Verzugszinsen auf Zinsschulden; kein Zinsanspruch für vollständig gläubigerverzugsbehafteten Zeitanteil.

Verzug und Anwendungszeitraum bereits festgestellt. Keine automatische Basiszinsreihe; Teilperioden bei Satz-/Kapitaländerung trennen. Nachgewiesener höherer/niedrigerer Schaden nach § 497 Abs. 1 sowie Schaden wegen Zinsverzugs nach Abs. 2 sind eigene Ansprüche, hier nicht berechnet. § 513-Verweisfälle möglich, deshalb Verbraucherdarlehenszweig nicht allein aus Verbraucherrolle ableiten. § 288 Abs. 6 und Übergangsrecht vorab prüfen.


Eingaben:


- `kapital`: Nichtnegative Dezimalzeichenfolge des zu verzinsenden Kapitals in EUR.

- `basiszinssatz_prozent`: Für den gesamten Teilzeitraum geltender Basiszinssatz als Dezimalzeichenfolge in Prozent.

- `zeitanteil_zaehler`: Nichtnegative ganze Zahl im ausdrücklich ermittelten Jahresanteil.

- `zeitanteil_nenner`: Positive ganze Zahl als Nenner des Jahresanteils.

- `zeitanteil_nachweis`: Nichtleere Beschreibung von Zeitraum und maßgeblicher Zeitkonvention. Keine automatische 30/360- oder 365-Tage-Annahme.

- `entgeltforderung`: Expliziter Wahrheitswert zur rechtlich eingeordneten Entgeltforderung.

- `verbraucher_beteiligt`: Expliziter Wahrheitswert, ob an dem Rechtsgeschäft ein Verbraucher beteiligt ist.

- `zinsschuld`: Expliziter Wahrheitswert, ob das eingegebene Kapital selbst eine Zinsschuld ist.

- `glaeubigerverzug`: Expliziter Wahrheitswert: liegt der gesamte eingegebene Zeitraum im Gläubigerverzug?

- `verzugsart`: allgemein, verbraucherdarlehen oder immobiliar_verbraucherdarlehen; die rechtliche Zuordnung ist eine Nutzervorgabe.

- `hoeherer_zinssatz_prozent`: Optionaler höherer Jahreszinssatz aus anderem Rechtsgrund in Prozent, nur bei verzugsart allgemein. Sonst None.

- `basiszinsnachweis`: Nichtleere Herkunfts- und Gültigkeitsangabe des Basiszinssatzes.


## verzug_nebenkosten

Bei Entgeltforderung, Schuldner kein Verbraucher und Verzug: Pauschale 40 EUR plus max(ersatzfähiger Rechtsverfolgungsschaden-40,0). Anrechnung=min(40,Rechtsverfolgungsschaden) gesondert ausweisen. Sonst NICHT_ANWENDBAR für diesen Pauschalenverbund; keine Aussage zum separat bestehenden Kostenerstattungsanspruch.

Nur eine konkret ausgewählte Entgeltforderung einschließlich Abschlags-/Ratenforderung. Keine automatische Vervielfachung mit Mahnungen oder Schuldnerzahl. Wirksame Vereinbarungs- und Übergangsfragen nach § 288 Abs. 6/EGBGB vorab prüfen; sonstiger Schaden wird nicht auf Pauschale angerechnet.


Eingaben:


- `rechtsverfolgungsschaden`: Nichtnegative Dezimalzeichenfolge des ersatzfähigen Rechtsverfolgungsschadens in EUR; bereits rechtlich bewertet.

- `entgeltforderung`: Expliziter Wahrheitswert zur rechtlich eingeordneten Entgeltforderung.

- `schuldner_verbraucher`: Expliziter Wahrheitswert zur Verbrauchereigenschaft des Schuldners.

- `schuldnerverzug`: Expliziter Wahrheitswert zum festgestellten Schuldnerverzug.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.

## Weitere Zinsansprüche und Zinsausschlusszeiten

Die geprüften Berechnungsketten in `pruefungen/kompositionsfaelle/zinsanspruch_normanwendung.json` verbinden den vorhandenen Zinskern mit den Ansprüchen nach §§ 290, 291, 641 Absatz 4 und 716 Absatz 4. Erster und letzter Zinstag sowie die Zeitkonvention müssen rechtlich bestimmt sein. Die Beispiele verwenden tatsächliche Tage/365 ausschließlich für 2023. Bei § 291 wird der Verzugszinssatz entsprechend angewandt; tatsächlicher Schuldnerverzug und eine Verzugspauschale werden damit nicht vorausgesetzt oder begründet.

`zinskalendertage_nach_ausschluss` vereinigt wirksame Ausschlussintervalle nach §§ 256, 301 und 379. Eine zurückgenommene Hinterlegung begründet keinen Ausschluss nach § 379; eigenständige Ausschlussgründe bleiben erhalten. Die anschließende Betragsrechnung ist in `zinsausschluss_normanwendung.json` geprüft.
