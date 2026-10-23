# Exakte Zahleneingaben

Als Dezimaltexte beschriebene Beträge, Zinssätze und Messwerte akzeptieren
alternativ ein Objekt mit genau `zaehler` und `nenner`. Beide Felder sind
kanonische Ganzzahlzeichenfolgen, beispielsweise
`{"zaehler": "1", "nenner": "3"}`. Der Nenner ist positiv. Die vollständigen
Format- und Bereichsregeln stehen im [Zahlenvertrag](../../fachkonzept/NUMERIK.md).
Fachliche Grenzen bleiben unverändert.

Ein geeignetes Betragsfeld eines Ergebnisses lässt sich direkt weiterverwenden:

```python
import bgbcalc

pflichtteil = bgbcalc.pflichtteil_betrag(
    "1", 1, 3, "0", False, True, "Synthetischer bewerteter Nachlass"
)
zusatz = bgbcalc.zusatzpflichtteil_betrag(
    pflichtteil["wert"], {"zaehler": "1", "nenner": "12"}, True
)
assert zusatz["wert"] == {"zaehler": "1", "nenner": "12"}
```

Dabei werden `1/6` und `1/12` nicht auf Dezimalstellen gerundet. Einheiten,
Bezugszeiträume und rechtliche Voraussetzungen müssen fachlich zusammenpassen.
Bei strukturierten Ergebnissen das passende Betragsfeld auswählen.
Getrennte ganzzahlige Quotenzähler und Quotennenner, Anzahlen, Altersstufen,
Datumsangaben und Nachweistexte behalten ihre bisherigen Eingabetypen.
