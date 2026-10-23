from .kalender import _auswahl, _datum, _ergebnis, _fehler, _frist, _tage_addieren, _text, _vorhanden


def _widerrufs_bezugstag(ereignistage, parameter, anzahl=None):
    _vorhanden(ereignistage,parameter)
    if not isinstance(ereignistage,list) or not 1<=len(ereignistage)<=10:
        _fehler(parameter,'Unbenannte Liste1bis10 tatsächlich eingetretener Ereignistage erforderlich.')
    if anzahl is not None and len(ereignistage)!=anzahl:
        _fehler(parameter,'Anzahl der Bezugsereignisse passt nicht zum gesetzlichen Höchstfristfall.')
    return max(_datum(t,parameter) for t in ereignistage)


def widerruf_regelfristende(fristart=None, erforderliche_ereignistage=None, einordnungsnachweis=None):
    """Spätesten Tag aller erforderlichen Anfangsvoraussetzungen wählen und14Tage oder einen Monat fortschreiben."""
    _auswahl(fristart,'fristart',('standard_vierzehn_tage','darlehen_angabennachholung_monat'))
    beginn = _widerrufs_bezugstag(erforderliche_ereignistage,'erforderliche_ereignistage')
    _text(einordnungsnachweis,'einordnungsnachweis')
    ende = _frist(beginn.isoformat(),14 if fristart=='standard_vierzehn_tage' else 1,'tage' if fristart=='standard_vierzehn_tage' else 'monate','ereignis')
    eingaben = dict(fristart=fristart,erforderliche_ereignistage=erforderliche_ereignistage,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(massgeblicher_ereignistag=beginn.isoformat(),regelfristende_ohne_kalenderkorrektur=ende.isoformat()),'daten','BGB_WIDERRUF_REGELFRISTENDE',eingaben,[dict(operation='Spätesten Tag aller erforderlichen Anfangsvoraussetzungen wählen und14Tage oder einen Monat fortschreiben.')],eingaben.copy())
    ergebnis['hinweise'] = ['§355II und356–356f:14Tage im qualifizierten Standardfall; ein Monat ausschließlich bei nachgeholten Angaben356bII. Liste muss sämtliche rechtlich erforderlichen eingetretenen Anfangsvoraussetzungen enthalten: je Norm insbesondere Vertrag/Vorvertrag, maßgeblicher Warenempfang, Vertragsurkunde, vollständige Informationen und Widerrufsbelehrung. Bei356II erste Ware bei regelmäßigen Lieferungen, letzte Ware/Teilsendung bei den anderen dort genannten Mehrlieferfällen rechtlich zutreffend auswählen.356cV gegebenenfalls maßgeblichen Teilzeit-Wohnrechtevertrag zugrunde legen. Solange eine erforderliche Voraussetzung fehlt, keine künstliche Ersatzdatierung eingeben. Kein automatischer Belehrungs-/Form-/Widerrufsrechtsentscheid; frühzeitiges Erlöschen356V/VI gesondert. Gesetzliche Höchstfristen und anwendbare193-Korrektur separat, rechtzeitige Absendung355I gesondert.']
    return ergebnis


