<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_eigenpflichtteilsschutz

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `verfuegbarer_nachlassanteil`: Nichtnegativer rechtlich bestimmter EUR-Wert des verfügbaren Nachlassanteils des Erben vor der betrachteten fremden Ergänzungsforderung, nach sonstigen relevanten Belastungen. Einheitliche Bewertungsbasis; nicht pauschal Gesamtnachlass bei mehreren Erben.
- `eigener_pflichtteil`: Nichtnegativer rechtlich berechneter eigener Pflichtteil in EUR einschließlich zutreffender Anrechnungen; nicht Erbquote oder gesamter Erbteil.
- `eigene_pflichtteilsergaenzung`: Nichtnegative rechtlich berechnete dem Erben selbst gebührende Pflichtteilsergänzung in EUR, anrechnungsbereinigt. Nicht gesamter Wert früherer Schenkungen und nicht bereits im eigenen Pflichtteil enthaltener Betrag.
- `fremde_ergaenzungsforderung`: Nichtnegative fremde Pflichtteilsergänzungsforderung in EUR vor Prüfung§2328. Bei mehreren Berechtigten konsistent aggregieren; keine wiederholte Nutzung desselben Deckungsbetrags und keine automatische Verteilung der verbleibenden Haftung.
- `erbe_selbst_pflichtteilsberechtigt`: Wahrheitswert des rechtlich geprüften Tatbestands§2328: in Anspruch genommener Erbe ist selbst pflichtteilsberechtigt. FALSE ergibt NICHT_ANWENDBAR für dieses Schutzmodell.
- `bewertungsnachweis`: Nichtleere Begründung eigener Pflichtteilsberechtigung, eigener Ansprüche, verfügbarem Nachlassanteil und betrachteter fremder Ergänzung; Bewertungen und Anrechnungen belegen.

Eigenen Schutzbetrag aus Pflichtteil plus eigener Ergänzung bilden. Deckung=max(0,verfügbarer Nachlassanteil minus Schutzbetrag). Nicht nach§2328 verweigerbarer Betrag=min(fremde Forderung,Deckung), Verweigerungsbetrag als verbleibende Differenz.

wert enthält eigener_schutzbetrag, nicht_nach_2328_verweigerbarer_betrag und verweigerungsbetrag als exakte EUR-Brüche. Ohne eigenen Pflichtteilsstatus NICHT_ANWENDBAR/null.

Nur Umfang des gesetzlichen Verweigerungsrechts, keine automatische Ausübung. Vorberechnung eigener Ansprüche, Nachlassbelastungen, Verteilung unter mehreren Gläubigern und Rückgriff§2329 separat. Nicht verweigerbar bedeutet nicht automatisch geschuldet.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2328_T0001

```python
from bgbcalc import pflichtteilsergaenzung_eigenpflichtteilsschutz
pflichtteilsergaenzung_eigenpflichtteilsschutz(
    verfuegbarer_nachlassanteil='100',
    eigener_pflichtteil='50',
    eigene_pflichtteilsergaenzung='20',
    fremde_ergaenzungsforderung='40',
    erbe_selbst_pflichtteilsberechtigt=True,
    bewertungsnachweis='Synthetisch einheitlich und anrechnungsbereinigt bestimmter eigener Schutzbetrag und verfügbarer Nachlassanteil.',
)
```
