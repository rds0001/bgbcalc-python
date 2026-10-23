# Indexmiete nach §557b

## indexmiete_betrag

Indexverhältnis=neuer Index/Ausgangsindex. Neue Miete=Ausgangsmiete mal Indexverhältnis. Mietänderung=neue Miete minus Ausgangsmiete; negative Änderung bedeutet Senkung.

- `ausgangsmiete`: Nichtnegative indexierte Mietbasis in EUR, passend zum angegebenen Ausgangsindex. Dezimalzeichenfolge oder exaktes Bruchobjekt mit den Zeichenfolgenfeldern zaehler und nenner nach NUMERIK.md. Bereits eingetretene Indexänderungen nicht erneut auf eine unpassende Ausgangsbasis anwenden. Nicht indexierte Betriebskosten und gesonderte Erhöhungen nach §§559 bis560 nicht ungeprüft in die Basis aufnehmen.
- `ausgangsindex`: Positiver zur Mietbasis gehörender Ausgangsstand des amtlichen Preisindexes gemäß §557b Abs.1. Dezimalzeichenfolge oder exaktes Bruchobjekt mit den Zeichenfolgenfeldern zaehler und nenner nach NUMERIK.md.
- `neuer_index`: Positiver neuer Stand derselben amtlichen Indexreihe auf derselben Basis. Dezimalzeichenfolge oder exaktes Bruchobjekt mit den Zeichenfolgenfeldern zaehler und nenner nach NUMERIK.md. Auch ein geringerer Indexstand ist zulässig; keine Gleichsetzung von Indexpunkten und Prozentpunkten.
- `indexnachweis`: Nichtleere Herkunftsangabe einschließlich Indexreihe, gemeinsamer Basis sowie Ausgangs- und Änderungsmonat. Die Vergleichbarkeit und Zuordnung der eingegebenen Werte werden vom Nutzer belegt; die Library prüft die amtliche Veröffentlichung nicht.
- `wirksame_indexvereinbarung`: Expliziter Wahrheitswert zur wirksamen schriftlichen Indexvereinbarung im gesetzlichen Anwendungsbereich. FALSE ergibt NICHT_ANWENDBAR. Form und Vertragsauslegung werden nicht automatisch entschieden.

Ergebnis wert enthält indexverhaeltnis als dimensionslosen exakten Bruch sowie neue_miete und mietaenderung als exakte EUR-Brüche. Bei NICHT_ANWENDBAR ist wert null.

Feste lokale BGB-Fassung. Teilbaustein der Indexmiete; keine automatische Beschaffung amtlicher Indizes oder Vertragsauslegung. Spezial- und Übergangsrecht einschließlich Anwendungsbereich vorab prüfen. Keine automatische Cent-Rundung. Jahresfrist und Erklärung sind gesondert zu prüfen. Ausgangsmietbegrenzung nach §§556d bis556g gilt nach §557b Abs.4 nur für die Ausgangsmiete; deren Prüfung ist hier nicht enthalten. Indexierte Mietbasis und etwaige nicht indexierte Zusatzbestandteile müssen getrennt bestimmt sein.

## indexmiete_aenderungstermin_pruefen

Beginn nach Zugang ist der erste Tag des übernächsten Kalendermonats. Frühester Beginn nach Jahresfrist ist der Tag nach Ablauf eines nach §§187 Abs.2/188 berechneten Jahres seit dem Tagesbeginn der bisherigen Indexmiete. Beide Termine werden verglichen.

- `zugang_erklaerung`: ISO-Datum YYYY-MM-DD des nachgewiesenen Zugangs der Änderungserklärung. Kein Versanddatum und keine automatische Ermittlung des Zugangs.
- `bisherige_indexmiete_ab`: ISO-Datum des Tagesbeginns, seit dem die bisherige Indexmiete gilt; bei der ersten Anpassung der maßgebliche Beginn der Ausgangsmiete. Darf nicht nach dem Zugang liegen. Erhöhungen nach §§559 bis560 sind von der unveränderten Jahresdauer ausgenommen und setzen diesen Zeitpunkt nicht automatisch neu.
- `erklaerung_formell_ordnungsgemaess`: Expliziter Wahrheitswert zu Textform und erforderlichen Angaben nach §557b Abs.3 Sätze1/2: eingetretene Indexänderung und jeweilige Miete oder Erhöhungsbetrag. Hier keine Behauptung bereits eingehaltener Jahresfrist; diese wird berechnet. Wirksame Indexvereinbarung und Anwendungsbereich vorausgesetzt. FALSE ergibt NICHT_ANWENDBAR.

Ergebnis wert enthält beginn_nach_zugang und fruehester_beginn_nach_jahresfrist als ISO-Daten sowie jahresfrist_eingehalten als Wahrheitswert. BERECHNET bedeutet durchgeführte Teilprüfung, auch wenn der Wahrheitswert FALSE lautet. Bei NICHT_ANWENDBAR ist wert null.

Feste lokale BGB-Fassung. Teilbaustein der Indexmiete; keine automatische Beschaffung amtlicher Indizes oder Vertragsauslegung. Spezial- und Übergangsrecht einschließlich Anwendungsbereich vorab prüfen. Keine automatische Cent-Rundung. Es wird kein abschließend wirksamer Änderungstermin festgestellt. Insbesondere wird bei nicht eingehaltener Jahresfrist weder die Erklärung automatisch verschoben noch deren rechtliches Schicksal entschieden. Ausnahme für Erhöhungen nach §§559 bis560 bei Ermittlung des vorgegebenen Beginns berücksichtigen. Keine Zahlungsfälligkeit nach §556b und keine Feiertagsverschiebung des Mietbeginns.

