"""Direkte Vergleichsrechnung für kleine gleiche Gesamtschuldnergruppen."""

from fractions import Fraction


def bruch(wert):
    return {"zaehler": str(wert.numerator), "nenner": str(wert.denominator)}


def vergleichswerte():
    ergebnisse = {}
    for anzahl in range(2, 10):
        for ausfaelle in range(anzahl):
            betrag = Fraction(anzahl * ausfaelle + 1, 10)
            grund = betrag / anzahl
            uebrige = anzahl - ausfaelle
            # Direkte Gesamtlast statt stufenweiser Addition des Ausfalls.
            gesamtlast = betrag / uebrige
            ergebnisse[f"GESAMTSCHULD_ORAKEL_{anzahl}_{ausfaelle}"] = {
                "status": "BERECHNET",
                "wert": {
                    "urspruenglicher_innenanteil": bruch(Fraction(1, anzahl)),
                    "urspruenglicher_beitrag": bruch(grund),
                    "gesamter_ausfallbetrag": bruch(betrag - grund * uebrige),
                    "zusaetzlicher_beitrag_je_uebrigem": bruch(gesamtlast - grund),
                    "gesamtbelastung_je_uebrigem": bruch(gesamtlast),
                    "anzahl_uebrige": uebrige,
                },
            }
    return ergebnisse
