# Finderlohn und Gastwirtshaftung

Exakte EUR-Brüche ohne automatische Rundung; Dezimaleingaben als Zeichenfolgen. Bewertete Tatsachen müssen vom Nutzer geliefert werden. Jede Funktion berechnet ausschließlich den dokumentierten Anspruchsbetrag und ersetzt keine vollständige Anspruchsprüfung.

## finderlohn_betrag

`finderlohn_betrag(sachwert, tier, nur_persoenlicher_wert, billiger_finderlohn, fundort, bediensteter, anzeigepflicht_verletzt, fund_verheimlicht, ablieferungspflicht_verletzt)`

Allgemeiner Fund: bei verletzter Anzeigepflicht oder Verheimlichen auf Nachfrage kein Anspruch aus § 971 (NICHT_ANWENDBAR). Sonst bei Tieren 3 Prozent des Sachwerts, bei anderen Sachen 5 Prozent bis einschließlich 500 EUR plus 3 Prozent darüber. Nur persönlicher Wert: billiger_finderlohn als bewerteter Betrag, keine Ermessensformel. Behörde/Verkehrsanstalt: mindestens 50 EUR Sachwert, kein Bediensteter und keine Ablieferungspflichtverletzung; dann Hälfte des nach § 971 Abs. 1 Satz 2/3 bestimmten Betrags. § 971 Abs. 2 nicht zusätzlich auf öffentlichen Fund anwenden.

Betrag eines grundsätzlich ausgewählten Finderlohnanspruchs, nicht Fälligkeit, Durchsetzbarkeit oder Erlöschensfrist. § 1001 bei öffentlichem Fund und § 978 Abs. 3 bei Erlösanfall gesondert beachten. Anzeigepflichtverletzung muss rechtlich bewertet sein: bei unbekanntem Empfangsberechtigten keine Behördenanzeige bis einschließlich 10 EUR nach § 965 Abs. 2, nicht pauschale Befreiung von jeder Anzeige. Der Bewertungszweig für ausschließlich persönlichen Wert ist nur Entscheidungs-/Eingabevertrag, keine implementierte Ermessensbemessung.

- `sachwert`: Nichtnegative Dezimalzeichenfolge in EUR des bewerteten Sachwerts. Bei öffentlichem Fund für die 50-EUR-Schwelle erforderlich; die Bewertung erfolgt durch den Nutzer.
- `tier`: Expliziter Wahrheitswert, ob es sich um ein Tier handelt; dann keine 5-Prozent-Stufe.
- `nur_persoenlicher_wert`: Expliziter Wahrheitswert, ob die Sache nur für den Empfangsberechtigten Wert hat. Dann billige Bemessung statt Prozentstaffel.
- `billiger_finderlohn`: Bei ausschließlich persönlichem Wert erforderliche nichtnegative Dezimalzeichenfolge in EUR. Sonst None. Dies ist eine bewertete Nutzervorgabe, keine von der Library ermittelte Ermessensentscheidung.
- `fundort`: allgemein oder behoerde_oder_verkehrsanstalt. Letzteres setzt den gesetzlichen Ortsbezug nach § 978 voraus, nicht beliebigen öffentlichen Raum.
- `bediensteter`: Expliziter Wahrheitswert, ob der Finder Bediensteter der betroffenen Behörde oder Verkehrsanstalt ist; Ausschluss nur im öffentlichen Fundzweig.
- `anzeigepflicht_verletzt`: Rechtlich bewertete Verletzung der Anzeigepflicht nach § 965. Die Ausnahme bis einschließlich 10 EUR betrifft die Behördenanzeige bei unbekanntem Empfangsberechtigten, nicht jede Anzeige.
- `fund_verheimlicht`: Expliziter Wahrheitswert, ob der Finder den Fund auf Nachfrage verheimlicht hat; § 971 Abs. 2 im allgemeinen Fundzweig.
- `ablieferungspflicht_verletzt`: Expliziter Wahrheitswert zur Pflicht aus § 978 Abs. 1; maßgeblich im öffentlichen Fundzweig.

Regel-ID: `BGB_FINDERLOHN_BETRAG`. Quellenanker: BGB_965_T0001, BGB_965_T0002, BGB_965_T0003, BGB_971_T0001, BGB_971_T0002, BGB_971_T0003, BGB_971_T0004, BGB_978_T0001, BGB_978_T0002, BGB_978_T0003, BGB_978_T0004, BGB_978_T0005, BGB_978_T0006, BGB_978_T0007, BGB_978_T0008, BGB_978_T0009, BGB_1001_T0001, BGB_1001_T0002, BGB_1001_T0003.

## gastwirt_haftungsbetrag

