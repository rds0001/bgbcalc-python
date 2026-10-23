from .kalender import _ergebnis, _text, _auswahl, _fehler
from .betraege import _geld
from .zahlen import _bruch, _subtrahieren
from .zinsen import _bruchteile
from .quotenverteilung import _begrenzte_quotenverteilung
from .gesamthypothek_nichtnegative_nettowertanteile import gesamthypothek_nichtnegative_nettowertanteile
from .gesamthypothek_regressanrechnung import gesamthypothek_regressanrechnung

def gesamthypothek_regress_restverteilung(gesamthypothekenbetrag=None, uebergegangener_regressbetrag=None, grundstuecke=None, ersatzpflichtiges_grundstueck_id=None, verteilungsmodell=None, methodennachweis=None):
    """Teilübergang abziehen,1174-Anrechnung auf Restquote ausführen und übrige Masse unter ausdrücklich vorgegebenem Modell den anderen Eigentümern proportional zuweisen."""
    gesamt=_geld(gesamthypothekenbetrag);regress=_geld(uebergegangener_regressbetrag);name=_text(ersatzpflichtiges_grundstueck_id,'ersatzpflichtiges_grundstueck_id');_auswahl(verteilungsmodell,'verteilungsmodell',('restquotierung_mit_anteiliger_restzuweisung',));_text(methodennachweis,'methodennachweis')
    if regress>gesamt:_fehler('uebergegangener_regressbetrag','Teilübergang höchstens Gesamtbetrag.')
    rest=_subtrahieren(gesamt,regress);basis=gesamthypothek_nichtnegative_nettowertanteile(_bruchteile(rest),grundstuecke,'positive_nettowerte',methodennachweis)['wert']
    if not basis['quoten_bestimmbar']:_fehler('grundstuecke','Keine positive Quotierungsbasis; Nettowertdiagnose separat verwenden.')
    namen=[p['grundstueck_id'] for p in basis['anteile']]
    if name not in namen:_fehler('ersatzpflichtiges_grundstueck_id','Grundstück muss enthalten sein.')
    i=namen.index(name);quote=basis['anteile'][i]['anteilsquote'];anrechnung=gesamthypothek_regressanrechnung(_bruchteile(rest),quote,_bruchteile(regress),methodennachweis)['wert'];eigen=_geld(anrechnung['verbleibender_anteil']);offen=_subtrahieren(rest,eigen)
    gewichte=[_geld(p['verteilungsgewicht']) if j!=i else _bruch(0) for j,p in enumerate(basis['nettowerte'])]
    anteile,nicht=_begrenzte_quotenverteilung(offen,gewichte,[offen for _ in gewichte]);anteile[i]=eigen
    wert=dict(uebergegangener_regressbetrag=_bruchteile(regress),verbleibende_gemeinschaftsmasse=_bruchteile(rest),eigentuemeranteile=[dict(grundstueck_id=k,hypothekenanteil=_bruchteile(x)) for k,x in zip(namen,anteile)],nicht_zugewiesener_restbetrag=_bruchteile(nicht))
    eingaben = dict(gesamthypothekenbetrag=gesamthypothekenbetrag, uebergegangener_regressbetrag=uebergegangener_regressbetrag, grundstuecke=grundstuecke, ersatzpflichtiges_grundstueck_id=ersatzpflichtiges_grundstueck_id, verteilungsmodell=verteilungsmodell, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'EUR','BGB_GESAMTHYPOTHEK_REGRESS_RESTVERTEILUNG',eingaben,[dict(operation='Teilübergang abziehen,1174-Anrechnung auf Restquote ausführen und übrige Masse unter ausdrücklich vorgegebenem Modell den anderen Eigentümern proportional zuweisen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingtes vollständiges Rechenmodell: Restmasse=Gesamtbetrag-Regressübergang.1172-Nettogewichte mit vorhandener positiver Nettowertmethode bestimmen.1174II-Anrechnung des Übergangs auf den quotierten Restanteil des ersatzpflichtigen Eigentümers durch vorhandenen Anrechnungskern. Verbleibende Restmasse proportional nach positiven Nettogewichten der übrigen Eigentümer verteilen. Dieses zusätzliche Zuweisungsmodell ist eine ausdrücklich zu qualifizierende Voraussetzung, keine aus dem Normwortlaut allein gesicherte generelle Auslegung. Ohne andere positive Gewichte bleibt der nicht zuweisbare Betrag sichtbar; keine künstliche Kopfquote oder Rückzuweisung entgegen der gewählten Anrechnung. Bei völlig fehlender positiver Nettowertbasis Eingabe ablehnen und separate Nettowertdiagnose verwenden. Summe Übergang+Eigentümeranteile+nichtzugewiesen=Gesamtbetrag.1176/1182-Rangschutz ist zusätzlich rechtlich zu beachten und wird nicht als allgemeiner ZVG-Verteilungsalgorithmus erfunden.']
    return ergebnis

