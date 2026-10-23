<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pflichtteilsergaenzung_grundbetrag

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `pflichtteilsnachlass`: Rechtlich bestimmter tatsächlicher Pflichtteilsnachlass in EUR, auch negativ, vor Hinzurechnung der hier genannten Drittschenkungen. Qualifizierte Nachlassverbindlichkeiten bereits berücksichtigen, keine Schenkungen doppelt hinzufügen.
- `hinzuzurechnende_schenkungen`: Nichtnegative Summe rechtlich relevanter Drittschenkungen in EUR, nach Bewertung§2325 Absatz2 und zeitlicher AbschmelzungAbsatz3. Ausnahmen§2330 zuvor ausscheiden. Keine eigenen Geschenke des Berechtigten im Grundmodell ohne§2327.
- `gesetzliche_erbquote_zaehler`: Nichtnegative ganze Zahl höchstens Nenner und2^53-1 der zuvor rechtlich bestimmten gesetzlichen Erbquote. Die Funktion halbiert diese Quote selbst zum Pflichtteil.
- `gesetzliche_erbquote_nenner`: Positive ganze Zahl höchstens2^53-1 der gesetzlichen Erbquote. Nicht schon die halbierte Pflichtteilsquote eingeben.
- `pflichtteilsberechtigt`: Wahrheitswert der Pflichtteilsberechtigung im konkreten Fall. FALSE ergibt NICHT_ANWENDBAR. Erbrechtliche Stellung und besondere Ausschlüsse zuvor prüfen.
- `bewertungsnachweis`: Nichtleere Beschreibung der konsistenten Nachlassbewertung, relevanten Drittschenkungen, gesetzlichen Erbquote und Berechtigung. Grundmodell ohne eigene Geschenke oder Ausgleichung; deren Wechselwirkungen separat.

Ordentlicher Pflichtteil=max(Nachlass,0)×gesetzliche Erbquote/2. Erhöhter Pflichtteil=max(Nachlass+qualifizierte Drittschenkungen,0)×gesetzliche Erbquote/2. Ergänzungsgrundbetrag ist Differenz beider Werte.

wert enthält ordentlicher_pflichtteilswert, erhoehter_pflichtteilswert und ergaenzungsgrundbetrag als exakte EUR-Brüche. Bei fehlender Berechtigung null und NICHT_ANWENDBAR.

Keine pauschale Quote×Schenkung bei negativem Nachlass. Grundmodell ohne eigene Geschenke§§2315/2327 oder Ausgleichung§2316. Mehrhinterlassung§2326, Schutz des Erben§2328, Beschenktenhaftung§2329 und weitere Anspruchsfragen gesondert.

Pflichtteilsnachlass als vorzeichenbehaftete Dezimalzeichenfolge/Bruchobjekt; Schenkungssumme nichtnegativ. Gesetzliche Quote0..1 mit ganzzahligem Zähler und positivem Nenner. Exakte Zwischenwerte höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2325_T0001, BGB_2303_T0002

```python
from bgbcalc import pflichtteilsergaenzung_grundbetrag
pflichtteilsergaenzung_grundbetrag(
    pflichtteilsnachlass='-800',
    hinzuzurechnende_schenkungen='0',
    gesetzliche_erbquote_zaehler=0,
    gesetzliche_erbquote_nenner=2,
    pflichtteilsberechtigt=True,
    bewertungsnachweis='Synthetisch vollständig bestimmte Drittschenkung ohne Eigengeschenke/Ausgleichung.',
)
```
