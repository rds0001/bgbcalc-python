"""Unabhängig erwartete Ergebnisse über mehrere öffentliche Fachfunktionen."""
from fractions import Fraction
from datetime import date, timedelta

import bgbcalc


def als_bruch(wert):
    return Fraction(int(wert["zaehler"]), int(wert["nenner"]))


def knoten(kennung, tritt_ein=True, abkoemmlinge=None):
    return dict(person_id=kennung, tritt_ein=tritt_ein,
                abkoemmlinge=[] if abkoemmlinge is None else abkoemmlinge)


def test_guetertrennung_mit_vertretenem_kinderstamm():
    ehe = bgbcalc.ehegatten_erbquote(
        "erste_ordnung", "guetertrennung", 2, 0, 1, True, False, False, False, False,
    )["wert"]
    anteil = als_bruch(ehe["verwandtenquote"])
    kinder = bgbcalc.abkoemmlings_erbquoten(
        [knoten("A"), knoten("B", False, [knoten("B1"), knoten("B2")])],
        anteil.numerator, anteil.denominator,
    )["wert"]
    quoten = {eintrag["person_id"]: als_bruch(eintrag["quote"]) for eintrag in kinder["erbquoten"]}
    assert als_bruch(ehe["ehegattenquote"]) == Fraction(1, 3)
    assert quoten == {"A": Fraction(1, 3), "B1": Fraction(1, 6), "B2": Fraction(1, 6)}
    assert sum(quoten.values()) + als_bruch(ehe["ehegattenquote"]) == 1


def test_grosselternabkoemmlingsanteil_geht_an_ehegatten():
    paare = dict(vaeterlich=[knoten("V1"), knoten("V2")],
                 muetterlich=[knoten("M1"), knoten("M2", False, [knoten("N")])])
    rein = bgbcalc.grosselternlinien_erbquoten(paare, False, 1, 1)["wert"]
    nachkommenanteil = als_bruch(rein["abkoemmlingsquote"])
    ehe = bgbcalc.ehegatten_erbquote(
        "grosseltern", "zugewinngemeinschaft", 0,
        nachkommenanteil.numerator, nachkommenanteil.denominator,
        True, False, False, False, False,
    )["wert"]
    basis = 1 - als_bruch(ehe["grundquote"]) - als_bruch(ehe["zugewinnzuschlag"])
    vor_zuschlag = bgbcalc.grosselternlinien_erbquoten(
        paare, False, basis.numerator, basis.denominator,
    )["wert"]
    grosseltern = {teil["person_id"]: als_bruch(teil["quote"])
                  for teil in vor_zuschlag["erbteile"] if len(teil["stammpfad"]) == 1}
    assert grosseltern == {"V1": Fraction(1, 16), "V2": Fraction(1, 16), "M1": Fraction(1, 16)}
    assert als_bruch(ehe["grosselternabkoemmlingszuschlag"]) == Fraction(1, 16)
    assert als_bruch(ehe["ehegattenquote"]) == Fraction(13, 16)
    assert sum(grosseltern.values()) + als_bruch(ehe["ehegattenquote"]) == 1


def test_alterswechsel_rundung_und_kindergeld_in_richtiger_reihenfolge():
    stufe = bgbcalc.unterhaltsaltersstufe("2020-05-20", "2026-05-01")["wert"]
    minimum = bgbcalc.mindestunterhalt_aus_existenzminimum(
        "6000", stufe, "Synthetische Jahresgrundlage",
    )["wert"]
    unterhalt = bgbcalc.dynamischer_kindesunterhalt(
        minimum, "100.19", "Synthetischer altersbezogener Mindestunterhalt",
    )["wert"]
    ergebnis = bgbcalc.kindbezogene_leistung_anrechnen(
        unterhalt, "200", "0", True, "kindergeld", True, False,
    )["wert"]
    assert stufe == 2
    assert als_bruch(minimum) == 500
    assert als_bruch(unterhalt) == 501
    assert als_bruch(ergebnis["verbleibender_barbedarf"]) == 401


def test_pflichtteil_zusatz_ohne_dezimalrundung():
    pflichtteil = bgbcalc.pflichtteil_betrag(
        "1", 1, 3, "0", False, True, "Synthetischer bewerteter Nachlass und gesetzliche Quote",
    )["wert"]
    zusatz = bgbcalc.zusatzpflichtteil_betrag(
        pflichtteil, dict(zaehler="1", nenner="12"), True,
    )
    assert als_bruch(pflichtteil) == Fraction(1, 6)
    assert als_bruch(zusatz["wert"]) == Fraction(1, 12)
    assert zusatz["nutzervorgaben"]["pflichtteilsbetrag"] == pflichtteil


def test_darlehenszuordnung_und_zinsvorteil_ohne_rundungsverlust():
    zuordnung = bgbcalc.modernisierung_drittmittel_aufteilen(
        "1", [
            dict(wohnung_id="A", aufgewendete_kosten="1"),
            dict(wohnung_id="B", aufgewendete_kosten="2"),
        ], False,
    )["wert"]
    ursprungsbetrag = zuordnung[0]["drittmittel"]
    vorteil = bgbcalc.modernisierung_zinsermaessigung(
        ursprungsbetrag, "1", "4", "Synthetischer Abschlussstichtag und Marktzinssatz", True, False,
    )["wert"]
    assert als_bruch(ursprungsbetrag) == Fraction(1, 3)
    assert als_bruch(vorteil) == Fraction(1, 100)
    grund = True  # Extern qualifizierte rechtliche Eingabe.
    zwischen = bgbcalc.modernisierung_regulaerer_zwischenbetrag(
        ursprungsbetrag, "0", "0", vorteil, "0", grund,
    )
    # 8 % von 1/3 minus 1/100 = 1/60 jährlich, geteilt durch 12.
    assert als_bruch(zwischen["wert"]["jaehrlicher_zwischenbetrag"]) == Fraction(1, 60)
    assert als_bruch(zwischen["wert"]["monatlicher_zwischenbetrag"]) == Fraction(1, 720)
    assert zwischen["nutzervorgaben"]["jaehrliche_zinsermaessigung"] == vorteil


