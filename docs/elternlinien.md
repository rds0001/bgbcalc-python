# Erbfolge der zweiten Ordnung

## elternlinien_erbquoten

Bei berufenen Verwandten erster Ordnung keine Anwendung. Sonst den Verwandtenanteil auf besetzte Elternlinien gleich verteilen; eintretende Eltern schließen ihre Abkömmlinge aus, sonst Stammteilung. Eine vollständig leere Elternlinie fällt der anderen zu. Mehrfachanteile derselben Person aus beiden Linien getrennt erhalten und summieren.

Gesetzliche zweite Ordnung. Rechtlich maßgebliche Elternschaft und Abkömmlingsbeziehungen vorgeben; insbesondere die Beziehungen mit Ausschluss nach § 1925 Abs. 4 i.V.m. § 1756 vorher abgrenzen. Erblasser selbst nicht als berufenen Abkömmling aufnehmen. Verwandtenanteil nach Ehegattenquote bereits bestimmt. Keine Feststellung von Adoption, Verzicht, Ausschlagung oder Erbunwürdigkeit. Fehlt erste Ordnung und ist auch zweite Ordnung leer, sind weitere Ordnungen gesondert zu prüfen.

wert enthält erbteile (person_id, stammpfad, quote) und erbquoten (person_id, quote). Quoten exakte Brüche als Ganzzahlzeichenfolgen. Reihenfolge folgt Eingabestämmen, Zusammenfassung je Person nach erstem Auftreten. Ohne eintretende Personen NICHT_ANWENDBAR und wert null.

- `elternlinien`: Genau zwei rekursive Knoten (je ein Elternteil), mit person_id, tritt_ein und abkoemmlinge entsprechend abkoemmlings_erbquoten. Fehlende berufene Personen als nicht eintretender Knoten ohne berufene Nachkommen darstellen.
- `erste_ordnung_vorhanden`: Expliziter Wahrheitswert: Ist ein gesetzlich berufener Verwandter erster Ordnung vorhanden? Dann ist die zweite Ordnung ausgeschlossen.
- `verwandtenanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des rechtlich bestimmten Verwandtenanteils am gesamten Nachlass.
- `verwandtenanteil_nenner`: Positive ganze Zahl als Nenner; der Verwandtenanteil darf 1 nicht überschreiten.

Beispiel: Beide Eltern sind vertreten; K1 gehört beiden Elternlinien an, K2 nur der väterlichen. Die väterliche Hälfte wird zwischen K1 und K2 geteilt, die mütterliche Hälfte erhält K1 allein. Gesamtquoten: K1 3/4, K2 1/4.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
