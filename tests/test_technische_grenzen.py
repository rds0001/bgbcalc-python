"""Technische Belastungsgrenzen: zulässiger Rand und unmittelbare Überschreitung."""

import pytest

import bgbcalc
from bgbcalc.zahlen import _pruefe_bruch


@pytest.mark.parametrize("anzahl", [10000, 10001])
def test_hemmungsintervallgrenze_und_doppelte_tage(anzahl):
    zeitraeume = [
        dict(erster_gehemmter_tag="2026-01-05", letzter_gehemmter_tag="2026-01-05")
        for _ in range(anzahl)
    ]
    if anzahl > 10000:
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            bgbcalc.verjaehrung_gehemmte_kalendertage("2026-01-01", "2026-01-10", zeitraeume, True)
        assert fehler.value.status == "EINGABE_UNGUELTIG"
    else:
        ergebnis = bgbcalc.verjaehrung_gehemmte_kalendertage(
            "2026-01-01", "2026-01-10", zeitraeume, True,
        )
        assert ergebnis["wert"] == dict(
            rechnerischer_letzter_tag="2026-01-11", beruecksichtigte_hemmungstage=1,
        )


@pytest.mark.parametrize("anzahl", [10000, 10001])
def test_stammknotengrenze(anzahl):
    staemme = [{
        "person_id": "Wurzel", "tritt_ein": True,
        "abkoemmlinge": [
            dict(person_id=f"K{i}", tritt_ein=False, abkoemmlinge=[])
            for i in range(anzahl - 1)
        ],
    }]
    if anzahl > 10000:
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            bgbcalc.abkoemmlings_erbquoten(staemme, 1, 1)
        assert fehler.value.status == "EINGABE_UNGUELTIG"
    else:
        ergebnis = bgbcalc.abkoemmlings_erbquoten(staemme, 1, 1)
        assert ergebnis["rechenschritte"][0]["knoten"] == anzahl
        assert ergebnis["wert"]["erbquoten"] == [
            dict(person_id="Wurzel", quote=dict(zaehler="1", nenner="1"))
        ]


@pytest.mark.parametrize("tiefe", [64, 65])
def test_stammtiefengrenze(tiefe):
    staemme = []
    for i in reversed(range(tiefe)):
        staemme = [dict(person_id=f"P{i}", tritt_ein=i == tiefe - 1, abkoemmlinge=staemme)]
    if tiefe > 64:
        with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
            bgbcalc.abkoemmlings_erbquoten(staemme, 1, 1)
        assert fehler.value.status == "EINGABE_UNGUELTIG"
    else:
        ergebnis = bgbcalc.abkoemmlings_erbquoten(staemme, 1, 1)
        assert ergebnis["wert"]["erbteile"][0]["stammpfad"] == [f"P{i}" for i in range(tiefe)]
        assert ergebnis["wert"]["erbquoten"] == [
            dict(person_id="P63", quote=dict(zaehler="1", nenner="1"))
        ]


def test_interner_zahlenvertrag_keine_rohzahl():
    with pytest.raises(bgbcalc.Berechnungsfehler) as fehler:
        _pruefe_bruch(1)
    assert fehler.value.status == "EINGABE_UNGUELTIG"
