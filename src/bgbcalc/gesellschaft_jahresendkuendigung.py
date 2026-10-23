from .kalender import _ergebnis, _frist, _auswahl, _text

def gesellschaft_jahresendkuendigung(kuendigungszugang_am=None, kuendigungsfall=None, einordnungsnachweis=None):
    """Dreimonats-Ereignisfrist berechnen und ersten danach liegenden Kalenderjahresablauf bestimmen."""
    _auswahl(kuendigungsfall,'kuendigungsfall',('mitgliedschaft_725','privatglaeubiger_726'));_text(einordnungsnachweis,'einordnungsnachweis')
    m=_frist(kuendigungszugang_am,3,'monate','ereignis');e=m.replace(month=12,day=31)
    wert=dict(dreimonatsfristende=m.isoformat(),beendigungsgrundtermin=e.isoformat())
    eingaben = dict(kuendigungszugang_am=kuendigungszugang_am, kuendigungsfall=kuendigungsfall, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten','BGB_GESELLSCHAFT_JAHRESENDKUENDIGUNG',eingaben,[dict(operation='Dreimonats-Ereignisfrist berechnen und ersten danach liegenden Kalenderjahresablauf bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['725I/726: drei Kalendermonate ab wirksamem Zugang nach187I/188; erster Kalenderjahresablauf, der nicht vor diesem Mindestfristende liegt. Keine90Tage-Pauschale.725Gesellschaftsvertrags-/Zweckabweichungen, wichtiger Grund und Unzeit separat;726wirksame Anteilspfändung, Titel und erfolgloseVollstreckung im Sechsmonatsrückblick rechtlich und zeitlich vorqualifizieren. Tatsächlicher Kündigungszugang ist Eingabe, keine automatische Vorverlegung oder193-Verschiebung. Ergebnis ausschließlich gesetzlicher ordentlicher Beendigungsgrundtermin.']
    return ergebnis

