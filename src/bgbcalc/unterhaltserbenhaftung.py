"""Kumulative rechnerische Erbenhaftungsgrenze für nachehelichen Unterhalt."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile


def unterhalt_erbenhaftungsbetrag(hypothetischer_pflichtteil=None, angerechnete_erbenleistungen=None, offener_unterhalt=None, haftungsnachweis=None):
    """§1586b: Pflichtteilsgrenze nach angerechneten Leistungen auf offene Forderung anwenden."""
    grenze = _geld(hypothetischer_pflichtteil)
    geleistet = _geld(angerechnete_erbenleistungen)
    offen = _geld(offener_unterhalt)
    _text(haftungsnachweis, 'haftungsnachweis')
    restgrenze = max(_subtrahieren(grenze,geleistet),_bruch(0))
    gedeckt = min(offen,restgrenze)
    eingaben = dict(hypothetischer_pflichtteil=hypothetischer_pflichtteil,angerechnete_erbenleistungen=angerechnete_erbenleistungen,offener_unterhalt=offener_unterhalt,haftungsnachweis=haftungsnachweis)
    wert = {k:_bruchteile(v) for k,v in dict(verbleibende_haftungsgrenze=restgrenze,haftungsbegrenzter_unterhaltsbetrag=gedeckt,nicht_von_dieser_haftung_gedeckt=_subtrahieren(offen,gedeckt),haftungsrest_nach_forderung=_subtrahieren(restgrenze,gedeckt)).items()}
    ergebnis = _ergebnis(wert,'EUR','BGB_UNTERHALT_ERBENHAFTUNGSBETRAG',eingaben,[dict(operation='Hypothetischen Pflichtteil um angerechnete Erbenleistungen vermindern, Rest mindestens null; offene Unterhaltsforderung höchstens bis zur verbleibenden Grenze berücksichtigen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1586b: ein qualifiziertes Unterhaltsverhältnis nach Tod des Verpflichteten. Hypothetischer Pflichtteil bei fortbestehend gedachter Ehe bewertet; güterstandsbedingte Besonderheiten nachAbsatz2 außer Betracht lassen. Keine erneute hypothetische Nachlass-/Pflichtteilsbewertung oder Prüfung von Pflichtteilsergänzung. Angerechnete Erbenleistungen sind nur rechtlich auf diese gemeinsame Grenze anzurechnende Leistungen, keine ungeprüften Unterhaltszahlungen des Erblassers zu Lebzeiten. Mehrere Erben haben keine vervielfachte Grenze; alle einschlägigen Leistungen konsolidiert vorgeben, interne Erbenverteilung außerhalb. §1581-Beschränkungen des verstorbenen Verpflichteten nicht fortschreiben. Offene Forderung bereits nach übrigen Unterhaltsregeln bestimmt; weitere gegenständliche Nachlasshaftungsbeschränkungen gesondert. Übersteigende Vorleistungen führen zu Restgrenze0, keinem automatisch festgestellten Rückzahlungsanspruch.']
    return ergebnis
