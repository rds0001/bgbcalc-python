from .kalender import _ergebnis, _text, _fehler
from .betraege import _geld
from .tilgung import _anrechnen

def draufgabe_geldanrechnung(anrechnungsfall=None, geschuldeter_betrag=None, draufgabebetrag=None, einordnungsnachweis=None):
    """Anrechenbare Geld-Draufgabe bis zur bestimmten Leistung oder zum Schadensersatz anrechnen, Restbetrag und nicht angerechneten Draufgabenteil ausweisen."""
    art = _text(anrechnungsfall,'anrechnungsfall')
    if art not in ('leistung_337','schadensersatz_338'): _fehler('anrechnungsfall','leistung_337 oder schadensersatz_338 erforderlich.')
    schuld = _geld(geschuldeter_betrag);draufgabe = _geld(draufgabebetrag)
    _text(einordnungsnachweis,'einordnungsnachweis')
    zuordnung = _anrechnen(draufgabe,dict(betrag=schuld),['betrag'])
    position = zuordnung['zuordnungen'][0]
    wert = dict(angerechneter_betrag=position['betrag'],verbleibender_betrag=position['restforderung'],nicht_angerechnete_draufgabe=zuordnung['nicht_zugeordnet'])
    eingaben = dict(anrechnungsfall=anrechnungsfall, geschuldeter_betrag=geschuldeter_betrag, draufgabebetrag=draufgabebetrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_DRAUFGABE_GELDANRECHNUNG',eingaben,[dict(operation='Anrechenbare Geld-Draufgabe bis zur bestimmten Leistung oder zum Schadensersatz anrechnen, Restbetrag und nicht angerechneten Draufgabenteil ausweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§337I beziehungsweise338Satz2: Anrechnung einer qualifizierten Geld-Draufgabe auf den bestimmten Leistungs- beziehungsweise Schadensersatzbetrag. Anrechnung höchstens in Höhe des geschuldeten Betrags, danach rechnerischer Rest. Ein nicht angerechneter Draufgabenteil wird separat ausgewiesen; daraus folgt weder Rückzahlungsanspruch noch Verwirkung. Insbesondere bei338 keine automatische Rückzahlung des den Schaden übersteigenden Betrags. Nicht anrechenbare Sach-Draufgaben und reine Rückgabepflichten337II/338 sind keine eigenständige Geldberechnung; weder Geldersatz noch Eigentums-/Rückgabeentscheidung wird erfunden. Keine automatische Bestimmung der gesetzlichen Zweifelregel oder Anrechnung auf zusätzliche Zinsen/Kosten.']
    return ergebnis

