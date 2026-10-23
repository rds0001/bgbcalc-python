<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## vertrauensschaden_nichtigkeit_anfechtung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vertrauensschaden`: Nichtnegativer kausal durch Vertrauen auf Gültigkeit entstandener Schaden des geschützten Empfängers/Dritten in EUR (negatives Interesse). Rechtlich bestimmt, nicht ungeprüft der gesamte Geschäftswert.
- `gueltigkeitsinteresse`: Nichtnegatives rechtlich bewertetes Interesse an Gültigkeit der Erklärung in EUR als Höchstbetrag (positives Interesse). Gleichen Bezugsfall und Bewertungsmaßstab verwenden.
- `nichtigkeit_nach_118`: Expliziter Wahrheitswert einer Nichtigkeit gerade nach§118. Andere Nichtigkeitsgründe eröffnen§122 nicht automatisch.
- `anfechtung_nach_119_120`: Expliziter Wahrheitswert einer wirksamen Anfechtung gerade aufgrund§119 oder§120. Rechtzeitigkeit, Erklärung, Anfechtungsgrund und Wirksamkeit vorab prüfen;§123 nicht gleichsetzen.
- `grund_bekannt_oder_kennen_muessen`: Wahrheitswert, ob der Beschädigte den Grund der Nichtigkeit/Anfechtbarkeit kannte oder infolge Fahrlässigkeit nicht kannte. TRUE schließt Ersatz nach§122 Absatz2 aus.
- `bewertungsnachweis`: Nichtleere Beschreibung des gesetzlichen Ausgangsfalls, geschützten Empfängers/Dritten, Kausalität, Kenntnislage und beider Schadens-/Interessenwerte.

Anwendbarkeit durch Nichtigkeit§118 oder Anfechtung§119/§120. Im Anwendungsfall bei Kenntnis/Kennenmüssen0, sonst min(Vertrauensschaden,Gültigkeitsinteresse). Ohne Ausgangsfall NICHT_ANWENDBAR.

wert ist exakter EUR-Schadenersatz; gesetzlicher Kenntnisausschluss ergibt BERECHNET mit0/1. Fehlender Anwendungsfall ergibt NICHT_ANWENDBAR mit null.

Keine automatische Haftung für jede Nichtigkeit oder Anfechtung, insbesondere nicht bloß§123. Schadenwerte und geschützter Personenkreis extern bestimmt; mögliche andere Anspruchsgrundlagen nicht ausgeschlossen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_122_T0001, BGB_122_T0002

```python
from bgbcalc import vertrauensschaden_nichtigkeit_anfechtung
vertrauensschaden_nichtigkeit_anfechtung(
    vertrauensschaden='0',
    gueltigkeitsinteresse='0',
    nichtigkeit_nach_118=False,
    anfechtung_nach_119_120=True,
    grund_bekannt_oder_kennen_muessen=False,
    bewertungsnachweis='Synthetischer geschützter Empfänger mit kausalem Vertrauensschaden.',
)
```

## vertrauensschaden_vertretungsmangel

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vertrauensschaden`: Nichtnegativer kausaler Schaden in EUR durch Vertrauen des anderen Teils auf Vertretungsmacht (negatives Interesse). Kein pauschaler Prozentsatz.
- `wirksamkeitsinteresse`: Nichtnegatives rechtlich bewertetes Interesse an Wirksamkeit des Vertrags in EUR als Höchstbetrag des§179 Absatz2.
- `vertretungsmangel_unbekannt`: Wahrheitswert, ob der Vertreter den Mangel seiner Vertretungsmacht nicht kannte. FALSE führt aus dem begrenzten Absatz2-Modell; umfassendere Folgen nach Absatz1 separat prüfen.
- `vertretungsmacht_nachgewiesen`: Wahrheitswert, ob Vertretungsmacht im konkreten Fall nachgewiesen ist. TRUE führt aus dem hier berechneten Haftungsfall heraus; keine automatische Beweiswürdigung.
- `genehmigung_verweigert`: Wahrheitswert einer rechtlich maßgeblichen Verweigerung der Vertragsgenehmigung durch den Vertretenen. Bloßes Schweigen ohne rechtlich einschlägige Verweigerungsfolge nicht ungeprüft gleichsetzen.
- `gegner_kennt_oder_kennen_muss`: Wahrheitswert, ob der andere Teil den Mangel der Vertretungsmacht kannte oder kennen musste. Im Anwendungsfall Ausschluss nach§179 Absatz3 Satz1.
- `vertreter_beschraenkt_geschaeftsfaehig`: Wahrheitswert zur beschränkten Geschäftsfähigkeit des Handelnden im konkreten Fall. Nicht automatisch mit bloßer Minderjährigkeit gleichsetzen; Ausnahmen/Ermächtigungen rechtlich einordnen.
- `mit_zustimmung_des_gesetzlichen_vertreters`: Wahrheitswert der Zustimmung des gesetzlichen Vertreters zum Handeln des beschränkt geschäftsfähigen Vertreters. Nur bei beschränkter Geschäftsfähigkeit für Ausschlussausnahme maßgeblich.
- `bewertungsnachweis`: Nichtleere Beschreibung von Vertragsschluss als Vertreter, Vertretungsmangel/Kenntnis, Genehmigung, Gegnerkenntnis, Geschäftsfähigkeit/Zustimmung und den beiden Geldwerten.

Absatz2-Modell bei unbekanntem Vertretungsmangel, nicht nachgewiesener Vertretungsmacht und verweigerter Genehmigung. Im Anwendungsfall0 bei Gegnerkenntnis/Kennenmüssen oder beschränkter Geschäftsfähigkeit ohne Zustimmung; sonst min(Vertrauensschaden,Wirksamkeitsinteresse).

wert ist exakter EUR-Betrag des begrenzten Vertrauensschadens. Ausschluss nach Absatz3 innerhalb dieses Modells ergibt0/1; fehlender Absatz2-Anwendungsfall null.

Keine Haftungsfreiheit aus NICHT_ANWENDBAR ableiten, insbesondere bei bekanntem Vertretungsmangel. Erfüllungs-/Schadenersatzwahl nach Absatz1 außerhalb des Modells. Geschäftsunfähigkeit oder andere Wirksamkeits-/Sonderfälle vorab gesondert prüfen.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_179_T0001, BGB_179_T0002, BGB_179_T0003, BGB_179_T0004

```python
from bgbcalc import vertrauensschaden_vertretungsmangel
vertrauensschaden_vertretungsmangel(
    vertrauensschaden='800',
    wirksamkeitsinteresse='500',
    vertretungsmangel_unbekannt=True,
    vertretungsmacht_nachgewiesen=False,
    genehmigung_verweigert=True,
    gegner_kennt_oder_kennen_muss=False,
    vertreter_beschraenkt_geschaeftsfaehig=False,
    mit_zustimmung_des_gesetzlichen_vertreters=False,
    bewertungsnachweis='Synthetischer Vertretervertrag; Tatsachen und Interessenwerte geprüft.',
)
```