def test_verspaetete_haertemitteilung_und_verzoegerter_erhoehungsbeginn():
    angekuendigt = dict(zaehler="100", nenner="1")
    tatsaechlich = dict(zaehler="11001", nenner="100")
    haerte = bgbcalc.modernisierung_haerteberuecksichtigung(
        True, True, False, True, False, angekuendigt, tatsaechlich,
    )["wert"]
    beginn = bgbcalc.modernisierung_erhoehungsbeginn(
        "2026-01-31", True, angekuendigt, tatsaechlich, True,
    )["wert"]
    # Heizungs-Ausnahmen ermöglichen die Abwägung trotz Vereinfachung und
    # fehlendem Vertretenmüssen. Mehr als 10 % hebt die Mitteilungssperre auf
    # und verschiebt zugleich den Beginn der erhöhten Miete.
    assert haerte["umstaende_beruecksichtigungsfaehig"] is True
    assert beginn == "2026-10-01"


def test_regelgrundfrist_mit_schalttagshemmung():
    grund = bgbcalc.regelverjaehrung_grundfrist("2019-05-01", "2019-06-01", True)["wert"]
    erster = date.fromisoformat(grund["beginn_mit_jahresschluss"]) + timedelta(days=1)
    ergebnis = bgbcalc.verjaehrung_gehemmte_kalendertage(
        erster.isoformat(), grund["rechnerischer_letzter_tag"],
        [dict(erster_gehemmter_tag="2020-02-28", letzter_gehemmter_tag="2020-03-01")], True,
    )["wert"]
    assert grund["rechnerischer_letzter_tag"] == "2022-12-31"
    assert ergebnis == dict(rechnerischer_letzter_tag="2023-01-03", beruecksichtigte_hemmungstage=3)


def test_verhandlungsnachlauf_nach_herausgerechneten_hemmungstagen():
    gehemmt = bgbcalc.verjaehrung_gehemmte_kalendertage(
        "2026-01-01", "2026-01-10",
        [dict(erster_gehemmter_tag="2026-01-05", letzter_gehemmter_tag="2026-01-20")], True,
    )["wert"]
    nachlauf = bgbcalc.verjaehrung_verhandlungen_mindestablauf(
        "2026-01-20", gehemmt["rechnerischer_letzter_tag"], True,
    )["wert"]
    assert gehemmt["rechnerischer_letzter_tag"] == "2026-01-26"
    # Mindestnachlauf ab Hemmungsende, nicht drei Monate ab dem verlängerten Fristende.
    assert nachlauf["rechnerischer_letzter_tag"] == "2026-04-20"


def test_aufgehobene_vollstreckung_und_eigenstaendiges_anerkenntnis():
    grund = bgbcalc.regelverjaehrung_grundfrist("2024-01-01", "2024-01-01", True)["wert"]
    assert "2026-01-15" < grund["rechnerischer_letzter_tag"]
    antrag = False  # Extern qualifizierte rechtliche Eingabe.
    anerkenntnis = True  # Extern qualifizierte rechtliche Eingabe.
    # Synthetischer Anspruch noch unverjährt; sonstige Wirksamkeitsvoraussetzungen
    # des eigenständigen Anerkenntnisses sind für diesen Test ausdrücklich erfüllt.
    verworfen = bgbcalc.verjaehrung_neubeginn_grundfrist(
        "2026-01-15", 3, "jahre", antrag,
    )
    erneuert = bgbcalc.verjaehrung_neubeginn_grundfrist(
        "2026-01-15", 3, "jahre", anerkenntnis,
    )
    assert verworfen["status"] == "NICHT_ANWENDBAR"
    assert verworfen["wert"] is None
    assert erneuert["wert"] == "2029-01-15"


def test_nachlass_ablaufhemmung_verlaengert_regelgrundfrist():
    # Synthetischer gewöhnlicher Anspruch des Erblassers; maßgeblicher Schutzfall
    # vor Ablauf eingetreten. Kein früheres schutzbeendendes Ereignis liegt vor.
    grund = bgbcalc.regelverjaehrung_grundfrist("2024-01-01", "2024-01-01", True)["wert"]
    nachlass = bgbcalc.verjaehrung_ablaufhemmung_mindestablauf(
        "nachlass", [dict(ereignis="erbschaft_angenommen", datum="2027-11-01")],
        3, "jahre", grund["rechnerischer_letzter_tag"], False, True,
    )["wert"]
    assert grund["rechnerischer_letzter_tag"] == "2027-12-31"
    assert nachlass["mindestablauf"] == "2028-05-01"
    assert nachlass["rechnerischer_letzter_tag"] == "2028-05-01"


def test_sachschaden_und_mitverschulden_nur_einmal_kuerzen():
    # Im ersten Schritt Quote null, damit dieselbe Kürzung nicht doppelt erfolgt.
    vor_quote = bgbcalc.sachschaden_ersatzbetrag("1000", "190", "0")["wert"]
    nach_quote = bgbcalc.vermoegensschaden_mitverschulden(
        vor_quote, "0.25", "Synthetische Quote für den gesamten Sachschaden dieser Position", True,
    )["wert"]
    assert als_bruch(vor_quote) == 1190
    assert als_bruch(nach_quote["kuerzungsbetrag"]) == Fraction(595, 2)
    assert als_bruch(nach_quote["verbleibender_ersatzbetrag"]) == Fraction(1785, 2)
    assert sum(als_bruch(b) for b in nach_quote.values()) == 1190


