"""Betragsgrenze nicht vollzogener Schenkungsauflagen und zeitliche Rückforderungsausschlüsse."""
from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _datum, _ergebnis, _frist, _text


def schenkungsauflage_rueckforderungsbetrag(
    bereicherungsrechtlicher_geschenkwert=None, fuer_auflage_einzusetzender_geschenkwert=None,
    auflage_nicht_vollzogen=None, ruecktrittsvoraussetzungen_erfuellt=None,
    dritter_zur_vollziehung_berechtigt=None, pflicht_oder_anstandsschenkung=None, einordnungsnachweis=None,
):
    """§527: qualifizierte Rückforderung höchstens im für Auflage einzusetzenden Geschenkwert."""
    geschenk = _geld(bereicherungsrechtlicher_geschenkwert)
    auflage = _geld(fuer_auflage_einzusetzender_geschenkwert)
    eingaben = dict(bereicherungsrechtlicher_geschenkwert=bereicherungsrechtlicher_geschenkwert,
        fuer_auflage_einzusetzender_geschenkwert=fuer_auflage_einzusetzender_geschenkwert,
        auflage_nicht_vollzogen=auflage_nicht_vollzogen,
        ruecktrittsvoraussetzungen_erfuellt=ruecktrittsvoraussetzungen_erfuellt,
        dritter_zur_vollziehung_berechtigt=dritter_zur_vollziehung_berechtigt,
        pflicht_oder_anstandsschenkung=pflicht_oder_anstandsschenkung, einordnungsnachweis=einordnungsnachweis)
    for name in tuple(eingaben)[2:-1]:
        _wahrheitswert(eingaben[name], name)
    _text(einordnungsnachweis, "einordnungsnachweis")
    gilt = (auflage_nicht_vollzogen and ruecktrittsvoraussetzungen_erfuellt and
        not dritter_zur_vollziehung_berechtigt and not pflicht_oder_anstandsschenkung)
    ergebnis = _geld_ergebnis(min(geschenk, auflage) if gilt else None,
        "BGB_SCHENKUNGSAUFLAGE_RUECKFORDERUNGSBETRAG", eingaben,
        [dict(operation="Nichtvollziehung und Rücktrittsvoraussetzungen ohne Drittrecht oder privilegierte Schenkung; geringeren Wert aus bereicherungsrechtlicher Herausgabe und Auflagenverwendungsanteil wählen")])
    ergebnis["hinweise"].append("Geldmäßig rechtlich bewerteter Rückforderungsrahmen; keine automatische Umwandlung eines Anspruchs auf Sachherausgabe in Geld. Bereicherungsrechtliche Grenzen und Umfang des für die Auflage einzusetzenden Geschenks vorab bestimmen. Nicht beliebige Erfüllungskosten mit einzusetzendem Geschenkwert gleichsetzen. Rechtmäßige Verweigerung nach§526 und Rücktrittsvoraussetzungen einschließlich Fristsetzung separat berücksichtigen. Anspruch eines Dritten auf Vollziehung schließt diesen Rückforderungsweg aus. Kein automatisches Rückfordern des gesamten Geschenks wegen beliebiger Nichterfüllung.")
    return ergebnis


def schenkung_verarmungsrueckforderung_ausschluss(
    geschenk_geleistet_am=None, beduerftigkeit_eingetreten_am=None,
    beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig=None,
    pflicht_oder_anstandsschenkung=None, einordnungsnachweis=None,
):
    """§529 Absatz1/§534: Verursachung, Zehnjahresablauf bei Bedürftigkeitseintritt und privilegierte Schenkung."""
    _datum(geschenk_geleistet_am, "geschenk_geleistet_am")
    beduerftigkeit = _datum(beduerftigkeit_eingetreten_am, "beduerftigkeit_eingetreten_am")
    _wahrheitswert(beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig, "beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig")
    _wahrheitswert(pflicht_oder_anstandsschenkung, "pflicht_oder_anstandsschenkung")
    _text(einordnungsnachweis, "einordnungsnachweis")
    grenze = _frist(geschenk_geleistet_am, 10, "jahre", "ereignis")
    zeitablauf = beduerftigkeit > grenze
    eingaben = dict(geschenk_geleistet_am=geschenk_geleistet_am, beduerftigkeit_eingetreten_am=beduerftigkeit_eingetreten_am,
        beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig=beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig,
        pflicht_oder_anstandsschenkung=pflicht_oder_anstandsschenkung, einordnungsnachweis=einordnungsnachweis)
    wert = dict(zehnjahreszeitraum_ende=grenze.isoformat(), zehnjahresfrist_bei_beduerftigkeit_abgelaufen=zeitablauf,
        rueckforderung_nach_529_absatz_eins_oder_534_ausgeschlossen=(zeitablauf or
            beduerftigkeit_vorsaetzlich_oder_grob_fahrlaessig or pflicht_oder_anstandsschenkung))
    ergebnis = _ergebnis(wert, "daten_und_wahrheitswerte", "BGB_SCHENKUNG_VERARMUNGSRUECKFORDERUNG_AUSSCHLUSS", eingaben,
        [dict(operation="Zehnjahresablauf gerade bei Eintritt der Bedürftigkeit, schwere Eigenverursachung und privilegierte Schenkung als alternative Ausschlüsse prüfen")], eingaben.copy())
    ergebnis["annahmen"] = ["Konkrete Schenkung, rechtlich fristauslösende Leistung und Eintritt der maßgeblichen Bedürftigkeit bestimmt; feste lokale BGB-Fassung."]
    ergebnis["hinweise"] = ["Nicht Datum der Klage oder Rückforderung als Bedürftigkeitseintritt einsetzen. Spätere Geltendmachung nach zehn Jahren begründet diesen Ausschluss nicht, wenn Bedürftigkeit rechtzeitig eintrat. Taggenaues Modell: Ereignisfrist bis Ende des Jahrestags; untertägige Grenzfälle gesondert normalisieren. FALSE bestätigt keinen Anspruch:§528, bereicherungsrechtliche Grenzen, Beschenktenschutz§529 Absatz2, mehrere Beschenkte und sonstige Ausschlüsse bleiben gesondert. Ein vor Leistung liegender Bedürftigkeitszeitpunkt löst hier keinen Zehnjahresausschluss aus; ob§528 dann greift, wird nicht entschieden. Keine Gleichsetzung mit Pflichtteilsergänzungsabschmelzung§2325."]
    return ergebnis
