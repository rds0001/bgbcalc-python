<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vergleichsmiete_ausgleich_und_drittmittel

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `ausgangsmiete_drei_jahre`: Rechtlich zutreffende Dreijahres-Ausgangsmiete ohne doppelte559/560-Anteile.
- `nicht_anzurechnende_erhoehungen`: Nach558IIIauszunehmende Erhöhungen als konsistenter Monatsbetrag.
- `derzeitige_monatsmiete`: Rechtlich geschuldete aktuelle Monatsmiete.
- `ortsuebliche_vergleichsmiete`: Qualifizierte Vergleichsmiete vor558V-Förderabzug.
- `gueltige_fuenfzehnprozent_verordnung`: Wahrheitswert der einschlägigen gültigen15%-Verordnung; sonst20%.
- `kapitalzuschuesse_559a_1`: Auf die Wohnung entfallende559aI-Zuschüsse;558Vsetzt8%jährlich an.
- `jaehrliche_zinsermaessigung`: Mit559aII/III-Kern errechneter Jahreszinsvorteil.
- `jaehrliche_laufende_foerderung`: 559aII4-Jahresbetrag laufender Zuschüsse/Darlehen, keine doppelte Kapitalförderung.
- `letzte_monatliche_ausgleichszahlung`: Rechtlich unter558IVfallender weggefallener Monatsbetrag;0wenn keine Ausnahme.
- `ausnahmemodell`: Zwingende rechtliche Wahl: alternative_erhoehungsgrenze oder zusaetzlicher_ausnahmebetrag.
- `methodennachweis`: 558-Anwendbarkeit, Wertgrundlagen,558IV-Tatbestand und Ausnahmemodell ausdrücklich qualifizieren; keine automatische Rechtsauslegung.

558V-Förderabzug berechnen und bereinigte Vergleichsmiete mit zwei ausdrücklich qualifizierten558IV-Kappungsmodellen verbinden.

Jahresförderabzug, bereinigte Vergleichsmiete, beide bedingten Monatsmieten und ausgewählter positiver Erhöhungsbetrag.

558V:8%der559aI-Zuschüsse plus jährliche Zinsermäßigung und laufende Förderbeträge vom Jahresbetrag der Vergleichsmiete abziehen, für Monatsgrenze durch12. Nicht den Zuschuss selbst als Jahresabzug und nicht nochmals von bereits bereinigter Vergleichsmiete abziehen. Reguläre Kappung aus Dreijahresbasis*1.15oder1.20plusausgenommenen Erhöhungen.558IV-Konkurrenz rechtlich zwingend wählen: alternativeErhöhungsgrenze=max(regulärer positiver Erhöhungsspielraum,Ausgleichszahlung); zusätzlicherAusnahmebetrag=regulärer positiver Spielraum+Ausgleichszahlung. Beide bedingten Wege werden ausgewiesen, keine allgemein bestätigte Addition behauptet. Vergleichsmiete nach Förderung bleibt in beiden Varianten Obergrenze. Bereits darüber liegende Bestandsmiete wird nicht automatisch gesenkt; nur positiver neuer Erhöhungsbetrag. Antwort-/Vorlauffristen und Wirksamkeit gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_558_T0001, BGB_558_T0002, BGB_558_T0003, BGB_558_T0004, BGB_558_T0005, BGB_558_T0006, BGB_558_T0007, BGB_558_T0008, BGB_558_T0009, BGB_558_T0010, BGB_558_T0011, BGB_558_T0012, BGB_558_T0013, BGB_558_T0014, BGB_558_T0015, BGB_559a_T0001, BGB_559a_T0002, BGB_559a_T0003, BGB_559a_T0004, BGB_559a_T0005, BGB_559a_T0006, BGB_559a_T0007, BGB_559a_T0008, BGB_559a_T0009

```python
from bgbcalc import vergleichsmiete_ausgleich_und_drittmittel
vergleichsmiete_ausgleich_und_drittmittel(
    ausgangsmiete_drei_jahre='500',
    nicht_anzurechnende_erhoehungen='0',
    derzeitige_monatsmiete='500',
    ortsuebliche_vergleichsmiete='900',
    gueltige_fuenfzehnprozent_verordnung=False,
    kapitalzuschuesse_559a_1='1500',
    jaehrliche_zinsermaessigung='60',
    jaehrliche_laufende_foerderung='60',
    letzte_monatliche_ausgleichszahlung='150',
    ausnahmemodell='alternative_erhoehungsgrenze',
    methodennachweis='558V:8%der559aI-Zuschüsse plus jährliche Zinsermäßigung und laufende Förderbeträge vom Jahresbetrag der Vergleichsmiete abziehen, für Monatsgrenze durch12. Nicht den Zuschuss selbst als Jahresabzug und nicht nochmals von bereits bereinigter Vergleichsmiete abziehen. Reguläre Kappung aus Dreijahresbasis*1.15oder1.20plusausgenommenen Erhöhungen.558IV-Konkurrenz rechtlich zwingend wählen: alternativeErhöhungsgrenze=max(regulärer positiver Erhöhungsspielraum,Ausgleichszahlung); zusätzlicherAusnahmebetrag=regulärer positiver Spielraum+Ausgleichszahlung. Beide bedingten Wege werden ausgewiesen, keine allgemein bestätigte Addition behauptet. Vergleichsmiete nach Förderung bleibt in beiden Varianten Obergrenze. Bereits darüber liegende Bestandsmiete wird nicht automatisch gesenkt; nur positiver neuer Erhöhungsbetrag. Antwort-/Vorlauffristen und Wirksamkeit gesondert.',
)
```
