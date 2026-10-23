<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dienstkuendigung_teilverguetung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtverguetung`: Nichtnegative rechtlich maßgebliche vereinbarte Gesamtvergütung in EUR für den betrachteten Leistungsumfang. Gleicher Bewertungsumfang wie Leistungsanteil.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bestimmten Anteils bisher erbrachter Leistung, höchstens Nenner und2^53-1. Nicht automatisch Zeitanteil; Wert/Umfang der vereinbarten Leistungen bestimmen.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der gesamten betrachteten Leistung im selben Maßstab, höchstens2^53-1. Leistungsanteil0..1.
- `interesseloser_verguetungsanteil`: Nichtnegativer EUR-Anteil der bisher erarbeiteten Teilvergütung, dessen zugehörige Leistungen infolge der Kündigung für den anderen Teil kein Interesse mehr haben. Höchstens bisherige Teilvergütung. Rechtlich bewerteter Vergütungsanteil, nicht beliebige Schadenhöhe oder Interessenbewertung des gesamten Vertrags.
- `selbst_gekuendigt`: Wahrheitswert einer Kündigung durch den Dienstverpflichteten selbst. Rechtliche Kündigungserklärung und maßgeblichen Sachverhalt bestimmen.
- `durch_vertragsbruch_des_anderen_veranlasst`: Wahrheitswert: Eigenkündigung wurde durch vertragswidriges Verhalten des anderen Teils veranlasst. Nur bei Eigenkündigung für diese Verlustalternative maßgeblich.
- `fremdkuendigung_durch_eigenen_vertragsbruch`: Wahrheitswert: Dienstverpflichteter hat durch eigenes vertragswidriges Verhalten die Kündigung des anderen Teils veranlasst. Nicht jede Fremdkündigung gleichsetzen.
- `kuendigung_nach_626_627_nach_dienstbeginn`: Wahrheitswert einer rechtlich wirksamen Kündigung gerade nach§626 oder§627 nach Beginn der Dienstleistung. Gründe, Fristen, Kündigungsbefugnis und weitere Voraussetzungen vorab prüfen.
- `bewertungsnachweis`: Nichtleere Beschreibung von Kündigungsgrund/-richtung, Dienstbeginn, Leistungsanteil und kausal durch Kündigung eingetretenem Interessenverlust. Vorauszahlungen und gesonderte Schadenersatzansprüche separat.

Gesamtvergütung×bisheriger Leistungsanteil. Davon interesselosen Vergütungsanteil abziehen bei Eigenkündigung ohne Veranlassung durch Vertragsbruch des anderen ODER durch eigenen Vertragsbruch veranlasster Fremdkündigung.

wert ist exakte verbleibende EUR-Teilvergütung. Fehlender Anwendungsfall ergibt NICHT_ANWENDBAR/null.

Nur§628 Absatz1 Sätze1/2; kein pauschaler Totalverlust bei Eigenkündigung. Interessenverlust gerade infolge Kündigung und höchstens bisherige Teilvergütung. VorausvergütungsrückzahlungSatz3 und KündigungsschadenAbsatz2 gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_628_T0001, BGB_628_T0002

```python
from bgbcalc import dienstkuendigung_teilverguetung
dienstkuendigung_teilverguetung(
    gesamtverguetung='1200',
    leistungsanteil_zaehler=1,
    leistungsanteil_nenner=3,
    interesseloser_verguetungsanteil='0',
    selbst_gekuendigt=False,
    durch_vertragsbruch_des_anderen_veranlasst=False,
    fremdkuendigung_durch_eigenen_vertragsbruch=False,
    kuendigung_nach_626_627_nach_dienstbeginn=True,
    bewertungsnachweis='Synthetisch wirksame fristlose Dienstkündigung und bewerteter Leistungs-/Interessenanteil.',
)
```

## werkkuendigung_wichtiger_grund_verguetung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verguetung_gekuendigter_umfang`: Nichtnegative vereinbarte EUR-Vergütung ausschließlich für den wirksam gekündigten Werkumfang. Bei Teilkündigung abgegrenzten betroffenen Teil verwenden, nicht Vergütung fortgesetzter anderer Werkteile.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bestimmten Anteils bisher erbrachter Leistung, höchstens Nenner und2^53-1. Nicht automatisch Zeitanteil; Wert/Umfang der vereinbarten Leistungen bestimmen.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der gesamten betrachteten Leistung im selben Maßstab, höchstens2^53-1. Leistungsanteil0..1.
- `wichtiger_grund_wirksam_gekuendigt`: Wahrheitswert einer rechtlich wirksamen Kündigung aus wichtigem Grund nach§648a, einschließlich erforderlicher Voraussetzungen nach§314 Absatz2/3 und bei Teilkündigung Abgrenzbarkeit. Freie Kündigung§648 nicht gleichsetzen.
- `bautraegervertrag`: Wahrheitswert eines Bauträgervertrags nach§650u. TRUE schließt dieses§648a-Modell gemäßAbsatz2 aus; andere Beendigungs-/Abrechnungswege separat.
- `leistungsstandsnachweis`: Nichtleere Beschreibung des gekündigten Umfangs und des bis Kündigung erbrachten Leistungsstands, einschließlich rechtlich maßgeblicher Feststellung/Beweislast§648a Absatz4. Leistungsanteil nicht ungeprüft Zeitquote.

Vergütung des gekündigten Werkumfangs×bis zur Kündigung erbrachter Leistungsanteil. Keine Vergütung für nicht erbrachten Anteil nach§648a Absatz5.

wert ist exakter EUR-Vergütungsbetrag des erbrachten gekündigten Werkteils; fehlende wirksame Kündigung aus wichtigem Grund ergibt NICHT_ANWENDBAR/null.