def test_mehrere_schulden_dann_bestandteile_tilgen():
    zuordnung = bgbcalc.faellige_geldschulden_gesetzlich_tilgen(
        "120", [
            dict(schuld_id="A", offener_betrag="100", sicherheitsrang=1,
                 laestigkeitsrang=1, altersrang=1),
            dict(schuld_id="B", offener_betrag="100", sicherheitsrang=2,
                 laestigkeitsrang=1, altersrang=1),
        ], False, True,
    )["wert"]["zuordnungen"]
    a = bgbcalc.zahlung_anrechnen(
        zuordnung[0]["tilgungsbetrag"], "10", "20", "70", None, False,
    )["wert"]
    b = bgbcalc.zahlung_anrechnen(
        zuordnung[1]["tilgungsbetrag"], "5", "10", "85", None, False,
    )["wert"]
    assert [als_bruch(x["betrag"]) for x in a["zuordnungen"]] == [10, 20, 70]
    assert [als_bruch(x["betrag"]) for x in b["zuordnungen"]] == [5, 10, 5]
    assert als_bruch(b["zuordnungen"][2]["restforderung"]) == 80
    assert als_bruch(a["nicht_zugeordnet"]) == als_bruch(b["nicht_zugeordnet"]) == 0


def test_indexmiete_fortschreibung_mit_passender_indexbasis():
    erste = bgbcalc.indexmiete_betrag(
        "800", "100", "110", "Synthetische gleiche Indexreihe und Basis", True,
    )["wert"]["neue_miete"]
    zweite = bgbcalc.indexmiete_betrag(
        erste, "110", "121", "Fortschreibung ab dem zur neuen Mietbasis gehörenden Index110", True,
    )["wert"]["neue_miete"]
    direkt = bgbcalc.indexmiete_betrag(
        "800", "100", "121", "Vergleichsrechnung von der ursprünglichen Basis", True,
    )["wert"]["neue_miete"]
    assert als_bruch(erste) == 880
    assert als_bruch(zweite) == als_bruch(direkt) == 968


def test_altersbeginn_und_deliktsgrenze_am_schalttag():
    beginn = bgbcalc.lebensalter_beginn("2016-02-29", 10)["wert"]
    vorher = bgbcalc.delikt_altersvoraussetzungen(
        "2016-02-29", "2026-02-28", True, False, True,
    )["wert"]
    nachher = bgbcalc.delikt_altersvoraussetzungen(
        "2016-02-29", beginn, True, False, True,
    )["wert"]
    assert beginn == "2026-03-01"
    assert vorher["ausschluss_nach_absatz_2"] is True
    assert nachher["ausschluss_nach_absatz_2"] is False
    assert nachher["vollendete_lebensjahre"] == 10


def test_darlehensnachfrist_mit_vorgeschalteter_werktagskorrektur():
    schwelle = bgbcalc.verbraucherdarlehen_verzugsschwelle(
        "10000", "1000", "3", 2, False, True,
    )["wert"]
    rechnerisch = bgbcalc.fristende("2026-10-10", 2, "wochen", "ereignis")["wert"]
    massgeblich = bgbcalc.werktagsverschiebung(
        rechnerisch, "leistung", [], "Synthetischer Leistungsort",
        "Synthetischer vollständiger Kalender ohne zusätzliche Feiertage",
        "2026-10-01", "2026-10-31",
    )["wert"]
    noch_offen = bgbcalc.verbraucherdarlehen_kuendigungsnachfrist(
        "2026-10-10", massgeblich, "2026-10-25", "Vorgeschaltete §193-Prüfung",
        False, True, True,
    )["wert"]
    abgelaufen = bgbcalc.verbraucherdarlehen_kuendigungsnachfrist(
        "2026-10-10", massgeblich, "2026-10-27", "Vorgeschaltete §193-Prüfung",
        True, True, True,
    )["wert"]
    assert rechnerisch == "2026-10-24"
    assert massgeblich == "2026-10-26"
    assert schwelle["voraussetzungen_nummer_1_erfuellt"] is True
    assert noch_offen["nachfrist_am_prueftag_abgelaufen"] is False
    assert noch_offen["voraussetzungen_nummer_2_erfuellt"] is False
    assert abgelaufen["voraussetzungen_nummer_2_erfuellt"] is True


def test_mietpreis_grundbetrag_und_vormietweg_ohne_addition():
    ausnahmen = bgbcalc.mietpreisbegrenzung_ausnahmen(
        "2000-01-01", "2000-02-01", False, "Synthetischer Altbau ohne umfassende Modernisierung",
    )["wert"]
    grundbetrag = bgbcalc.mietpreisbegrenzung_grundbetrag(
        "800", True, ausnahmen["ausnahme_von_556d"],
        "Synthetische gültige Verordnung; keine Ausnahme oder Auskunftshindernisse",
    )["wert"]
    mit_privileg = bgbcalc.mietpreisbegrenzung_vormietgrenze(
        grundbetrag, "900", True, "Bereinigte geschuldete Vormiete, erforderliche Auskunft erteilt",
    )["wert"]
    ohne_privileg = bgbcalc.mietpreisbegrenzung_vormietgrenze(
        grundbetrag, "900", False, "Vormietprivileg wegen fehlender Auskunft derzeit nicht nutzbar",
    )["wert"]
    assert als_bruch(grundbetrag) == 880
    assert als_bruch(mit_privileg) == 900
    assert als_bruch(ohne_privileg) == 880






def test_vereinsliquidation_kalender_und_anteil_bei_vorgegebener_ausantwortungsreife():
    bestand = bgbcalc.vereins_liquidationsueberschuss(
        "1000", "100", "Synthetischer konsistenter Liquidationsbestand",
    )["wert"]
    kalender = bgbcalc.vereins_liquidationssperrjahr(
        "2024-02-27", True, "Synthetische ordnungsgemäße erste Einrückung",
    )["wert"]
    anteil = bgbcalc.vereinsvermoegen_mitgliederanteil(
        bestand["ueberschuss"], 7, False, True,
        "Synthetisch am 01.03.2025 sämtliche Gläubiger befriedigt, Sicherungsfragen erledigt, keine andere Anfallbestimmung",
    )["wert"]
    assert kalender["fruehester_tag_nach_sperrjahr"] == "2025-03-01"
    assert als_bruch(bestand["fehlbetrag"]) == 0
    assert 7 * als_bruch(anteil) == als_bruch(bestand["ueberschuss"]) == 900


