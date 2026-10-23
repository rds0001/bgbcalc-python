import json
from pathlib import Path

import pytest
import bgbcalc

FAELLE = json.loads(
    (Path(__file__).parents[1] / "tests/fixtures/referenzfaelle/abzinsung.json").read_text()
)


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_abzinsung(fall):
    if fall["erwartung"]["status"].startswith("EINGABE_"):
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            bgbcalc.vorzeitiger_befriedigungsbetrag(**fall["eingaben"])
        assert fehler.value.status == fall["erwartung"]["status"]
    else:
        ergebnis = bgbcalc.vorzeitiger_befriedigungsbetrag(**fall["eingaben"])
        assert {k: ergebnis[k] for k in ("wert", "status")} == fall["erwartung"]
        assert ergebnis["eingaben"] == fall["eingaben"]
