# Minderung

## minderung_betrag

Minderungsbetrag = vereinbarter Preis * (1 - wirklicher Wert/mangelfreier Wert) * Mangelzeitanteil. Geminderter Preis = vereinbarter Preis - Minderungsbetrag. Erstattungsbetrag = max(geleistete Zahlung - geminderter Preis, 0). Kauf/Werk und digitale Einmalbereitstellung verlangen Zeitanteil 1; digitale Dauerbereitstellung und Reise berücksichtigen betroffene Dauer.

Kauf/Werk/Reise: Bewertungszeitpunkt Vertragsschluss; digitale Produkte: Bereitstellung. Kauf/Werk/Digital: wirksame Minderungserklärung erforderlich; Reise kraft Gesetzes ohne Erklärung. Anzeigeausschluss nur Reise: schuldhaft unterlassene Anzeige hat Abhilfe verhindert, § 651o Abs. 2; bloß verspätete Anzeige genügt nicht. Sonstige Voraussetzungen und Ausschlüsse einschließlich gemeinsamer Erklärung bei mehreren Käufern/Bestellern/Verkäufern/Unternehmern werden in minderungsrecht bewertet eingegeben. Zeitanteil setzt eine entsprechend gleichmäßig bepreiste Bezugsperiode voraus; bei unterschiedlichen Preis-/Mangelabschnitten getrennte Bewertung erforderlich, keine blind nach Tagen verteilte Gesamtreise. Schätzungen sind Nutzervorgaben; kein automatischer Bewertungsalgorithmus. Erstattungsfrist/Zahlungsmittel nach § 327n Abs. 4 sowie Nutzungsherausgabe §§ 346/347 sind gesondert.

wert enthält geminderter_preis, minderungsbetrag, erstattungsbetrag als exakte EUR-Brüche. Bei Nichtanwendbarkeit wert null. Keine automatische Cent-Rundung.

- `vereinbarter_preis`: Nichtnegative Dezimalzeichenfolge des vereinbarten Preises in EUR für die bewertete Leistung oder Bezugsperiode.
- `mangelfreier_wert`: Positive Dezimalzeichenfolge des bewerteten Werts in mangelfreiem Zustand zum maßgeblichen Bewertungszeitpunkt.
- `wirklicher_wert`: Nichtnegative Dezimalzeichenfolge des tatsächlichen Werts zum selben Bewertungszeitpunkt; höchstens der mangelfreie Wert.
- `geleistete_zahlung`: Nichtnegative Dezimalzeichenfolge der auf die ausgewählte Leistung bereits gezahlten Summe in EUR.
- `regelbereich`: kauf, werk, digital_einmal, digital_dauer oder reise. Mietminderung gehört nicht zu dieser Funktion.
- `wertzeitpunkt`: vertragsschluss für Kauf/Werk/Reise; bereitstellung für digitale Produkte. Beide Vergleichswerte müssen diesem Zeitpunkt zugeordnet sein.
- `mangelzeitanteil_zaehler`: Nichtnegative ganze Zahl des betroffenen Zeitanteils. Bei Kauf/Werk/digital_einmal muss der Anteil genau 1 sein.
- `mangelzeitanteil_nenner`: Positive ganze Zahl als Nenner; der Zeitanteil darf insgesamt 1 nicht überschreiten.
- `wert_und_zeitnachweis`: Nichtleere Beschreibung der Wertansätze und der zeitlichen Zuordnung. Zeitgewichtung nur für passend bepreiste Bezugsperiode; unterschiedliche Preis- oder Mangelabschnitte getrennt bewerten.
- `minderungsrecht`: Expliziter Wahrheitswert zu den sonstigen rechtlichen Voraussetzungen und Ausschlüssen; ersetzt keine automatische Rechtsprüfung.
- `minderungserklaerung`: Expliziter Wahrheitswert zur wirksamen Erklärung. Im Reisebereich wird keine Erklärung verlangt; der Wert beeinflusst dort die Berechnung nicht.
- `anzeigeausschluss`: Nur für Reise: schuldhaft unterlassene Anzeige hat eine Abhilfe verhindert. In anderen Bereichen False. Bloße Verspätung reicht für den Ausschluss nicht aus.

Beispiel: Vereinbarter Preis 800 EUR, mangelfreier Wert 1.000 EUR, wirklicher Wert 750 EUR ergeben 600 EUR geminderten Preis. Bei vollständig gezahltem Preis sind 200 EUR zu erstatten. Vergleichswerte sind bewertete Eingaben, keine automatisch geschätzten Marktdaten.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
