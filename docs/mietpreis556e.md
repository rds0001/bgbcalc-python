<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mietpreisbegrenzung_modernisierungsalternative

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `grund_oder_vormietgrenze`: Bereits berechnete nutzbare Monatsgrenze des Grund-/Vormietwegs; etwa Ergebnis mietpreisbegrenzung_vormietgrenze.
- `grundbetrag_ohne_modernisierung`: 556d-Grundbetrag auf Basis der Vergleichsmiete OHNE betrachtete Modernisierung, grundsätzlich110Prozent dieser qualifizierten Vergleichsmiete.
- `modernisierung_monatlich`: Mit559I–IIIa/559aI–IV berechneter hypothetischer monatlicher Erhöhungsbetrag; nicht bloße Kosten oder ungeprüfter Zwischenbetrag. Vorhandene Kosten-/Förder-/Kappungskerne verwenden.
- `modernisierungsprivileg_nutzbar`: Expliziter Wahrheitswert: Maßnahmen im maßgeblichen Dreijahresfenster, gesetzlicher Anwendungsfall und Auskunftslage erlauben diesen Weg.
- `einordnungsnachweis`: Rechtliche Nutzbarkeit, Vergleichsmiete ohne Modernisierung, zugehörige Maßnahmen und vorgeschaltete hypothetische Erhöhungsrechnung nachweisen.

Eigenständigen Modernisierungsweg berechnen und bei rechtlicher Nutzbarkeit mit bisheriger Monatsgrenze vergleichen.

Optionaler Modernisierungsalternativbetrag und höhere nutzbare Monatsgrenze, exakte EUR-Brüche.

556eII-Alternativweg: Grundbetrag auf unmodernisierter Vergleichsmiete plus hypothetischer559/559a-Erhöhung; anschließend höherer nutzbarer Betrag gegenüber eigenständigem Grund-/Vormietweg. Niemals Modernisierungszuschlag zusätzlich auf die Vormiete aufschlagen. Bei nicht nutzbarem Privileg bleibt nur bisheriger Weg; hypothetischer Alternativbetrag wird dann nicht ausgegeben. Keine doppelte Einbeziehung der Modernisierung in Vergleichsmiete und Zuschlag. Zeitliche Dreijahreszuordnung, Maßnahmenqualifikation und556g-Auskunft sind rechtliche Eingaben. Die rechtliche Förderabzugs-/Kappungsreihenfolge bleibt bei einschlägiger Konkurrenz ausdrücklich vorzugeben; kein neuer Standard dafür.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556e_T0001, BGB_556e_T0002, BGB_556e_T0003, BGB_556e_T0004

```python
from bgbcalc import mietpreisbegrenzung_modernisierungsalternative
mietpreisbegrenzung_modernisierungsalternative(
    grund_oder_vormietgrenze='950',
    grundbetrag_ohne_modernisierung='880',
    modernisierung_monatlich='100',
    modernisierungsprivileg_nutzbar=True,
    einordnungsnachweis='556eII-Alternativweg: Grundbetrag auf unmodernisierter Vergleichsmiete plus hypothetischer559/559a-Erhöhung; anschließend höherer nutzbarer Betrag gegenüber eigenständigem Grund-/Vormietweg. Niemals Modernisierungszuschlag zusätzlich auf die Vormiete aufschlagen. Bei nicht nutzbarem Privileg bleibt nur bisheriger Weg; hypothetischer Alternativbetrag wird dann nicht ausgegeben. Keine doppelte Einbeziehung der Modernisierung in Vergleichsmiete und Zuschlag. Zeitliche Dreijahreszuordnung, Maßnahmenqualifikation und556g-Auskunft sind rechtliche Eingaben. Die rechtliche Förderabzugs-/Kappungsreihenfolge bleibt bei einschlägiger Konkurrenz ausdrücklich vorzugeben; kein neuer Standard dafür.',
)
```

## mietpreisbegrenzung_vormiete_bereinigen

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `letzte_geschuldete_monatsmiete`: Zuletzt rechtlich geschuldete Monatsmiete nach tatsächlicher Mietminderung, nicht tatsächlicher Zahlungseingang oder bloß geforderte Vertragsmiete.
- `minderungsbetrag`: In dieser Monatsmiete wirksam enthaltene Minderung in EUR, die556eI2 unberücksichtigt lässt.
- `auszunehmende_erhoehungsbetraege`: Liste0..1000 nichtnegativer monatlicher Erhöhungsanteile, die innerhalb des letzten Jahres vor Vertragsende mit dem Vormieter vereinbart wurden. Rechtlich und zeitlich qualifizierte, in der ungeminderten letzten Monatsmiete noch enthaltene, überschneidungsfreie Betragskomponenten; keine Prozentangaben.
- `bereinigungsnachweis`: Nachweis rechtlich geschuldeter Miete, Minderungsbetrag und zeitlich/inhaltlich ausgeschlossener Erhöhungsanteile; keine bloße Istzahlung.

Minderungsbetrag hinzurechnen, ausgeschlossene Erhöhungsanteile summieren und abziehen.

Ungeminderte Monatsmiete, ausgeschlossene Erhöhungssumme und bereinigte Vormiete als exakte EUR-Brüche.

556eI2: zunächst Minderung aus letzter geschuldeter Monatsmiete herausrechnen, dann Summe der rechtlich ausgeschlossenen Erhöhungsanteile abziehen. Das Ergebnis ist Eingabe für vorhandenen Vormietgrenzenkern. Erhöhungsanteile nach tatsächlicher Wirkung in der ungeminderten letzten Miete bestimmen; verkettete Prozentänderungen oder später aufgehobene Erhöhungen nicht doppelt zählen. Rechtswirksamkeit, zeitliche Einordnung ins letzte Jahr, Staffel-/Indexsonderfälle und Nutzbarkeit nach556g sind vorqualifiziert. Keine automatische Vertragszeitreihenbewertung. Abzüge oberhalb ungeminderter Miete sind widersprüchliche Eingaben und werden nicht still auf null gekappt.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_556e_T0001, BGB_556e_T0002

```python
from bgbcalc import mietpreisbegrenzung_vormiete_bereinigen
mietpreisbegrenzung_vormiete_bereinigen(
    letzte_geschuldete_monatsmiete='900',
    minderungsbetrag='100',
    auszunehmende_erhoehungsbetraege=['50', '25'],
    bereinigungsnachweis='556eI2: zunächst Minderung aus letzter geschuldeter Monatsmiete herausrechnen, dann Summe der rechtlich ausgeschlossenen Erhöhungsanteile abziehen. Das Ergebnis ist Eingabe für vorhandenen Vormietgrenzenkern. Erhöhungsanteile nach tatsächlicher Wirkung in der ungeminderten letzten Miete bestimmen; verkettete Prozentänderungen oder später aufgehobene Erhöhungen nicht doppelt zählen. Rechtswirksamkeit, zeitliche Einordnung ins letzte Jahr, Staffel-/Indexsonderfälle und Nutzbarkeit nach556g sind vorqualifiziert. Keine automatische Vertragszeitreihenbewertung. Abzüge oberhalb ungeminderter Miete sind widersprüchliche Eingaben und werden nicht still auf null gekappt.',
)
```
