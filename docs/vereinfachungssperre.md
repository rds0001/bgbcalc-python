<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## modernisierung_vereinfachung_sperrfrist

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `zugang_vereinfachte_erhoehung_am`: ISO-Datum des rechtlich maßgeblichen Zugangs der Mieterhöhungserklärung im vereinfachten Verfahren beim Mieter. Nicht Modernisierungsbeginn, Ankündigung oder Beginn der erhöhten Zahlung. Fünfjährige Ereignisfrist muss im Datumsbereich0001..9999 enden.
- `neue_geltendmachung_am`: ISO-Datum der beabsichtigten/erfolgten neuen Geltendmachung nach§559 oder§559e, nicht deren Zahlungsbeginn. Nicht vor Ausgangszugang. Ende der Fünfjahressperre wird bis Tagesschluss berücksichtigt.
- `gesetzliche_modernisierungspflicht`: Wahrheitswert: Vermieter muss die konkret abgegrenzte neue Modernisierungsmaßnahme während des betreffenden Zeitraums aufgrund gesetzlicher Verpflichtung durchführen. Nicht bloßer Wunsch oder bereits anderweitig pauschal bewerteter Ausnahmefall.
- `pflicht_damals_bekannt_oder_kennen_muessen`: Wahrheitswert: Vermieter kannte die Verpflichtung bei Geltendmachung der früheren vereinfachten Erhöhung oder musste sie kennen. TRUE verhindert die Pflichtausnahme. Nicht Kenntniszeitpunkt erst der neuen Erhöhung.
- `modernisierung_auf_weg_beschluss`: Wahrheitswert: konkrete Maßnahme wird aufgrund des bezeichneten Beschlusses von Wohnungseigentümern durchgeführt. TRUE verlangt Datum dieses Beschlusses; bloße Zugehörigkeit zu WEG genügt nicht.
- `weg_beschluss_am`: ISO-Datum der tatsächlichen Beschlussfassung, bei maßnahmebezogenem WEG-Beschluss Pflicht, sonst optional. Nicht nach neuer Geltendmachung. Mindestabstand zwei voll abgelaufene Ereignisjahre ab ursprünglichem Zugang; Grenze mit vorhandenem Kalenderkern.
- `vereinfachte_erhoehung_geltend_gemacht`: Wahrheitswert einer rechtlich maßgeblichen früheren Geltendmachung im vereinfachten Verfahren. FALSE führt aus diesem Sperrfristmodell, kein Beleg eines sonst wirksamen neuen Erhöhungsanspruchs.
- `einordnungsnachweis`: Nichtleere Beschreibung von früherem vereinfachten Verfahren/Zugang, neuer§559/§559e-Maßnahme und gesetzlicher Verpflichtung samt damaliger Kenntnis beziehungsweise maßnahmebezogenem WEG-Beschluss. Gemischte Maßnahmen nach Ausnahmeumfang getrennt prüfen.

Fünfjährige Ereignisfrist ab Zugang bestimmen. Innerhalb Sperre keine neue§559/§559e-Erhöhung, außer maßnahmebezogene damals unbekannte/nicht kennen zu müssende gesetzliche Verpflichtung oder maßgeblicher WEG-Beschluss frühestens nach zwei voll abgelaufenen Ereignisjahren.

wert enthält sperrfrist_letzter_tag, weg_beschluss_fruehestens als ISO-Daten und pflichtausnahme, wegausnahme, neue_erhoehung_nach_559_559e_gesperrt als Wahrheitswerte. Ohne frühere maßgebliche vereinfachte Erhöhung NICHT_ANWENDBAR/null.

Nur§559c Absatz4; keine umfassende Erhöhungsberechtigung. Pflichtausnahme nur soweit gesetzlich erzwungene konkrete Maßnahmen während Sperrzeit; WEG-Ausnahme nur bei Durchführung aufgrund dieses Beschlusses. Keine automatische Werktagsverschiebung, neue Sperren separat.

ISO-Daten0001..9999, explizite Wahrheitswerte und nichtleerer Nachweis. Ergebnisse müssen im Datumsbereich liegen.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_559c_T0007, BGB_559c_T0008, BGB_559c_T0009, BGB_559c_T0010, BGB_187_T0001, BGB_187_T0002, BGB_188_T0001, BGB_188_T0002, BGB_188_T0003

```python
from bgbcalc import modernisierung_vereinfachung_sperrfrist
modernisierung_vereinfachung_sperrfrist(
    zugang_vereinfachte_erhoehung_am='2020-06-15',
    neue_geltendmachung_am='2024-06-15',
    gesetzliche_modernisierungspflicht=False,
    pflicht_damals_bekannt_oder_kennen_muessen=False,
    modernisierung_auf_weg_beschluss=False,
    weg_beschluss_am='2022-06-15',
    vereinfachte_erhoehung_geltend_gemacht=True,
    einordnungsnachweis='Synthetische frühere vereinfachte Erhöhung und konkret abgegrenzte neue Maßnahme.',
)
```
