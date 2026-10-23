"""Gesetzliche geburtsbezogene Rechenzeiträume ohne medizinische oder Abstammungsentscheidung."""
from .kalender import _datum, _ergebnis, _frist, _monatsende, _tage_addieren


def empfaengniszeit_gesetzlicher_zeitraum(geburt_am=None):
    """§1600dIII1: 300. bis181.Tag vor Geburt einschließlich beider Grenzen."""
    geburt = _datum(geburt_am, 'geburt_am')
    anfang = _tage_addieren(geburt,-300)
    ende = _tage_addieren(geburt,-181)
    eingaben = dict(geburt_am=geburt_am)
    ergebnis = _ergebnis(dict(zeitraum_beginn=anfang.isoformat(),zeitraum_ende=ende.isoformat(),tage_einschliesslich=120),'daten','BGB_EMPFAENGNISZEIT_GESETZLICHER_ZEITRAUM',eingaben,[dict(operation='300 und181 Kalendertage vom Geburtsdatum abziehen; beide Grenztage einbeziehen, insgesamt120 Tage.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur gesetzlicher Ausgangszeitraum nach§1600dIII1. Ein feststehender abweichender Empfängniszeitraum nachSatz2 verdrängt diesen Zeitraum und muss fachlich belegt gesondert verwendet werden. Keine medizinische Schätzung und keine Feststellung der Vaterschaft; Beischlaf, Zweifel und sonstige Ausschlüsse nicht geprüft. Nicht mit300-Tage-Regel nach§1593 gleichsetzen.']
    return ergebnis


def geburtsunterhalt_zeitgrenzen(geburt_am=None):
    """§1615lI/II: sechs Wochen vor, acht Wochen nach, vier Monate vor und drei Jahre nach Geburt."""
    geburt = _datum(geburt_am, 'geburt_am')
    vor_sechs = _tage_addieren(geburt,-42)
    nach_acht = _frist(geburt_am,8,'wochen','ereignis')
    vor_vier = _monatsende(geburt,-4,False)
    nach_drei = _frist(geburt_am,3,'jahre','ereignis')
    eingaben = dict(geburt_am=geburt_am)
    ergebnis = _ergebnis(dict(regelzeitraum_beginn=vor_sechs.isoformat(),regelzeitraum_ende=nach_acht.isoformat(),erweiterung_fruehester_beginn=vor_vier.isoformat(),dreijahresgrundgrenze=nach_drei.isoformat()),'daten','BGB_GEBURTSUNTERHALT_ZEITGRENZEN',eingaben,[dict(operation='Geburt minus sechs Wochen und plus acht Wochen; früheste Erweiterung minus vier Kalendermonate und Dreijahresgrundgrenze plus drei Jahre.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur gesetzliche Zeitgrenzen nach§1615lI1/II3, kein automatischer Anspruch für den gesamten erweiterten Zeitraum. Schwangerschaft/Krankheit oder Betreuung, fehlende Erwerbserwartung und tatsächlicher Beginn/Umfang rechtlich qualifizieren. Billigkeitsverlängerungen nachAbsatz2 sind nicht auf drei Jahre begrenzt. Schwangerschafts-/Entbindungskosten können nachAbsatz1Satz2 auch außerhalb des Regelzeitraums entstehen. Absatz4-Verweis für betreuenden Vater gesondert qualifizieren. Keine Unterhaltshöhe, Tagesproration oder medizinische Berechnung. Ereignisbezogene Enddaten sind Ablaufdaten, keine Altersbeginnberechnung nach§187II2.']
    return ergebnis
