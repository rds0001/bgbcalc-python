from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .betraege import _geld, _wahrheitswert
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung

def geldschulden_nach_bestimmung_oder_rang_tilgen(zahlung=None, schulden=None, bestimmte_schuld_id=None, einordnungsnachweis=None):
    """Eindeutige Tilgungsbestimmung ausführen oder gesetzliche Fälligkeits-/Sicherheits-/Lästigkeits-/Altersgruppen proportional bedienen."""
    rest=_geld(zahlung);_text(einordnungsnachweis,'einordnungsnachweis');_vorhanden(schulden,'schulden')
    if not isinstance(schulden,list) or not 1<=len(schulden)<=1000: _fehler('schulden','Liste1..1000 erforderlich.')
    namen=[];forderungen=[];raenge=[]
    for p in schulden:
        if not isinstance(p,dict) or set(p)!={'schuld_id','offener_betrag','faellig','sicherheitsrang','laestigkeitsrang','altersrang'}: _fehler('schulden','Genau Kennung, offener Betrag, Fälligkeit und drei Rangfelder erforderlich.')
        name=_text(p['schuld_id'],'schuld_id');betrag=_geld(p['offener_betrag']);_wahrheitswert(p['faellig'],'faellig')
        if name in namen: _fehler('schuld_id','Doppelte Kennung unzulässig.')
        if betrag<=0: _fehler('offener_betrag','Positiver offener Betrag erforderlich.')
        rang=(0 if p['faellig'] else 1,)+tuple(_ganzzahl(p[k],k,1,9007199254740991) for k in ('sicherheitsrang','laestigkeitsrang','altersrang'))
        namen.append(name);forderungen.append(betrag);raenge.append(rang)
    if bestimmte_schuld_id is not None:
        _text(bestimmte_schuld_id,'bestimmte_schuld_id')
        if bestimmte_schuld_id not in namen: _fehler('bestimmte_schuld_id','Bestimmte Schuld muss in der Liste stehen.')
        gruppen=[[namen.index(bestimmte_schuld_id)]]
    else: gruppen=[[i for i,r in enumerate(raenge) if r==rang] for rang in sorted(set(raenge))]
    zugeteilt=[_geld('0') for _ in namen]
    for gruppe in gruppen:
        betraege=[forderungen[i] for i in gruppe]
        teile,rest=_begrenzte_quotenverteilung(rest,betraege,betraege)
        for j,i in enumerate(gruppe): zugeteilt[i]=teile[j]
    wert=dict(zuordnungen=[dict(schuld_id=name,tilgungsbetrag=_bruchteile(zugeteilt[i]),restschuld=_bruchteile(forderungen[i]-zugeteilt[i])) for i,name in enumerate(namen)],nicht_zugeordnet=_bruchteile(rest))
    eingaben = dict(zahlung=zahlung, schulden=schulden, bestimmte_schuld_id=bestimmte_schuld_id, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GELDSCHULDEN_NACH_BESTIMMUNG_ODER_RANG_TILGEN',eingaben,[dict(operation='Eindeutige Tilgungsbestimmung ausführen oder gesetzliche Fälligkeits-/Sicherheits-/Lästigkeits-/Altersgruppen proportional bedienen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§366I/II: bei qualifizierter eindeutiger Tilgungsbestimmung nur bestimmte Schuld bedienen; Überschuss bleibt unzugeordnet, keine erfundene weitere Schuldnerbestimmung. Ohne Bestimmung fällige vor nicht fälligen Schulden, dann geringere Sicherheit, größere Lästigkeit, höheres Alter; bei vollständigem Gleichrang verhältnismäßig nach offenen Beträgen. Nicht fällige Forderungen müssen vorzeitig erfüllbar sein. Qualifizierte Rangwerte sind keine automatisch bewertete Sicherheit/Lästigkeit. Mehrfachbestimmungen, Gläubiger-/Parteivereinbarungen und Spezialregeln gesondert. Innerhalb jeder Schuld Kosten/Zinsen/Hauptforderung367 separat; keine automatische Erstattung des unzugeordneten Betrags.']
    return ergebnis

