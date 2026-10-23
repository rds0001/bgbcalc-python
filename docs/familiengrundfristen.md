<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## ehefaehigkeitszeugnis_geltungsende

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ausstellung_am`: ISO-Datum der Ausstellung des qualifizierten Ehefähigkeitszeugnisses als Ereignis.
- `urkundenende_am`: Optionales ISO-Datum des qualifizierten letzten Urkundengeltungstages, frühestens Ausstellung. NULL wenn keine besondere Begrenzung. Spätere Urkundengeltung verlängert gesetzliche Höchstfrist nicht.

Ende=min(Ausstellung+6Kalendermonate,gegebenenfalls qualifiziertes Urkundenende).

wert ist ISO-Datum des letzten Geltungstages.

§1309I3, nur Zeugnisgeltung. In der Urkunde angegebene kürzere Dauer vorab in rechtlich maßgeblichen letzten Geltungstag umsetzen; fehlende Begrenzung als NULL. Späteres Urkundenende verlängert die gesetzliche Sechsmonatsgrenze nicht. Keine automatische Prüfung von Ehefähigkeit, Herkunft, Befreiung oder Eheschließung. Keine Verlängerung einer materiellen Geltungsdauer durch Wochenende/Feiertag.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1309_T0003

```python
from bgbcalc import ehefaehigkeitszeugnis_geltungsende
ehefaehigkeitszeugnis_geltungsende(
    ausstellung_am='2030-08-31',
    urkundenende_am=None,
)
```

## familienrecht_grundfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `ereignis_am`: ISO-Datum des qualifizierten Ereignisses gemäß fristfall; Ereignistag nach§187I nicht mitzählen.
- `fristfall`: Zulässige feste Normbindungen: verloebnis_verjaehrung: Auflösung des Verlöbnisses; regelmäßige Verjährungsdauer nach§195 bei besonderem Beginn§1302. Kein Jahresendbeginn.; rueckkehrabsicht_ehewohnung: Auszug aus Ehewohnung nach qualifizierter Trennung;§1361bIV.; ehegatten_genehmigung: Empfang der qualifizierten Aufforderung nach§1366III; dieselbe Grenze für Mitteilung gerichtlicher Ersetzung.; vormundverein_mitteilung: Bestellung des Vereins zum vorläufigen Vormund;§1781II2.; vormund_bestellung: Bestellung des vorläufigen Vormunds;§1781III1. Ohne gerichtliche Verlängerung.; vormund_bereitschaft: Rechtlich maßgebliches Wirksamwerden der gerichtlichen Aufforderung zur Übernahme;§1783I5.; vormund_nachholantrag: Bestellung des bisherigen Vormunds;§1783II1, nicht Ende der vorübergehenden Verhinderung.; betreuungsverein_mitteilung: Bestellung des Betreuungsvereins;§1818II3. Personenwechsel nur bei rechtlich qualifiziertem entsprechendem Ereignis.; betreuer_genehmigungsmitteilung: Empfang der Aufforderung nach§1856II; Ende des zweiten nachfolgenden Kalendermonats.; betreuer_aufwendungsersatz: Entstehung des Aufwendungsersatzanspruchs;§1877IV1. Gerichtliche Abweichungen nachAbsatz5 nicht in dieser Grundfrist.; ehefaehigkeitsbefreiung: Qualifiziertes Wirksamkeitsereignis der Befreiung nach§1309II4; materielle Geltungsdauer, keine automatische§193-Verlängerung.; eheaufhebung_irrtum_taeuschung: Entdeckung des Irrtums/der Täuschung nach§1317I, bei Vertreterbeginn erst maßgebliche Vertreterkenntnis; wirksamen relativen Beginn bereits qualifizieren. §§206/210-Korrekturen separat.; eheaufhebung_drohung: Aufhören der Zwangslage nach§1317I, bei Vertreterbeginn erst maßgebliche Vertreterkenntnis; §§206/210-Korrekturen separat.; eheaufhebung_eigenantrag: Wegfall der Geschäftsunfähigkeit nach§1317II bei vorher versäumtem Vertreterantrag. Keine automatische Aufhebungsberechtigung.; eheaufhebung_todeserklaerung: Kenntnis des früheren Ehegatten vom Fortleben des für tot erklärten Ehegatten nach§1320I. §§1317/206/210-Korrekturen separat.; scheidung_ehewohnung_mietanspruch: Rechtskraft der Endentscheidung in der Scheidungssache;§1568aVI. Rechtzeitige Rechtshängigkeit und andere Rechtswirkungen gesondert.; scheidung_betreuungsunterhalt: Geburt des gemeinschaftlichen Kindes;§1570I1. Dreijahres-Mindestgrundgrenze, kein maximales Unterhaltsende; tatsächliche Voraussetzungen/Billigkeitsverlängerung gesondert.; unterhaltsauskunft_wiederholung: Rechtlich maßgebliches Ereignis der vorherigen vollständigen Auskunft für§1605II bereits qualifiziert. Wesentliche Änderungen können frühere Auskunft erlauben; kein automatisches Verbot früherer Anforderung.; unterhalt_sonderbedarf: Entstehung des rechtlich qualifizierten Sonderbedarfs nach§1613II1. Vorheriger Verzug/Rechtshängigkeit gesondert; kein automatisches Erlöschen bei Grundfristablauf.; geburtsname_bestimmung: Geburt des Kindes; gesetzliche Bestimmungsfrist§1617IV1 in lokaler Fassung. Keine automatische Namensbildung oder Anwendung einer gesondert gerichtlichen Frist.; adoption_elterneinwilligung: Wirksamwerden der Einwilligung eines Elternteils durch Zugang beim Familiengericht;§1750IV2. Frühere Kraftverluste durch Rücknahme/Versagung und andere Einwilligungsarten gesondert.; betreuung_anfangsbericht: Bestellung des Betreuers;§1863I Sollfrist. Ausnahme für bestimmte ehrenamtliche Betreuung nachAbsatz2 vorqualifizieren; keine automatische Berichtspflichtentscheidung.
- `ereignisnachweis`: Nichtleerer Nachweis der rechtlichen Auswahl und Ereignisqualifikation. Nur Grundfrist, Sonderkorrekturen gesondert.

Gesetzlich feste Tage-/Wochen-/Monats-/Jahresdauer per Kalenderkern. §1856II ist Monatsende des zweiten Folgemonats, nicht Ereignistag plus2Monate.

wert ist ISO-Datum des letzten Grundfristtages.

Nur gesetzliche Grundfrist, kein Wirksamkeits-, Anspruchs- oder Erlöschensurteil. Ereignisse rechtlich qualifizieren und Regeln nicht frei wählen. Hemmung, Ablaufhemmung, Neubeginn, gerichtliche Fristabweichungen/-verlängerungen und eine einschlägige§193-Verschiebung gesondert anwenden. Alsbald-Pflichten bleiben trotz Höchstfrist bestehen. Bei§1856II endet die Frist am letzten Tag des zweiten Folgemonats, auch bei Aufforderung am ersten Monatstag; keine bloße Addition zweier Monate zum Empfangstag. Verjährung§1302 benötigt außerhalb des ungestörten Grundfalls weitere Berechnung. Die zusätzlichen Bindungen sind qualifizierte Ereignisgrundfristen. §1570 nur Mindestgrundgrenze,§1605II mit möglicher vorzeitiger Auskunft bei wesentlicher Änderung,§1863I Sollfrist mit Ausnahmen; keine automatischen Statusentscheidungen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1302_T0001, BGB_195_T0001, BGB_1361b_T0008, BGB_1366_T0005, BGB_1366_T0006, BGB_1781_T0003, BGB_1781_T0004, BGB_1783_T0006, BGB_1783_T0008, BGB_1818_T0005, BGB_1818_T0006, BGB_1856_T0003, BGB_1877_T0008, BGB_1309_T0007, BGB_1317_T0001, BGB_1317_T0002, BGB_1317_T0004, BGB_1320_T0002, BGB_1320_T0003, BGB_1568a_T0012, BGB_1570_T0001, BGB_1605_T0004, BGB_1613_T0004, BGB_1617_T0009, BGB_1750_T0003, BGB_1750_T0010, BGB_1863_T0007

```python
from bgbcalc import familienrecht_grundfrist
familienrecht_grundfrist(
    ereignis_am='2030-01-15',
    fristfall='verloebnis_verjaehrung',
    ereignisnachweis='Normbindung und maßgebliches Ereignis rechtlich qualifiziert; ungestörte Grundfrist.',
)
```
