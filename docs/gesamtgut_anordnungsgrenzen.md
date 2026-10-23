<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## gesamtgut_anteilsherabsetzung_halbgrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `ungekuerzter_anteilswert`: Rechtlich gebührender ungekürzter Anteil am Gesamtgut bei Beendigung der fortgesetzten Gütergemeinschaft, in Euro unter zutreffendem Bewertungsmaßstab.
- `angeordneter_anteilswert`: Aus der qualifizierten letztwilligen Herabsetzung resultierender Anteil, unter demselben Maßstab in Euro; höchstens ungekürzter Anteil.
- `einordnungsnachweis`: Nichtleerer Nachweis des1512-Falls, anteilsberechtigtem Abkömmling und gleichen Bewertungsgrundlagen. Keine automatische Testamentsauslegung.

Hälfte des ungekürzten Gesamtgutsanteils berechnen, angeordnete Herabsetzung und Unterschreitung dieser Grenze ausweisen.

wert.halbe_anteilsuntergrenze, angeordneter_minderungsbetrag und unterschreitungsbetrag als exakte Eurobrüche; halbgrenze_eingehalten als Wahrheitswert.

§1512: ungekürzten gebührenden Anteil halbieren und angeordneten Wert mit dieser Untergrenze vergleichen. Angeordnete Minderung und positive Grenzunterschreitung getrennt ausweisen. Keine automatische Anhebung einer unwirksamen Anordnung, keine Vermögensbewertung oder Verteilung des freiwerdenden Anteils auf andere Beteiligte. Pflichtteil, Ausschluss1511, Erb-/Gesamtgutsquote und Wirksamkeit der Verfügung gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1512_T0001

```python
from bgbcalc import gesamtgut_anteilsherabsetzung_halbgrenze
gesamtgut_anteilsherabsetzung_halbgrenze(
    ungekuerzter_anteilswert='100',
    angeordneter_anteilswert='60',
    einordnungsnachweis='§1512: ungekürzten gebührenden Anteil halbieren und angeordneten Wert mit dieser Untergrenze vergleichen. Angeordnete Minderung und positive Grenzunterschreitung getrennt ausweisen. Keine automatische Anhebung einer unwirksamen Anordnung, keine Vermögensbewertung oder Verteilung des freiwerdenden Anteils auf andere Beteiligte. Pflichtteil, Ausschluss1511, Erb-/Gesamtgutsquote und Wirksamkeit der Verfügung gesondert.',
)
```

## gesamtgut_landgut_uebernahmepreisgrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `qualifizierter_ertragswert`: Nach1515II/2049 rechtlich festgestellter Ertragswert des Landguts in Euro; kein automatisch gleichgesetzter Verkehrswert.
- `angeordneter_uebernahmepreis`: Qualifizierter testamentarischer Übernahmepreis in Euro.
- `einordnungsnachweis`: Nichtleerer Nachweis des1515II/III-Übernahmefalls und zutreffender Ertragswertermittlung.

Angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert als Untergrenze vergleichen.

wert.ertragswertgrenze_eingehalten als Wahrheitswert; unterschreitungsbetrag als exakter Eurobruch.

§1515II/III: angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert vergleichen; Gleichheit erreicht die Untergrenze. Ertragswert selbst ist Bewertungsinput nach2049, keine erfundene Kapitalisierungsformel. Keine automatische Anhebung eines unzulässigen Preises, keine Entscheidung über Testamentswirksamkeit, Übernahmeberechtigung oder Ausgleichszahlungsverteilung.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1515_T0002, BGB_1515_T0003, BGB_1515_T0004

```python
from bgbcalc import gesamtgut_landgut_uebernahmepreisgrenze
gesamtgut_landgut_uebernahmepreisgrenze(
    qualifizierter_ertragswert='200000',
    angeordneter_uebernahmepreis='200000',
    einordnungsnachweis='§1515II/III: angeordneten Landgut-Übernahmepreis mit qualifiziertem Ertragswert vergleichen; Gleichheit erreicht die Untergrenze. Ertragswert selbst ist Bewertungsinput nach2049, keine erfundene Kapitalisierungsformel. Keine automatische Anhebung eines unzulässigen Preises, keine Entscheidung über Testamentswirksamkeit, Übernahmeberechtigung oder Ausgleichszahlungsverteilung.',
)
```
