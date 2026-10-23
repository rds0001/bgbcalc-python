# Altersabhängige rechtliche Voraussetzungen

## geschaeftsfaehigkeit_altersvoraussetzungen

Vollendete Lebensjahre am Stichtag bestimmen und die Altersbereiche unter7, ab7bis unter18 und ab18 unterscheiden. Am29.Februar Geborene erreichen in Nichtschaltjahren die nächste Altersstufe am1.März.

- `geburtsdatum`: Tatsächliches Geburtsdatum als ISO-Zeichenfolge YYYY-MM-DD. Der Tag wird bei der Altersberechnung nach §187 Abs.2 mitgerechnet; die Geburtsuhrzeit ist für diese Altersstufen nicht maßgeblich. Keine Aussage zum tatsächlichen Beginn der Rechtsfähigkeit vor der Geburt.
- `stichtag`: ISO-Datum des Tages, für den die Altersstufe benötigt wird; darf nicht vor der Geburt liegen. Der nächste Geburtstag wird nicht jenseits des unterstützten Kalenders vorausberechnet.

wert enthält vollendete_lebensjahre und die drei Wahrheitswerte unter_sieben, minderjaehrig_ab_sieben und volljaehrig. Genau eine Alterskategorie trifft zu.

Nur Altersvoraussetzungen nach §§104 Nr.1 und106 in Verbindung mit §2. Keine abschließende Einordnung der Geschäftsfähigkeit; insbesondere §104 Nr.2 und §105 Abs.2 sowie die Regeln der §§107bis113 bleiben gesondert. Volljährigkeit bedeutet hier keine Zusicherung uneingeschränkter Geschäftsfähigkeit. Keine Entscheidung über ein konkretes Rechtsgeschäft.

## delikt_altersvoraussetzungen

Unter7 Ausschluss nach §828 Abs.1. Ab7 und unter10 bei sachlich anwendbarem Unfallprivileg Ausschluss nach Abs.2, außer vorsätzlich herbeigeführter Verletzung. Soweit Abs.1/2 nicht ausschließen, unter18 Ausschluss nach Abs.3 bei fehlender erforderlicher Einsicht. Ab18 kein Ausschluss durch §828.

- `geburtsdatum`: Tatsächliches Geburtsdatum als ISO-Zeichenfolge YYYY-MM-DD. Der Tag wird bei der Altersberechnung nach §187 Abs.2 mitgerechnet; die Geburtsuhrzeit ist für diese Altersstufen nicht maßgeblich. Keine Aussage zum tatsächlichen Beginn der Rechtsfähigkeit vor der Geburt.
- `handlungstag`: ISO-Datum der schädigenden Handlung; darf nicht vor der Geburt liegen. Das Lebensalter wird auf diesen Tag bezogen, nicht auf einen späteren Zahlungs- oder Gerichtstermin.
- `unfallprivileg_sachlich_anwendbar`: Expliziter Wahrheitswert zur rechtlich bewerteten sachlichen Anwendbarkeit des Unfallprivilegs nach §828 Abs.2 bei Unfall mit Kraftfahrzeug, Schienenbahn oder Schwebebahn. Altersgrenzen und Vorsatzausnahme nicht in diesen Wert vorwegnehmen; sie werden berechnet. Die sachliche Einordnung wird nicht automatisch aus einem beliebigen Fahrzeugkontakt hergeleitet.
- `verletzung_vorsaetzlich`: Expliziter Wahrheitswert zur vorsätzlichen Herbeiführung der Verletzung. TRUE beseitigt nur den Ausschluss des §828 Abs.2, nicht pauschal den Altersausschluss unter7 oder die Prüfung des Absatzes3.
- `erforderliche_einsicht_vorhanden`: Expliziter Wahrheitswert, ob bei Begehung der schädigenden Handlung die zur Erkenntnis der Verantwortlichkeit erforderliche Einsicht vorlag. Keine automatische psychologische Bewertung. Erst subsidiär nach Absätzen1/2 und nur unter18 berücksichtigt. Alle Wahrheitswerte müssen ausdrücklich vorliegen, auch wenn der Alterszweig sie im Einzelfall nicht benötigt.

wert enthält vollendete_lebensjahre, ausschluss_nach_absatz_1, ausschluss_nach_absatz_2, ausschluss_nach_absatz_3 und verantwortlichkeit_nach_828_ausgeschlossen. Der Gesamtausschluss ist die Vereinigung der drei gesetzlichen Zweige; deren Vorrang wird berücksichtigt.

Kein vollständiger Schadensersatzanspruch oder allgemeiner Haftungsstatus. Sachlicher Anwendungsbereich des Unfallprivilegs, Vorsatz und Einsicht sind ausdrücklich bewertete Nutzervorgaben. FALSE beim Gesamtausschluss bedeutet lediglich keinen Ausschluss nach dieser Regel; Tatbestand, §827, Billigkeitshaftung nach §829, Aufsichtspflichten und weitere Normen sind gesondert. Keine automatische Feststellung psychischer Zustände oder tatsächlicher Unfallumstände.