def widerruf_hoechstfristende(fristfall=None, bezugsereignistage=None, einordnungsnachweis=None):
    """Gesetzlichen Höchstfristbezug als spätesten Bezugstag wählen, drei oder zwölf Monate und danach14Tage addieren."""
    faelle = {'fernabsatz_aussergeschaeftlich_356':(12,1),'immobiliardarlehen_356b':(12,2),'teilzeitwohnrecht_informationen_356c':(3,2),'teilzeitwohnrecht_belehrung_356c':(12,2),'ratenlieferung_356d':(12,1),'verbraucherbau_356e':(12,1),'unentgeltliches_darlehen_356f':(12,2),'unentgeltliches_darlehen_ohne_unterrichtung_356f':(12,1)}
    _auswahl(fristfall,'fristfall',tuple(faelle));monate,anzahl = faelle[fristfall]
    bezug = _widerrufs_bezugstag(bezugsereignistage,'bezugsereignistage',anzahl)
    _text(einordnungsnachweis,'einordnungsnachweis')
    ende = _tage_addieren(_frist(bezug.isoformat(),monate,'monate','ereignis'),14)
    eingaben = dict(fristfall=fristfall,bezugsereignistage=bezugsereignistage,einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(dict(massgeblicher_bezugstag=bezug.isoformat(),hoechstfrist_monate=monate,hoechstfristende_ohne_kalenderkorrektur=ende.isoformat()),'daten_und_zahlen','BGB_WIDERRUF_HOECHSTFRISTENDE',eingaben,[dict(operation='Gesetzlichen Höchstfristbezug als spätesten Bezugstag wählen, drei oder zwölf Monate und danach14Tage addieren.')],eingaben.copy())
    ergebnis['hinweise'] = ['Feste lokale Fassung:356IV zwölfMonate+14Tage ab356II/355II2, nicht ab verspäteter Belehrung; bei Finanzdienstleistungen Ausnahme fehlender Belehrung356IV2 beachten, dann diesen Höchstfristfall nicht anwenden.356bII nur Immobiliardarlehen: späterer Vertragsschluss/Urkundenzeitpunkt356bI; keine pauschale Höchstfrist für Allgemeindarlehen.356c: späterer Vertrags-/Vorvertragsabschluss und Urkundenerhalt; dreiMonate+14Tage bei Informations-/Formblattmangel, zwölfMonate+14Tage bei Belehrungsmangel, letzterer auch bei beidem maßgeblich. Bei Urkunde bereits zum Abschluss denselben Tag zweimal angeben.356d/e: ein Bezugstag Vertragsschluss.356f: Bei tatsächlich erteilter Unterrichtung späteren Vertragsschluss/Unterrichtung verwenden, beide Tage müssen feststehen. Bei vollständig ausgebliebener Unterrichtung ausdrücklich unentgeltliches_darlehen_ohne_unterrichtung_356f wählen: nur tatsächlicher Vertragsschlusstag, zwölfMonate+14Tage. Dies ist keine fiktive Unterrichtung und startet keine14Tage-Regelfrist. Belegt durchBT-Drs18/7584S.141zur inhaltsgleichen früheren356d-Regelung. Vollständig fehlende Unterrichtung von unbekannter Informationslage unterscheiden. Ein bereits erloschenes Recht wird durch spätere Information nicht automatisch wiederbelebt; den Zwei-Ereignisfall nicht ungeprüft dafür verwenden. Regelwiderrufsfrist, frühzeitiges Erlöschen und gegebenenfalls193-Korrektur separat; Monatsanteil nicht eigenständig vor Addition der14Tage verschieben.']
    return ergebnis


def widerruf_fristenden_zusammenfuehren(regelfristende_am=None, hoechstfristende_am=None, einordnungsnachweis=None):
    """Früheres von Regelfristende und anwendbarem Höchstfristende bestimmen; fehlende berechenbare Enden ausdrücklich ausweisen."""
    regel = _datum(regelfristende_am,'regelfristende_am') if regelfristende_am is not None else None
    grenze = _datum(hoechstfristende_am,'hoechstfristende_am') if hoechstfristende_am is not None else None
    _text(einordnungsnachweis,'einordnungsnachweis')
    enden = [d for d in (regel,grenze) if d is not None]
    eingaben = dict(regelfristende_am=regelfristende_am,hoechstfristende_am=hoechstfristende_am,einordnungsnachweis=einordnungsnachweis)
    wert = dict(rechnerisch_bestimmbares_ende=min(enden).isoformat() if enden else None,regelfristende_vorhanden=regel is not None,hoechstfristende_vorhanden=grenze is not None)
    ergebnis = _ergebnis(wert,'datum_und_wahrheitswerte','BGB_WIDERRUF_FRISTENDEN_ZUSAMMENFUEHREN',eingaben,[dict(operation='Früheres von Regelfristende und anwendbarem Höchstfristende bestimmen; fehlende berechenbare Enden ausdrücklich ausweisen.')],eingaben.copy())
    ergebnis['hinweise'] = ['Nur zeitliche Kombination rechtlich vorqualifizierter Enddaten355/356–356f. Vorher gegebenenfalls einschlägige Kalenderkorrekturen wie193 für das jeweilige Ende vornehmen; rohe Fristdaten nicht ungeprüft als endgültige Erklärungstermine verwenden. NULL/None bedeutet ausdrücklich kein vorliegendes berechenbares Ende dieses Typs, nicht stillschweigend erfüllte Anfangsvoraussetzungen oder eine pauschale unbegrenzte Widerrufsmöglichkeit. Sind beide EndenNULL, bleibt das ErgebnisdatumNULL. Bei noch nicht begonnener Regelfrist kann eine qualifizierte Höchstfrist dennoch maßgeblich sein. Frühzeitiges Erlöschen, Anwendungsbereich, Form und rechtzeitige Absendung gesondert.']
    return ergebnis
