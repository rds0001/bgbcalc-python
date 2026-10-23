# Gesetzliche Ehegattenquote

## ehegatten_erbquote

Grundquote erste Ordnung 1/4, zweite/Großeltern 1/2, ohne erste/zweite/Großeltern 1. Bei Gütertrennung und ein/zwei Kinderstämmen 1/(Stämme+1). Bei Zugewinngemeinschaft grundsätzlich +1/4, außer bereits Alleinerbe. Im Großelternfall anschließend den auf Abkömmlinge entfallenden Teil des verbleibenden Verwandtenanteils zuschlagen. Restquote verbleibt Verwandten. § 1933 durch jeweilige UND-Verknüpfungen prüfen.

Gesetzliche erbrechtliche Lösung für überlebenden Ehegatten bei deutschem Erb- und Güterrecht. Erbverzicht, Ausschlagung, Erbunwürdigkeit, abweichende letztwillige Verfügungen und internationale Zuordnung vorab gesondert prüfen. Keine Pflichtteilsquote oder güterrechtliche Lösung nach § 1371 Abs. 2/3. ohne_erbquoten_sonderregel setzt rechtlich geprüfte Nichtanwendung der Zuschlags-/Gütertrennungsregel voraus. Kinderstämme zählen einschließlich Vertretung, nicht sämtliche Enkel einzeln. Großelternabkömmlingsquote ist reine §-1926-Quote bei gedachtem Verwandtenanteil 1; Ehegattenquote noch nicht darin enthalten. § 1934-Verwandtenerbteil des Ehegatten sowie Voraus § 1932 separat. Großeltern-Zuschlag folgt der dokumentierten Auslegung in entscheidung_1931_reihenfolge.json. Komposition: Bei erster/zweiter Ordnung kann die verbleibende Verwandtenquote unmittelbar in die passende Stammverteilung eingehen. Im Großelternfall nicht die endgültige Restquote nochmals auf Großeltern und Abkömmlinge verteilen. Stattdessen den Anteil vor dem Abkömmlingszuschlag nach § 1926 verteilen und die Abkömmlingsanteile dem Ehegatten zuweisen; nur unmittelbar berufene Großeltern behalten ihre so bestimmten Anteile.

wert enthält grundquote, zugewinnzuschlag, grosselternabkoemmlingszuschlag, ehegattenquote und verwandtenquote als exakte Brüche. Ehegatten- und Verwandtenquote summieren sich zu 1. Bei fehlender Ehe oder §-1933-Ausschluss NICHT_ANWENDBAR.

- `konstellation`: erste_ordnung, zweite_ordnung, grosseltern oder keine_ersten_zweiten_und_keine_grosseltern. Maßgeblich sind rechtlich berufene Verwandte und der Vorrang der Ordnungen.
- `gueterstand`: zugewinngemeinschaft, guetertrennung oder ohne_erbquoten_sonderregel. Letzteres ist eine vorab rechtlich eingeordnete Konstellation ohne beide genannten Sonderregeln, beispielsweise einschlägige Gütergemeinschaft; keine automatische Prüfung anderer Güterstände.
- `anzahl_kinderstaemme`: Ganze Zahl 0 bis 10000. Bei erster Ordnung Anzahl besetzter Kinderstämme, mindestens 1; bei anderen Konstellationen 0. Vertretene Kinderstämme einmal zählen, nicht ihre sämtlichen Nachkommen.
- `grosselternabkoemmlingsquote_zaehler`: Nichtnegative ganze Zahl als Zähler der reinen Abkömmlingsquote nach § 1926 ohne Ehegattenanteil. Nur im Großelternfall von null verschieden.
- `grosselternabkoemmlingsquote_nenner`: Positive ganze Zahl als Nenner. Quote muss unter 1 bleiben, weil im Großelternfall unmittelbar berufene Großeltern vorhanden sein müssen.
- `ehe_beim_erbfall`: Expliziter Wahrheitswert zum Bestehen der Ehe beim Erbfall.
- `scheidungsvoraussetzungen_erfuellt`: Expliziter Wahrheitswert: Scheidungsvoraussetzungen waren beim Erbfall erfüllt.
- `erblasser_scheidung_beantragt_oder_zugestimmt`: Expliziter Wahrheitswert: Der Erblasser hatte die Scheidung beantragt oder ihr zugestimmt. Ausschluss nur zusammen mit erfüllten Scheidungsvoraussetzungen.
- `erblasser_aufhebungsberechtigt`: Expliziter Wahrheitswert: Erblasser war zur Beantragung der Eheaufhebung berechtigt.
- `erblasser_aufhebung_beantragt`: Expliziter Wahrheitswert: Erblasser hatte Eheaufhebung beantragt. Ausschluss nur zusammen mit Aufhebungsberechtigung.

Im Großelternfall ist die Reihenfolge in [entscheidung_1931_reihenfolge.json](../../fachkonzept/entscheidung_1931_reihenfolge.json) begründet. Die externe Recherche betrifft nur diesen Auslegungspunkt; maßgebliche Normtexte stammen aus der lokalen PDF.
