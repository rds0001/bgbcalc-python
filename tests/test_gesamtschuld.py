import copy
import importlib.util
import json
from pathlib import Path

import pytest
import bgbcalc


FAELLE = json.loads(
    (Path(__file__).parents[1] / "tests/fixtures/referenzfaelle/gesamtschuld.json").read_text()
)


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_gesamtschuld(fall):
    vorher = copy.deepcopy(fall["eingaben"])
    if fall["erwartung"]["status"].startswith("EINGABE_"):
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            getattr(bgbcalc, fall["funktion"])(**fall["eingaben"])
        assert fehler.value.status == fall["erwartung"]["status"]
    else:
        ergebnis = getattr(bgbcalc, fall["funktion"])(**fall["eingaben"])
        assert {k: ergebnis[k] for k in ("wert", "status")} == fall["erwartung"]
        assert ergebnis["eingaben"] == vorher
        assert ergebnis["nutzervorgaben"] == vorher
    assert fall["eingaben"] == vorher


def test_referenzmatrix_gegen_unabhaengiges_orakel():
    pfad = Path(__file__).parents[1] / "tests/helpers/gesamtschuld_orakel.py"
    spez = importlib.util.spec_from_file_location("gesamtschuld_orakel", pfad)
    modul = importlib.util.module_from_spec(spez)
    spez.loader.exec_module(modul)
    assert {f["fall_id"]: f["erwartung"] for f in FAELLE
            if f["fall_id"].startswith("GESAMTSCHULD_ORAKEL_")} == modul.vergleichswerte()
