# Verbraucherbau: Grenzen für Abschläge und Sicherheiten

## verbraucherbau_abschlagsgrenze

Gesamtgrenze = 90 Prozent der vereinbarten Gesamtvergütung einschließlich Nachtragsleistungen. Verbleibender Rahmen = max(Gesamtgrenze - bisherige Abschläge, 0).

Gilt nur im Verbraucherbauvertrag für verlangte Abschläge nach § 632a; Bauträgervertrag nach § 650u Abs. 2 ausgeschlossen. Der verbleibende Rahmen ist keine automatisch fällige Abschlagsforderung: Leistungswert, Nachweis, Eigentumsübertragung oder Materialsicherheit, Mängelrechte und Sicherheitseinbehalt nach § 650m Abs. 2 sind gesondert zu prüfen. Keine Berechnung eines Rückzahlungsanspruchs bei bereits überschrittener Grenze. Abweichende Vertragsregelungen werden nicht ausgewertet.

wert enthält gesamtgrenze und verbleibender_rahmen als exakte EUR-Brüche. Ergebnisobjekt mit Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten; NICHT_ANWENDBAR mit wert null außerhalb des Tatbestands.

- `gesamtverguetung`: Nichtnegative EUR-Dezimalzeichenfolge der vereinbarten Gesamtvergütung einschließlich Nachtragsleistungen nach § 650c.
- `bisherige_abschlaege`: Nichtnegative EUR-Dezimalzeichenfolge der bereits in Anspruch genommenen Abschläge, die bei der Gesamtgrenze anzurechnen sind. Keine doppelte Zählung bereits in einer weiteren Forderung enthaltener Beträge.
- `verbraucherbauvertrag`: Expliziter Wahrheitswert zur rechtlichen Einordnung nach § 650i, gegebenenfalls in Verbindung mit § 650u.
- `bautraegervertrag`: Expliziter Wahrheitswert zur Einordnung als Bauträgervertrag nach § 650u. Dessen Absatz 2 schließt die 90-Prozent-Grenze aus.
- `abschlag_nach_632a`: Expliziter Wahrheitswert: Der Unternehmer verlangt eine Abschlagszahlung nach § 632a.

## verbraucherbau_sicherungsgrenze

Betragsgrenze = Minimum aus nächster Abschlagszahlung und 20 Prozent der vereinbarten Vergütung. Überschreitung nur bei strikt größerer vereinbarter Sicherheit.

Sicherheit des Verbrauchers für die Vergütung, nicht die vom Unternehmer geschuldete Herstellungssicherheit nach Absatz 2. Anwendbar bei verlangten Abschlägen nach § 632a oder vereinbarten Abschlägen. § 650u Abs. 2 schließt nur Absatz 1, nicht Absatz 4 aus. Die Überschreitung kennzeichnet den betragsmäßigen Unwirksamkeitstatbestand; die Funktion reduziert eine unwirksame Vereinbarung nicht automatisch auf den Grenzbetrag. Weitere Wirksamkeitsgründe werden nicht geprüft.

wert enthält betragsgrenze als exakten EUR-Bruch und betragsgrenze_ueberschritten als Wahrheitswert. Ergebnisobjekt mit Regel- und Quellenfassung, Eingaben, Nutzervorgaben und Rechenschritten; NICHT_ANWENDBAR mit wert null außerhalb des Tatbestands.

- `vereinbarte_verguetung`: Nichtnegative EUR-Dezimalzeichenfolge der für § 650m Abs. 4 maßgeblichen vereinbarten Vergütung.
- `naechste_abschlagszahlung`: Nichtnegative EUR-Dezimalzeichenfolge der nächsten maßgeblichen Abschlagszahlung.
- `vereinbarte_sicherheit`: Nichtnegative EUR-Dezimalzeichenfolge der Sicherheit, zu der die Vereinbarung den Verbraucher verpflichtet.
- `verbraucherbauvertrag`: Expliziter Wahrheitswert zur rechtlichen Einordnung nach § 650i, gegebenenfalls in Verbindung mit § 650u.
- `abschlaege_verlangt`: Expliziter Wahrheitswert: Der Unternehmer verlangt Abschlagszahlungen nach § 632a.
- `abschlaege_vereinbart`: Expliziter Wahrheitswert: Die Parteien haben Abschlagszahlungen vereinbart; dies genügt auch ohne bereits erhobene Forderung.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
