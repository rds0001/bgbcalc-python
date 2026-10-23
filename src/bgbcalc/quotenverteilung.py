"""Interne proportionale Betragsverteilung mit qualifizierten Obergrenzen."""
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _subtrahieren

def _begrenzte_quotenverteilung(fehl, quoten, grenzen):
    """Bereits validierte exakte Werte; Nullgewichte erhalten keine Zuweisung."""
    zugeordnet=[_bruch(0) for _ in quoten]; aktiv=[i for i,q in enumerate(quoten) if q>0]; rest=fehl
    while rest>0 and aktiv:
        anteilssumme=_bruch(0)
        for i in aktiv: anteilssumme=_addieren(anteilssumme,quoten[i])
        vorschlag={i:_multiplizieren(rest,_dividieren(quoten[i],anteilssumme)) for i in aktiv}
        begrenzt=[i for i in aktiv if grenzen[i]<vorschlag[i]]
        if not begrenzt:
            for i in aktiv:zugeordnet[i]=vorschlag[i]
            rest=_bruch(0)
        else:
            for i in begrenzt:zugeordnet[i]=grenzen[i];rest=_subtrahieren(rest,grenzen[i])
            aktiv=[i for i in aktiv if i not in begrenzt]
    return zugeordnet, rest
