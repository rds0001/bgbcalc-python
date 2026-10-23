"""Geförderte Heizungsmodernisierung: Kapitalzuschussfall mit qualifizierter Restkappung."""
from .betraege import _geld
from .kalender import _text, _fehler, _ergebnis
from .zahlen import _bruch, _subtrahieren, _multiplizieren
from .zinsen import _bruchteile

def heizungsmodernisierung_gefoerderter_betrag(kosten_wohnung=None, von_erhaltungspauschale_ausgenommene_kosten=None, abzuziehende_drittmittel=None, monatliche_restkappungsgrenze=None, einordnungsnachweis=None):
    """15 Prozent des nicht ausgenommenen Kostenanteils abziehen, danach qualifizierte Drittmittel abziehen und bei null begrenzen; zehn Prozent jährlich, durch zwölf teilen und auf vorab bestimmte monatliche Restkappungsgrenze begrenzen."""
    kosten, ausgenommen, drittmittel, kappung = [_geld(kosten_wohnung), _geld(von_erhaltungspauschale_ausgenommene_kosten), _geld(abzuziehende_drittmittel), _geld(monatliche_restkappungsgrenze)]
    _text(einordnungsnachweis,"einordnungsnachweis")
    if ausgenommen > kosten:
        _fehler("von_erhaltungspauschale_ausgenommene_kosten","Ausgenommener Teil darf Gesamtkosten nicht übersteigen.")
    if drittmittel <= 0 or drittmittel > kosten:
        _fehler("abzuziehende_drittmittel","Positive kostenmindernde Drittmittel höchstens in Höhe der Kosten erforderlich.")
    pauschale = _multiplizieren(_subtrahieren(kosten,ausgenommen),_bruch(3,20))
    basis = max(_subtrahieren(_subtrahieren(kosten,pauschale),drittmittel),_bruch(0))
    jahr = _multiplizieren(basis,_bruch(1,10))
    monat = _multiplizieren(jahr,_bruch(1,12))
    begrenzt = min(monat,kappung)
    wert = dict(erhaltungspauschale=_bruchteile(pauschale),kostenbasis=_bruchteile(basis),jahresbetrag_vor_kappung=_bruchteile(jahr),monatsbetrag_vor_kappung=_bruchteile(monat),gekappter_monatsbetrag=_bruchteile(begrenzt))
    eingaben = dict(kosten_wohnung=kosten_wohnung, von_erhaltungspauschale_ausgenommene_kosten=von_erhaltungspauschale_ausgenommene_kosten, abzuziehende_drittmittel=abzuziehende_drittmittel, monatliche_restkappungsgrenze=monatliche_restkappungsgrenze, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"EUR","BGB_HEIZUNGSMODERNISIERUNG_GEFOERDERTER_BETRAG",eingaben,[dict(operation='15 Prozent des nicht ausgenommenen Kostenanteils abziehen, danach qualifizierte Drittmittel abziehen und bei null begrenzen; zehn Prozent jährlich, durch zwölf teilen und auf vorab bestimmte monatliche Restkappungsgrenze begrenzen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Nur §559e mit tatsächlich in Anspruch genommenen, einmaligen kostenmindernden Drittmitteln als positivem Betrag. Kosten bereits nach §559 Absatz3 der Wohnung zugeordnet. Ausgenommenen Kostenanteil nach lokaler Fassung §559e Absatz2 Satz2 (Heizungsanlage im Sinne §43 Gebäudemodernisierungsgesetz) ausdrücklich qualifizieren, andernfalls null. Keine automatische Förderfähigkeit, Kostenverteilung, Härteprüfung oder Wirksamkeit. Restkappungsgrenze zuvor nach §559e Absatz3 rechtlich bestimmen, etwa mit modernisierung_kappungsgrenze; keine doppelte Anrechnung bisheriger Erhöhungen. Fälle laufender Zuschüsse, Darlehen und Zinsvergünstigungen einschließlich ihrer Reihenfolge zur Kappung bleiben außerhalb dieses Kapitalzuschussfalls. Ohne Förderung gilt anderer Ansatz §559. Keine tatsächlichen Erhaltungskosten zusätzlich zur Pauschale abziehen.']
    return ergebnis
