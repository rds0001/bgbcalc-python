"""Zeitgrenze letztwilliger Auseinandersetzungsbeschränkungen (§2044 Absatz2)."""
from .betraege import _wahrheitswert
from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _text


def erbauseinandersetzung_dreissigjahresgrenze(erbfall_am=None, prueftag=None,
    fortgeltungsanordnung=None, angeordnetes_ereignis_am=None,
    miterbe_juristische_person=None, anordnung_rechtlich_qualifiziert=None, einordnungsnachweis=None):
    """Dreißigjahresgrenze und ausdrücklich angeordnetes Ereignisende getrennt prüfen."""
    erbfall = _datum(erbfall_am, 'erbfall_am')
    tag = _datum(prueftag, 'prueftag')
    if tag < erbfall:
        _fehler('prueftag', 'Prüftag darf nicht vor Erbfall liegen.')
    ende = _frist(erbfall_am, 30, 'jahre', 'ereignis')
    _auswahl(fortgeltungsanordnung, 'fortgeltungsanordnung', ('keine', 'miterbenereignis', 'nacherbfolge', 'vermaechtnisanfall'))
    ereignis = _datum(angeordnetes_ereignis_am, 'angeordnetes_ereignis_am') if angeordnetes_ereignis_am is not None else None
    if ereignis is not None and not erbfall <= ereignis <= tag:
        _fehler('angeordnetes_ereignis_am', 'Angeordnetes Ereignis muss zwischen Erbfall und Prüftag liegen.')
    if fortgeltungsanordnung == 'keine' and ereignis is not None:
        _fehler('angeordnetes_ereignis_am', 'Ohne besondere Anordnung kein zugehöriges Ereignisdatum angeben.')
    _wahrheitswert(miterbe_juristische_person, 'miterbe_juristische_person')
    _wahrheitswert(anordnung_rechtlich_qualifiziert, 'anordnung_rechtlich_qualifiziert')
    _text(einordnungsnachweis, 'einordnungsnachweis')
    verlaengerbar = fortgeltungsanordnung != 'keine' and not (fortgeltungsanordnung == 'miterbenereignis' and miterbe_juristische_person)
    wert = dict(dreissigjahresfristende=ende.isoformat(), besondere_fortgeltung_zulaessig=verlaengerbar,
        angeordnetes_ereignis_eingetreten=ereignis is not None,
        zeitliche_wirkung_beendet=ereignis is not None or (tag >= ende and not verlaengerbar))
    eingaben = dict(erbfall_am=erbfall_am, prueftag=prueftag, fortgeltungsanordnung=fortgeltungsanordnung,
        angeordnetes_ereignis_am=angeordnetes_ereignis_am, miterbe_juristische_person=miterbe_juristische_person,
        anordnung_rechtlich_qualifiziert=anordnung_rechtlich_qualifiziert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert, 'daten_und_wahrheitswerte', 'BGB_ERBAUSEINANDERSETZUNG_DREISSIGJAHRESGRENZE', eingaben,
        [dict(operation='Dreißig Jahre ab Erbfall; besondere Anordnung und juristischen Ereignismiterben prüfen; eingetretenes Ereignis beendet Anordnung')], eingaben.copy())
    if not anordnung_rechtlich_qualifiziert:
        ergebnis['wert'] = None
        ergebnis['status'] = 'NICHT_ANWENDBAR'
    ergebnis['annahmen'] = ['Prüfung nach vollständigem Ablauf des Prüftags; frühere andere Beendigungstatbestände gesondert geprüft. Feste lokale BGB-Fassung.']
    ergebnis['hinweise'] = ['Nur zeitliche Wirkung nach§2044 Absatz2 bei wirksamer letztwilliger Beschränkung für Nachlass oder einzelne Gegenstände; kein vollständiger Auseinandersetzungsanspruch. Modell umfasst unbefristete Anordnung oder ausdrückliches Ereignisende, keine anderweitig kürzer befristete Anordnung. Wichtiger Grund§749 Absatz2/3, Zweifelsregel bei Tod§750, Gläubiger-/Nachfolgewirkung§751 und Grundbucheintragung§1010 Absatz1 gesondert prüfen. Besonderes Ereignis muss letztwillig als Endpunkt angeordnet sein; Nacherbfolge/Vermächtnis allein verlängern nicht automatisch. Ereignisdatum NULL bedeutet bis Prüftag nicht eingetreten, nicht unbekannt; ein Ereignis beendet ab seinem Eintritt. Juristische Person sperrt Verlängerung nur bei Ereignis gerade in der Person dieses Miterben, nicht pauschal bei Vermächtnis-/Nacherbfolgeanordnung. §2044 enthält keinen ausdrücklichen Verweis auf§2109; dessen Lebend- und Geschwistervoraussetzungen nicht übertragen. Wirksamkeit einer zugrunde gelegten Nacherbfolge gegebenenfalls einschließlich§2109 separat qualifizieren. Keine automatische Wochenend-/Feiertagsverschiebung.']
    return ergebnis
