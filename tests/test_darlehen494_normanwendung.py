import json
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
from bgbcalc import verbraucherdarlehen_sollzinskorrektur, verbraucherdarlehen_centannuitaet_neuberechnen

def test_darlehen494_langzeitplan():
    f=json.loads((Path(__file__).resolve().parents[1]/"tests/fixtures/kompositionsfaelle/darlehen494_normanwendung.json").read_text())
    def q(x):return Fraction(int(x["zaehler"]),int(x["nenner"]))
    korr=verbraucherdarlehen_sollzinskorrektur(f["vertraglicher_sollzinssatz"],f["angegebener_effektiver_jahreszins"],f["tatsaechlicher_effektiver_jahreszins"],"Qualifizierte Unterangabe494III.")
    assert korr["status"]=="BERECHNET"
    monat=q(korr["wert"]["rechnerisch_verminderter_sollzinssatz"])/12
    erg=verbraucherdarlehen_centannuitaet_neuberechnen(f["anfangskapital"],dict(zaehler=str(monat.numerator),nenner=str(monat.denominator)),f["laufzeit_monate"],"0","kaufmaennisch","Vertraglich konstante nachschüssige Monatsrate, Zinsen aufCent, letzte Rate angepasst.")
    assert erg["status"]=="BERECHNET"
    e=erg["wert"]
    assert q(e["regelmaessiger_kapitaldienst"])==Fraction(f["erwartete_rate"])
    assert q(e["teilzahlungen"][-1]["kapitaldienst"])==Fraction(f["erwartete_schlussrate"])
    assert q(e["zinsgesamtbetrag"])==Fraction(f["erwartete_zinssumme"])
    assert q(e["neuer_gesamtbetrag"])==Fraction(f["erwartete_zahlungssumme"])
    assert q(e["restkapital"])==0
    # Unabhängiges Dezimalorakel beweist Minimalität der Centrate.
    rest=Decimal(f["anfangskapital"]);rate=Decimal(f["erwartete_rate"])-Decimal("0.01")
    for _ in range(f["laufzeit_monate"]):
        rest=max(rest+(rest*Decimal("0.0025")).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)-rate,Decimal(0))
    assert rest==Decimal(f["rest_bei_rate_einen_cent_kleiner"])
