from .kalender import _datum, _ergebnis, _frist, _auswahl, _fehler
from .betraege import _geld
from .zinsen import _bruchteile
from .mieterhoehung_sonderkuendigungsfenster import mieterhoehung_sonderkuendigungsfenster

def mieterhoehung_sonderkuendigung_beendigungsmodell(zugang_erhoehungsmitteilung_am=None, verlangter_erhoehungsbeginn_am=None, kuendigungseingang_am=None, beendigungsmodell=None, bisherige_monatsmiete=None, einordnungsnachweis=None):
    """561-Erklärungsfenster prüfen und zwei Monatsendbezüge berechnen; ausschließlich rechtlich vorgegebenes Modell auswählen und unveränderte Miete ausweisen."""
    _auswahl(beendigungsmodell,'beendigungsmodell',('kuendigungszugangsmonat','letzter_ausuebungsmonat'));miete=_geld(bisherige_monatsmiete)
    f=mieterhoehung_sonderkuendigungsfenster(zugang_erhoehungsmitteilung_am,verlangter_erhoehungsbeginn_am,kuendigungseingang_am,einordnungsnachweis)['wert']
    if not f['erklaerung_im_zeitfenster']:_fehler('kuendigungseingang_am','Dieser Ablauf setzt Eingang innerhalb561-Fenster voraus.')
    k=_datum(kuendigungseingang_am,'kuendigungseingang_am');frueh=_frist(k.replace(day=1).isoformat(),3,'monate','tagesbeginn').isoformat();spaet=f['mietende_bei_voller_fristausnutzung']
    wert=dict(termin_nach_kuendigungszugangsmonat=frueh,termin_nach_letztem_ausuebungsmonat=spaet,beendigung_nach_vorgegebenem_modell=frueh if beendigungsmodell=='kuendigungszugangsmonat' else spaet,weitergeltende_monatsmiete=_bruchteile(miete))
    eingaben = dict(zugang_erhoehungsmitteilung_am=zugang_erhoehungsmitteilung_am, verlangter_erhoehungsbeginn_am=verlangter_erhoehungsbeginn_am, kuendigungseingang_am=kuendigungseingang_am, beendigungsmodell=beendigungsmodell, bisherige_monatsmiete=bisherige_monatsmiete, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_und_EUR','BGB_MIETERHOEHUNG_SONDERKUENDIGUNG_BEENDIGUNGSMODELL',eingaben,[dict(operation='561-Erklärungsfenster prüfen und zwei Monatsendbezüge berechnen; ausschließlich rechtlich vorgegebenes Modell auswählen und unveränderte Miete ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['561-Beendigungsrechnung als ausdrücklich bedingtes Modell: Ende des zweiten Monats nach tatsächlichem Kündigungszugangsmonat oder nach letztem Ausübungsmonat. Beide Termine ausweisen, keine stille Gleichsetzung früher Erklärung mit voller Fristausnutzung. Vorhandenes561-Fenster berücksichtigt später verlangte Erhöhung nachBGH25.9.2013VIIIZR280/12; diese Quelle belegt volle Fristausnutzung, nicht universell den früheren Beendigungsbezug. Rechtliche Auswahl daher zwingend. Eingang muss im berechneten Fenster liegen. Bei rechtlich wirksamer561-Kündigung tritt die Erhöhung nicht ein, bisherige Monatsmiete bleibt bis Ende maßgeblich. Keine automatische Wirksamkeitsfeststellung oder taganteilige Schlussabrechnung. Monatsendtermin nicht wegen Wochenende verschieben.']
    return ergebnis