def test_besondere_verjaehrung_mit_altershemmung_am_schalttagsgeburtstag():
    grund = bgbcalc.verjaehrung_besondere_grundfrist(
        "vorsaetzliche_personenverletzung", "2025-02-27", None, False, False,
        "Synthetischer vorsätzlicher Eingriff in sexuelle Selbstbestimmung; Anspruch entsteht 27.02.2025",
    )["wert"]
    vor = bgbcalc.verjaehrung_sexuelle_selbstbestimmung_hemmung(
        "2004-02-29", "2025-02-28", True, False, False, "Keine häusliche Gemeinschaft",
    )["wert"]
    nach = bgbcalc.verjaehrung_sexuelle_selbstbestimmung_hemmung(
        "2004-02-29", "2025-03-01", True, False, False, "Vollendung21 am1.März",
    )["wert"]
    gehemmt = bgbcalc.verjaehrung_gehemmte_kalendertage(
        "2025-02-28", grund["rechnerischer_letzter_tag"],
        [{"erster_gehemmter_tag": "2025-02-28", "letzter_gehemmter_tag": "2025-02-28"}], True,
    )["wert"]
    assert vor["hemmungstatbestand_am_stichtag"] is True
    assert nach["hemmungstatbestand_am_stichtag"] is False
    assert grund["rechnerischer_letzter_tag"] == "2055-02-27"
    assert gehemmt == {"rechnerischer_letzter_tag": "2055-02-28", "beruecksichtigte_hemmungstage": 1}


def test_verwirkte_vertragsstrafe_und_annahmevorbehalt_ohne_doppelschaeden():
    verwirkt = True  # Extern qualifizierte rechtliche Eingabe.
    mit = bgbcalc.vertragsstrafe_schadensmindestbetrag(
        "500", "800", "nicht_gehoerige_erfuellung", verwirkt, True, True, True,
        "Synthetisch bei Annahme wirksam vorbehalten",
    )["wert"]
    ohne = bgbcalc.vertragsstrafe_schadensmindestbetrag(
        "500", "800", "nicht_gehoerige_erfuellung", verwirkt, True, False, True,
        "Kein Strafvorbehalt, aber unabhängig bestehender Schadenanspruch",
    )["wert"]
    assert verwirkt is True
    assert als_bruch(mit["strafmindestbetrag"]) == 500
    assert als_bruch(mit["weiterer_schadensbetrag"]) == 300
    assert als_bruch(mit["gesamtbetrag"]) == 800
    assert als_bruch(ohne["strafmindestbetrag"]) == 0
    assert als_bruch(ohne["weiterer_schadensbetrag"]) == 800
    assert als_bruch(ohne["gesamtbetrag"]) == 800


def test_pflichtteilsergaenzung_bewertung_abschmelzung_differenz_mehrhinterlassung():
    wert = bgbcalc.pflichtteil_schenkungswert(
        "500", "800", False, False, "Synthetische vergleichbare Werte ohne Belastungen",
    )["wert"]
    zeit = bgbcalc.pflichtteil_schenkungsabschmelzung(
        wert, "2000-06-15", "2005-06-16", True, False, None,
        "Synthetisch fristauslösende Drittschenkung ohne vorbehaltene Rechte",
    )["wert"]
    grund = bgbcalc.pflichtteilsergaenzung_grundbetrag(
        "1000", zeit["beruecksichtigter_schenkungswert"], 1, 2, True,
        "Synthetischer positiver Nachlass ohne Eigengeschenke/Ausgleichung",
    )["wert"]
    rest = bgbcalc.pflichtteilsergaenzung_mehrhinterlassung(
        grund["ergaenzungsgrundbetrag"], "280", grund["ordentlicher_pflichtteilswert"],
        "Synthetisch unbelastet hinterlassener Wert280",
    )["wert"]
    assert als_bruch(wert) == 500
    assert als_bruch(zeit["beruecksichtigter_schenkungswert"]) == 250
    assert als_bruch(grund["ordentlicher_pflichtteilswert"]) == 250
    assert als_bruch(grund["ergaenzungsgrundbetrag"]) == Fraction(125, 2)
    assert als_bruch(rest["mehrhinterlassung"]) == 30
    assert als_bruch(rest["verbleibende_ergaenzung"]) == Fraction(65, 2)


def test_sachenverbindung_quoten_fuer_gemeinschaftslasten():
    quoten = bgbcalc.sachenverbindung_eigentumsquoten(
        [{"eigentuemer_id": "A", "sachenwert": "100"}, {"eigentuemer_id": "B", "sachenwert": "300"}],
        "verbindung", True, False, False, None, "Synthetische wesentliche Verbindung ohne Hauptsache",
    )["wert"]
    teilhaber = [{"person_id": eintrag["eigentuemer_id"],
        "anteil_zaehler": int(eintrag["eigentumsquote"]["zaehler"]),
        "anteil_nenner": int(eintrag["eigentumsquote"]["nenner"])} for eintrag in quoten]
    kosten = bgbcalc.gemeinschaft_lastenanteile("100", teilhaber, False, True)["wert"]
    assert [als_bruch(e["eigentumsquote"]) for e in quoten] == [Fraction(1, 4), Fraction(3, 4)]
    assert [als_bruch(e["betrag"]) for e in kosten] == [25, 75]


