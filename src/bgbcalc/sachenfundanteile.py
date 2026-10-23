"""Gesetzliche Eigentumsanteile bei vereinigten Bienenschwärmen und Schatzfund."""
from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _ganzzahl, _text, _vorhanden
from .zahlen import GRENZE, _bruch
from .zinsen import _bruchteile


def _fundanteile_ergebnis(wert, kennung, eingaben, operation, hinweis):
    ergebnis = _ergebnis(wert, "eigentumsquoten", kennung, eingaben,
        [dict(operation=operation)], eingaben.copy())
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = ["Gesetzlicher Eigentumstatbestand und beteiligte Personen rechtlich bestimmt; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = [hinweis]
    return ergebnis


def bienenschwarm_eigentumsquoten(
    eigentuemer_schwaerme=None, ausgezogene_schwaerme_vereinigt=None,
    gesamtschwarm_eingefangen=None, einzug_in_fremde_besetzte_wohnung=None, einordnungsnachweis=None,
):
    """§963: Quoten nach Anzahl eigentumserhaltend verfolgter Schwärme, nicht Bienenzahl oder Wert."""
    _vorhanden(eigentuemer_schwaerme, "eigentuemer_schwaerme")
    if not isinstance(eigentuemer_schwaerme, list) or not 2 <= len(eigentuemer_schwaerme) <= 1000:
        _fehler("eigentuemer_schwaerme", "Liste mit 2 bis 1000 unterschiedlichen berechtigten Eigentümern erforderlich.")
    namen, zahlen = [], []
    summe = 0
    for eintrag in eigentuemer_schwaerme:
        if not isinstance(eintrag, dict) or set(eintrag) != {"eigentuemer_id", "verfolgte_schwaerme"}:
            _fehler("eigentuemer_schwaerme", "Genau eigentuemer_id und verfolgte_schwaerme erforderlich.")
        name = _text(eintrag["eigentuemer_id"], "eigentuemer_id")
        if name in namen:
            _fehler("eigentuemer_id", "Eigentümer nicht doppelt aufführen; Schwärme je Eigentümer zusammenfassen.")
        anzahl = _ganzzahl(eintrag["verfolgte_schwaerme"], "verfolgte_schwaerme", 1, GRENZE)
        summe = _ganzzahl(summe + anzahl, "gesamtzahl_schwaerme", 1, GRENZE)
        namen.append(name)
        zahlen.append(anzahl)
    eingaben = dict(eigentuemer_schwaerme=eigentuemer_schwaerme,
        ausgezogene_schwaerme_vereinigt=ausgezogene_schwaerme_vereinigt,
        gesamtschwarm_eingefangen=gesamtschwarm_eingefangen,
        einzug_in_fremde_besetzte_wohnung=einzug_in_fremde_besetzte_wohnung,
        einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[1:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    gilt = ausgezogene_schwaerme_vereinigt and gesamtschwarm_eingefangen and not einzug_in_fremde_besetzte_wohnung
    wert = [dict(eigentuemer_id=name, eigentumsquote=_bruchteile(_bruch(anzahl, summe)))
        for name, anzahl in zip(namen, zahlen)] if gilt else None
    return _fundanteile_ergebnis(wert, "BGB_BIENENSCHWARM_EIGENTUMSQUOTEN", eingaben,
        "Verfolgte Schwärme je berechtigtem Eigentümer durch Gesamtzahl der verfolgten Schwärme teilen",
        "Nur vereinigte ausgezogene Schwärme mehrerer berechtigter Eigentümer und eingefangener Gesamtschwarm. Eigentumserhaltende Verfolgung§961 vorab prüfen; aufgegebene oder nicht unverzüglich verfolgte Schwärme nicht als weiterhin berechtigte Beiträge zählen. Fall§964 in fremder besetzter Bienenwohnung ist anderes Erwerbsmodell. Keine Gewichtung nach Bienenzahl, Gewicht, Geldwert oder Arbeitsaufwand. Einzelberechtigter, vorbestehendes Miteigentum eines Schwarms und andere Sonderlagen außerhalb dieses Mehrpersonenmodells.")


def schatzfund_eigentumsquoten(
    entdecker_id=None, eigentuemer_verbergende_sache_id=None, qualifizierter_schatz=None,
    entdeckt_und_infolge_entdeckung_besitzgenommen=None, abweichendes_landesrecht=None, einordnungsnachweis=None,
):
    """§984: je eine Hälfte für Entdecker und Eigentümer der verbergenden Sache im BGB-Fall."""
    entdecker = _text(entdecker_id, "entdecker_id")
    eigentuemer = _text(eigentuemer_verbergende_sache_id, "eigentuemer_verbergende_sache_id")
    eingaben = dict(entdecker_id=entdecker_id, eigentuemer_verbergende_sache_id=eigentuemer_verbergende_sache_id,
        qualifizierter_schatz=qualifizierter_schatz,
        entdeckt_und_infolge_entdeckung_besitzgenommen=entdeckt_und_infolge_entdeckung_besitzgenommen,
        abweichendes_landesrecht=abweichendes_landesrecht, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    gilt = qualifizierter_schatz and entdeckt_und_infolge_entdeckung_besitzgenommen and not abweichendes_landesrecht
    wert = None
    if gilt:
        if entdecker == eigentuemer:
            wert = [dict(eigentuemer_id=entdecker, eigentumsquote=_bruchteile(_bruch(1)))]
        else:
            wert = [dict(eigentuemer_id=name, eigentumsquote=_bruchteile(_bruch(1, 2)))
                for name in (entdecker, eigentuemer)]
    return _fundanteile_ergebnis(wert, "BGB_SCHATZFUND_EIGENTUMSQUOTEN", eingaben,
        "Im einschlägigen BGB-Schatzfundfall je Hälfte an Entdecker und Eigentümer der verbergenden Sache; bei Personenidentität vereinigen",
        "Nur ein rechtlich bestimmter Entdecker und ein Alleineigentümer der verbergenden Sache. Mehrere Entdecker/Miteigentümer oder besondere Zuordnungsfragen gesondert. Schatz muss so lange verborgen sein, dass Eigentümer nicht mehr ermittelbar; bloß unbekannter Eigentümer eines gewöhnlichen Funds genügt nicht. Landesrechtliche Schatzregale und sonstige abweichende Erwerbsregeln vorab prüfen; keine automatische Rechtsrecherche oder pauschale Aussage zu archäologischen Funden. Eigentumsquote ist kein Finderlohn und kein automatischer Zahlungsanspruch.")
