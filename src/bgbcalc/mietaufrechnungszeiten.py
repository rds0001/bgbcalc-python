from .reisezeitschwellen import _reise_utc_zeitpunkt
from .kalender import _ergebnis, _text

def miete_gegenforderung_zeitvergleich(kenntnis_eigentumsuebergang_utc=None, gegenforderung_erworben_utc=None, gegenforderung_faellig_utc=None, miete_faellig_utc=None, einordnungsnachweis=None):
    """Erwerb nach Kenntnis oder Gegenforderungsfälligkeit sowohl nach Kenntnis als auch nach Mietfälligkeit durch strikte Zeitvergleiche bestimmen."""
    kenntnis_eigentumsuebergang = _reise_utc_zeitpunkt(kenntnis_eigentumsuebergang_utc,'kenntnis_eigentumsuebergang_utc')
    gegenforderung_erworben = _reise_utc_zeitpunkt(gegenforderung_erworben_utc,'gegenforderung_erworben_utc')
    gegenforderung_faellig = _reise_utc_zeitpunkt(gegenforderung_faellig_utc,'gegenforderung_faellig_utc')
    miete_faellig = _reise_utc_zeitpunkt(miete_faellig_utc,'miete_faellig_utc')
    _text(einordnungsnachweis,'einordnungsnachweis')
    erwerbspaeter = gegenforderung_erworben>kenntnis_eigentumsuebergang
    faelligspaeter = gegenforderung_faellig>kenntnis_eigentumsuebergang and gegenforderung_faellig>miete_faellig
    wert = dict(erwerb_nach_kenntnis=erwerbspaeter,faelligkeit_nach_kenntnis_und_miete=faelligspaeter,zeitlicher_ausschluss=erwerbspaeter or faelligspaeter)
    eingaben = dict(kenntnis_eigentumsuebergang_utc=kenntnis_eigentumsuebergang_utc, gegenforderung_erworben_utc=gegenforderung_erworben_utc, gegenforderung_faellig_utc=gegenforderung_faellig_utc, miete_faellig_utc=miete_faellig_utc, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,"wahrheitswerte",'BGB_MIETE_GEGENFORDERUNG_ZEITVERGLEICH',eingaben,[dict(operation='Erwerb nach Kenntnis oder Gegenforderungsfälligkeit sowohl nach Kenntnis als auch nach Mietfälligkeit durch strikte Zeitvergleiche bestimmen.')],eingaben.copy())
    ergebnis["hinweise"] = ['§566dSatz2: ausschließlich numerische Chronologie der zeitlichen Ausschlusstatbestände. Gleichzeitigkeit erfüllt das jeweilige nach/später nicht. Erwerb der Gegenforderung nach Kenntnis genügt unabhängig vom Fälligkeitsvergleich; bei früherem/gleichzeitigem Erwerb ist die zweite Alternative nur bei Fälligkeit nach BEIDEN Bezugspunkten erfüllt. Keine automatische Aufrechnungsberechtigung:566dSatz1,566c, übrige Aufrechnungsvoraussetzungen und Beträge gesondert. Sekundengenaue tatsächliche UTC-Zeitpunkte erforderlich; keine Zeitzonenannahme, keine künstliche Mitternacht bei lediglich bekannten Tagen, keine Subsekunden abschneiden. Standard-Datumsbibliotheken über vorhandenen UTC-Parser wiederverwendet.']
    return ergebnis