def test_vergleichsmiete_zeit_und_betragsrahmen_mit_ausgenommenem_modernisierungsanteil():
    zeit = bgbcalc.vergleichsmiete_zeitvoraussetzungen("2024-01-01", "2025-01-15", True)["wert"]
    betrag = bgbcalc.vergleichsmiete_kappungsrahmen(
        "500", "100", "650", "750", True, False, False, True,
        "Synthetischer Dreijahresverlauf:500 Ausgangsmiete,50 reguläre Erhöhung ab01.01.2024,100 ausgeschlossene Modernisierung; gültige15Prozent-Verordnung",
    )["wert"]
    assert zeit["jahresfrist_eingehalten"] is True
    assert zeit["wartefrist_eingehalten"] is True
    assert zeit["mietbeginn_bei_zustimmung"] == "2025-04-01"
    assert als_bruch(betrag["kappungsbetrag_monatlich"]) == 675
    assert als_bruch(betrag["maximaler_erhoehungsbetrag"]) == 25
    assert als_bruch(betrag["miete_nach_maximaler_erhoehung"]) == 675


def test_werkkuendigungsarten_getrennte_verguetungsfolgen():
    wichtiger_grund = bgbcalc.werkkuendigung_wichtiger_grund_verguetung(
        "1200", 1, 3, True, False, "Synthetische wirksame wichtige Kündigung; ein Drittel erbracht",
    )["wert"]
    freie_kuendigung = bgbcalc.werk_bestellerkuendigung_verguetung(
        "400", "800", "vermutung", "0", "0", "0", True, False, False,
    )["wert"]
    bautraeger = bgbcalc.werkkuendigung_wichtiger_grund_verguetung(
        "1200", 1, 3, True, True, "Synthetischer Bauträgervertrag:§648a ausgeschlossen",
    )
    assert als_bruch(wichtiger_grund) == 400
    assert als_bruch(freie_kuendigung) == 440
    assert bautraeger["status"] == "NICHT_ANWENDBAR"
    assert bautraeger["wert"] is None


def test_betragsaufrechnung_mit_qualifizierter_zulaessigkeit():
    for zulaessig in (False, True):
        wirkung = bgbcalc.aufrechnung_betragswirkung("1200", "800", "2024-01-01", "2026-01-01", zulaessig,
            "Zulässigkeit und Erklärung extern rechtlich qualifiziert; Beträge zum Aufrechnungszeitpunkt")
        if zulaessig:
            assert als_bruch(wirkung["wert"]["erloschener_betrag_je_forderung"]) == 800
            assert als_bruch(wirkung["wert"]["rest_eigene_forderung"]) == 400
            assert als_bruch(wirkung["wert"]["rest_gegenforderung"]) == 0
            assert wirkung["wert"]["erloeschenszeitpunkt_am"] == "2024-01-01"
        else:
            assert wirkung["status"] == "NICHT_ANWENDBAR"




def test_betriebskostenpauschale_betrag_und_rueckwirkungsgrenze():
    betrag = bgbcalc.betriebskostenpauschale_aenderungsbetrag(
        "120", "150", 1, 3, True, True, True,
        "Synthetisch monatliche wirtschaftliche Gesamtkosten; Drittel-Umlageanteil",
    )["wert"]
    zeit = bgbcalc.betriebskostenpauschale_erhoehungsbeginn(
        "2025-04-30", "2023-12-01", "2025-01-31", "2025-04-30", True, True,
        "Synthetische nachträgliche Kostensteigerung und fristgerechte Erklärung am letzten Tag",
    )["wert"]
    assert als_bruch(betrag) == 10
    assert zeit["dreimonatsfrist_eingehalten"] is True
    assert zeit["rueckwirkung_anwendbar"] is True
    assert zeit["erhoehungsbeginn"] == "2024-01-01"
    assert zeit["regulaerer_erhoehungsbeginn"] == "2025-06-01"


def test_maengelgrundfrist_einmalige_verlaengerung_und_konkurrierende_nachlaeufe():
    grund = bgbcalc.maengel_verjaehrungsgrundfrist(
        "kauf", "sonstige_sache", "2030-01-31", False, None, False,
        "Synthetisch Ablieferung2030 und gesetzlicher Zweijahresweg",
    )["wert"]["rechnerischer_letzter_tag"]
    verlaengert = bgbcalc.verbrauchsgueterkauf_nachbesserungsverlaengerung(
        grund, True, True, "Synthetisch Nachbesserung/Rückgabe31.05.2032, vorherige Übergabe vor Ablauf der ursprünglichen Frist; Absatz5 zeitlich anwendbar",
    )["wert"]["rechnerischer_letzter_tag"]
    nochmals = bgbcalc.verbrauchsgueterkauf_nachbesserungsverlaengerung(
        grund, True, True, "Synthetisch weitere Nachbesserung; unveränderter ursprünglicher Grundtermin",
    )["wert"]["rechnerischer_letzter_tag"]
    zeigen = bgbcalc.verbrauchsgueterkauf_verjaehrungsnachlauf(
        "erstmaliges_zeigen_des_mangels", "2031-12-30", verlaengert, True,
        "Synthetisch derselbe Mangel erstmals30.12.2031, bereits innerhalb ursprünglicher Frist",
    )["wert"]["rechnerischer_letzter_tag"]
    rueckgabe = bgbcalc.verbrauchsgueterkauf_verjaehrungsnachlauf(
        "rueckgabe_nach_nacherfuellung_garantie", "2032-05-31", zeigen, True,
        "Synthetisch Übergabe zur Nacherfüllung vor31.01.2032 und Rückgabe31.05.2032",
    )["wert"]["rechnerischer_letzter_tag"]
    assert grund == "2032-01-31"
    assert verlaengert == nochmals == "2033-01-31"
    assert zeigen == "2033-01-31"
    assert rueckgabe == "2033-01-31"


