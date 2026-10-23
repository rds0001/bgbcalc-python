import json
from pathlib import Path

import pytest
import bgbcalc

FAELLE = json.loads(
    (Path(__file__).parents[1] / "tests/fixtures/referenzfaelle/bausicherheit.json").read_text()
)


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_bausicherheit_regel(fall):
    if fall["erwartung"]["status"].startswith("EINGABE_"):
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            getattr(bgbcalc, fall["funktion"])(**fall["eingaben"])
        assert fehler.value.status == fall["erwartung"]["status"]
    else:
        ergebnis = getattr(bgbcalc, fall["funktion"])(**fall["eingaben"])
        assert {k: ergebnis[k] for k in ("wert", "status")} == fall["erwartung"]
        assert ergebnis["eingaben"] == fall["eingaben"]
        assert ergebnis["einheit"] == "EUR"
