import copy
import json
from pathlib import Path

import pytest
import bgbcalc


FAELLE = json.loads(
    (Path(__file__).parents[1] / "tests/fixtures/referenzfaelle/arbeitnehmerzahl.json").read_text()
)


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_arbeitnehmerzahl(fall):
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


def test_personenlimit_10000_und_10001():
    person = dict(wochenstunden="20", teilzeitbeschaeftigt=True,
                  zur_berufsbildung_beschaeftigt=False)
    ergebnis = bgbcalc.arbeitnehmerzahl_kuendigungsfrist([person] * 10000, "Synthetischer Grenzbestand")
    assert ergebnis["wert"]["gewichtete_arbeitnehmerzahl"] == {"zaehler": "5000", "nenner": "1"}
    assert len(ergebnis["wert"]["personengewichte"]) == 10000
    with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
        bgbcalc.arbeitnehmerzahl_kuendigungsfrist([person] * 10001, "Synthetischer Grenzbestand")
    assert fehler.value.status == "EINGABE_UNGUELTIG"