def test_modernisierungszeitgrenzen_und_objektiver_grund():
    beginn = bgbcalc.modernisierung_beginnverzoegerung(
        "2022-12-01", "2023-01-01", "2024-03-01", "2025-04-01",
        "Synthetisch verspäteter tatsächlicher Beginn der angekündigten Baumaßnahme",
    )["wert"]["beginnverzoegerung_nummer_1"]
    ruhe = bgbcalc.modernisierung_arbeitsruhe(
        "2024-04-01", "tagesbeginn", None, "2025-04-01",
        "Synthetisch nach Beginn seit01.04.2024 ununterbrochen ruhend, Prüfung zum Tagesschluss",
    )["wert"]["arbeitsruhe_nummer_4"]
    assert beginn is True
    assert ruhe is True
    for grund in (False, True):
        vermutung = bgbcalc.modernisierung_pflichtverletzungsvermutung(
            "800", "100", True, beginn, False, ruhe, grund,
            "Synthetisch objektiver Grund, falls bejaht, für beide zeitlichen Tatbestände dargelegt",
        )["wert"]
        assert vermutung["verdoppelung_nummer_2"] is False
        assert vermutung["vermutungstatbestand_erfuellt"] is True
        assert vermutung["pflichtverletzung_wird_vermutet"] is (not grund)




def test_erbausschlagungsgrundfrist_und_anfechtung_der_versaeumung():
    ausschlagung = bgbcalc.erbausschlagung_grundfrist(
        "2029-12-01", "2030-01-01", True, "2030-01-15", False, False, True,
        "Synthetische Verfügung: gerichtliche Bekanntgabe später als Kenntnis; keine Fristkorrekturen",
    )["wert"]
    anfechtung = bgbcalc.erbrecht_anfechtungsgrundfrist(
        "ausschlagungsfristversaeumung", ausschlagung["rechnerischer_letzter_tag"], "2030-03-01",
        False, False, True,
        "Synthetisch Ausschlagung unterblieben, Annahmefiktion am Fristablauf; Kenntnis des Anfechtungsgrunds erst01.03.2030",
    )["wert"]
    assert ausschlagung["fristbeginnereignis_am"] == "2030-01-15"
    assert ausschlagung["rechnerischer_letzter_tag"] == "2030-02-26"
    assert anfechtung["rechnerisches_grundfristende"] == "2030-04-12"
    assert anfechtung["dreissigjahresgrenze"] == "2060-02-26"
    assert anfechtung["rechnerischer_letzter_tag"] == "2030-04-12"


def test_krankenfuersorgezeitraum_und_periodengleiche_kostenanrechnung():
    zeit = bgbcalc.dienst_krankenfuersorge_zeitraum(
        "2024-02-29", "tagesbeginn", "2024-03-15", True, True, False, False, False,
        "Synthetisch fortdauernder Fürsorgebedarf bis gewöhnlichem Dienstende15.03.2024",
    )["wert"]
    tage = (date.fromisoformat(zeit["fuersorge_spaetestens_bis"]) - date(2024, 2, 29)).days + 1
    betrag = bgbcalc.dienst_krankheitskosten_anrechnung(
        "800", str(tage * 20), True, True,
        "Synthetisch erforderliche belegte Kosten20EUR je tatsächlichem Fürsorgetag und zugehörige Vergütung800EUR",
    )["wert"]
    assert tage == 16
    assert zeit["sechswochengrenze"] == "2024-04-10"
    assert als_bruch(betrag["angerechnete_kosten"]) == 320
    assert als_bruch(betrag["verbleibende_verguetung"]) == 480


def test_vererbte_ausschlagung_vergleicht_zwei_getrennte_erbschaften():
    nachweis = "Synthetisch gesetzliche Erbfolge ohne Fristkorrekturen; Erbe stirbt vor ursprünglichem Fristablauf"
    zuerst = bgbcalc.erbausschlagung_grundfrist(
        "2030-01-01", "2030-01-01", False, None, False, False, True, nachweis,
    )["wert"]["rechnerischer_letzter_tag"]
    danach = bgbcalc.erbausschlagung_grundfrist(
        "2030-02-01", "2030-02-01", False, None, False, False, True, nachweis,
    )["wert"]["rechnerischer_letzter_tag"]
    ende = bgbcalc.vererbte_ausschlagungsfrist("2030-02-01", zuerst, danach, True, nachweis)["wert"]
    assert zuerst == "2030-02-12"
    assert danach == "2030-03-15"
    assert ende == danach


def test_untervermaechtnis_kuerzung_wirkt_auf_naechste_beschwerung():
    verweigerung = bgbcalc.untervermaechtnis_verweigerungsbetrag(
        "80", "100", True, "Synthetisch A erhält80 und schuldet B aus Untervermächtnis100",
    )["wert"]
    bei_b = Fraction(100) - als_bruch(verweigerung)
    kuerzung = bgbcalc.vermaechtnis_beschwerungskuerzung(
        "100", str(bei_b), "50", "untervermaechtnis_2187", False, True,
        "Synthetisch A übt Verweigerung20 aus; B erhält80 statt100 und darf eigene Beschwerung50 proportional kürzen",
    )["wert"]
    assert als_bruch(verweigerung) == 20
    assert als_bruch(kuerzung["verbleibensquote"]) == Fraction(4, 5)
    assert als_bruch(kuerzung["gekuerzte_beschwerung"]) == 40
    assert als_bruch(kuerzung["kuerzungsbetrag"]) == 10


def test_testamentquoten_und_lasten_nur_beschwerter_erben():
    quoten = bgbcalc.testament_erbquoten(
        [dict(erbe_id="A", bestimmter_erbteil="0.25"), dict(erbe_id="B", bestimmter_erbteil="0.5")],
        False, True, "Synthetisch A/B mit festen Quoten und gesetzlichem Rest1/4",
    )["wert"]
    beschwerte = [dict(beschwerter_id=e["erbe_id"], gewicht=e["erbquote"]) for e in quoten["erbquoten"]]
    lasten = bgbcalc.vermaechtnis_lastenanteile(
        "120", beschwerte, "erben", "vermaechtnis", True,
        "Synthetisch nur A/B mit derselben Last beschwert, gesetzliche Resterben ausdrücklich unbelastet",
    )["wert"]
    assert als_bruch(quoten["rest_gesetzliche_erbfolge"]) == Fraction(1, 4)
    assert [als_bruch(e["lastbetrag"]) for e in lasten] == [40, 80]
    assert [als_bruch(e["lastquote"]) for e in lasten] == [Fraction(1, 3), Fraction(2, 3)]


