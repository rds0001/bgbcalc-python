<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pauschalreise_notbeherbergungskosten

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachtkosten`: Unbenannte chronologische Liste0..10000 nichtnegativer EUR-Nachtbeträge ab erster notwendiger Nacht; kostenlose Nächte ausdrücklich als0 einfügen. Leere Liste bedeutet keine Nächte, fehlende Liste ist keine Null.
- `dreinaechtegrenze_anwendbar`: Expliziter Wahrheitswert: gesetzliche Begrenzung auf drei Nächte greift. FALSE nur bei rechtlich qualifizierter Ausnahme651kV; eingegebener Gesamtzeitraum dann bereits dem anderweitig maßgeblichen notwendigen Umfang zugeordnet.
- `einordnungsnachweis`: Nichtleerer Nachweis notwendiger Beherbergung wegen unmöglicher vertraglicher Rückbeförderung und außergewöhnlicher Umstände; Reihenfolge und gegebenenfalls Ausnahme/Zeitraum qualifiziert.

Notwendige Nachtkosten chronologisch summieren, gegebenenfalls auf die ersten drei Nächte begrenzen.

wert: anzahl_erfasster_naechte, anzahl_beruecksichtigter_naechte sowie kosten_im_qualifizierten_umfang und kosten_ausserhalb_dreinaechtegrenze als EUR-Brüche.

§651kIV/V: nur qualifizierte notwendige Beherbergung wegen unmöglicher vertraglicher Rückbeförderung infolge unvermeidbarer außergewöhnlicher Umstände. Nachtkosten chronologisch ab erster notwendiger Nacht vollständig eingeben, auch eine kostenlose Nacht als0, damit keine spätere Nacht an ihre Stelle rückt. Bei anwendbarer Begrenzung keine Auswahl der teuersten drei Nächte. FALSE nur nach qualifizierter Ausnahme651kV; dann sämtliche eingegebenen Nächte rechtlich dem anderweitig maßgeblichen notwendigen Umfang zuordnen, keine unbegrenzte Hotelzusage. Vorrangige EU-Regelungen, persönliche Voraussetzungen/48Stundeninformation, Gleichwertigkeit der Unterkunft und bereits gezahlte Kosten separat. Keine Cent-Rundung und keine automatische Rückzahlung oder Verdoppelung schon übernommener Kosten.

Nichtnegative exakte EUR-Dezimaltexte/Brüche nach NUMERIK.md. Kostenlisten ohne doppelte Positionen, keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651k_T0010, BGB_651k_T0011, BGB_651k_T0012, BGB_651k_T0013, BGB_651k_T0014, BGB_651k_T0015, BGB_651k_T0016, BGB_651k_T0017

```python
from bgbcalc import pauschalreise_notbeherbergungskosten
pauschalreise_notbeherbergungskosten(
    nachtkosten=['100', '200', '300', '400'],
    dreinaechtegrenze_anwendbar=True,
    einordnungsnachweis='Qualifizierte überschneidungsfreie Kosten des gesetzlichen Normfalls; Information beziehungsweise notwendige Beherbergung/Zeitraum festgestellt.',
)
```

## pauschalreise_zusatzkosten_informationsgrenze

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `kostenpositionen`: Unbenannte Liste1..1000 Objekte mit genau kosten_id (nichtleer, eindeutig), betrag (nichtnegativer EUR-Dezimaltext/Bruch), rechtzeitig_ordnungsgemaess_informiert (expliziter Wahrheitswert). Rechtzeitig vor Vertragserklärung des Reisenden; bei keinen Zusatzkosten einzelne Nullposition.
- `einordnungsnachweis`: Nichtleerer Nachweis der qualifizierten Zusatzkosten und der rechtzeitigen inhaltlich ordnungsgemäßen Information; übrige Anspruchsvoraussetzungen vorqualifiziert.

Zusatzkosten nach rechtzeitiger ordnungsgemäßer Information auswählen und getrennt summieren.

wert: nach_informationsgrenze_einbezogene_kosten und wegen_information_ausgeschlossene_kosten als exakte EUR-Brüche.

§651dII: zusätzliche Gebühren, Entgelte und sonstige Kosten; rechtzeitig bedeutet vor Abgabe der Vertragserklärung des Reisenden, nicht bloß vor Bestätigung des Veranstalters. Inhaltlich ordnungsgemäße Information nach dem verwiesenen EGBGB rechtlich vorqualifizieren; die Library prüft kein Informationsformular. Einbeziehung ist nur diese numerische Teilgrenze, kein Nachweis sämtlicher Anspruchsvoraussetzungen oder Vertragswirksamkeit. Positionen müssen im Übrigen der maßgeblichen Reise zugeordnet und überschneidungsfrei sein; bereits gezahlte Beträge separat. Keine Zusatzkosten ausdrücklich als einzelne Nullposition, keine fehlende Liste.

Nichtnegative exakte EUR-Dezimaltexte/Brüche nach NUMERIK.md. Kostenlisten ohne doppelte Positionen, keine Rundung.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651d_T0003

```python
from bgbcalc import pauschalreise_zusatzkosten_informationsgrenze
pauschalreise_zusatzkosten_informationsgrenze(
    kostenpositionen=[{'kosten_id': 'A', 'betrag': '100', 'rechtzeitig_ordnungsgemaess_informiert': True}, {'kosten_id': 'B', 'betrag': '50', 'rechtzeitig_ordnungsgemaess_informiert': False}],
    einordnungsnachweis='Qualifizierte überschneidungsfreie Kosten des gesetzlichen Normfalls; Information beziehungsweise notwendige Beherbergung/Zeitraum festgestellt.',
)
```
