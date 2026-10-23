from .kalender import _datum, _ergebnis, _fehler, _auswahl, _text
from .rueckwaertsfrist_kalendergrenze import rueckwaertsfrist_kalendergrenze
from .hoehere_gewalt_fenster import verjaehrung_hoehere_gewalt_fenster

def verjaehrung_hoehere_gewalt_festes_ablauffenster(fristlauf_erster_tag=None, fristende_ohne_diese_hemmung=None, verhinderungszeitraeume=None, fenstermodell=None, monatsendregel=None, methodennachweis=None):
    """Festes rechtlich ausgewähltes Sechsmonatsfenster aus Ausgangsablauf berechnen, auf tatsächlichen Fristlauf begrenzen und bestehende206/209-Schnittmengenrechnung anwenden."""
    a=_datum(fristlauf_erster_tag,'fristlauf_erster_tag');e=_datum(fristende_ohne_diese_hemmung,'fristende_ohne_diese_hemmung');_auswahl(fenstermodell,'fenstermodell',('fester_ablauf_ohne_206',));_text(methodennachweis,'methodennachweis')
    if a>e:_fehler('fristlauf','Erster Fristtag liegt nach Ausgangsende.')
    g=rueckwaertsfrist_kalendergrenze(fristende_ohne_diese_hemmung,6,'monate','tagesende',monatsendregel,methodennachweis)['wert']['grenztag_beginn']
    von=max(a,_datum(g,'fensterbeginn')).isoformat()
    r=verjaehrung_hoehere_gewalt_fenster(fristlauf_erster_tag,fristende_ohne_diese_hemmung,von,fristende_ohne_diese_hemmung,verhinderungszeitraeume,methodennachweis)['wert']
    wert=dict(fenster_erster_tag=von,fenster_letzter_tag=fristende_ohne_diese_hemmung,rechnerischer_letzter_tag=r['rechnerischer_letzter_tag'],beruecksichtigte_hemmungstage=r['beruecksichtigte_hemmungstage'])
    eingaben = dict(fristlauf_erster_tag=fristlauf_erster_tag, fristende_ohne_diese_hemmung=fristende_ohne_diese_hemmung, verhinderungszeitraeume=verhinderungszeitraeume, fenstermodell=fenstermodell, monatsendregel=monatsendregel, methodennachweis=methodennachweis)
    ergebnis = _ergebnis(wert,'daten_und_tage','BGB_VERJAEHRUNG_HOEHERE_GEWALT_FESTES_ABLAUFFENSTER',eingaben,[dict(operation='Festes rechtlich ausgewähltes Sechsmonatsfenster aus Ausgangsablauf berechnen, auf tatsächlichen Fristlauf begrenzen und bestehende206/209-Schnittmengenrechnung anwenden.')],eingaben.copy())
    ergebnis["hinweise"] = ['Bedingte vollständige206-Fensterarithmetik für das ausdrücklich gewählte feste Ablaufmodell. Sechs Kalendermonate vom Tagesende der Ausgangsfrist rückwärts, Fensterbeginn ist Grenztagesbeginn, frühestens erster Fristlauftag. Verhinderungsintervalle schneiden, Überschneidungen vereinigen und209-Tage fortschreiben. Kein vom Nutzer vorberechneter Fensterbeginn erforderlich. LGRegensburg18.6.2026,45O1916/24,Rn35–37 stützt im dortigen Fall Begrenzung auf festen Zeitraum bis zum Ablauf ohne206; keine Behauptung höchstrichterlicher oder universeller Freigabe. Keine automatische dynamische Fensterverschiebung; deren ursprüngliche Inventarbezeichnung war eine offene Hypothese, kein belegter gesetzlicher Algorithmus. Hindernisse außerhalb des festen Fensters werden in diesem Modell nicht erfasst. Ein fortdauerndes Hindernis ohne rechtlich feststehendes Ende erlaubt keinen endgültigen Ablauf. Weitere Hemmungen nicht doppelt zählen;210/211,Neubeginn und gegebenenfalls193 anschließend gesondert qualifizieren.']
    return ergebnis

