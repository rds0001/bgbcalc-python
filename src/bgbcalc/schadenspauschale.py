from .kalender import _ergebnis, _text
from .betraege import _geld
from .zinsen import _bruchteile

def schadenspauschale_betragsvergleich(pauschalbetrag=None, gewoehnlich_zu_erwartender_betrag=None, einordnungsnachweis=None):
    """Schadens- oder Wertminderungspauschale mit qualifiziertem gewöhnlichen Erwartungsbetrag vergleichen und positiven Überschreitungsbetrag berechnen."""
    pauschale = _geld(pauschalbetrag);vergleich = _geld(gewoehnlich_zu_erwartender_betrag)
    _text(einordnungsnachweis,'einordnungsnachweis')
    wert = dict(pauschale_uebersteigt_vergleichsbetrag=pauschale>vergleich,ueberschreitungsbetrag=_bruchteile(max(0,pauschale-vergleich)))
    eingaben = dict(pauschalbetrag=pauschalbetrag, gewoehnlich_zu_erwartender_betrag=gewoehnlich_zu_erwartender_betrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR_und_wahrheitswert','BGB_SCHADENSPAUSCHALE_BETRAGSVERGLEICH',eingaben,[dict(operation='Schadens- oder Wertminderungspauschale mit qualifiziertem gewöhnlichen Erwartungsbetrag vergleichen und positiven Überschreitungsbetrag berechnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§309Nr5a: strenger Betragsvergleich der Pauschale mit dem qualifizierten gewöhnlich zu erwartenden Schaden oder der Wertminderung. Vergleichsmaßstab ist nicht automatisch der konkret entstandene Einzelschaden. Keine automatische Wirksamkeitsentscheidung, insbesondere keine Prüfung von309Nr5b. Der positive Überschreitungsbetrag ist keine automatische Rückforderung oder geltungserhaltende Herabsetzung auf einen zulässigen Vertragsbetrag.']
    return ergebnis