def test_eigenpflichtteilsschutz_und_beschenktennachrang():
    schutz = bgbcalc.pflichtteilsergaenzung_eigenpflichtteilsschutz(
        "100", "50", "20", "40", True, "Synthetisch Erbe macht eigenen Schutz70 geltend",
    )["wert"]
    rang = bgbcalc.pflichtteilsergaenzung_beschenktenrang(
        schutz["verweigerungsbetrag"],
        [dict(beschenkter_id="frueher", schenkungsrang=1, haftungsgrenze="20"),
         dict(beschenkter_id="spaeter", schenkungsrang=2, haftungsgrenze="3")],
        True, "Synthetisch Erbe insoweit10 nicht verpflichtet; frühere und spätere Schenkung rechtlich geordnet",
    )["wert"]
    assert als_bruch(schutz["verweigerungsbetrag"]) == 10
    assert [als_bruch(x["haftungsbetrag"]) for x in rang["zugeordnete_haftung"]] == [7, 3]
    assert als_bruch(rang["nicht_gedeckter_fehlbetrag"]) == 0


def test_nachlasseinreden_haben_unterschiedliche_endgrenzen():
    for tag in ("2030-03-01", "2031-02-01"):
        kurz = bgbcalc.nachlass_dreimonatseinrede(
            "2030-02-01", "2030-01-01", "2030-03-01", tag, False, False,
            "Synthetisch früher Verwaltungspfleger und rechtzeitig errichtetes Inventar",
        )["wert"]
        aufgebot = bgbcalc.nachlass_aufgebotseinrede(
            "2030-02-01", "2030-01-01", "2030-02-15", "2031-01-01", True, None,
            tag, False, False, "Synthetisch rechtzeitig zugelassenes Aufgebot ohne rechtskräftige Beendigung",
        )["wert"]
        assert kurz["fristbeginnereignis_am"] == aufgebot["fristbeginnereignis_am"] == "2030-01-01"
        assert kurz["dreimonatsfristende"] == "2030-04-01"
        assert kurz["verweigerungsrecht_am_prueftag"] is False
        assert aufgebot["verweigerungsrecht_am_prueftag"] is True


def test_inventargrundfrist_und_ehegatten_mindestende():
    grund = bgbcalc.inventarfrist_grundrahmen(
        "2030-01-31", "2030-01-01", "2030-02-28", True,
        "Synthetisch erstmalige Monatsfrist ab Zustellung nach Annahme",
    )["wert"]
    ehe = bgbcalc.inventarfrist_ehegatten(
        grund["einmonatsgrenze"], "2030-03-31", True, True, True, True,
        "Synthetisch Gesamtgut und gemeinschaftliche Verwaltung, beide Fristen bestimmt, Inventar des anderen wirksam",
    )["wert"]
    assert grund["bestimmtes_ende_im_sollrahmen"] is True
    assert ehe["inventarfristende_erbe"] == "2030-03-31"
    assert ehe["inventar_kommt_erben_zustatten"] is True


def test_besitzrueckerlangung_erhaelt_ersitzungsperiode():
    ausnahme = bgbcalc.ersitzung_besitzverlust_nichtunterbrechung(
        "2028-01-01", "2030-01-01", "2029-01-01", "2029-06-01", "2028-12-01",
        True, True, "Tatsächliche Rückerlangung mittels rechtzeitig erhobener Klage",
    )["wert"]
    erwerb = bgbcalc.ersitzung_bewegliche_sache(
        "2020-01-01", "2030-01-01", "2030-01-01", None, True, True,
        ausnahme["unterbrechung_gilt_als_nicht_erfolgt"], True,
        "Sonstiger Besitzverlauf und fehlende Hemmung unabhängig qualifiziert",
    )["wert"]
    assert ausnahme["wiedererlangung_binnen_jahresfrist"] is False
    assert ausnahme["wiedererlangung_durch_rechtzeitige_klage"] is True
    assert erwerb["eigentum_durch_ersitzung_erworben"] is True


def test_ersatzerbenvorrang_verhindert_doppelte_anwachsung():
    original = [dict(erbe_id="A", erbquote="0.5", gemeinschaft_id=None),
        dict(erbe_id="B", erbquote="0.3", gemeinschaft_id=None),
        dict(erbe_id="C", erbquote="0.2", gemeinschaft_id=None)]
    ersatz = bgbcalc.ersatzerben_quoten("0.5", [
        dict(erbe_id=e["erbe_id"], urspruenglicher_erbteil=e["erbquote"],
            gleicher_gemeinschaftlicher_erbteil=False) for e in original[1:]],
        True, True, "Wirksam berufene gegenseitige Ersatzerben B und C")
    assert ersatz["wert"]["ersatzerbquoten"][0]["zusaetzlicher_erbteil"] == {"zaehler": "3", "nenner": "10"}
    anwachsung = bgbcalc.erbteil_anwachsungsquoten(original, "A", True, False,
        ersatz["status"] == "BERECHNET", "Derselbe Wegfall wird bereits durch Ersatzerben aufgefangen")["wert"]
    assert anwachsung["anwachsung_erfolgt"] is False
    assert all(e["angewachsener_erbteil"] == {"zaehler": "0", "nenner": "1"} for e in anwachsung["erbteile"])


