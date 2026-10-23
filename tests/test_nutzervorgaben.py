"""Bewertete Nutzereingaben dürfen in der Herkunftsspur nicht verloren gehen."""
import bgbcalc


def test_bewertete_vergleichswerte_bleiben_als_nutzervorgaben_sichtbar():
    ergebnis = bgbcalc.minderung_betrag(
        "800", "1000", "750", "800", "kauf", "vertragsschluss",
        1, 1, "Synthetische Bewertung zum Vertragsschluss", True, True, False,
    )
    assert ergebnis["nutzervorgaben"]["mangelfreier_wert"] == "1000"
    assert ergebnis["nutzervorgaben"]["wirklicher_wert"] == "750"
    assert ergebnis["nutzervorgaben"]["minderungsrecht"] is True
    assert ergebnis["wert"]["minderungsbetrag"] == {"zaehler": "200", "nenner": "1"}


def test_optionale_nicht_gelieferte_bewertung_bleibt_null():
    ergebnis = bgbcalc.gesetzliche_zinsen(
        "1000", 1, 1, "Ein belegter Jahresanteil", False, None,
    )
    assert "abweichender_zinssatz_prozent" in ergebnis["nutzervorgaben"]
    assert ergebnis["nutzervorgaben"]["abweichender_zinssatz_prozent"] is None
    assert ergebnis["wert"] == {"zaehler": "40", "nenner": "1"}


def test_nichtanwendbarkeit_bewahrt_die_entgegenstehende_tatsache():
    ergebnis = bgbcalc.bau_sicherungsbetrag(
        "10000", "0", False, False, "oeffentlich_insolvenzunfaehig", True,
    )
    assert ergebnis["status"] == "NICHT_ANWENDBAR"
    assert ergebnis["nutzervorgaben"]["bestellerart"] == "oeffentlich_insolvenzunfaehig"
    assert ergebnis["nutzervorgaben"]["baubetreuer_bevollmaechtigt"] is True
