"""Aggregierter Ausbildungsrahmen aus dem zusätzlichen Zugewinnviertel."""
from .betraege import _geld
from .kalender import _ergebnis, _text
from .zahlen import _bruch, _dividieren, _subtrahieren
from .zinsen import _bruchteile


def zusatzviertel_ausbildungsrahmen(viertelbemessungsgrundlage=None, qualifizierter_ausbildungsgesamtbedarf=None, bewertungsnachweis=None):
    """§1371IV: Gesamtbedarf berechtigter Abkömmlinge durch zusätzliches Nachlassviertel begrenzen."""
    basis = _geld(viertelbemessungsgrundlage)
    bedarf = _geld(qualifizierter_ausbildungsgesamtbedarf)
    _text(bewertungsnachweis,'bewertungsnachweis')
    viertel = _dividieren(basis,_bruch(4))
    mittel = min(viertel,bedarf)
    eingaben = dict(viertelbemessungsgrundlage=viertelbemessungsgrundlage,qualifizierter_ausbildungsgesamtbedarf=qualifizierter_ausbildungsgesamtbedarf,bewertungsnachweis=bewertungsnachweis)
    wert = dict(zusaetzliches_viertel=_bruchteile(viertel),ausbildungsrahmen=_bruchteile(mittel),nicht_aus_viertel_gedeckter_bedarf=_bruchteile(_subtrahieren(bedarf,mittel)),nicht_fuer_diesen_gesamtbedarf_benoetigtes_viertel=_bruchteile(_subtrahieren(viertel,mittel)))
    ergebnis = _ergebnis(wert,'EUR','BGB_ZUSATZVIERTEL_AUSBILDUNGSRAHMEN',eingaben,[dict(operation='Rechtlich bewertete Viertelbemessungsgrundlage durch vier teilen und qualifizierten gesamten Ausbildungsbedarf auf dieses zusätzliche Viertel begrenzen.')],eingaben.copy())
    ergebnis['hinweise'] = ['§1371IV setzt tatsächlich nachAbsatz1 zusätzlich gewährtes Viertel und bedürftige erbberechtigte Abkömmlinge voraus, die nicht aus der aufgelösten Ehe stammen. Bemessungsgrundlage und angemessener bedürftigkeitsabhängiger Gesamtausbildungsbedarf rechtlich qualifiziert, keine pauschalen Bruttonachlass- oder Ausbildungskostenannahmen. Aggregierte Rahmenrechnung für vollständig abgegrenzten Kreis/Bedarfsumfang; keine Einzelverteilung, Rangregel oder Priorität nach zeitlicher Geltendmachung erfunden. Vergangene Leistungen/Verbrauch des Viertels, Wertänderungen, abweichende Nachlassbindungen und Wiederverwendung desselben Viertels für neue Bedarfsrunden gesondert rechtlich abgrenzen; dieser Rahmen darf nicht wiederholt ohne Anrechnung ausgeschöpft werden. Keine autonome Prüfung von Erbberechtigung, Abstammung, Bedürftigkeit oder Angemessenheit.']
    return ergebnis
