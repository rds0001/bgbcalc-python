"""Kauf-, Wiederkauf- und Vorkauf-Sonderbeträge mit qualifizierten Werten."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _multiplizieren, _dividieren, _bruch


def bau_nachtragsverguetung_differenz(erforderliche_mehrkosten=None, angemessene_zuschlaege_mehrkosten=None, entfallende_kosten=None, entfallende_zuschlaege=None, einordnungsnachweis=None):
    """Tatsächlich erforderliche Mehrkosten und angemessene Zuschläge addieren; entfallende Kosten und zugehörige entfallende Zuschläge abziehen."""
    werte = [_geld(erforderliche_mehrkosten), _geld(angemessene_zuschlaege_mehrkosten), _geld(entfallende_kosten), _geld(entfallende_zuschlaege)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(erforderliche_mehrkosten=erforderliche_mehrkosten, angemessene_zuschlaege_mehrkosten=angemessene_zuschlaege_mehrkosten, entfallende_kosten=entfallende_kosten, entfallende_zuschlaege=entfallende_zuschlaege, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(_addieren(werte[0],werte[1]),_addieren(werte[2],werte[3])), 'BGB_BAU_NACHTRAGSVERGUETUNG_DIFFERENZ', eingaben, [dict(operation='Tatsächlich erforderliche Mehrkosten und angemessene Zuschläge addieren; entfallende Kosten und zugehörige entfallende Zuschläge abziehen')])
    ergebnis['hinweise'].append('Nur qualifizierte Anordnung nach §650b Absatz2 und Berechnung nach §650c Absatz1; positiver Wert bedeutet Mehrvergütung, negativer Wert Vergütungsminderung. Die vier nichtnegativen Kostenkomponenten müssen in derselben Preisbasis ohne Doppelzählung vorliegen; Zuschläge für Geschäftskosten, Wagnis und Gewinn sind qualifizierte Geldbeträge, keine erfundenen Prozentsätze. Nach §650c Absatz1 Satz2 ausgeschlossener vermehrter Planungsaufwand darf nicht enthalten sein. Urkalkulationsmethode nach Absatz2, Fälligkeit und Abschlagsberechnung gesondert.')
    return ergebnis


def bau_nachtrag_vorlaeufiger_abschlagsansatz(angebotene_mehrverguetung=None, einordnungsnachweis=None):
    """Qualifizierte angebotene Mehrvergütung mit vier Fünfteln multiplizieren."""
    werte = [_geld(angebotene_mehrverguetung)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(angebotene_mehrverguetung=angebotene_mehrverguetung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_bruch(4,5)), 'BGB_BAU_NACHTRAG_VORLAEUFIGER_ABSCHLAGSANSATZ', eingaben, [dict(operation='Qualifizierte angebotene Mehrvergütung mit vier Fünfteln multiplizieren')])
    ergebnis['hinweise'].append('Nur gewählter zulässiger80%-Weg nach §650c Absatz3 Satz1; fehlende Einigung und gerichtliche Entscheidung rechtlich qualifizieren. Ergebnis ist der anzusetzende Nachtragsanteil, nicht automatisch eine fällige Gesamtabschlagszahlung. Bereits gezahlte Abschläge und §632a-Einbehalt sowie §650m-Grenzen separat anwenden. Keine80%-Kürzung der endgültigen geschuldeten Vergütung.')
    return ergebnis


def bau_nachtrag_ueberzahlungsbetrag(gezahlte_vorlaeufige_nachtragsverguetung=None, geschuldete_mehrverguetung=None, einordnungsnachweis=None):
    """Vorläufig gezahlte Nachtragsvergütung minus endgültig geschuldete Mehrvergütung, mindestens null."""
    werte = [_geld(gezahlte_vorlaeufige_nachtragsverguetung), _geld(geschuldete_mehrverguetung)]
    _text(einordnungsnachweis, 'einordnungsnachweis')
    eingaben = dict(gezahlte_vorlaeufige_nachtragsverguetung=gezahlte_vorlaeufige_nachtragsverguetung, geschuldete_mehrverguetung=geschuldete_mehrverguetung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_BAU_NACHTRAG_UEBERZAHLUNGSBETRAG', eingaben, [dict(operation='Vorläufig gezahlte Nachtragsvergütung minus endgültig geschuldete Mehrvergütung, mindestens null')])
    ergebnis['hinweise'].append('Nur Zahlungen nach §650c Absatz3 Satz1 und rechtlich feststehende nichtnegative Mehrvergütung nach Absatz1/2. Mehrfachzahlungen nur einmal summieren; echte Vergütungsminderungsfälle gesondert abrechnen. Überzahlungszinsen ab jeweiligem Zahlungseingang nach entsprechend §288 Absatz1 Satz2/Absatz2 ohne Zinseszins (§289 Satz1); vorhandene Zinskerne mit qualifizierter Überzahlungszuordnung und Datumsbasis separat verwenden, nicht pauschal gesamte Bruttozahlung verzinsen.')
    return ergebnis
