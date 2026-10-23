<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## betreuung_genehmigung_ablaufgrenze

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `rechnerisches_fristende_ohne_genehmigungsverfahren`: Bereits nach sonstigen einschlägigen Regeln bestimmter letzter Tag der gesetzlichen FristYYYY-MM-DD, ohne die hier betrachtete1858III-Ablaufhemmung.
- `genehmigungsverfahren_beginn_am`: Erster rechtlich wirksamer Tag des schützenden GenehmigungsverfahrensYYYY-MM-DD, spätestens am sonstigen letzten Fristtag. Nicht beliebige Kenntnis oder erst nach Fristablauf gestellter Antrag.
- `genehmigung_rechtskraft_am`: Feststehender Tag der Rechtskraft des Beschlusses über die Erteilung der nachträglichen GenehmigungYYYY-MM-DD; kein lediglich erwarteter Tag und keine Versagung.
- `einordnungsnachweis`: Nichtleerer Nachweis von1858III, rechtzeitigem Schutzbeginn, gesetzlicher Frist und rechtskräftig erteilter nachträglicher Genehmigung.

Rechtzeitig begonnenes Genehmigungsverfahren prüfen; bisherigen letzten Fristtag frühestens auf die Rechtskraft der Erteilung verschieben, ohne Verfahrenstage zu addieren.

wert.rechnerisches_fristende alsYYYY-MM-DD, im ausdrücklich qualifizierten Erteilungsfall.

§1858III: qualifiziertes einseitiges Rechtsgeschäft gegenüber Gericht oder Behörde, für das eine nachträgliche betreuungsgerichtliche Genehmigung rechtskräftig erteilt wird. Gesetzlicher Fristablauf während des wirksamen Genehmigungsverfahrens gehemmt; keine Addition sämtlicher Verfahrenstage nach209 und keine neue volle Frist ab Rechtskraft. Verfahrensbeginn und Rechtskraft der Erteilung bereits rechtlich bestimmt. Rechtskraft einer Versagung, nichtgesetzliche Fristen und andere Genehmigungslagen sind nicht Gegenstand dieses Bausteins. Ein bereits vor Verfahrensbeginn außerhalb des Schutzes eingetretener Fristablauf wird nicht wiederbelebt. Bei laufendem Verfahren ohne Rechtskraft kein fiktiver Endtag. Ereignisse auf rechtlich maßgebliche Kalendertage normalisieren; weitere Fristkorrekturen gesondert.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_1858_T0003, BGB_1858_T0004, BGB_1858_T0005, BGB_1858_T0006, BGB_1858_T0007

```python
from bgbcalc import betreuung_genehmigung_ablaufgrenze
betreuung_genehmigung_ablaufgrenze(
    rechnerisches_fristende_ohne_genehmigungsverfahren='2024-02-29',
    genehmigungsverfahren_beginn_am='2024-02-15',
    genehmigung_rechtskraft_am='2024-04-10',
    einordnungsnachweis='§1858III: qualifiziertes einseitiges Rechtsgeschäft gegenüber Gericht oder Behörde, für das eine nachträgliche betreuungsgerichtliche Genehmigung rechtskräftig erteilt wird. Gesetzlicher Fristablauf während des wirksamen Genehmigungsverfahrens gehemmt; keine Addition sämtlicher Verfahrenstage nach209 und keine neue volle Frist ab Rechtskraft. Verfahrensbeginn und Rechtskraft der Erteilung bereits rechtlich bestimmt. Rechtskraft einer Versagung, nichtgesetzliche Fristen und andere Genehmigungslagen sind nicht Gegenstand dieses Bausteins. Ein bereits vor Verfahrensbeginn außerhalb des Schutzes eingetretener Fristablauf wird nicht wiederbelebt. Bei laufendem Verfahren ohne Rechtskraft kein fiktiver Endtag. Ereignisse auf rechtlich maßgebliche Kalendertage normalisieren; weitere Fristkorrekturen gesondert.',
)
```
