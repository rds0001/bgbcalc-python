# Erbfolge nach Stämmen

## abkoemmlings_erbquoten

Jeder mit einer eintretenden Person besetzte Stamm erhält gleichen Anteil; ohne eigene eintretende Person wird der Anteil rekursiv auf seine besetzten Unterstämme verteilt. Eintretende Vorfahren schließen ihre über diesen Pfad verwandten Nachkommen aus. Leere Stämme fallen weg. Erbteile einer Person aus mehreren Stämmen bleiben separat nachgewiesen und werden zusätzlich zur Gesamtquote addiert.

Rechnerische Erbfolge erster Ordnung bei vorab rechtlich bestimmter Abstammung und Erbenstellung. tritt_ein bildet die maßgebliche rechtliche Stellung ab, einschließlich § 1923 Abs. 2 und einschlägiger Vertretungsfolgen; keine automatische Feststellung von Abstammung, Adoption, Erbunwürdigkeit, Ausschlagung oder testamentarischem Ausschluss. Gesetzlicher Übergang in andere Ordnungen, Ehegattenquote, Ausgleichungen und Pflichtteile gesondert. Verwandtenanteil ist bereits rechtlich ausgewählter Anteil des Nachlasses; Ausgabequoten beziehen sich auf gesamten Nachlass. Daten auch in ausgeschlossenen Unterzweigen validieren, damit Widersprüche nicht still verborgen bleiben.

wert enthält erbteile (person_id, stammpfad, quote) und erbquoten (person_id, quote). Quoten exakte Brüche als Ganzzahlzeichenfolgen. Reihenfolge folgt Eingabestämmen, Zusammenfassung je Person nach erstem Auftreten. Ohne eintretende Personen NICHT_ANWENDBAR und wert null.

- `kinderstaemme`: Liste rekursiver Knoten mit genau person_id (nichtleere Zeichenfolge), tritt_ein (expliziter Wahrheitswert zur rechtlich bestimmten Erbenstellung) und abkoemmlinge (Liste gleicher Knotenstruktur). Leere Liste erlaubt. Höchstens 64 Ebenen und 10000 Knoten. Keine doppelte Person in derselben Geschwistergruppe oder entlang eines Abstammungspfads; Mehrfachzugehörigkeit in verschiedenen Stämmen ist erlaubt.
- `verwandtenanteil_zaehler`: Nichtnegative ganze Zahl als Zähler des bereits rechtlich bestimmten Verwandtenanteils am gesamten Nachlass.
- `verwandtenanteil_nenner`: Positive ganze Zahl als Nenner des Verwandtenanteils. Anteil darf 1 nicht überschreiten.

Ein eintretendes Kind A und ein vertretenes Kind B mit zwei eintretenden Kindern B1/B2 erhalten bei vollem Verwandtenanteil A: 1/2, B1: 1/4, B2: 1/4. Eine gleiche Verteilung auf alle drei Endpersonen wäre falsch.

`tritt_ein` ist keine bloße Lebensanzeige: Bereits gezeugte Personen können nach § 1923 Abs. 2 berücksichtigt werden; Ausschlagungs-, Erbunwürdigkeits- oder Ausschlussfolgen müssen vorher rechtlich eingeordnet sein. Die Library leitet diese Tatsachen nicht aus Namen oder der Baumstruktur ab.

Die Unterscheidung zwischen geordneten Listen und Objekten sowie die zulässigen nativen R-Formen sind im [Strukturvertrag](../../fachkonzept/EINGABESTRUKTUREN.md) festgelegt.