Keine Fünfprozentvermutung§648 übertragen. Kündigungswirksamkeit, Beweislast/Leistungsstand und Teilabgrenzung vorab. Schadenersatz§648a Absatz6 und Vergütung fortgesetzter Werkteile separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_648a_T0001, BGB_648a_T0002, BGB_648a_T0003, BGB_648a_T0004, BGB_648a_T0005, BGB_648a_T0006, BGB_648a_T0007, BGB_648a_T0008, BGB_648a_T0009, BGB_650u_T0004

```python
from bgbcalc import werkkuendigung_wichtiger_grund_verguetung
werkkuendigung_wichtiger_grund_verguetung(
    verguetung_gekuendigter_umfang='1200',
    leistungsanteil_zaehler=0,
    leistungsanteil_nenner=3,
    wichtiger_grund_wirksam_gekuendigt=True,
    bautraegervertrag=False,
    leistungsstandsnachweis='Synthetisch wirksame Kündigung und belegter abgegrenzter Leistungsstand.',
)
```

## werk_teilverguetung_und_auslagen

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `gesamtverguetung`: Nichtnegative rechtlich maßgebliche vereinbarte Gesamtvergütung in EUR für den betrachteten Leistungsumfang. Gleicher Bewertungsumfang wie Leistungsanteil.
- `leistungsanteil_zaehler`: Nichtnegative ganze Zahl des rechtlich bestimmten Anteils bisher erbrachter Leistung, höchstens Nenner und2^53-1. Nicht automatisch Zeitanteil; Wert/Umfang der vereinbarten Leistungen bestimmen.
- `leistungsanteil_nenner`: Positive ganze Bezugsgröße der gesamten betrachteten Leistung im selben Maßstab, höchstens2^53-1. Leistungsanteil0..1.
- `nicht_inbegriffene_auslagen`: Nichtnegative rechtlich ersatzfähige Auslagen in EUR, die in der Vergütung gerade nicht enthalten sind. Bereits im Vergütungsanteil enthaltene Material-/Kostenpositionen nicht nochmals addieren.
- `werkbeeintraechtigung_vor_abnahme`: Wahrheitswert: Werk ist vor Abnahme untergegangen, verschlechtert oder unausführbar geworden. Maßgeblichen Zeitraum und tatsächlichen Zustand rechtlich feststellen.
- `bestellerstoffmangel_oder_anweisung_ursaechlich`: Wahrheitswert: Beeinträchtigung beruht auf Mangel des vom Besteller gelieferten Stoffs oder dessen für die Ausführung erteilter Anweisung. Bloße Materialbeteiligung nicht automatisch ausreichend.
- `unternehmer_zu_vertretender_umstand`: Wahrheitswert eines mitwirkenden Umstands, den der Unternehmer zu vertreten hat. TRUE schließt den hier geprüften Werkbeeinträchtigungsfall§645 Absatz1 Satz1 aus; unabhängige qualifizierte Aufhebung/Kündigung separat.
- `aufhebung_nach_643`: Wahrheitswert einer wirksamen Aufhebung gemäß§643: gesetzlicher Mitwirkungsfall§642, angemessene Frist samt Kündigungserklärung, ausgebliebene Nachholung bis Ablauf. Bloß beliebige Vertragsbeendigung nicht einsetzen.
- `kuendigung_nach_649`: Wahrheitswert einer Bestellerkündigung gerade wegen wesentlicher Überschreitung eines zugrunde gelegten Kostenanschlags ohne übernommene Richtigkeitsgewähr. Rechtliche Wesentlichkeit und Kündigungsgrund bestimmen; keine erfundene Prozentschwelle.
- `bewertungsnachweis`: Nichtleere Beschreibung von Werkbeeinträchtigung, Ursache/Vertretenmüssen oder qualifizierter Aufhebung/Kündigung, bisherigem Leistungsanteil und nicht bereits in Vergütung enthaltenen Auslagen.

Bei Beeinträchtigung vor Abnahme aus Bestellerstoffmangel/Anweisung ohne Unternehmervertretenmüssen ODER Aufhebung§643 ODER qualifizierter Kostenanschlagskündigung§649: Gesamtvergütung×geleisteter Anteil + nicht inbegriffene Auslagen.

wert ist exakter EUR-Teilvergütungs- und Auslagenbetrag. Fehlender gesetzlicher Fall ergibt NICHT_ANWENDBAR/null.

Nicht freie Kündigung§648. Aufhebungs-/Kündigungstatbestände rechtlich vollständig als Eingabe belegen; Wesentlichkeit einer Kostenüberschreitung nicht durch pauschale Prozentzahl ersetzen. Auslagen überschneidungsfrei. Weitergehende Haftung/Anzeigepflichten gesondert.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_645_T0001, BGB_645_T0002, BGB_643_T0001, BGB_643_T0002, BGB_649_T0001

```python
from bgbcalc import werk_teilverguetung_und_auslagen
werk_teilverguetung_und_auslagen(
    gesamtverguetung='1200',
    leistungsanteil_zaehler=1,
    leistungsanteil_nenner=3,
    nicht_inbegriffene_auslagen='50',
    werkbeeintraechtigung_vor_abnahme=False,
    bestellerstoffmangel_oder_anweisung_ursaechlich=False,
    unternehmer_zu_vertretender_umstand=False,
    aufhebung_nach_643=False,
    kuendigung_nach_649=True,
    bewertungsnachweis='Synthetischer gesetzlicher Teilvergütungsfall mit überschneidungsfreien Auslagen.',
)
```