`gastwirt_haftungsbetrag(beherbergungspreis_tag, schaden, beherbergung_gewerblich, eingebracht_nach_701, sachenart, ursache, verschulden_gastwirt_oder_leute, aufbewahrung_uebernommen, aufbewahrung_pflichtwidrig_abgelehnt, anzeige_unverzueglich)`

Nur gewerbliche Beherbergung, nach § 701 Abs. 2 eingebrachte Sache, keine Ausschlussursache und keine ausgeschlossene Sachenart. Ohne unverzügliche Anzeige Anspruch erloschen, außer Aufbewahrung übernommen oder Gastwirt/Leute schuldhaft. Bei Verschulden, übernommener Aufbewahrung oder pflichtwidrig abgelehnter Aufbewahrung unbeschränkt bis zum tatsächlichen ersatzfähigen Schaden. Sonst Grenze=min(max(100*Beherbergungspreis je Tag,600),3500), bei Geld/Wertpapieren/Kostbarkeiten 800 statt 3500; Betrag=min(Schaden,Grenze).

Nur gesetzliche Haftung nach §§ 701–703, keine Entscheidung über zusätzliche vertragliche/deliktische Ansprüche. eingebracht_nach_701 erfordert Aufenthalts-/Obhuts-/Ortsbezug, bei Leuten deren Bestellung bzw. zurechenbare Bestellung; angemessener Vor-/Nachzeitraum ist bewertete Eingabe. Pflichtwidrige Ablehnung muss Voraussetzungen/Ausnahmen des § 702 Abs. 3 berücksichtigen. Ablehnung allein befreit nicht von der Anzeige nach § 703. Schaden als ersatzfähiger Betrag nach allgemeinen Schadensregeln, keine doppelte Mitverschuldensreduktion.

- `beherbergungspreis_tag`: Nichtnegative Dezimalzeichenfolge in EUR des Beherbergungspreises für einen Tag; keine automatische Ableitung aus Gesamtpreis inklusive Zusatzleistungen.
- `schaden`: Nichtnegative Dezimalzeichenfolge in EUR des ersatzfähigen Schadens, bereits nach den einschlägigen allgemeinen Schadensregeln ermittelt.
- `beherbergung_gewerblich`: Expliziter Wahrheitswert zur gewerbsmäßigen Aufnahme des betroffenen Gastes zur Beherbergung.
- `eingebracht_nach_701`: Rechtlich bewerteter Wahrheitswert: Sache in Unterkunft, angewiesenem/bestimmtem Außenort oder Obhut während Aufenthalts bzw. Obhut innerhalb angemessener Vor-/Nachfrist; bei Leuten auch Bestellungs-/Zurechnungsanforderung. Keine automatische Orts- oder Angemessenheitsprüfung.
- `sachenart`: sonstige, geld_wertpapiere_kostbarkeiten, fahrzeug, fahrzeuginhalt oder lebendes_tier. Letzte drei sind vom gesetzlichen Haftungsregime ausgeschlossen.
- `ursache`: sonstige oder rechtlich festgestellte Ausschlussursache gast, begleiter, aufgenommene_person, sachbeschaffenheit oder hoehere_gewalt. Keine automatische Kausalitätsentscheidung.
- `verschulden_gastwirt_oder_leute`: Expliziter Wahrheitswert zum Verschulden am Verlust/Schaden; führt im gesetzlichen Anwendungsbereich zu unbeschränkter Haftung und Anzeigeausnahme.
- `aufbewahrung_uebernommen`: Expliziter Wahrheitswert zur übernommenen Aufbewahrung; unbeschränkte Haftung und Anzeigeausnahme.
- `aufbewahrung_pflichtwidrig_abgelehnt`: Rechtlich bewertete Ablehnung entgegen § 702 Abs. 3, unter Berücksichtigung von übermäßigem Wert/Umfang und Gefahr. Führt zur unbeschränkten Haftung, allein aber nicht zur Anzeigeausnahme.
- `anzeige_unverzueglich`: Expliziter Wahrheitswert zur unverzüglichen Schadensanzeige ab Kenntnis. Unverzüglich wird nicht durch eine erfundene feste Tageszahl ersetzt.

Regel-ID: `BGB_GASTWIRT_HAFTUNGSBETRAG`. Quellenanker: BGB_701_T0001, BGB_701_T0002, BGB_701_T0003, BGB_701_T0004, BGB_701_T0005, BGB_701_T0006, BGB_701_T0007, BGB_702_T0001, BGB_702_T0002, BGB_702_T0003, BGB_702_T0004, BGB_702_T0005, BGB_702_T0006, BGB_703_T0001, BGB_703_T0002.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
