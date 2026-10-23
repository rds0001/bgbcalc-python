<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesellschaft_fuenfjahresgrundfrist

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `fristfall`: nachhaftung_728b oder erloeschen_verjaehrung_739; unterschiedliche Rechtswirkungen trotz gleichem Kalenderkern.
- `ausscheiden_oder_erloeschen_am`: Tag des rechtlich wirksamen Ausscheidens beziehungsweise Erlöschens der Gesellschaft YYYY-MM-DD.
- `glaeubigerkenntnis_am`: Tag der rechtlich maßgeblichen Kenntnis des konkreten Gläubigers, sonst null.
- `registereintragung_am`: Tag der maßgeblichen Eintragung des Ausscheidens beziehungsweise Erlöschens im Gesellschaftsregister, sonst null.
- `kuerzere_gesellschaftsfrist_letzter_tag`: Optional ausschließlich739: bereits vollständig bestimmter letzter Tag der rechtlich kürzeren Gesellschaftsanspruchsverjährung. Null bedeutet kein berechneter Vergleich; nicht automatisch Fehlen einer kürzeren Frist.
- `einordnungsnachweis`: Nichtleerer Nachweis des Fristfalls, Wirksamkeit, richtigen Registereintrags und individueller Gläubigerkenntnis; mindestens einer der beiden Beginnanlässe muss feststehen.

Frühere qualifizierte Gläubigerkenntnis oder Registereintragung bestimmen und fünfjährige Ereignisgrundfrist berechnen.

wert.massgeblicher_beginnanlass_am und wert.rechnerisches_fuenfjahresende alsYYYY-MM-DD; zusätzlich ende_im_qualifizierten_kuerzeren_grundfall als Datum oder null ohne Vergleichseingabe. Keine abschließende Haftungs-/Verjährungsgrenze.

§728bI3 beziehungsweise739II: frühester feststehender Beginnanlass aus Gläubigerkenntnis und Registereintragung, danach fünf Kalenderjahre ohne Jahresendverschiebung. Ausscheiden oder Erlöschen allein ersetzt weder Kenntnis noch Eintragung. Vorherige bloße Kenntnis einer Absicht beziehungsweise unzutreffender Registereintrag sind nicht qualifiziert. Nur ungestörter Grundlauf:728b-Nachhaftung verlangt zusätzlich rechtzeitig fällige Altverbindlichkeit sowie Feststellung/Vollstreckung oder schriftliches Anerkenntnis; bei Schadensersatz muss Pflichtverletzung vor Ausscheiden liegen.728b-Verweise204/206/210/211/212II/III gesondert.739: Optionaler Minimumvergleich mit rechtlich bestimmtem Ende der kürzeren Gesellschaftsanspruchsfrist ausschließlich für den ungestörten Fünfjahresgrundlauf. Ohne Eingabe bleibt Vergleich null. Bei Hemmung/Neubeginn739III zuvor beide Laufzeiten gesondert korrigieren; ein Vergleich mit unberichtigter Grundfrist wäre dann unzulässig; Ergebnis keinesfalls als abschließende Haftungs-/Verjährungsgrenze verwenden. Kein automatischer Haftungsausschluss.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_728b_T0001, BGB_728b_T0002, BGB_728b_T0003, BGB_728b_T0004, BGB_728b_T0005, BGB_728b_T0006, BGB_739_T0001, BGB_739_T0002, BGB_739_T0003

```python
from bgbcalc import gesellschaft_fuenfjahresgrundfrist
gesellschaft_fuenfjahresgrundfrist(
    fristfall='nachhaftung_728b',
    ausscheiden_oder_erloeschen_am='2024-01-01',
    glaeubigerkenntnis_am='2024-01-31',
    registereintragung_am='2024-02-29',
    kuerzere_gesellschaftsfrist_letzter_tag=None,
    einordnungsnachweis='§728bI3 beziehungsweise739II: frühester feststehender Beginnanlass aus Gläubigerkenntnis und Registereintragung, danach fünf Kalenderjahre ohne Jahresendverschiebung. Ausscheiden oder Erlöschen allein ersetzt weder Kenntnis noch Eintragung. Vorherige bloße Kenntnis einer Absicht beziehungsweise unzutreffender Registereintrag sind nicht qualifiziert. Nur ungestörter Grundlauf:728b-Nachhaftung verlangt zusätzlich rechtzeitig fällige Altverbindlichkeit sowie Feststellung/Vollstreckung oder schriftliches Anerkenntnis; bei Schadensersatz muss Pflichtverletzung vor Ausscheiden liegen.728b-Verweise204/206/210/211/212II/III gesondert.739: Optionaler Minimumvergleich mit rechtlich bestimmtem Ende der kürzeren Gesellschaftsanspruchsfrist ausschließlich für den ungestörten Fünfjahresgrundlauf. Ohne Eingabe bleibt Vergleich null. Bei Hemmung/Neubeginn739III zuvor beide Laufzeiten gesondert korrigieren; ein Vergleich mit unberichtigter Grundfrist wäre dann unzulässig; Ergebnis keinesfalls als abschließende Haftungs-/Verjährungsgrenze verwenden. Kein automatischer Haftungsausschluss.',
)
```
