<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## immobiliardarlehen_wechselkursrechnung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `fremdwaehrungsbetrag`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `wechselkurs_vertrag`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `wechselkurs_vergleich`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `wechselkurs_umstellung`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten gesetzlichen Falls und rechtlich bestimmten Zinssatz-/Kursgrundlagen; keine automatische Markt-/Effektivzinsberechnung.

Identischen Rest- oder Ratenbetrag zum Vertrags-/Vergleichskurs bewerten,120%-Grenze prüfen und Umstellungswert berechnen.

wert enthält exakte Zinsquoten einschließlich gegebenenfalls negativem mathematischem Korrekturwert bzw. Landeswährungswerte und strikt geprüften120%-Grenzvergleich.

Nur §503 für qualifiziertes Immobiliar-Verbraucherdarlehen in Fremdwährung. Derselbe aktuelle Restbetrag oder dieselbe regelmäßige Rate wird in beiden Vergleichswerten verwendet, nicht ursprünglicher Nennbetrag gegen heutige Restschuld. Landeswährung nach Absatz1 einschließlich wirksamer Währungsvereinbarung rechtlich bestimmen. Restbetrag und Rate bei unterschiedlichen relevanten Werten separat prüfen; numerischer Auslöser liegt vor, wenn wenigstens einer strikt über20% gestiegen ist. Umstellungskurs ist grundsätzlich Marktwechselkurs am Antragstag, bei wirksamer abweichender Vereinbarung deren Kurs; muss extern belegt werden. Kein Kursabruf, keine automatische Umwandlung/Vertragsänderung. Alle Kurse haben dieselbe ausdrückliche Orientierung Landeswährung je Fremdwährungseinheit.

Exakte gemeinsame rationale Zahlengrenzen; Eingangszinsen nichtnegativ, rechnerischer korrigierter Sollzins vorzeichenbehaftet; Wechselkurse positiv, Währungsbetrag nichtnegativ.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_503_T0002, BGB_503_T0004, BGB_503_T0005

```python
from bgbcalc import immobiliardarlehen_wechselkursrechnung
immobiliardarlehen_wechselkursrechnung(
    fremdwaehrungsbetrag='1000',
    wechselkurs_vertrag='1',
    wechselkurs_vergleich='1.21',
    wechselkurs_umstellung='1.25',
    einordnungsnachweis='Qualifiziertes503-Fremdwährungsdarlehen; gleicher aktueller Restbetrag und belegter Umstellungskurs.',
)
```

## verbraucherdarlehen_sollzinskorrektur

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `vertraglicher_sollzinssatz`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `angegebener_effektiver_jahreszins`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `tatsaechlicher_effektiver_jahreszins`: Nichtnegative exakte Dezimalzeichenfolge oder Bruchobjekt. Zinssätze als Jahresquoten (0.05=5%); Wechselkurse strikt positiv als Landeswährung je Fremdwährungseinheit, Fremdwährungsbetrag nichtnegativ.
- `einordnungsnachweis`: Nichtleerer Nachweis des qualifizierten gesetzlichen Falls und rechtlich bestimmten Zinssatz-/Kursgrundlagen; keine automatische Markt-/Effektivzinsberechnung.

Sollzinssatz um die positive Differenz zwischen tatsächlichem und angegebenem Effektivzins vermindern.

wert enthält exakte Zinsquoten einschließlich gegebenenfalls negativem mathematischem Korrekturwert bzw. Landeswährungswerte und strikt geprüften120%-Grenzvergleich.

Nur §494 Absatz3 bei qualifiziert zu niedrig angegebenem effektivem Jahreszins. Zinssätze als Jahresquoten eingeben, etwa0.05 für5Prozent; Differenz von6%und5% ist ein Prozentpunkt, kein relativer Abschlag von20%. Tatsächlichen Effektivzins extern nach einschlägigen Vorgaben berechnen. Ergebnis ist der vorzeichenbehaftete mathematische Korrekturwert ohne im Normtext nicht genannte Nulluntergrenze; negative Ergebnisse begründen hier keine automatische Zahlungspflicht des Darlehensgebers. Fehlende Angaben nach Absatz2, Kostenwegfall nach Absatz4 und neue Raten nach Absatz5 separat behandeln; keine automatische Annuitätenformel.

Exakte gemeinsame rationale Zahlengrenzen; Eingangszinsen nichtnegativ, rechnerischer korrigierter Sollzins vorzeichenbehaftet; Wechselkurse positiv, Währungsbetrag nichtnegativ.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_494_T0004

```python
from bgbcalc import verbraucherdarlehen_sollzinskorrektur
verbraucherdarlehen_sollzinskorrektur(
    vertraglicher_sollzinssatz='0.05',
    angegebener_effektiver_jahreszins='0.06',
    tatsaechlicher_effektiver_jahreszins='0.08',
    einordnungsnachweis='Qualifizierte Effektivzins-Unterangabe und Jahresquoten.',
)
```
