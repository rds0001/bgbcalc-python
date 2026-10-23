"""Relative Ersatzerbquoten und Gruppenrang (§§2098/2099)."""

from .betraege import _wahrheitswert
from .kalender import _ergebnis, _fehler, _text, _vorhanden
from .zahlen import _addieren, _bruch, _dividieren, _multiplizieren, _zahleneingabe
from .zinsen import _bruchteile


def ersatzerben_quoten(
    weggefallener_erbteil=None,
    ersatzerben=None,
    gegenseitige_ersatzerbeneinsetzung=None,
    auslegungsregel_anwendbar=None,
    einordnungsnachweis=None,
):
    """Einen weggefallenen Anteil nach ursprünglichen Quoten auf berufene Ersatzerben verteilen."""
    _vorhanden(weggefallener_erbteil, "weggefallener_erbteil")
    weggefallen = _zahleneingabe(weggefallener_erbteil)
    if not 0 < weggefallen <= 1:
        _fehler(
            "weggefallener_erbteil",
            "Weggefallener Anteil muss positiv und höchstens eins sein.",
        )
    _vorhanden(ersatzerben, "ersatzerben")
    if not isinstance(ersatzerben, list) or not 1 <= len(ersatzerben) <= 1000:
        _fehler(
            "ersatzerben",
            "Liste mit 1 bis 1000 rechtlich berufenen Ersatzerben erforderlich.",
        )
    namen, quoten, gruppe = [], [], []
    summe = _bruch(0)
    for eintrag in ersatzerben:
        if not isinstance(eintrag, dict) or set(eintrag) != {
            "erbe_id",
            "urspruenglicher_erbteil",
            "gleicher_gemeinschaftlicher_erbteil",
        }:
            _fehler(
                "ersatzerben",
                "Genau erbe_id, urspruenglicher_erbteil und gleicher_gemeinschaftlicher_erbteil erforderlich.",
            )
        name = _text(eintrag["erbe_id"], "erbe_id")
        if name in namen:
            _fehler("erbe_id", "Ersatzerben nicht doppelt aufführen.")
        _vorhanden(eintrag["urspruenglicher_erbteil"], "urspruenglicher_erbteil")
        quote = _zahleneingabe(eintrag["urspruenglicher_erbteil"])
        if not 0 < quote <= 1:
            _fehler(
                "urspruenglicher_erbteil",
                "Ursprünglicher Erbteil muss positiv und höchstens eins sein.",
            )
        _wahrheitswert(
            eintrag["gleicher_gemeinschaftlicher_erbteil"],
            "gleicher_gemeinschaftlicher_erbteil",
        )
        namen.append(name)
        quoten.append(quote)
        gruppe.append(eintrag["gleicher_gemeinschaftlicher_erbteil"])
        summe = _addieren(summe, quote)
    if _addieren(summe, weggefallen) > 1:
        _fehler(
            "ersatzerben",
            "Ursprüngliche persönliche Erbteile und weggefallener Anteil dürfen zusammen eins nicht überschreiten.",
        )
    _wahrheitswert(
        gegenseitige_ersatzerbeneinsetzung, "gegenseitige_ersatzerbeneinsetzung"
    )
    _wahrheitswert(auslegungsregel_anwendbar, "auslegungsregel_anwendbar")
    _text(einordnungsnachweis, "einordnungsnachweis")
    eingaben = dict(
        weggefallener_erbteil=weggefallener_erbteil,
        ersatzerben=ersatzerben,
        gegenseitige_ersatzerbeneinsetzung=gegenseitige_ersatzerbeneinsetzung,
        auslegungsregel_anwendbar=auslegungsregel_anwendbar,
        einordnungsnachweis=einordnungsnachweis,
    )
    wert = None
    if auslegungsregel_anwendbar:
        vorrang = gegenseitige_ersatzerbeneinsetzung and any(gruppe)
        ausgewaehlt = [not vorrang or g for g in gruppe]
        verteilungssumme = _bruch(0)
        for q, gilt in zip(quoten, ausgewaehlt):
            if gilt:
                verteilungssumme = _addieren(verteilungssumme, q)
        anteile = []
        for name, q, gilt in zip(namen, quoten, ausgewaehlt):
            relativ = _dividieren(q, verteilungssumme) if gilt else _bruch(0)
            anteile.append(
                dict(
                    erbe_id=name,
                    anteil_am_weggefallenen_erbteil=_bruchteile(relativ),
                    zusaetzlicher_erbteil=_bruchteile(
                        _multiplizieren(weggefallen, relativ)
                    ),
                )
            )
        wert = dict(
            gruppenvorrang_angewandt=vorrang,
            ersatzerbquoten=anteile,
            verbleibender_anteil_fuer_anwachsung=_bruchteile(_bruch(0)),
        )
    ergebnis = _ergebnis(
        wert,
        "erbquoten",
        "BGB_ERSATZERBEN_QUOTEN",
        eingaben,
        [
            dict(
                operation="Bei gegenseitiger Einsetzung vorrangige Mitberechtigte desselben gemeinschaftlichen Erbteils auswählen; ursprüngliche Erbteile der ausgewählten Personen normieren und weggefallenen Anteil proportional verteilen"
            )
        ],
        eingaben.copy(),
    )
    ergebnis["status"] = "BERECHNET" if wert is not None else "NICHT_ANWENDBAR"
    ergebnis["annahmen"] = [
        "Ein einzelner weggefallener persönlicher Erbteil; Kreis tatsächlich berufener Ersatzerben und ursprüngliche persönliche Quoten sind rechtlich bestimmt; keine abweichende testamentarische Anordnung."
    ]
    ergebnis["hinweise"] = [
        "§2098 Absatz1 ist Zweifelsregel bei gegenseitiger Einsetzung oder Einsetzung der übrigen Erben für einen Erben. Anwendbarkeit und Berufung einschließlich§§2096/2097 ausdrücklich vorqualifizieren; keine automatische Testamentsauslegung. Gruppenvorrang Absatz2 nur bei gegenseitiger Einsetzung und tatsächlich berufenen Mitberechtigten desselben gemeinschaftlichen Erbteils. Persönliche Quote am Gesamtnachlass verwenden, nicht gesamte Gruppenquote mehrfach eingeben. Nicht ausgewählte Ersatzerben erhalten aus diesem Wegfall null; ihre ursprünglichen Erbteile bleiben unberührt. Einsetzungsvoraussetzungen, Überleben, Ausschlagung und weitere Wegfälle vorab prüfen. Kein kaskadierender Mehrfachwegfall. Ersatzerbrecht geht§2099 zufolge Anwachsung vor: der hier vollständig verteilte Anteil verbleibt nicht zusätzlich zur Anwachsung. Gesamtquoten nach weiteren Wegfällen oder andere Erwerbsgründe werden nicht berechnet."
    ]
    return ergebnis
