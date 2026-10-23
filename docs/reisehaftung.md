<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## pauschalreise_haftungsbegrenzung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reisepreis`: Nichtnegativer rechtlich maßgeblicher Reisepreis in EUR als Basis der Dreifachgrenze.
- `ersatzfaehiger_schaden`: Nichtnegative bereits dem Grunde und der Höhe nach bestimmte Schadenersatzposition in EUR vor dieser Haftungsbegrenzung. Keine bloß behauptete Schadenssumme; gemischte Körper-/Vermögenspositionen separat prüfen.
- `haftungsbeschraenkung_vereinbart`: Wahrheitswert einer im Übrigen wirksamen Vereinbarung, die Haftung nach§651p Absatz1 auf den dreifachen Reisepreis zu begrenzen. Keine automatische gesetzliche Begrenzung ohne Vereinbarung. Körper-/Verschuldensvoraussetzungen werden zusätzlich hier verknüpft.
- `koerperschaden`: Wahrheitswert, ob die konkrete Position ein Körperschaden ist. TRUE verhindert die Begrenzung nach Absatz1.
- `schuldhaft_herbeigefuehrt`: Wahrheitswert zur rechtlich zurechenbaren schuldhaften Herbeiführung des konkreten Schadens im Sinne§651p Absatz1 Nummer2. TRUE verhindert die Dreifachgrenze; Zurechnung und Verschuldensmaßstab extern prüfen.
- `bewertungsnachweis`: Nichtleere Beschreibung von ersatzfähigem Schaden, Vereinbarung, Schadensart und Verschuldenseinordnung. Andere Haftungsvoraussetzungen nicht durch diesen Nachweis automatisch bestätigt.

Bei Vereinbarung UND keinem Körperschaden UND keiner schuldhaften Herbeiführung: min(ersatzfähiger Schaden,3×Reisepreis). Sonst wird dieser Begrenzungstatbestand nicht angewandt und der vorgegebene Schaden ausgegeben.

wert ist exakter EUR-Betrag nach Prüfung der Dreifachgrenze, immer BERECHNET bei gültigen Eingaben.

Absatz1 allein. Internationale Beschränkungen nach Absatz2 und wechselseitige Anrechnung nach Absatz3 nicht enthalten. Ungekürzter Betrag ist kein neu festgestellter Haftungsanspruch.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651p_T0001, BGB_651p_T0002, BGB_651p_T0003

```python
from bgbcalc import pauschalreise_haftungsbegrenzung
pauschalreise_haftungsbegrenzung(
    reisepreis='1000',
    ersatzfaehiger_schaden='2999.99',
    haftungsbeschraenkung_vereinbart=False,
    koerperschaden=False,
    schuldhaft_herbeigefuehrt=False,
    bewertungsnachweis='Synthetische ersatzfähige Position und vereinbarte Haftungsgrenze.',
)
```

## pauschalreise_ruecktrittsentschaedigung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `reisepreis`: Nichtnegativer vereinbarter Reisepreis in EUR für die zurückgetretene Pauschalreise.
- `ersparte_aufwendungen`: Nichtnegativer Wert der durch den Rücktritt ersparten Aufwendungen des Veranstalters in EUR. Für konkrete Differenzrechnung tatsächliche rechtlich anrechenbare Ersparnis vorgeben, keine frei gewählte Pauschalquote.
- `anderweitiger_erwerb`: Nichtnegativer Erwerb durch anderweitige Verwendung der Reiseleistungen in EUR, rechtlich dem Fall zugeordnet. Nicht nochmals in ersparte_aufwendungen berücksichtigen.
- `entschaedigungspauschale_vereinbart`: Wahrheitswert, ob eine für den Fall wirksam maßgebliche Entschädigungspauschale vereinbart ist. TRUE führt ohne vorrangigen Ausschluss zu NICHT_ANWENDBAR, weil diese Funktion keine Pauschalen berechnet oder auf Angemessenheit prüft.
- `ausschluss_aussergewoehnliche_umstaende`: Expliziter Wahrheitswert zum vollständigen Ausschluss nach§651h Absatz3: unvermeidbare außergewöhnliche Umstände am Bestimmungsort oder in unmittelbarer Nähe, erhebliche Beeinträchtigung der Reise oder Beförderung. Bloße Sorge oder ein beliebiges Ereignis genügt nicht; rechtliche Definition nach Satz2 mitprüfen. TRUE ergibt0 auch bei Pauschalvereinbarung.
- `bewertungsnachweis`: Nichtleere Beschreibung des wirksamen Reisendenrücktritts vor Reisebeginn, Ersparnis, anderweitigen Erwerbs, Pauschalstatus und gegebenenfalls Ausschlusstatbestands.

Vorrangiger Ausschluss§651h Absatz3 führt zu0. Ohne Ausschluss und ohne maßgebliche Pauschalvereinbarung: Entschädigung=max(Reisepreis minus ersparte Aufwendungen minus anderweitigen Erwerb,0). Sonst NICHT_ANWENDBAR.

wert ist exakte EUR-Entschädigung. Ausschluss bedeutet BERECHNET mit0/1. Pauschalweg ohne Ausschluss bedeutet NICHT_ANWENDBAR und null.

Nur Rücktritt des Reisenden vor Reisebeginn und konkrete Differenzrechnung. Keine Stornostaffel oder Quote erfinden; Entschädigungspauschale, Rücktritt des Veranstalters sowie Rückerstattungs-/Leistungsfristen getrennt.

Geldbeträge als nichtnegative Dezimalzeichenfolge oder Bruchobjekt mit Zeichenfolgen zaehler/nenner. Exakte Ganzzahl-Zwischenwerte höchstens 2^53-1. Fehlende Pflichteingabe EINGABE_FEHLT, unzulässige Typen oder Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_651h_T0001, BGB_651h_T0002, BGB_651h_T0003, BGB_651h_T0004, BGB_651h_T0005, BGB_651h_T0006, BGB_651h_T0007, BGB_651h_T0008, BGB_651h_T0009, BGB_651h_T0010, BGB_651h_T0011

```python
from bgbcalc import pauschalreise_ruecktrittsentschaedigung
pauschalreise_ruecktrittsentschaedigung(
    reisepreis='1000',
    ersparte_aufwendungen='0',
    anderweitiger_erwerb='0',
    entschaedigungspauschale_vereinbart=False,
    ausschluss_aussergewoehnliche_umstaende=False,
    bewertungsnachweis='Synthetischer Reisendenrücktritt vor Beginn; konkrete Ersparnis und Erwerb.',
)
```
