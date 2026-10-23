from .betraege import _geld, _geld_ergebnis, _wahrheitswert
from .kalender import _auswahl, _ergebnis, _fehler, _text
from .zahlen import _addieren, _bruch, _subtrahieren, _zahleneingabe
from .zinsen import _bruchteile


def kleinbetragsinstrument_betragsgrenze(grenzfall=None, massgeblicher_betrag=None, ausschliesslich_inland=None, einordnungsnachweis=None):
    """Qualifizierte Instrumentenbeträge mit30,150oder200EUR vergleichen."""
    _auswahl(grenzfall,'grenzfall',('einzelzahlung','ausgabenobergrenze','speicherobergrenze','egeld_sperrausnahme'))
    betrag=_geld(massgeblicher_betrag);_text(einordnungsnachweis,'einordnungsnachweis')
    if grenzfall in ('ausgabenobergrenze','speicherobergrenze'):
        _wahrheitswert(ausschliesslich_inland,'ausschliesslich_inland');grenze=200 if ausschliesslich_inland else 150
    else:
        if ausschliesslich_inland is not None:
            _fehler('ausschliesslich_inland','Bei Einzelzahlung oder E-Geld-Sperrausnahme keine ungenutzte Inlandsauswahl eingeben.')
        grenze=30 if grenzfall=='einzelzahlung' else 200
    eingaben=dict(grenzfall=grenzfall,massgeblicher_betrag=massgeblicher_betrag,ausschliesslich_inland=ausschliesslich_inland,einordnungsnachweis=einordnungsnachweis)
    wert=dict(betragsgrenze_euro=_bruchteile(_bruch(grenze)),grenze_eingehalten=betrag<=grenze,ueberschreitungsbetrag=_bruchteile(max(_subtrahieren(betrag,_bruch(grenze)),_bruch(0))))
    ergebnis=_ergebnis(wert,'EUR_und_wahrheitswert','BGB_KLEINBETRAGSINSTRUMENT_BETRAGSGRENZE',eingaben,[dict(operation='Anwendbare Betragsgrenze auswählen, einschließlich Gleichheit vergleichen und positiven Überschreitungsbetrag bestimmen.')],eingaben.copy())
    ergebnis['hinweise']=['§675iI: Einzelzahlungslimit höchstens30EUR; Ausgaben-/Speicherobergrenze150EUR, nur bei ausschließlich möglichen inländischen Vorgängen200EUR. Maßgeblich ist die rechtlich vorgesehene Instrumentengrenze, nicht ein zufällig kleiner Einzelumsatz; Speicherbetrag darf die Grenze zu keiner Zeit überschreiten. Drei alternative Instrumentenwege, kein kumulatives Erfordernis aller Grenzen. egeld_sperrausnahme betrifft nur die200EUR-Wertgrenze675iIII; fehlende Sperrmöglichkeit und übrige Voraussetzungen separat. Kein automatischer Ausschluss sämtlicher Zahlungsdienste-Schutzregeln aus einem positiven Zahlenvergleich; Vereinbarungen und spezifische Bedingungen675iII/III prüfen.']
    return ergebnis


