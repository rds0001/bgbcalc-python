# Zugewinn: rechnerische Grundstufen

Diese Funktionen arbeiten mit bereits rechtlich bewerteten Vermögenswerten. Sie ermitteln keine Verkehrswerte, Inflationsindizes oder Sonderbewertungen. Sämtliche Eingaben bleiben als nutzervorgaben im Ergebnis sichtbar.

## zugewinn_betrag

Zugewinn = max(Endvermögen - Anfangsvermögen, 0). Negative Anfangs- und Endvermögen sind zulässig; Schuldenabbau kann Zugewinn erzeugen.

Rechnerischer Kern nach § 1373; keine automatische Vermögensbewertung, Kaufkraftbereinigung, Bestimmung privilegierter Erwerbe oder illoyaler Vermögensminderungen. Eingaben müssen für den maßgeblichen Fall rechtlich zutreffend und vergleichbar bewertet sein. § 1376 Abs. 4 einschließlich verfassungsgerichtlicher Maßgaben bleibt eigener ungeklärter Bewertungszweig, nicht durch diese Funktion freigegeben.

wert enthält den exakten Zugewinn als Bruch mit zaehler und nenner als Ganzzahlzeichenfolgen.

- `anfangsvermoegen`: Signierte Dezimalzeichenfolge des rechtlich bewerteten und erforderlichenfalls bereinigten Anfangsvermögens in EUR, einschließlich maßgeblicher Hinzurechnungen. Negative Werte sind zulässig.
- `endvermoegen`: Signierte Dezimalzeichenfolge des rechtlich bewerteten Endvermögens in EUR, einschließlich maßgeblicher Hinzurechnungen. Negative Werte sind zulässig.
- `bewertungsnachweis`: Nichtleere Beschreibung der Werte, Bereinigungen, Hinzurechnungen und maßgeblichen Bewertungsstichtage. Keine automatische Kaufkraft- oder Sonderbewertung.

## zugewinnausgleich_grundbetrag

Richtung aus größerem Zugewinn bestimmen; halber Überschuss = abs(Zugewinn A - Zugewinn B)/2. Haftungsgrenze = max(vorhandenes Nettovermögen des Verpflichteten + anerkannte Hinzurechnung nach § 1375 Abs. 2 Satz 1, 0). Grundbetrag = min(halber Überschuss, Haftungsgrenze). Bei Gleichheit Richtung kein_ueberschuss und alle Beträge null.

Berechnungsstufe nach § 1378 Abs. 1/2 vor Anrechnung nach § 1380, Leistungsverweigerung § 1381, Stundung § 1382 oder besonderen Vereinbarungen. Kein abschließender durchsetzbarer Zahlbetrag. Richtige Stichtage nach §§ 1384/1387 und rechtlich anerkannte Hinzurechnungen vorgeben; Berechnungsstichtag nicht mit Entstehung/Fälligkeit gleichsetzen. Negative Nettovermögen erst nach Addition der Hinzurechnung auf null begrenzen. Hinzurechnungen nicht doppelt im vorhandenen Nettovermögen erfassen.

wert enthält richtung (a_an_b, b_an_a oder kein_ueberschuss), halber_ueberschuss, haftungsgrenze und grundbetrag. Beträge sind exakte EUR-Brüche mit zaehler und nenner als Ganzzahlzeichenfolgen. Die Richtung beschreibt den Zugewinnüberschuss auch dann, wenn die Haftungsgrenze den Betrag auf null begrenzt.

- `zugewinn_ehegatte_a`: Nichtnegative Dezimalzeichenfolge des bereits berechneten Zugewinns von Ehegatte A in EUR.
- `zugewinn_ehegatte_b`: Nichtnegative Dezimalzeichenfolge des bereits berechneten Zugewinns von Ehegatte B in EUR.
- `nettovermoegen_ehegatte_a`: Signierte Dezimalzeichenfolge des tatsächlich vorhandenen Vermögens von A nach Schuldenabzug, ohne die separat angegebene Hinzurechnung.
- `nettovermoegen_ehegatte_b`: Signierte Dezimalzeichenfolge des tatsächlich vorhandenen Vermögens von B nach Schuldenabzug, ohne die separat angegebene Hinzurechnung.
- `hinzurechnung_ehegatte_a`: Nichtnegative Dezimalzeichenfolge der anerkannten Hinzurechnung nach § 1375 Abs. 2 Satz 1 für A, unter Berücksichtigung der Ausschlüsse aus Abs. 3.
- `hinzurechnung_ehegatte_b`: Nichtnegative Dezimalzeichenfolge der anerkannten Hinzurechnung nach § 1375 Abs. 2 Satz 1 für B, unter Berücksichtigung der Ausschlüsse aus Abs. 3.
- `bewertungsnachweis`: Nichtleere Beschreibung der Werte, Bereinigungen, Hinzurechnungen und maßgeblichen Bewertungsstichtage. Keine automatische Kaufkraft- oder Sonderbewertung.

## Exakte Zahleneingaben

Für die als Dezimaltexte beschriebenen Eingaben sind auch exakte Bruchobjekte wie `{"zaehler": "1", "nenner": "3"}` zulässig, einschließlich solcher Felder in Listen. Zähler und Nenner sind kanonische Ganzzahlzeichenfolgen; der Nenner ist positiv. Fachliche Wertebereiche bleiben unverändert. Siehe [gemeinsamer Zahlenvertrag](../../fachkonzept/NUMERIK.md). Dadurch können passende Betragsfelder von Ergebnissen ohne Dezimalrundung weiterverwendet werden. Getrennte ganzzahlige Quotenzähler/-nenner, Anzahlen, Altersstufen und Datumsangaben behalten ihre bisherigen Typen.