def test_gesamtgutszuwendung_vor_pflichtteilsergaenzung_zuordnen():
    bewertung = bgbcalc.pflichtteil_schenkungswert("100", "80", False, False,
        "Vergleichbare Werte, keine Pflicht- oder Anstandsschenkung")["wert"]
    zuordnung = bgbcalc.gesamtgutszuwendung_anteile(bewertung, "keine", "keine", True,
        "Gemeinsames Gesamtgut ohne Sonderzuordnung")["wert"]
    ergaenzung = bgbcalc.pflichtteilsergaenzung_grundbetrag("200", zuordnung["betrag_ehegatte_1"],
        1, 2, True, "Erbfall des ersten Ehegatten; qualifizierte Drittschenkung im ersten Jahr, keine weiteren Anrechnungen")["wert"]
    assert zuordnung["betrag_ehegatte_1"] == {"zaehler": "40", "nenner": "1"}
    assert ergaenzung["ergaenzungsgrundbetrag"] == {"zaehler": "10", "nenner": "1"}


def test_qualifizierte_nacherbfolge_und_angeordneter_teilungsausschluss():
    nacherbe = bgbcalc.nacherbeneinsetzung_dreissigjahresgrenze("2000-01-01", "2031-01-01",
        None, "personenereignis", True, False,
        "Vorerbe bei Erbfall lebend; Nacherbfolge auf dessen noch nicht eingetretenen Tod angeordnet")["wert"]
    sonstige_voraussetzungen_geprueft = True
    qualifiziert = sonstige_voraussetzungen_geprueft and not nacherbe["unwirksam_wegen_dreissigjahresgrenze"]
    ohne = bgbcalc.erbauseinandersetzung_dreissigjahresgrenze("2000-01-01", "2031-01-01",
        "keine", None, False, qualifiziert, "Wirksamer Teilungsausschluss ohne besonderen Fortdauerendpunkt")["wert"]
    mit = bgbcalc.erbauseinandersetzung_dreissigjahresgrenze("2000-01-01", "2031-01-01",
        "nacherbfolge", None, False, qualifiziert, "Wirksamer Teilungsausschluss ausdrücklich bis zur separat qualifizierten Nacherbfolge")["wert"]
    assert qualifiziert is True
    assert ohne["zeitliche_wirkung_beendet"] is True
    assert mit["zeitliche_wirkung_beendet"] is False


def test_testamentsaltersgrenzen_2229_2247():
    # Nur numerische Altersgrenzen, keine Feststellung der Testierfähigkeit.
    sechzehn = bgbcalc.lebensalter_beginn("2012-02-29", 16)["wert"]
    achtzehn = bgbcalc.volljaehrigkeitsbeginn("2012-02-29")["wert"]
    assert sechzehn == "2028-02-29"
    assert achtzehn == "2030-03-01"
    assert "2030-02-28" < achtzehn <= "2030-03-01"


def test_pflichtteilsquote_2310_mit_enterbtem_ohne_verzichtenden():
    # Qualifiziert: A und enterbtes B mitzählen, kinderlos verzichtendes C nicht.
    quoten = bgbcalc.abkoemmlings_erbquoten([knoten("A"), knoten("B")], 1, 1)["wert"]
    quote = next(e["quote"] for e in quoten["erbquoten"] if e["person_id"] == "A")
    betrag = bgbcalc.pflichtteil_betrag("120", int(quote["zaehler"]), int(quote["nenner"]),
        "0", False, True, "§2310: B enterbt, C wirksam verzichtend und kinderlos; kein Ehegatte, keine Ausgleichung")["wert"]
    assert als_bruch(quote) == Fraction(1, 2)
    assert als_bruch(betrag) == 30


def test_einkindfiktion_1963_2141_quotenbasis():
    ehe = bgbcalc.ehegatten_erbquote("erste_ordnung", "zugewinngemeinschaft", 2, 0, 1,
        True, False, False, False, False)["wert"]
    anteil = als_bruch(ehe["verwandtenquote"])
    kinder = bgbcalc.abkoemmlings_erbquoten([knoten("vorhandenes_kind"), knoten("erwartetes_einzelkind")],
        anteil.numerator, anteil.denominator)["wert"]
    assert als_bruch(ehe["ehegattenquote"]) == Fraction(1, 2)
    assert all(als_bruch(k["quote"]) == Fraction(1, 4) for k in kinder["erbquoten"])
    # Die erwartete Geburt wird auch bei Mehrlingserwartung nur einmal eingesetzt.
    # Angemessener Unterhalt selbst ist eine gesonderte qualifizierte Bewertung.


def test_nachlassgeld_zinsen_2218_668():
    zins = bgbcalc.gesetzliche_zinsen("1200", 1, 2,
        "§2218 i.V.m.§668: bestimmungswidrig verwendetes Geld; qualifiziertes halbes Zinsjahr", False)["wert"]
    assert als_bruch(zins) == 24


def test_beschwerungskenntnis_2306_fristbeginn():
    kenntnis_berufung = "2030-01-01"
    bekanntgabe = "2030-01-10"
    kenntnis_beschwerung = "2030-02-01"
    beginn = max(kenntnis_berufung, bekanntgabe, kenntnis_beschwerung)
    # Qualifizierter Inlandsfall ohne Hemmung: sechs Wochen nach spätestem Auslöser.
    assert bgbcalc.fristende(beginn, 6, "wochen", "ereignis")["wert"] == "2030-03-15"


def test_erbunwuerdigkeit_2340_2345_fristverweis():
    jahresende = bgbcalc.fristende("2029-07-01", 1, "jahre", "ereignis")["wert"]
    frist = bgbcalc.testament_anfechtungsfrist("2000-01-01", "2029-07-01", jahresende,
        "2030-01-01", True, "§2340III/§2345: entsprechende2082-Zeitgrenzen; Anfall und Kenntnis qualifiziert, keine Hemmung")["wert"]
    assert frist["massgebliche_kalendergrenze"] == "2030-01-01"
    assert frist["anfechtung_fristgerecht"] is True