def zahlung_sonstiger_schadenbetrag(begrenzbarer_schaden=None, nicht_begrenzbarer_schaden=None, vereinbarte_haftungsgrenze=None, einordnungsnachweis=None):
    """Qualifizierten sonstigen Zahlungsschaden begrenzen und nicht begrenzbare Anteile ungekürzt addieren."""
    begrenzbar=_geld(begrenzbarer_schaden);unbegrenzt=_geld(nicht_begrenzbarer_schaden);_text(einordnungsnachweis,'einordnungsnachweis')
    grenze=None if vereinbarte_haftungsgrenze is None else _geld(vereinbarte_haftungsgrenze)
    if grenze is not None and grenze<12500:
        _fehler('vereinbarte_haftungsgrenze','Grenze nach675z darf12500EUR nicht unterschreiten; keine Heilung unwirksamer Vereinbarung durch Kürzung.')
    wert=_addieren(begrenzbar if grenze is None else min(begrenzbar,grenze),unbegrenzt)
    eingaben=dict(begrenzbarer_schaden=begrenzbarer_schaden,nicht_begrenzbarer_schaden=nicht_begrenzbarer_schaden,vereinbarte_haftungsgrenze=vereinbarte_haftungsgrenze,einordnungsnachweis=einordnungsnachweis)
    ergebnis=_geld_ergebnis(wert,'BGB_ZAHLUNG_SONSTIGER_SCHADENBETRAG',eingaben,[dict(operation='Nur begrenzbaren Schaden auf wirksam vereinbarte Grenze begrenzen; nicht begrenzbare Komponenten ungekürzt hinzurechnen. Ohne Vereinbarung keine gesetzliche Automatikkappung.')])
    ergebnis['hinweise'].append('§675z: nur sonstiger Schaden außerhalb bereits von675y erfasster Ansprüche. Keine Doppelzählung mit Zahlungsbetrag, Entgelten oder Zinsen nach675y. Vereinbarte Grenze optional; null bedeutet keine Begrenzungsvereinbarung, nicht automatisch12500EUR. Vorsatz, grobe Fahrlässigkeit, Zinsschaden und besonders übernommene Gefahren dürfen nicht in den begrenzbaren Anteil eingehen. Bei insgesamt vorsätzlicher/grob fahrlässiger Ausführung gesamten qualifizierten Schaden als nicht begrenzbar zuordnen. Wirksamkeit der Vereinbarung, Haftungszurechnung, fehlerhafte Kundenkennung und Sonderrecht extern bestimmen.')
    return ergebnis


def zahlung_kontoberichtigung(regelfall=None, aktueller_kontostand=None, fehlerhafte_belastung=None, bereits_korrigierter_betrag=None, einordnungsnachweis=None):
    """Noch nicht korrigierten Fehlbelastungsbetrag zum aktuellen Kontostand addieren."""
    _auswahl(regelfall,'regelfall',('nichtautorisiert_675u','ausfuehrungsfehler_675y'))
    stand=_zahleneingabe(aktueller_kontostand);belastung=_geld(fehlerhafte_belastung);korrigiert=_geld(bereits_korrigierter_betrag);_text(einordnungsnachweis,'einordnungsnachweis')
    if korrigiert>belastung:
        _fehler('bereits_korrigierter_betrag','Bereits korrigierter Teil darf die betrachtete Fehlbelastung nicht übersteigen.')
    rest=_subtrahieren(belastung,korrigiert)
    eingaben=dict(regelfall=regelfall,aktueller_kontostand=aktueller_kontostand,fehlerhafte_belastung=fehlerhafte_belastung,bereits_korrigierter_betrag=bereits_korrigierter_betrag,einordnungsnachweis=einordnungsnachweis)
    wert=dict(noch_zu_korrigierender_betrag=_bruchteile(rest),berichtigter_kontostand=_bruchteile(_addieren(stand,rest)))
    ergebnis=_ergebnis(wert,'EUR','BGB_ZAHLUNG_KONTOBERICHTIGUNG',eingaben,[dict(operation='Fehlbelastung um bereits im aktuellen Kontostand berücksichtigte Korrektur vermindern; verbleibenden Betrag einmal gutschreiben.')],eingaben.copy())
    ergebnis['hinweise']=['§675u beziehungsweise675yI/II/IV: isolierte rechnerische Rückgängigmachung der qualifizierten Fehlbelastung. Aktueller Kontostand darf negativ sein und muss bereits_korrigierter_betrag bereits enthalten; andere Kontobewegungen bleiben unberührt. Kein mehrfaches Erstatten derselben Belastung. Anspruchsvoraussetzungen, Haftungsausnahmen und675u-Betrugsverdachtsfall extern klären. Wertstellung, gesonderte Entgelte/Zinsen675yVI und Folgeschäden675z separat; diese Rechnung allein bildet noch keine vollständige rückwirkende Kontorekonstruktion.']
    return ergebnis
