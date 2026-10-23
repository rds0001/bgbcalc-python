<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## testament_erbquoten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `erbeinsetzungen`: Unbenannte Liste mit1..1000 eindeutigen Erben, je Objekt genau erbe_id (nichtleere Zeichenfolge) und bestimmter_erbteil (positive exakte Dezimalzeichenfolge/Bruchobjekt höchstens1 oder NULL). NULL bezeichnet fehlende Quotenbestimmung im Testament, nicht unbekannte Tatsachen. Einzelner Erbe mit NULL außerhalb des Modells. Keine gemeinschaftlichen Gruppen§2093 in dieser flachen Liste.
- `alleinige_erben_gewollt`: Wahrheitswert des rechtlich ermittelten Willens, dass die eingesetzten Erben alleinige Erben sein sollen. Bei Unterbelegung ausschließlich bestimmter Quoten proportional erhöhen statt gesetzlichen Rest belassen. Keine automatische Auslegung aus Bezeichnung als Erbe.
- `auslegungsregeln_anwendbar`: Wahrheitswert: wirksame Erbeinsetzungen nach rechtlicher Auslegung, auf welche die gesetzlichen Rechenregeln§§2088–2092 anwendbar sind. Abweichenden Willen, Sonderauslegung§§2066–2069, Vermächtnisse, Wegfall/Ersatz und gemeinschaftliche Erbteile vorab abgrenzen. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung von Erbenstellung, Quotenbestimmung, Alleinerbenwillen und Anwendbarkeit der Auslegungsregeln; keine erfundene Bewertung des Testaments.

Nur bestimmte Quoten: bei Überbelegung oder Alleinerbenwillen mit Unterbelegung auf1 normieren, sonst gesetzlichen Rest ausweisen. Nicht bestimmte Quoten: freien Rest gleich teilen; bei bereits erschöpfter Masse jedem unbestimmten Erben Gewicht des kleinsten bestimmten Anteils geben und alle Gewichte zusammen normieren.

wert enthält erbquoten als Liste in Eingabereihenfolge mit erbe_id/erbquote und rest_gesetzliche_erbfolge; alle Quoten als exakte dimensionslose Brüche. Summe inklusive Rest1. Außerhalb Anwendungsbereich NICHT_ANWENDBAR/null.

Keine automatische Testamentsauslegung, Gruppenauflösung§2093 oder Anwachsung§2094. Sonderauslegung§§2066–2069 und abweichender Wille vorab prüfen. Gesetzlichen Rest nicht automatisch verteilen.

1..1000 eindeutige Erben, positive bestimmte Einzelquoten höchstens1 oder NULL für nicht bestimmte Quote. Alle exakten Ganzzahl-Zwischenwerte höchstens2^53-1.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_2088_T0001, BGB_2088_T0002, BGB_2089_T0001, BGB_2090_T0001, BGB_2091_T0001, BGB_2092_T0001, BGB_2092_T0002

```python
from bgbcalc import testament_erbquoten
testament_erbquoten(
    erbeinsetzungen=[{'erbe_id': '0', 'bestimmter_erbteil': {'zaehler': '1', 'nenner': '4'}}],
    alleinige_erben_gewollt=False,
    auslegungsregeln_anwendbar=True,
    einordnungsnachweis='Synthetisch qualifizierte Erbeinsetzungen ohne abweichende Auslegung oder gemeinschaftliche Erbteile.',
)
```
