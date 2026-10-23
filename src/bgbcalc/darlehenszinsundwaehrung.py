"""Exakte Sollzinskorrektur und Fremdwährungsdarlehens-Vergleichswerte."""
from .betraege import _geld
from .kalender import _text, _fehler, _ergebnis
from .zahlen import _bruch, _multiplizieren, _subtrahieren
from .zinsen import _bruchteile


def verbraucherdarlehen_sollzinskorrektur(vertraglicher_sollzinssatz=None, angegebener_effektiver_jahreszins=None, tatsaechlicher_effektiver_jahreszins=None, einordnungsnachweis=None):
    """Sollzinssatz um die positive Differenz zwischen tatsächlichem und angegebenem Effektivzins vermindern."""
    soll,angegeben,tatsaechlich=[_geld(x) for x in (vertraglicher_sollzinssatz,angegebener_effektiver_jahreszins,tatsaechlicher_effektiver_jahreszins)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if angegeben>tatsaechlich:
        _fehler('angegebener_effektiver_jahreszins','Diese Korrektur verlangt höchstens den tatsächlichen Effektivzins als Angabe.')
    differenz=_subtrahieren(tatsaechlich,angegeben); korrigiert=_subtrahieren(soll,differenz)
    wert=dict(effektivzins_unterangabe=_bruchteile(differenz),rechnerisch_verminderter_sollzinssatz=_bruchteile(korrigiert))
    eingaben=dict(vertraglicher_sollzinssatz=vertraglicher_sollzinssatz,angegebener_effektiver_jahreszins=angegebener_effektiver_jahreszins,tatsaechlicher_effektiver_jahreszins=tatsaechlicher_effektiver_jahreszins,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'zinssaetze','BGB_VERBRAUCHERDARLEHEN_SOLLZINSKORREKTUR',eingaben,[dict(operation='Tatsächlicher Effektivzins minus angegebener Effektivzins als absolute Zinsdifferenz vom Sollzinssatz abziehen.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §494 Absatz3 bei qualifiziert zu niedrig angegebenem effektivem Jahreszins. Zinssätze als Jahresquoten eingeben, etwa0.05 für5Prozent; Differenz von6%und5% ist ein Prozentpunkt, kein relativer Abschlag von20%. Tatsächlichen Effektivzins extern nach einschlägigen Vorgaben berechnen. Ergebnis ist der vorzeichenbehaftete mathematische Korrekturwert ohne im Normtext nicht genannte Nulluntergrenze; negative Ergebnisse begründen hier keine automatische Zahlungspflicht des Darlehensgebers. Fehlende Angaben nach Absatz2, Kostenwegfall nach Absatz4 und neue Raten nach Absatz5 separat behandeln; keine automatische Annuitätenformel.']
    return ergebnis


def immobiliardarlehen_wechselkursrechnung(fremdwaehrungsbetrag=None, wechselkurs_vertrag=None, wechselkurs_vergleich=None, wechselkurs_umstellung=None, einordnungsnachweis=None):
    """Identischen Rest- oder Ratenbetrag zum Vertrags-/Vergleichskurs bewerten,120%-Grenze prüfen und Umstellungswert berechnen."""
    betrag,vertrag,vergleich,umstellung=[_geld(x) for x in (fremdwaehrungsbetrag,wechselkurs_vertrag,wechselkurs_vergleich,wechselkurs_umstellung)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if min(vertrag,vergleich,umstellung)<=0:
        _fehler('wechselkurse','Alle Kurse müssen positiv sein und Landeswährung je einer Fremdwährungseinheit ausdrücken.')
    vertragswert=_multiplizieren(betrag,vertrag); vergleichswert=_multiplizieren(betrag,vergleich); grenze=_multiplizieren(vertragswert,_bruch(6,5)); umstellungswert=_multiplizieren(betrag,umstellung)
    wert=dict(wert_zum_vertragskurs=_bruchteile(vertragswert),wert_zum_vergleichskurs=_bruchteile(vergleichswert),zwanzigprozent_grenzwert=_bruchteile(grenze),grenze_strikt_ueberschritten=vergleichswert>grenze,wert_zum_umstellungskurs=_bruchteile(umstellungswert))
    eingaben=dict(fremdwaehrungsbetrag=fremdwaehrungsbetrag,wechselkurs_vertrag=wechselkurs_vertrag,wechselkurs_vergleich=wechselkurs_vergleich,wechselkurs_umstellung=wechselkurs_umstellung,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_ergebnis(wert,'landeswaehrung','BGB_IMMOBILIARDARLEHEN_WECHSELKURSRECHNUNG',eingaben,[dict(operation='Denselben Fremdwährungsbetrag mit jeweils Landeswährung/Fremdwährung-Kurs multiplizieren; Vergleichswert strikt über6/5 des Vertragskurswerts; Umstellung zum gesondert qualifizierten Kurs.')],eingaben.copy())
    ergebnis['hinweise']=['Nur §503 für qualifiziertes Immobiliar-Verbraucherdarlehen in Fremdwährung. Derselbe aktuelle Restbetrag oder dieselbe regelmäßige Rate wird in beiden Vergleichswerten verwendet, nicht ursprünglicher Nennbetrag gegen heutige Restschuld. Landeswährung nach Absatz1 einschließlich wirksamer Währungsvereinbarung rechtlich bestimmen. Restbetrag und Rate bei unterschiedlichen relevanten Werten separat prüfen; numerischer Auslöser liegt vor, wenn wenigstens einer strikt über20% gestiegen ist. Umstellungskurs ist grundsätzlich Marktwechselkurs am Antragstag, bei wirksamer abweichender Vereinbarung deren Kurs; muss extern belegt werden. Kein Kursabruf, keine automatische Umwandlung/Vertragsänderung. Alle Kurse haben dieselbe ausdrückliche Orientierung Landeswährung je Fremdwährungseinheit.']
    return ergebnis
