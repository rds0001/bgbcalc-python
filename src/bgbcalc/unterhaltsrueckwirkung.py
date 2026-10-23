"""Anlassminimum und Monatsbeginn für Unterhaltsrückwirkung nach§1613I."""
from .kalender import _datum, _ergebnis, _fehler, _text


def unterhalt_rueckwirkungsbeginn(auskunftsaufforderung_am=None, verzug_am=None, rechtshaengigkeit_am=None, anspruchsbeginn_am=None, anlassnachweis=None):
    """Frühesten qualifizierten Anlass mit Anspruchsbeginn und bedingter Monatsrückwirkung kombinieren."""
    anspruch = _datum(anspruchsbeginn_am,'anspruchsbeginn_am')
    ereignisse=[]
    for name,wert in [('auskunftsaufforderung_am',auskunftsaufforderung_am),('verzug_am',verzug_am),('rechtshaengigkeit_am',rechtshaengigkeit_am)]:
        if wert is not None:
            ereignisse.append(_datum(wert,name))
    if not ereignisse:
        _fehler('anlass','Mindestens ein rechtlich qualifizierter Anlass nach§1613I erforderlich.','EINGABE_FEHLT')
    _text(anlassnachweis,'anlassnachweis')
    fruehester = min(ereignisse)
    monatsanfang = fruehester.replace(day=1)
    beginn = monatsanfang if anspruch <= monatsanfang else max(fruehester,anspruch)
    eingaben = dict(auskunftsaufforderung_am=auskunftsaufforderung_am,verzug_am=verzug_am,rechtshaengigkeit_am=rechtshaengigkeit_am,anspruchsbeginn_am=anspruchsbeginn_am,anlassnachweis=anlassnachweis)
    ergebnis = _ergebnis(dict(fruehester_qualifizierter_anlass=fruehester.isoformat(),anlassmonatsanfang=monatsanfang.isoformat(),rueckwirkungsbeginn=beginn.isoformat()),'daten','BGB_UNTERHALT_RUECKWIRKUNGSBEGINN',eingaben,[dict(operation='Frühesten qualifizierten Anlass wählen; bei bereits am Monatsanfang bestehendem Anspruch auf diesen zurückgehen, sonst frühestens Anlass und Anspruchsbeginn.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1613I für ein rechtlich abgegrenztes durchgehend bestehendes Unterhaltsverhältnis. Nur für Geltendmachung dieses Unterhalts wirksame Auskunftsaufforderung, wirksamen Verzug oder Rechtshängigkeit eingeben; unwirksame oder anders zugeordnete Ereignisse nicht eintragen. Anspruchsbeginn ist qualifizierter Beginn des dem Grunde nach bestehenden Anspruchs, nicht Beginn bloß einer späteren Betragsänderung. Besteht er am ersten Tag des Monats des frühesten Ereignisses, gilt dieser Monatsanfang; andernfalls keine pauschale Rückverlagerung auf Anspruchsentstehung vor dem Anlass. Ein rechtlich bereits vor Anspruchsbeginn wirksamer Anlass kann keinen Unterhalt vor Anspruchsentstehung erzeugen. Anspruchsunterbrechungen oder wechselnde Unterhaltsverhältnisse getrennt berechnen. Sonderbedarf/Hinderungsfälle nachAbsatz2, HärteregelAbsatz3, Erfüllung und Betragshöhe nicht berechnet.']
    return ergebnis
