from .kalender import _datum, _ergebnis, _fehler, _frist, _text
from .betraege import _geld
from .zahlen import _bruch, _multiplizieren
from .zinsen import _bruchteile

def grundstuecksrente_jahresabrechnung(jahresrentenbetrag=None, rentenjahr_beginnt_am=None, berechtigungszeitraum_von=None, berechtigungszeitraum_bis=None, einordnungsnachweis=None):
    """Rentenjahr ab Tagesbeginn bestimmen; Schnittmenge mit Berechtigungszeitraum zählen und Jahresbetrag nach tatsächlichen Tagen zuordnen."""
    rente=_geld(jahresrentenbetrag);beginn=_datum(rentenjahr_beginnt_am,'rentenjahr_beginnt_am');von=_datum(berechtigungszeitraum_von,'berechtigungszeitraum_von');bis=_datum(berechtigungszeitraum_bis,'berechtigungszeitraum_bis');_text(einordnungsnachweis,'einordnungsnachweis')
    if bis<von: _fehler('berechtigungszeitraum_bis','Ende darf nicht vor Beginn liegen.')
    ende=_frist(rentenjahr_beginnt_am,1,'jahre','tagesbeginn');tage=(ende-beginn).days+1;anteiltage=max(0,(min(ende,bis)-max(beginn,von)).days+1)
    anteil=_multiplizieren(rente,_bruch(anteiltage,tage))
    wert=dict(rentenjahr_endet_am=ende.isoformat(),regel_vorauszahlung_am=beginn.isoformat(),tage_im_rentenjahr=tage,zugeordnete_tage=anteiltage,jahresvorauszahlungsbetrag=_bruchteile(rente),zeitanteilig_zugeordneter_betrag=_bruchteile(anteil))
    eingaben = dict(jahresrentenbetrag=jahresrentenbetrag, rentenjahr_beginnt_am=rentenjahr_beginnt_am, berechtigungszeitraum_von=berechtigungszeitraum_von, berechtigungszeitraum_bis=berechtigungszeitraum_bis, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _ergebnis(wert,'daten_tage_und_eur','BGB_GRUNDSTUECKSRENTE_JAHRESABRECHNUNG',eingaben,[dict(operation='Rentenjahr ab Tagesbeginn bestimmen; Schnittmenge mit Berechtigungszeitraum zählen und Jahresbetrag nach tatsächlichen Tagen zuordnen.')],eingaben.copy())
    ergebnis["hinweise"] = ['Gesetzlicher Jahresvorauszahlungsfall §§913II/917II; Jahresrentenhöhe und Ausgangstag rechtlich bestimmt. §101Nr2 zeitanteilige Zuordnung regelmäßig wiederkehrender Erträge bei begrenztem Bezugszeitraum; tatsächliche Kalendertage der Schnittmenge durch tatsächliche Tage des Rentenjahrs teilen. Kein pauschales365-Tage-Jahr und keine Übernahme der Sonderregel voller begonnener Leibrentenperioden aus§760. §915I Grundstückswert ist historische Bewertung, kein von der Bibliothek geschätzter Preis; bis zur rechtlich bestimmten Übertragung bleibt die Rentenpflicht nachII maßgeblich. Jahresvorauszahlungsbetrag und zugeordneter Zeitanteil getrennt: keine automatische Rückforderung bereits bezahlter Beträge oder doppelte zusätzliche Forderung. Andere Eigentümer getrennt mit überschneidungsfreien Berechtigungszeiten abrechnen.']
    return ergebnis

