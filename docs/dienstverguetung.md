<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## dienstverguetung_annahmeverzug

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_verguetung`: Nichtnegative vereinbarte Vergütung in EUR für die gerade wegen Annahmeverzugs beziehungsweise zugeordneten Arbeitsausfallrisikos nicht geleisteten Dienste im rechtlich abgegrenzten Zeitraum. Kein beliebiger Monatslohn bei nur teilweisem Ausfall.
- `ersparte_aufwendungen`: Nichtnegativer rechtlich anrechenbarer Wert der infolge desselben Dienstausfalls ersparten Aufwendungen in EUR. Keine ohnehin unverändert anfallenden Kosten abziehen.
- `anderweitiger_erwerb`: Nichtnegativer rechtlich anrechenbarer Erwerb durch anderweitige Verwendung derselben Dienste im maßgeblichen Zeitraum in EUR. Zeitliche/kausale Anrechenbarkeit und konsistente Brutto-/Nettobezüge vorab bestimmen; unabhängig ohnehin vorhandener Nebenverdienst nicht ungeprüft gleichsetzen.
- `boeswillig_unterlassener_erwerb`: Nichtnegativer rechtlich bewerteter Betrag in EUR des böswillig unterlassenen anderweitigen Erwerbs für denselben Ausfall. Kein pauschal geschätztes fiktives Gehalt und keine automatische Sanktion für fehlende Bewerbungen. Nicht zugleich im tatsächlichen anderweitigen Erwerb enthalten.
- `annahmeverzug`: Wahrheitswert des rechtlich festgestellten Annahmeverzugs des Dienstberechtigten. Leistungsfähigkeit/-willigkeit, Angebot und sonstige Voraussetzungen vorab prüfen.
- `arbeitgeber_traegt_arbeitsausfallrisiko`: Wahrheitswert des rechtlich dem Arbeitgeber zugewiesenen Arbeitsausfallrisikos nach§615 Satz3. Bloßer Ausfall oder allgemeine Betriebsstörung genügt nicht automatisch.
- `bewertungsnachweis`: Nichtleere Beschreibung von Dienst-/Arbeitsverhältnis, Ausfallzeitraum, Annahmeverzug/Risikozuordnung und kausal/zeitlich anrechenbaren überschneidungsfreien Geldwerten. Sondergesetze und abweichende zulässige Regelungen gesondert.

Bei Annahmeverzug ODER rechtlich zugeordnetem Arbeitgeber-Arbeitsausfallrisiko Vergütung minus ersparte Aufwendungen minus anderweitiger Erwerb minus böswillig unterlassener Erwerb, mindestens0.

wert ist exakter EUR-Vergütungsrest mindestens0. Fehlender gesetzlicher Ausgangsfall ergibt NICHT_ANWENDBAR/null, keine abschließende Verneinung anderer Vergütung.

Kein automatischer Annahmeverzug, keine generelle Arbeitgeberhaftung für jeden Ausfall, keine erfundene Erwerbsobliegenheit. Abzüge nur rechtlich anrechenbar aus demselben Zeitraum/Ausfall. Sondergesetze wie besondere Kündigungsschutzfolgen separat.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_615_T0001, BGB_615_T0002, BGB_615_T0003

```python
from bgbcalc import dienstverguetung_annahmeverzug
dienstverguetung_annahmeverzug(
    vereinbarte_verguetung='1000',
    ersparte_aufwendungen='0',
    anderweitiger_erwerb='0',
    boeswillig_unterlassener_erwerb='0',
    annahmeverzug=False,
    arbeitgeber_traegt_arbeitsausfallrisiko=True,
    bewertungsnachweis='Synthetisch rechtlich abgegrenzter Dienstausfall mit konsistenten anrechenbaren Werten.',
)
```

## dienstverguetung_persoenliche_verhinderung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vereinbarte_verguetung`: Nichtnegative Vergütung in EUR für den gesamten rechtlich betrachteten persönlichen Verhinderungszeitraum. Nicht künstlich einen kurzen vergüteten Teil aus einem insgesamt erheblichen Zeitraum bilden.
- `gesetzliche_kranken_unfallversicherungsleistung`: Nichtnegativer anrechenbarer Betrag in EUR, der gerade für dieselbe Verhinderungszeit aus einer aufgrund gesetzlicher Verpflichtung bestehenden Kranken- oder Unfallversicherung zukommt. Nicht beliebige private Versicherung, Sozialleistung oder andere Zeiträume.
- `grund_in_der_person`: Wahrheitswert eines rechtlich in der Person des Dienstverpflichteten liegenden Verhinderungsgrundes. Allgemeine äußere Hindernisse nicht ungeprüft gleichsetzen.
- `ohne_verschulden`: Wahrheitswert fehlenden Verschuldens des Dienstverpflichteten an der konkreten Verhinderung. Rechtliche Bewertung ausdrücklich dokumentieren.
- `zeit_verhaeltnismaessig_nicht_erheblich`: Wahrheitswert der rechtlich verhältnismäßig nicht erheblichen Dauer im konkreten Dienstverhältnis. Keine allgemeine Tageszahl vorgegeben; gesamten Verhinderungsfall und maßgebliche Umstände beurteilen.
- `regel_616_anwendbar`: Wahrheitswert der sachlich/zeitlich einschlägigen§616-Regel ohne wirksamen Vertrags-/Tarifausschluss oder vorrangige Sonderregel. FALSE ergibt NICHT_ANWENDBAR.
- `bewertungsnachweis`: Nichtleere Beschreibung von Dienstverhältnis, persönlichem Grund, Verschulden, Dauerbewertung und qualifizierter Versicherungsleistung desselben Zeitraums. Andere Anspruchsgrundlagen separat.

Nur bei anwendbarem§616 und persönlichem Grund ohne Verschulden für rechtlich verhältnismäßig nicht erhebliche Zeit: Vergütung minus qualifizierte Kranken-/Unfallversicherungsleistung, mindestens0.

wert ist exakter EUR-Vergütungsrest mindestens0. Fehlende Voraussetzungen ergeben NICHT_ANWENDBAR/null, nicht zwingend vollständigen Verlust anderer Vergütungsansprüche.

Keine feste Tagesgrenze und keine automatische medizinische Bewertung. Ganze Dauer rechtlich beurteilen; nicht einen kurzen Teil eines insgesamt erheblichen Falls auswählen. Anrechnung nur aus gesetzlich verpflichtender Kranken-/Unfallversicherung für dieselbe Verhinderungszeit.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_616_T0001, BGB_616_T0002

```python
from bgbcalc import dienstverguetung_persoenliche_verhinderung
dienstverguetung_persoenliche_verhinderung(
    vereinbarte_verguetung='500',
    gesetzliche_kranken_unfallversicherungsleistung='0',
    grund_in_der_person=True,
    ohne_verschulden=True,
    zeit_verhaeltnismaessig_nicht_erheblich=True,
    regel_616_anwendbar=True,
    bewertungsnachweis='Synthetisch rechtlich bewertete kurze persönliche Verhinderung ohne Verschulden.',
)
```
