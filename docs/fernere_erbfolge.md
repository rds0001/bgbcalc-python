# Vierte und fernere Erbordnungen

## fernere_erbquoten

Bei Vorrang einer früheren Ordnung keine Anwendung. Sind Voreltern der ausgewählten Ordnung vorhanden, teilen diese den Anteil gleich, unabhängig von Linien. Sonst nur Abkömmlinge mit kleinstem Verwandtschaftsgrad auswählen und gleich teilen. Wiederholt aufgeführte Person nur einmal zählen; bei verschiedenen Wegen kleinsten Grad dieser Person berücksichtigen. Keine Stammvertretung.

Rechtliche Berufung, gewählte Ordnung, Vorelterneigenschaft und Verwandtschaftsgrade sind vorgegeben; Grade zählen vermittelnde Geburten nach § 1589. Keine automatische Stammbaumauswertung, Adoption oder Erbausschlussprüfung. Voreltern und Abkömmlinge sind innerhalb derselben ausgewählten Ordnung disjunkte Rollen. Ein überlebender Ehegatte kann nach § 1931 Abs. 2 fernere Verwandte vollständig ausschließen; keine zusätzliche Ehegattenquote in dieser Funktion. § 1927 über besondere Stammanteile gilt nur bis dritter Ordnung.

wert enthält auswahl (voreltern oder naechste_abkoemmlinge), massgeblicher_grad und erbquoten je Person. Exakte Brüche, Personenreihenfolge nach erstem Auftreten. Ohne berufene Personen oder bei Vorrang NICHT_ANWENDBAR.

- `ordnungsnummer`: Ganze Zahl ab 4 bis zur technischen Grenze 10000. Die rechtlich maßgebliche Ordnung ist vorab festgestellt.
- `voreltern`: Liste von person_id-Zeichenfolgen der berufenen Voreltern dieser Ordnung; in R ebenfalls list verwenden. Leere Liste, wenn keine vorhanden. Mehrfach aufgeführte Personen werden einmal gezählt.
- `abkoemmlinge`: Liste von Objekten mit genau person_id und verwandtschaftsgrad. Grad ist eine positive ganze Zahl bis 10000; bei mehreren Verwandtschaftswegen derselben Person gilt ihr kleinster eingegebener Grad.
- `vorrangige_ordnung_vorhanden`: Expliziter Wahrheitswert zum Vorhandensein berufener Verwandter einer früheren Ordnung.
- `verwandtenanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des vorgegebenen Verwandtenanteils am Nachlass.
- `verwandtenanteil_nenner`: Positive ganze Zahl als Nenner, Anteil höchstens 1.

Anders als in den ersten drei Ordnungen zählen keine besonderen Stammanteile. Zwei nächstverwandte Personen teilen gleich, auch wenn sie verschiedenen Linien angehören. Eine mehrfach auftauchende Person erhält dadurch keinen zusätzlichen Anteil.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
