from .kalender import _datum, _ergebnis, _fehler, _frist, _text

def miete_formmangel_beendigungsgrenze(ueberlassung_am=None, ordentlicher_beendigungstag=None, einordnungsnachweis=None):
    """Jahresmindestbindung550mit regulaerem Monatsendtermin verbinden und erforderlichenfalls bis zum naechsten zulaessigen Monatsende verschieben."""
    u=_datum(ueberlassung_am,'ueberlassung_am');o=_datum(ordentlicher_beendigungstag,'ordentlicher_beendigungstag');_text(einordnungsnachweis,'einordnungsnachweis')
    if o!=_frist(o.replace(day=1).isoformat(),1,'monate','tagesbeginn'): _fehler('ordentlicher_beendigungstag','Regulaerer Monatsendtermin erforderlich.')
    j=_frist(u.isoformat(),1,'jahre','ereignis');basis=max(j,o);ende=_frist(basis.replace(day=1).isoformat(),1,'monate','tagesbeginn')
    wert=dict(jahresmindestgrenze=j.isoformat(),fruehester_monatsendtermin=ende.isoformat())
    eingaben = dict(ueberlassung_am=ueberlassung_am, ordentlicher_beendigungstag=ordentlicher_beendigungstag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_MIETE_FORMMANGEL_BEENDIGUNGSGRENZE',eingaben,[dict(operation='Jahresmindestbindung550mit regulaerem Monatsendtermin verbinden und erforderlichenfalls bis zum naechsten zulaessigen Monatsende verschieben.')],eingaben.copy())
    ergebnis["hinweise"] = ['§550Satz2: regulaeren ordentlichen Monatsendtermin mit dem Ablauf eines Jahres nach tatsaechlicher Ueberlassung vergleichen. Liegt der regulaere Termin davor, ersten Monatsendtermin bestimmen, der die Jahresgrenze erreicht. Nicht bloss das Maximum mit einem mitten im Monat liegenden Jahrestag als angeblich zulaessigen Kuendigungstermin ausgeben. Ueberlassungsereignis nach187I, keine pauschale365Tage-Dauer. Die ordentliche Frist wird vom bestehenden Wohnraummietkern berechnet; diese Funktion fuegt nur550-Mindestbindung hinzu. Kein automatischer Formmangelentscheid, keine Kuendigungssperre fuer ausserordentliche wichtige Gruende und keine Behandlung abweichender wirksamer Terminvereinbarungen. Bei rechtlich anderem Beginn187II gesondert qualifizieren.']
    return ergebnis

