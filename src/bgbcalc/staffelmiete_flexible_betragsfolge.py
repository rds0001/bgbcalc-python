from .kalender import _ergebnis, _auswahl, _text, _vorhanden, _fehler
from .betraege import _geld
from .zahlen import _subtrahieren
from .zinsen import _bruchteile
from .staffelmietzeit import staffelmiete_mindestabstaende

def staffelmiete_flexible_betragsfolge(staffeln=None, schutzmodell=None, einordnungsnachweis=None):
    """Vereinbarte Staffelbeträge mit aktueller Grenze und rechtlich gewähltem historischen Schutz vergleichen, ohne niedrigere Vereinbarung anzuheben."""
    _vorhanden(staffeln,'staffeln');_text(einordnungsnachweis,'einordnungsnachweis');_auswahl(schutzmodell,'schutzmodell',('hoechste_wirksame_vorstaffel','unmittelbar_vorherige_staffel'))
    if not isinstance(staffeln,list) or not 2<=len(staffeln)<=1000:_fehler('staffeln','Liste2..1000erforderlich.')
    daten=[];betraege=[]
    for s in staffeln:
        if not isinstance(s,dict) or set(s)!={'staffelbeginn_am','vereinbarte_monatsmiete','zulaessige_monatsmiete_ohne_vorstaffelschutz'}:_fehler('staffeln','Genau Beginn,Vereinbarungsbetrag und Grenze erforderlich.')
        daten.append(s['staffelbeginn_am']);betraege.append((_geld(s['vereinbarte_monatsmiete']),_geld(s['zulaessige_monatsmiete_ohne_vorstaffelschutz'])))
    if not staffelmiete_mindestabstaende(daten,einordnungsnachweis)['wert']['alle_jahresabstaende_eingehalten']:_fehler('staffeln','Gültige Jahresabstände erforderlich.')
    schutz=_geld('0');wert=[]
    for datum,(vereinbart,grenze) in zip(daten,betraege):
        grenze=max(grenze,schutz);miete=min(vereinbart,grenze)
        wert.append(dict(staffelbeginn_am=datum,rechnerische_monatsgrenze=_bruchteile(grenze),rechnerische_monatsmiete=_bruchteile(miete),monatlicher_ueberhoehungsbetrag=_bruchteile(_subtrahieren(vereinbart,miete))))
        schutz=max(schutz,miete) if schutzmodell=='hoechste_wirksame_vorstaffel' else miete
    eingaben = dict(staffeln=staffeln, schutzmodell=schutzmodell, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_STAFFELMIETE_FLEXIBLE_BETRAGSFOLGE',eingaben,[dict(operation='Vereinbarte Staffelbeträge mit aktueller Grenze und rechtlich gewähltem historischen Schutz vergleichen, ohne niedrigere Vereinbarung anzuheben.')],eingaben.copy())
    ergebnis["hinweise"] = ['Jede vereinbarte Staffel wird nur nach oben durch ihre individuelle556d–g-Grenze samt qualifiziertem Vorstaffelschutz begrenzt. Geschützte frühere Miete darf eine niedriger vereinbarte Miete nicht erhöhen. Modell höchste_wirksame_Vorstaffel hält den höchsten tatsächlich zulässigen früheren Betrag; Modell unmittelbar_vorherige_Staffel schreibt nur den zuletzt wirksam begründeten Betrag fort. Rechtliche Fortgeltung bei sinkenden/neu vereinbarten Beträgen ist ausdrücklich vorzugeben, keine allgemeine Entscheidung dieser Auslegungsfrage. In keiner Variante anfänglich unzulässige Überhöhung schützen. Eine rechtlich eigenständige neue Folge gesondert rechnen und etwaiges556e-Vormietprivileg mit vorhandenem Vormietkern bestimmen; nicht ungeprüft historischen Höchstwert übertragen. Mindestjahresabstände mit vorhandenem Kalenderkern.556g-Auskunft/Privilegnutzbarkeit und Rüge gesondert; keine automatische10%-Grenze ohne556e-Ausnahmen.']
    return ergebnis

