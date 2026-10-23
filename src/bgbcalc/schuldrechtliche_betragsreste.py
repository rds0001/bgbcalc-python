"""Nettobeträge und gesetzliche Anrechnungsreste nach §§252,675qII,776."""
from .betraege import _geld, _geld_ergebnis
from .kalender import _text, _fehler
from .zahlen import _addieren, _subtrahieren, _bruch, _multiplizieren


def entgangener_gewinn_nettobetrag(erwartbare_erloese=None, zugehoerige_aufwendungen=None, einordnungsnachweis=None):
    """Erwartbare Erlöse um zugehörige Aufwendungen vermindern; positiver Nettogewinn mindestens null."""
    werte = [_geld(erwartbare_erloese), _geld(zugehoerige_aufwendungen)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(erwartbare_erloese=erwartbare_erloese, zugehoerige_aufwendungen=zugehoerige_aufwendungen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_ENTGANGENER_GEWINN_NETTOBETRAG', eingaben, [dict(operation='Erwartbare Erlöse um zugehörige Aufwendungen vermindern; positiver Nettogewinn mindestens null.')])
    ergebnis["hinweise"].append('§252: rein rechnerische Nettogewinnermittlung aus qualifizierter kontrafaktischer Basis. Wahrscheinlichkeit, Kausalität und Bewertungsansatz werden nicht ermittelt. Kein zusätzlicher Anspruch auf Erlös und Nettogewinn zugleich; weitere Vorteile, tatsächlich verbleibende Erträge, Mitverschulden und Schadensminderung getrennt berücksichtigen. Negative Marge begründet hier keinen entgangenen Gewinn; kein vollständiger Schadensersatzbetrag.')
    return ergebnis


def zahlung_empfaengerentgelt_restbetrag(vollstaendiger_zahlungsbetrag=None, vereinbartes_empfaengerentgelt=None, einordnungsnachweis=None):
    """Vollständigen Zahlungsbetrag um das zulässige vereinbarte Empfängerentgelt vermindern."""
    werte = [_geld(vollstaendiger_zahlungsbetrag), _geld(vereinbartes_empfaengerentgelt)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if werte[1] > werte[0]:
        _fehler('vereinbartes_empfaengerentgelt','Abzugsbetrag darf den verfügbaren Zahlungsbetrag nicht übersteigen.')
    eingaben = dict(vollstaendiger_zahlungsbetrag=vollstaendiger_zahlungsbetrag, vereinbartes_empfaengerentgelt=vereinbartes_empfaengerentgelt, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(werte[0],werte[1]), 'BGB_ZAHLUNG_EMPFAENGERENTGELT_RESTBETRAG', eingaben, [dict(operation='Vollständigen Zahlungsbetrag um das zulässige vereinbarte Empfängerentgelt vermindern.')])
    ergebnis["hinweise"].append('§675qII-Grundfall, vor Erteilung der Gutschrift vereinbarter Abzug eines zustehenden Entgelts. Vollständiger Zahlungsbetrag und Entgelt bleiben in eingaben und nutzervorgaben getrennt dokumentiert; gesetzliche Zahlungsinformationen müssen sie separat ausweisen. Keine Kürzung durch zwischengeschaltete Stellen nachAbsatz1, keine Entgeltberechnung und keine Abweichung nachAbsatz4. Entgelt über Zahlungsbetrag und gesonderte Kontobelastungen außerhalb dieses Modells.')
    return ergebnis


def buergschaft_regressverlust_restbetrag(buergschaftsverbindlichkeit=None, verlorener_erlangbarer_regress=None, einordnungsnachweis=None):
    """Offene Bürgschaftsverbindlichkeit um erlangbaren verlorenen Regress mindern, mindestens null."""
    werte = [_geld(buergschaftsverbindlichkeit), _geld(verlorener_erlangbarer_regress)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(buergschaftsverbindlichkeit=buergschaftsverbindlichkeit, verlorener_erlangbarer_regress=verlorener_erlangbarer_regress, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_BUERGSCHAFT_REGRESSVERLUST_RESTBETRAG', eingaben, [dict(operation='Offene Bürgschaftsverbindlichkeit um erlangbaren verlorenen Regress mindern, mindestens null.')])
    ergebnis["hinweise"].append('§776: Maßgeblich ist der erlangbare Ersatz aus dem aufgegebenen Recht, nicht automatisch dessen Nominalwert. Verwertbarkeit, Rang, Mitbürgenquote und weitere Bedingungen vorqualifizieren. Keine automatische Auslegung einer wirksamen Rechtsaufgabe oder kumulative Anrechnung gleicher Sicherheiten. Ergebnis ist verbleibende betragsmäßige Bürgschaftsbindung vor weiteren Einreden; überschießender Regresswert begründet hier keine Forderung des Bürgen.')
    return ergebnis


def annahmeverzug_mehraufwendungsbetrag(mehraufwand_erfolgloses_angebot=None, mehraufwand_aufbewahrung=None, mehraufwand_erhaltung=None, einordnungsnachweis=None):
    """Erforderliche zusätzliche Aufwendungen für erfolgloses Angebot, Aufbewahrung und Erhaltung addieren."""
    werte = [_geld(mehraufwand_erfolgloses_angebot), _geld(mehraufwand_aufbewahrung), _geld(mehraufwand_erhaltung)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(mehraufwand_erfolgloses_angebot=mehraufwand_erfolgloses_angebot, mehraufwand_aufbewahrung=mehraufwand_aufbewahrung, mehraufwand_erhaltung=mehraufwand_erhaltung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(_addieren(werte[0],werte[1]),werte[2]), 'BGB_ANNAHMEVERZUG_MEHRAUFWENDUNGSBETRAG', eingaben, [dict(operation='Erforderliche zusätzliche Aufwendungen für erfolgloses Angebot, Aufbewahrung und Erhaltung addieren.')])
    ergebnis["hinweise"].append('§304: nur rechtlich zugeordnete erforderliche Mehraufwendungen infolge des Annahmeverzugs; keine pauschale Bewertung von Arbeitszeit oder ohnehin angefallenen Kosten. Kostenpositionen überschneidungsfrei den drei Gruppen zuordnen; dieselbe Rechnung nur einmal erfassen. Grundvoraussetzungen des Annahmeverzugs sowie weitergehende Schadensersatzansprüche werden nicht ermittelt.')
    return ergebnis


def anweisung_schuldrest_nach_leistung(schuld_vor_leistung=None, tatsaechlich_geleisteter_betrag=None, einordnungsnachweis=None):
    """Offene Anweisungsschuld um tatsächlich bewirkte zugeordnete Leistung mindern, mindestens null."""
    werte = [_geld(schuld_vor_leistung), _geld(tatsaechlich_geleisteter_betrag)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(schuld_vor_leistung=schuld_vor_leistung, tatsaechlich_geleisteter_betrag=tatsaechlich_geleisteter_betrag, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_ANWEISUNG_SCHULDREST_NACH_LEISTUNG', eingaben, [dict(operation='Offene Anweisungsschuld um tatsächlich bewirkte zugeordnete Leistung mindern, mindestens null.')])
    ergebnis["hinweise"].append('§787I: nur Betrag der Schuld des Angewiesenen gegenüber dem Anweisenden im qualifizierten Deckungsverhältnis. §788 trennt bloße Annahme von tatsächlicher Leistung im Valutaverhältnis; die Annahme allein wird nicht als Zahlung eingestellt. Andere Schuldverhältnisse nicht vermischen. Überschießende Zahlung begründet hier weder negative Schuld noch automatisch einen Rückforderungsanspruch.')
    return ergebnis


def zahlungsinstrument_ersatzentgelt_grenze(vereinbartes_ersatzentgelt=None, unmittelbare_ersatzkosten=None, einordnungsnachweis=None):
    """Numerisch auf die ausschließlich unmittelbaren Ersatzkosten begrenztes Entgelt: Minimum aus vereinbartem Entgelt und Kosten."""
    werte = [_geld(vereinbartes_ersatzentgelt), _geld(unmittelbare_ersatzkosten)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(vereinbartes_ersatzentgelt=vereinbartes_ersatzentgelt, unmittelbare_ersatzkosten=unmittelbare_ersatzkosten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte[0],werte[1]), 'BGB_ZAHLUNGSINSTRUMENT_ERSATZENTGELT_GRENZE', eingaben, [dict(operation='Numerisch auf die ausschließlich unmittelbaren Ersatzkosten begrenztes Entgelt: Minimum aus vereinbartem Entgelt und Kosten.')])
    ergebnis["hinweise"].append('§675lI: ausschließlich numerische Entgeltobergrenze für Ersatz nach Verlust, Diebstahl, Missbrauch oder sonst nicht autorisierter Nutzung. Das Minimum heilt keine unwirksame Entgeltvereinbarung und entscheidet keinen Zahlungsanspruch; Wirksamkeit und Rechtsfolgen einer überschießenden Klausel gesondert. Kosten müssen dem konkreten Ersatz unmittelbar und ausschließlich zurechenbar sein; kein allgemeines Entgelt für Sperrung oder Anzeige.')
    return ergebnis


def buergschaft_forderungsuebergang_betrag(offene_hauptforderung=None, befriedigung_durch_buergen=None, einordnungsnachweis=None):
    """Numerischer Forderungsübergang: Minimum aus noch bestehender erfasster Hauptforderung und darauf bewirkter Befriedigung durch den Bürgen."""
    werte = [_geld(offene_hauptforderung), _geld(befriedigung_durch_buergen)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(offene_hauptforderung=offene_hauptforderung, befriedigung_durch_buergen=befriedigung_durch_buergen, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte[0],werte[1]), 'BGB_BUERGSCHAFT_FORDERUNGSUEBERGANG_BETRAG', eingaben, [dict(operation='Numerischer Forderungsübergang: Minimum aus noch bestehender erfasster Hauptforderung und darauf bewirkter Befriedigung durch den Bürgen.')])
    ergebnis["hinweise"].append('§774I: ausschließlich Höhe des gesetzlichen Übergangs der konkret erfassten Hauptforderung. Entsprechend§1143I bei Befriedigung durch den Grundstückseigentümer, der nicht persönlicher Schuldner ist; befriedigung_durch_buergen bezeichnet in dieser Normanwendung dessen qualifizierten Befriedigungsbetrag. Der Funktionsname bezeichnet den wiederverwendeten774-Kern, keine zusätzlich vorausgesetzte Bürgschaft. Gesamthypothekenfolgen1143II/1173 und Sicherheitenverteilung werden hier nicht berechnet. Keine Vermehrung der Forderung bei Überzahlung und keine Berechnung eines daraus möglichen Rückforderungsanspruchs. Durchsetzung darf dem verbleibenden Gläubiger nicht schaden; Hauptschuldnereinwendungen bleiben bestehen. Innenausgleich unter Mitbürgen nach774II/426, Sicherheiten, Zinsen und Kosten separat zuordnen; keine doppelte Erfassung bereits übergegangener Forderungen.')
    return ergebnis


def mietsicherheit_mit_anlageertraegen(sicherheit_vor_ertragszuwachs=None, hinzukommende_anlageertraege=None, einordnungsnachweis=None):
    """Bestehende Sicherheit und noch nicht enthaltene zugeordnete Anlageerträge addieren."""
    werte = [_geld(sicherheit_vor_ertragszuwachs), _geld(hinzukommende_anlageertraege)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(sicherheit_vor_ertragszuwachs=sicherheit_vor_ertragszuwachs, hinzukommende_anlageertraege=hinzukommende_anlageertraege, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(werte[0],werte[1]), 'BGB_MIETSICHERHEIT_MIT_ANLAGEERTRAEGEN', eingaben, [dict(operation='Bestehende Sicherheit und noch nicht enthaltene zugeordnete Anlageerträge addieren.')])
    ergebnis["hinweise"].append('§551III: tatsächlicher Ertragszuwachs erhöht die Sicherheit; keine erneute Begrenzung des Ertragszuwachses auf drei Monatsmieten. Ausgangssicherheit gesondert nach551I prüfen. Keine Hochrechnung eines hypothetischen Sparzinses, kein Ersatz einer unterlassenen Anlage und keine automatische Kautionsfreigabe. Anlageverluste, Entnahmen und bereits eingerechnete Erträge getrennt berücksichtigen; keine Doppelzählung.')
    return ergebnis


def landpacht_verbesserungsmassnahme_ersatzbetrag(ersatzfaehige_aufwendungen=None, ersatzfaehige_entgangene_ertraege=None, einordnungsnachweis=None):
    """Angemessene ersatzfähige Aufwendungen und überschneidungsfrei bewertete entgangene Erträge addieren."""
    werte = [_geld(ersatzfaehige_aufwendungen), _geld(ersatzfaehige_entgangene_ertraege)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(ersatzfaehige_aufwendungen=ersatzfaehige_aufwendungen, ersatzfaehige_entgangene_ertraege=ersatzfaehige_entgangene_ertraege, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_addieren(werte[0],werte[1]), 'BGB_LANDPACHT_VERBESSERUNGSMASSNAHME_ERSATZBETRAG', eingaben, [dict(operation='Angemessene ersatzfähige Aufwendungen und überschneidungsfrei bewertete entgangene Erträge addieren.')])
    ergebnis["hinweise"].append('§588II: numerischer Ersatzumfang aus qualifizierten Betragskomponenten. Keine automatische Billigkeitsbewertung oder Brutto-/Nettobewertung entgangener Erträge; diese ist widerspruchsfrei mit den Aufwendungen vorzugeben. Vorschüsse/Zahlungen gesondert anrechnen. Eine Pachterhöhung wegen höherer Erträge588III ist ein anderer Rechengegenstand und wird nicht erfunden.')
    return ergebnis


def landpacht_verwendungsersatz_mehrwertgrenze(ersatzfaehige_verwendungen=None, fortbestehender_mehrwert=None, einordnungsnachweis=None):
    """Ersatzfähige Verwendungen auf den über die Pachtzeit hinaus fortbestehenden Mehrwert begrenzen."""
    werte = [_geld(ersatzfaehige_verwendungen), _geld(fortbestehender_mehrwert)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(ersatzfaehige_verwendungen=ersatzfaehige_verwendungen, fortbestehender_mehrwert=fortbestehender_mehrwert, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte[0],werte[1]), 'BGB_LANDPACHT_VERWENDUNGSERSATZ_MEHRWERTGRENZE', eingaben, [dict(operation='Ersatzfähige Verwendungen auf den über die Pachtzeit hinaus fortbestehenden Mehrwert begrenzen.')])
    ergebnis["hinweise"].append('§591I: Grundbetrag als Minimum aus ersatzfähigen Verwendungen und fortbestehendem Mehrwert. Notwendige Verwendungen590b und Wegnahmerechte591a, Zustimmung/gerichtliche Ersetzung, Bewertungsmethode und gerichtliche Teilzahlungen oder Vertragsfortsetzung591III separat. Kein automatischer Zahlungsplan und keine automatische Fälligkeit bei gerichtlich abweichender Regelung.')
    return ergebnis


def billigkeitshaftung_mittelbegrenzter_betrag(billig_erforderlicher_ersatzbetrag=None, verfuegbare_mittel=None, geschuetzter_unterhaltsbedarf=None, einordnungsnachweis=None):
    """Vom verfügbaren Mittelbestand geschützten Unterhaltsbedarf abziehen, mindestens null; Billigkeitsersatz auf diesen verbleibenden Betrag begrenzen."""
    werte = [_geld(billig_erforderlicher_ersatzbetrag), _geld(verfuegbare_mittel), _geld(geschuetzter_unterhaltsbedarf)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(billig_erforderlicher_ersatzbetrag=billig_erforderlicher_ersatzbetrag, verfuegbare_mittel=verfuegbare_mittel, geschuetzter_unterhaltsbedarf=geschuetzter_unterhaltsbedarf, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(min(werte[0],max(_subtrahieren(werte[1],werte[2]),_bruch(0))), 'BGB_BILLIGKEITSHAFTUNG_MITTELBEGRENZTER_BETRAG', eingaben, [dict(operation='Vom verfügbaren Mittelbestand geschützten Unterhaltsbedarf abziehen, mindestens null; Billigkeitsersatz auf diesen verbleibenden Betrag begrenzen.')])
    ergebnis["hinweise"].append('§829: nur numerische Mittelgrenze eines bereits nach Billigkeit qualifizierten Ersatzbetrags. Keine automatische Billigkeitsentscheidung aus Vermögenszahlen und keine Tabelle für angemessenen Unterhalt. Haftungsvoraussetzungen827/828, fehlende Erlangbarkeit von Ersatz durch einen aufsichtspflichtigen Dritten und Verhältnisse der Beteiligten extern feststellen. Keine Entscheidung über zeitliche Streckung, künftige Einkünfte oder Vollstreckbarkeit.')
    return ergebnis


def landpacht_beschreibung_kostenhaelfte(sachverstaendigenkosten=None, einordnungsnachweis=None):
    """Qualifizierte Sachverständigenkosten zur Hälfte je Vertragsseite aufteilen."""
    werte = [_geld(sachverstaendigenkosten)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(sachverstaendigenkosten=sachverstaendigenkosten, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_multiplizieren(werte[0],_bruch(1,2)), 'BGB_LANDPACHT_BESCHREIBUNG_KOSTENHAELFTE', eingaben, [dict(operation='Qualifizierte Sachverständigenkosten zur Hälfte je Vertragsseite aufteilen.')])
    ergebnis["hinweise"].append('§585bII: Verpächter und Pächter tragen jeweils eine Hälfte der qualifizierten Kosten. Nicht erneut durch die Anzahl einzelner Personen innerhalb einer Vertragsseite teilen. Keine Kostenentscheidung über andere Verfahren; bereits gezahlte Beiträge separat. Exakte Hälfte ohne Cent-Rundung; beide Seitenanteile ergeben zusammen den Gesamtbetrag.')
    return ergebnis


def landpacht_erzeugnisse_mehrwert(wert_erforderlicher_endbestand=None, vergleichswert_uebernommener_anfangsbestand=None, einordnungsnachweis=None):
    """Wert erforderlicher zurückzulassender Erzeugnisse abzüglich gleichartig bewerteten übernommenen Anfangsbestands, mindestens null."""
    werte = [_geld(wert_erforderlicher_endbestand), _geld(vergleichswert_uebernommener_anfangsbestand)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(wert_erforderlicher_endbestand=wert_erforderlicher_endbestand, vergleichswert_uebernommener_anfangsbestand=vergleichswert_uebernommener_anfangsbestand, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(werte[0],werte[1]),_bruch(0)), 'BGB_LANDPACHT_ERZEUGNISSE_MEHRWERT', eingaben, [dict(operation='Wert erforderlicher zurückzulassender Erzeugnisse abzüglich gleichartig bewerteten übernommenen Anfangsbestands, mindestens null.')])
    ergebnis["hinweise"].append('§596bII: Ersatz nur für den rechtlich qualifizierten Mehrbestand beziehungsweise bessere Beschaffenheit der nachAbsatz1 zurückzulassenden Erzeugnisse. Werte müssen den Unterschied in Menge/Beschaffenheit abbilden, nicht bloße allgemeine Preissteigerung. Über die erforderlichen Erzeugnisse hinaus freiwillig zurückgelassene Mengen nicht einrechnen; Pflicht nachAbsatz1 kann auch ohne Anfangsübernahme bestehen, dann Vergleichswert0. Bei verschiedenen Produktgruppen gesondert qualifizieren; keine pauschale Verrechnung fremder Minderbestände. Kein automatischer Anspruch wegen Bestandsangaben allein; Zahlungen separat.')
    return ergebnis


def werk_annahmeverzug_entschaedigungsbetrag(verzugsbezogene_verguetungsbasis=None, ersparte_aufwendungen=None, anderweitiger_arbeitskraft_erwerb=None, einordnungsnachweis=None):
    """Qualifizierte verzugsbezogene Vergütungsbasis abzüglich ersparter Aufwendungen und anderweitigen Arbeitskrafterwerbs, mindestens null."""
    werte = [_geld(verzugsbezogene_verguetungsbasis), _geld(ersparte_aufwendungen), _geld(anderweitiger_arbeitskraft_erwerb)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    eingaben = dict(verzugsbezogene_verguetungsbasis=verzugsbezogene_verguetungsbasis, ersparte_aufwendungen=ersparte_aufwendungen, anderweitiger_arbeitskraft_erwerb=anderweitiger_arbeitskraft_erwerb, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(max(_subtrahieren(_subtrahieren(werte[0],werte[1]),werte[2]),_bruch(0)), 'BGB_WERK_ANNAHMEVERZUG_ENTSCHAEDIGUNGSBETRAG', eingaben, [dict(operation='Qualifizierte verzugsbezogene Vergütungsbasis abzüglich ersparter Aufwendungen und anderweitigen Arbeitskrafterwerbs, mindestens null.')])
    ergebnis["hinweise"].append('§642I/II: numerischer Abrechnungsschritt aus rechtlich bestimmter Verzugsdauer-/Vergütungsbasis und zugehörigen Abzügen. Basis nicht blind als gesamte Vergütung geteilt durch gesamte Vertragszeit bilden; tatsächlich betroffene Vorhaltung und rechtlich maßgebliche Bewertungsanteile qualifizieren. Keine automatische Entschädigung sämtlicher Mehrkosten nach Verzugsende und keine Schadensersatzprognose. Ersparnis und anderweitiger Erwerb nur einmal, nicht bereits netto in der Basis und erneut als Abzug. Kein zusätzliches Böswilligkeitserfordernis aus615/648 übertragen. Negative Differenz ergibt0, keinen automatisch begründeten Zahlungsanspruch des Bestellers. Zahlungen separat.')
    return ergebnis


def bereicherung_entreicherungsrest(qualifizierter_geldherausgabebetrag=None, anrechenbare_entreicherung=None, einordnungsnachweis=None):
    """Qualifizierten Geldherausgabebetrag um rechtlich anrechenbare Entreicherung vermindern."""
    werte = [_geld(qualifizierter_geldherausgabebetrag), _geld(anrechenbare_entreicherung)]
    _text(einordnungsnachweis,'einordnungsnachweis')
    if werte[1] > werte[0]:
        _fehler('anrechenbare_entreicherung','Abzugsbetrag darf den verfügbaren Zahlungsbetrag nicht übersteigen.')
    eingaben = dict(qualifizierter_geldherausgabebetrag=qualifizierter_geldherausgabebetrag, anrechenbare_entreicherung=anrechenbare_entreicherung, einordnungsnachweis=einordnungsnachweis)
    ergebnis = _geld_ergebnis(_subtrahieren(werte[0],werte[1]), 'BGB_BEREICHERUNG_ENTREICHERUNGSREST', eingaben, [dict(operation='Qualifizierten Geldherausgabebetrag um rechtlich anrechenbare Entreicherung vermindern.')])
    ergebnis["hinweise"].append('§818III: ausschließlich numerische Begrenzung auf Grundlage bereits rechtlich bestimmter Beträge. Entreicherung nicht automatisch aus vermindertem Kontostand, Konsumausgaben oder Verlusten ablesen. Anrechenbaren Wegfall auf die tatsächlich erfassten Komponenten und den maßgeblichen Haftungszeitraum beziehen. Verschärfte Haftung818IV/819/820, Nutzungsgrenze820II, Drittweitergabe822 und Einreden821 gesondert; ausgeschlossene Entreicherung darf nicht durch positives Eingabefeld wieder eingeführt werden. Keine automatische Saldotheorie oder Verrechnung beider Leistungsrichtungen, keine körperliche Sachherausgabe als Geldrest behandeln. Zahlungen separat.')
    return ergebnis
