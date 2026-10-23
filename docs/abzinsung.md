# Vorzeitige Befriedigung

## vorzeitiger_befriedigungsbetrag

Bei erfüllten Voraussetzungen und unverzinslicher noch nicht fälliger Forderung: Auszahlungsbetrag = Forderungsbetrag / (1 + 4/100 * Jahresanteil bis Fälligkeit).

§ 1133: hypothekarische Sicherheit durch Grundstücksverschlechterung gefährdet, angemessene Abhilfefrist abgelaufen und Gefährdung nicht beseitigt. § 1217 Abs. 2: erhebliche fortgesetzte Rechtsverletzung trotz Abmahnung nach Abs. 1 und Rückgabe gegen Befriedigung statt Hinterlegung/Verwahrung verlangt. Diese Voraussetzungen werden in voraussetzungen_erfuellt bewertet eingegeben. Bei fehlender Voraussetzung NICHT_ANWENDBAR, nicht eine Berechnung anderer Ansprüche. Gesetzlicher Satz § 246 von 4 Prozent; kein Verzugszins oder Zinseszins.

- `forderungsbetrag`: Nichtnegative Dezimalzeichenfolge des Forderungsbetrags in EUR.
- `zeitanteil_zaehler`: Nichtnegative ganze Zahl des belegten Jahresanteils von Zahlung bis Fälligkeit.
- `zeitanteil_nenner`: Positive ganze Zahl als Nenner des Jahresanteils.
- `zeitanteil_nachweis`: Nichtleere Beschreibung des maßgeblichen Zeitraums und der Zeitkonvention.
- `unverzinslich`: Expliziter Wahrheitswert, ob die Forderung unverzinslich ist.
- `noch_nicht_faellig`: Expliziter Wahrheitswert, ob die Forderung bei Zahlung noch nicht fällig ist.
- `befriedigungsgrund`: hypothek_gefaehrdung für § 1133 oder pfand_rueckgabe für § 1217 Abs. 2.
- `voraussetzungen_erfuellt`: Expliziter Wahrheitswert zur rechtlichen Bewertung der nachfolgend erläuterten Voraussetzungen des ausgewählten Befriedigungsgrundes.

Beispiel: 1.040 EUR Forderung und ein voller Jahresanteil ergeben 1.000 EUR Auszahlung, weil 1.000 + 4 % von 1.000 = 1.040. Nicht 4 % vom Forderungsbetrag abziehen. Exakte Bruchausgabe, keine Cent-Rundung.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
