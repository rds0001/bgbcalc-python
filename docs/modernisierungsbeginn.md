# Beginn der erhöhten Miete

## modernisierung_erhoehungsbeginn

Bei wirksamer Erklärung: erster Tag des dritten Kalendermonats nach dem Zugangsmonat. Wenn die Ankündigung nicht ordnungsgemäß war oder der tatsächliche Erhöhungsbetrag mehr als 110 Prozent des angekündigten beträgt, einmalig sechs Monate später. Genau zehn Prozent Überschreitung verlängern nicht.

Berechnet den Beginn der erhöhten Miete, nicht die Fälligkeit einer konkreten Zahlung. Keine Verschiebung von Sonn- oder Feiertagen. Die beiden Verlängerungsgründe werden mit ODER verbunden und nicht kumuliert. Entsprechende Anwendung im vereinfachten Verfahren (§ 559c Absatz 3) und beim Heizungseinbau (§ 559e Absatz 4) setzt deren gesonderte Voraussetzungen voraus. Keine Ermittlung der zulässigen Erhöhung oder Prüfung der Ankündigungs- und Erklärungsvoraussetzungen. Gleiche Bezugszeiträume der beiden Beträge sind durch den Aufrufer sicherzustellen.

ISO-Datum in wert; bei NICHT_ANWENDBAR wert null. Ergebnisobjekt enthält ursprüngliche Eingaben, Nutzervorgaben und die beiden Verzögerungsprüfungen. Datumsüberschreitung über 9999 führt zu EINGABE_UNGUELTIG.

- `zugang_erklaerung`: Kalenderdatum des Zugangs der Mieterhöhungserklärung als ISO-Zeichenfolge JJJJ-MM-TT im Bereich 0001 bis 9999; der Zugangstag wird nicht automatisch rechtlich festgestellt.
- `ankuendigung_ordnungsgemaess`: Expliziter Wahrheitswert, ob die Ankündigung den in § 559b Absatz 2 Nummer 1 genannten Anforderungen des § 555c entspricht, einschließlich einschlägiger Ausnahmen. FALSE auch bei fehlender erforderlicher Ankündigung.
- `angekuendigter_erhoehungsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Angekündigter Erhöhungsbetrag, nicht gesamte Miete. Bei vollständig fehlender Ankündigung ausdrücklich null Euro eingeben. Gleicher Bezugszeitraum wie der tatsächliche Betrag.
- `tatsaechlicher_erhoehungsbetrag`: Nichtnegative EUR-Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Rechtlich ermittelter tatsächlicher Erhöhungsbetrag im gleichen Bezugszeitraum wie die Ankündigung; keine automatische Kosten- oder Kappungsberechnung.
- `erklaerung_wirksam`: Expliziter Wahrheitswert zur wirksamen Erhöhungserklärung und sonstigen Voraussetzungen des ausgewählten Falls. Form, Berechnung und Erläuterung nach § 559b Absatz 1 sowie Besonderheiten des Verfahrens sind zuvor zu prüfen; FALSE ergibt NICHT_ANWENDBAR.
