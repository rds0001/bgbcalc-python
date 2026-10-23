# Bausicherheiten

Beträge in EUR, ohne automatische Cent-Rundung. Sicherungsbetrag und rechtliche Geeignetheit einer konkreten Sicherheit sind zu unterscheiden.

## bau_sicherungsbetrag

Sicherungsbetrag = 110 Prozent der offenen Vergütung nach Abzug unstreitiger oder rechtskräftig festgestellter aufrechenbarer Gegenforderung, mindestens null. Streitige, nicht rechtskräftig festgestellte Gegenforderungen bleiben unberücksichtigt.

Offene Vergütung umfasst Zusatzaufträge und einschlägige Ersatzansprüche nach Abs. 1 Satz 2; Leistungen nicht doppelt zählen. bestellerart sonstiger umfasst auch Verbraucher außerhalb eines Verbraucherbau-/Bauträgervertrags. Öffentlich-rechtlicher Ausschluss setzt Insolvenzunfähigkeit voraus. Verbraucher-Ausnahme entfällt nur bei Baubetreuer, der zur Verfügung über Finanzierungsmittel ermächtigt ist. Abs. 2 Zahlungsbedingungen einer Garantie, Sicherungskosten, Sicherungshypothekenausschluss und Kündigungsfolgen sind gesonderte Regeln. Bei mehreren Gegenforderungen nach rechtlicher Qualifikation getrennt summieren; keine pauschale Anerkennung streitiger Teile.

wert enthält den exakten Sicherungsbetrag als Bruch mit zaehler und nenner als Ganzzahlzeichenfolgen.

- `offene_verguetung`: Nichtnegative Dezimalzeichenfolge der offenen vereinbarten Vergütung einschließlich Zusatzaufträgen bzw. einschlägiger Ersatzansprüche, vor Abzug der hier angegebenen Gegenforderung.
- `aufrechenbare_gegenforderung`: Nichtnegative Dezimalzeichenfolge einer zur Aufrechnung geeigneten Gegenforderung. Bei mehreren Forderungen vorher nach unstreitig/rechtskräftig und streitig gruppieren.
- `gegenforderung_unstreitig`: Expliziter Wahrheitswert: Die angegebene Gegenforderung ist unstreitig.
- `gegenforderung_rechtskraeftig`: Expliziter Wahrheitswert: Die angegebene Gegenforderung ist rechtskräftig festgestellt.
- `bestellerart`: sonstiger, oeffentlich_insolvenzunfaehig, verbraucherbau oder bautraeger_verbraucher. sonstiger umfasst auch Verbraucher außerhalb von § 650i/§ 650u. Öffentlich-rechtliche Rechtsform allein genügt nicht; Insolvenzverfahren muss unzulässig sein.
- `baubetreuer_bevollmaechtigt`: Expliziter Wahrheitswert: Ein Baubetreuer betreut das Vorhaben und ist zur Verfügung über Finanzierungsmittel des Bestellers ermächtigt. Nur der Verbraucherausschluss wird dadurch aufgehoben.

## verbraucherbau_herstellungssicherheit

Grundsicherheit = 5 Prozent der ursprünglichen vereinbarten Gesamtvergütung. Überschreitet die kumulierte Mehrvergütung 10 Prozent der ursprünglichen Gesamtvergütung, zusätzliche Sicherheit = 5 Prozent der gesamten Mehrvergütung. Noch zu stellen = max(Grundsicherheit + zusätzliche Sicherheit - bereits gestellte Sicherheit, 0).

§ 650m Abs. 2 im Verbraucherbauvertrag nach § 650i. Grundsicherheit bei erster Abschlagszahlung, zusätzliche Sicherheit bei nächster Abschlagszahlung nach Schwellenüberschreitung. Berechnung bestimmt Betrag, nicht automatisch Fälligkeit. Gesetzlich relevante Änderungen/Ergänzungen als kumulierte positive Mehrvergütung eingeben; Minderungen oder wechselnde Vertragsbasen erfordern eigene Bewertung. Bereits gestellte Sicherheit muss rechtlich geeignet und noch verfügbar sein. Kein automatischer Freigabeanspruch bei Übersicherung. Einbehalt nur auf Verlangen des Unternehmers; konkrete Verteilung auf Abschlagszahlungen gesondert.

wert enthält grundsicherheit, zusaetzliche_sicherheit, gesamtsicherheit und noch_zu_stellen, jeweils als exakten Bruch mit zaehler und nenner als Ganzzahlzeichenfolgen.

- `urspruengliche_gesamtverguetung`: Positive Dezimalzeichenfolge der ursprünglichen vereinbarten Gesamtvergütung in EUR.
- `zusaetzliche_verguetung`: Nichtnegative Dezimalzeichenfolge der kumulierten relevanten Mehrvergütung aus Änderungen oder Ergänzungen in EUR.
- `bereits_gestellte_sicherheit`: Nichtnegative Dezimalzeichenfolge der rechtlich geeigneten, noch verfügbaren bereits gestellten Herstellungssicherheit in EUR.
- `verbraucherbauvertrag`: Expliziter Wahrheitswert zur Einordnung als Verbraucherbauvertrag nach § 650i.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
