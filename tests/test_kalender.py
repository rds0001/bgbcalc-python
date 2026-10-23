"""Vorab festgelegte fachliche Referenzfälle, nicht aus dem Rechenkern erzeugt."""
import json
from pathlib import Path

import pytest

import bgbcalc

WURZEL = Path(__file__).parents[1]
FAELLE = json.loads((WURZEL / "tests/fixtures/referenzfaelle/kalender.json").read_text())


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_referenzfall(fall):
    funktion = getattr(bgbcalc, fall["funktion"])
    erwartet = fall["erwartung"]
    if erwartet["status"] != "BERECHNET":
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            funktion(**fall["eingaben"])
        assert fehler.value.status == erwartet["status"]
    else:
        ergebnis = funktion(**fall["eingaben"])
        assert ergebnis["status"] == erwartet["status"]
        assert ergebnis["wert"] == erwartet["wert"]
        assert ergebnis["eingaben"] == fall["eingaben"]
        assert ergebnis["regel_id"].startswith("BGB_")
        assert ergebnis["rechenschritte"]


@pytest.mark.parametrize("anzahl", [True, 1.0, float("nan"), "1", [], 3652060])
def test_keine_stille_typumwandlung(anzahl):
    with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
        bgbcalc.fristende("2026-01-01", anzahl, "tage", "ereignis")
    assert fehler.value.status == "EINGABE_UNGUELTIG"
