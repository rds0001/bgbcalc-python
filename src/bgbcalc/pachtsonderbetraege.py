"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def pacht_inventar_ausgleichsdifferenz(uebernommener_gesamtschaetzwert_zu_endpreisen=None, zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen=None, einordnungsnachweis=None):
    """Gesamtschätzwert des übernommenen Inventars minus Gesamtschätzwert des zurückzugewährenden Inventars, beide zu Preisen bei Pachtende."""
    werte = [_geld(uebernommener_gesamtschaetzwert_zu_endpreisen), _geld(zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(uebernommener_gesamtschaetzwert_zu_endpreisen=uebernommener_gesamtschaetzwert_zu_endpreisen, zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen=zurueckzugewaehrender_gesamtschaetzwert_zu_endpreisen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(werte[0],werte[1]), 'BGB_PACHT_INVENTAR_AUSGLEICHSDIFFERENZ', eingaben, [dict(operation='Gesamtschätzwert des übernommenen Inventars minus Gesamtschätzwert des zurückzugewährenden Inventars, beide zu Preisen bei Pachtende')])
    ergebnis['hinweise'].append('§582a Absatz3 bei qualifizierter Inventarübernahme/-rückgewähr zum Schätzwert; entsprechend §590 Absatz3 bei qualifizierter wesentlicher Inventarverminderung während der Pachtzeit ohne gesetzliche Verwendungsausnahme. Im letzteren Fall sind Endpreise die einheitlichen Preise des rechtlich maßgeblichen Zwischenabrechnungszeitpunkts; der zweite Bestand ist das dort verbleibende Inventar, nicht ein erfundener künftiger Rückgabebestand. Positives Ergebnis bezeichnet Ausgleich vom Pächter an Verpächter, negatives Ergebnis den Betrag mit umgekehrter Richtung, null keinen Wertausgleich. Beide Inventarbestände mit Preisen desselben maßgeblichen Abrechnungszeitpunkts bewerten, nicht historische Anfangspreise gegen aktuelle Endpreise. Rechtlich wirksam abgelehnte überflüssige/überwertige Stücke zuvor aus dem zurückzugewährenden Bestand ausschließen. Keine Inventarbewertung, Eigentumsentscheidung oder zusätzliche Schadensersatzrechnung.')
    return ergebnis


def pacht_holzmehrnutzung_wertersatz(eingeschlagene_holzmenge=None, ordnungsgemaess_zulaessige_holzmenge=None, wert_je_mengeneinheit=None, einordnungsnachweis=None):
    """Positive Mehrmenge des Holzeinschlags gegenüber ordnungsgemäß zulässiger Menge mit qualifiziertem Wert je gleicher Mengeneinheit multiplizieren."""
    werte = [_geld(eingeschlagene_holzmenge), _geld(ordnungsgemaess_zulaessige_holzmenge), _geld(wert_je_mengeneinheit)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(eingeschlagene_holzmenge=eingeschlagene_holzmenge, ordnungsgemaess_zulaessige_holzmenge=ordnungsgemaess_zulaessige_holzmenge, wert_je_mengeneinheit=wert_je_mengeneinheit, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(max(_subtrahieren(werte[0],werte[1]),_bruch(0)),werte[2]), 'BGB_PACHT_HOLZMEHRNUTZUNG_WERTERSATZ', eingaben, [dict(operation='Positive Mehrmenge des Holzeinschlags gegenüber ordnungsgemäß zulässiger Menge mit qualifiziertem Wert je gleicher Mengeneinheit multiplizieren')])
    ergebnis['hinweise'].append('Nur §596a Absatz3 Satz2. Mengen beziehen sich auf denselben rechtlich maßgeblichen Nutzungsumfang, Zeitraum und dieselbe Holzeinheit/-qualität; zulässige ordnungsgemäße Nutzung und Wert extern qualifizieren. Bei verschiedenen Sortimenten oder Wertstufen getrennte überschneidungsfreie Positionen rechnen, keine pauschale Preisannahme. Weiterer Schaden gesondert ohne Doppelzählung. Nicht Ernte-/Holzwertersatz für noch nicht getrennte Früchte nach Absatz1–3Satz1.')
    return ergebnis
