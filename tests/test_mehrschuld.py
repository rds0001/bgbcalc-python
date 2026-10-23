import copy
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path

import pytest
import bgbcalc


FAELLE = json.loads(
    (Path(__file__).parents[1] / "tests/fixtures/referenzfaelle/mehrschuld.json").read_text()
)


@pytest.mark.parametrize("fall", FAELLE, ids=lambda f: f["fall_id"])
def test_mehrschuld(fall):
    vorher = copy.deepcopy(fall["eingaben"])
    if fall["erwartung"]["status"].startswith("EINGABE_"):
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            bgbcalc.faellige_geldschulden_gesetzlich_tilgen(**fall["eingaben"])
        assert fehler.value.status == fall["erwartung"]["status"]
    else:
        ergebnis = bgbcalc.faellige_geldschulden_gesetzlich_tilgen(**fall["eingaben"])
        assert {k: ergebnis[k] for k in ("wert", "status")} == fall["erwartung"]
        assert ergebnis["eingaben"] == vorher
        assert ergebnis["nutzervorgaben"] == vorher
    assert fall["eingaben"] == vorher


def test_reihenfolge_unabhaengig_und_betraege_erhalten():
    # Die Eingabeliste darf niemals als weiteres gesetzliches Rangmerkmal wirken.
    fall = next(f for f in FAELLE if f["fall_id"] == "MEHRSCHULD_FOLGEGRUPPE")

    def bruch(wert):
        return Fraction(int(wert["zaehler"]), int(wert["nenner"]))

    for schulden in permutations(fall["eingaben"]["schulden"]):
        ergebnis = bgbcalc.faellige_geldschulden_gesetzlich_tilgen(
            "50", list(schulden), False, True
        )["wert"]
        erwartet = {x["schuld_id"]: x for x in fall["erwartung"]["wert"]["zuordnungen"]}
        assert {x["schuld_id"]: x for x in ergebnis["zuordnungen"]} == erwartet
        assert sum(bruch(x["tilgungsbetrag"]) for x in ergebnis["zuordnungen"]) == 50
        for schuld, zuordnung in zip(schulden, ergebnis["zuordnungen"]):
            assert bruch(zuordnung["tilgungsbetrag"]) + bruch(zuordnung["restschuld"]) == Fraction(schuld["offener_betrag"])
