from .kalender import _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text

def mieterhoehung_sonderkuendigungsfenster(zugang_erhoehungsmitteilung_am=None, verlangter_erhoehungsbeginn_am=None, kuendigungseingang_am=None, einordnungsnachweis=None):
    """Ausübungsgrundfrist und bei später verlangter Erhöhung verlängertes Erklärungsfenster sowie Mietende bei voller Fristausnutzung berechnen."""
    zugang=_datum(zugang_erhoehungsmitteilung_am,'zugang_erhoehungsmitteilung_am');erhoehung=_datum(verlangter_erhoehungsbeginn_am,'verlangter_erhoehungsbeginn_am');kuendigung=_datum(kuendigungseingang_am,'kuendigungseingang_am');_text(einordnungsnachweis,'einordnungsnachweis')
    grund=_frist(zugang.replace(day=1).isoformat(),3,'monate','tagesbeginn')
    if erhoehung.day!=1 or erhoehung<=grund: _fehler('verlangter_erhoehungsbeginn_am','Monatserster nicht vor regulärem Erhöhungsbeginn erforderlich.')
    letzt=_tage_addieren(erhoehung,-1);ende=_frist(erhoehung.isoformat(),2,'monate','tagesbeginn')
    wert=dict(regulaerer_letzter_erklaerungstag=grund.isoformat(),letzter_erklaerungstag_bei_verlangtem_beginn=letzt.isoformat(),mietende_bei_voller_fristausnutzung=ende.isoformat(),erklaerung_im_zeitfenster=zugang<=kuendigung<=letzt)
    eingaben = dict(zugang_erhoehungsmitteilung_am=zugang_erhoehungsmitteilung_am, verlangter_erhoehungsbeginn_am=verlangter_erhoehungsbeginn_am, kuendigungseingang_am=kuendigungseingang_am, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_wahrheitswert','BGB_MIETERHOEHUNG_SONDERKUENDIGUNGSFENSTER',eingaben,[dict(operation='Ausübungsgrundfrist und bei später verlangter Erhöhung verlängertes Erklärungsfenster sowie Mietende bei voller Fristausnutzung berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§561I mit§558bI; spätere verlangte Erhöhung nach BGH25.9.2013,VIII ZR280/12,Rn17–18. Reguläre Ausübungsgrundfrist endet am letzten Tag des zweiten Folgemonats; bei später verlangter Erhöhung bleibt die Erklärung bis zum Vortag des Erhöhungsbeginns möglich. Mietende bei voller Ausnutzung: Ende des zweiten mit Erhöhungsbeginn beginnenden Kalendermonats. Dieses Datum ist der bei voller Fristausnutzung erreichbare Termin, nicht automatisch das tatsächliche Ende jeder früheren oder anders formulierten Kündigung. Der zeitliche Eingangsvergleich bestätigt keine übrige Wirksamkeit. Bei wirksamer561Kündigung bleibt die bisherige Miete maßgeblich; diese Rechtsfolge ist keine zusätzliche eigenständige Zahlenformel. Sonderkorrekturen des Zugangs/§193 gesondert, keine automatische Verschiebung der erklärten Termine.']
    return ergebnis

