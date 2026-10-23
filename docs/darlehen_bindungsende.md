<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## darlehen_kuendigung_zum_sollzinsbindungsende

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kuendigungszugang_am`: Tatsächlicher rechtlich wirksamer Zugang der Kündigung YYYY-MM-DD.
- `sollzinsbindung_endet_am`: Letzter eingeschlossener Tag der rechtlich maßgeblichen Sollzinsbindung YYYY-MM-DD.
- `periodische_anpassung_bis_ein_jahr`: Wahrheitswert: rechtlich qualifizierte Sollzinsanpassung in Zeiträumen bis zu einem Jahr gemäß489I1Halbsatz2.
- `einordnungsnachweis`: Nichtleerer Nachweis489I1: Bindung endet vor bestimmter Rückzahlungszeit, keine neue Sollzinsvereinbarung, maßgebliche Periodeneinordnung und Zugang qualifiziert.

Einmonatige Kündigungsfrist mit Sollzinsbindungsende und gesetzlicher Periodenbeschränkung verbinden.

wert.einmonatige_kuendigungsfrist_letzter_tag alsDatum, monatsfrist_zum_bindungsende_eingehalten alsWahrheitswert, rechnerischer_beendigungstag alsDatum odernull bei verfehltem periodischem Endtermin.

§489I1: Einmonatsfrist ab Zugang mit Sollzinsbindungsende verbinden. Ohne Periodenbeschränkung ist der spätere dieser beiden Tage der rechnerisch früheste Beendigungstag. Bei qualifizierter Anpassung in Zeiträumen bis zu einem Jahr ist ausschließlich der vorgegebene Bindungsendtag erfasst; ist dafür die Monatsfrist nicht eingehalten, kein fristgerechter Termin in dieser Periode (null). Keine nächste Periode oder neue Zinsvereinbarung erfinden. Kündigungsrecht und formelle Wirksamkeit sind vorqualifiziert; keine Feiertagsverschiebung der Kündigungsfrist.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_489_T0001, BGB_489_T0002, BGB_489_T0003

```python
from bgbcalc import darlehen_kuendigung_zum_sollzinsbindungsende
darlehen_kuendigung_zum_sollzinsbindungsende(
    kuendigungszugang_am='2024-01-31',
    sollzinsbindung_endet_am='2024-02-29',
    periodische_anpassung_bis_ein_jahr=False,
    einordnungsnachweis='§489I1: Einmonatsfrist ab Zugang mit Sollzinsbindungsende verbinden. Ohne Periodenbeschränkung ist der spätere dieser beiden Tage der rechnerisch früheste Beendigungstag. Bei qualifizierter Anpassung in Zeiträumen bis zu einem Jahr ist ausschließlich der vorgegebene Bindungsendtag erfasst; ist dafür die Monatsfrist nicht eingehalten, kein fristgerechter Termin in dieser Periode (null). Keine nächste Periode oder neue Zinsvereinbarung erfinden. Kündigungsrecht und formelle Wirksamkeit sind vorqualifiziert; keine Feiertagsverschiebung der Kündigungsfrist.',
)
```
