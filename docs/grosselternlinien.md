# Erbfolge der dritten Ordnung

## grosselternlinien_erbquoten

Zunächst Verwandtenanteil zwischen besetzten Großelternpaaren teilen, danach innerhalb jedes Paars auf besetzte Großelternstämme. Eintretende Großeltern schließen ihre Nachkommen aus; andernfalls rekursive Stammteilung. Vollständig leere Paare entfallen. Besondere Erbteile und Personenquoten sowie unmittelbar eintretenden Großeltern und deren Abkömmlingen zugeordnete Quoten getrennt ausweisen.

Gesetzliche dritte Ordnung, bei erster oder zweiter Ordnung nicht anwendbar. Rechtlich maßgebliche Abstammung und Erbenstellungen vorgegeben, keine automatische Feststellung von Adoption oder Ausschlüssen. § 1931 über Ehegatten und Großelternabkömmlinge noch nicht angewandt: diese Funktion verteilt den eingegebenen Anteil nach § 1926, sie entscheidet keine Ehegattenansprüche. Gleiche Person darf beiden Paaren angehören; besondere Anteile werden nach Großelternlinie unterschieden. Erblasser und vorrangig berufene Personen nicht widersprüchlich als berufene Nachkommen eintragen.

wert enthält erbteile mit person_id, grosselternlinie, stammpfad, quote; erbquoten summiert je Person; grosselternquote und abkoemmlingsquote summieren die beiden Personengruppen. Alle Quoten beziehen sich auf gesamten Nachlass und sind exakte Brüche. Feste Reihenfolge vaeterlich, dann muetterlich. Ohne besetzte dritte Ordnung oder bei Vorrang NICHT_ANWENDBAR.

- `grosselternpaare`: Objekt mit genau vaeterlich und muetterlich. Jeder Eintrag enthält genau zwei rekursive Knoten mit person_id, tritt_ein und abkoemmlinge entsprechend abkoemmlings_erbquoten. Innerhalb eines Paars keine doppelten Personen; dieselbe Person in beiden Paaren zulässig, sofern ihre rechtliche Erbenstellung konsistent ist.
- `vorrangige_ordnung_vorhanden`: Expliziter Wahrheitswert: Gibt es berufene Verwandte erster oder zweiter Ordnung? Dann ist die dritte Ordnung ausgeschlossen.
- `verwandtenanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des zu verteilenden Verwandtenanteils am gesamten Nachlass.
- `verwandtenanteil_nenner`: Positive ganze Zahl als Nenner; Anteil höchstens 1.

Beispiel: Ein väterlicher Großelternteil tritt ein, der andere hinterlässt keinen besetzten Stamm; beide mütterlichen Großeltern treten ein. Bei ganzem Verwandtenanteil ergeben sich 1/2 für den väterlichen Teil und je 1/4 für die mütterlichen Teile, nicht drei gleiche Drittel.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
