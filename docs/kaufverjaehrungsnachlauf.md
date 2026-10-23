<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verbrauchsgueterkauf_nachbesserungsverlaengerung

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `urspruenglicher_letzter_tag`: ISO-Datum0001..9999 des Endes der unveränderten ursprünglichen Verjährungsgrundfrist. Keine bereits umAbsatz5 verlängerte Frist und keine bereits nachAbsätzen1–4 gebildete Mindestnachlaufgrenze eingeben. Derselbe feste Ursprung ist auch bei weiteren Nachbesserungen beizubehalten.
- `nachbesserung_nach_439_geleistet`: Wahrheitswert, ob die gesetzlich qualifizierte Nacherfüllung gemäß§439 durch Nachbesserung geleistet ist. Mindestens eine qualifizierte Nachbesserung genügt; zusätzliche Reparaturen ändern die einmalige Zwölfmonatsverlängerung nicht. Bloßer Antrag oder Ersatzlieferung sind nicht ohne Weiteres Nachbesserung.
- `regel_475e_absatz_fuenf_anwendbar`: Wahrheitswert der sachlichen und insbesondere zeitlichen Anwendbarkeit von§475e Absatz5 in der lokalen BGB-Fassung auf den konkreten Fall; nicht automatisch auf Altfälle übertragen. Bereits verjährte Ansprüche nicht ohne rechtliche Grundlage wiederbeleben. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung von ursprünglicher Frist, geleisteter Nachbesserung und sachlicher/zeitlicher Anwendbarkeit. Andere Fristveränderungen gesondert dokumentieren und in rechtlicher Reihenfolge kombinieren.

Bei geleisteter Nachbesserung ursprüngliche Grundfrist genau einmal um zwölf Monate verlängern; ohne Nachbesserung unveränderten Grundtermin ausweisen.

wert enthält verlaengerung_monate (0oder12) und rechnerischer_letzter_tag als ISO-Datum. Ohne Anwendbarkeit NICHT_ANWENDBAR/null. Andere Friständerungen sind noch nicht integriert.

Kein Neubeginn der gesamten Verjährung ab Reparatur und keine wiederholte Zwölfmonatsaddition. Eingabe muss immer ursprüngliche Frist bleiben; keine gesetzliche Übergangsregel aus dem bloßen Vorliegen der lokalen Norm ableiten.

ISO-Daten und berechnete Fristgrenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_475e_T0005

```python
from bgbcalc import verbrauchsgueterkauf_nachbesserungsverlaengerung
verbrauchsgueterkauf_nachbesserungsverlaengerung(
    urspruenglicher_letzter_tag='2024-02-29',
    nachbesserung_nach_439_geleistet=False,
    regel_475e_absatz_fuenf_anwendbar=True,
    einordnungsnachweis='Synthetisch qualifizierte Nachbesserung und zeitliche Anwendbarkeit der lokalen Absatz5-Fassung; unveränderte ursprüngliche Frist.',
)
```

## verbrauchsgueterkauf_verjaehrungsnachlauf

Feste lokale BGB-Fassung; rechtlichen Anwendungsbereich und Bewertungen ausdrücklich bestimmen.

Parameter:

- `nachlaufgrund`: Auswahl ende_digitaler_bereitstellung (Absatz1,12Monate), ende_aktualisierungspflicht (Absatz2,12Monate), erstmaliges_zeigen_des_mangels (Absatz3,4Monate) oder rueckgabe_nach_nacherfuellung_garantie (Absatz4,2Monate). Diese Gründe haben verschiedene Anknüpfungsereignisse.
- `anknuepfung_am`: ISO-Datum0001..9999: je nach Auswahl Ende des rechtlichen Bereitstellungszeitraums, Ende des Zeitraums der Aktualisierungspflicht, erstmaliges Zeigen gerade dieses Mangels oder Übergabe der nachgebesserten/ersetzten Ware zurück an den Verbraucher. Nicht ursprüngliche Übergabe zur Reparatur mit Rückgabe verwechseln. Noch nicht feststehendes Schutzende nicht durch fiktives Datum ersetzen.
- `bisheriger_letzter_tag`: ISO-Datum0001..9999 des rechtlich maßgeblichen bisherigen letzten unverjährten Tags vor Anwendung dieses Nachlaufs. Einschlägige Frist und bereits wirksame andere Verlängerungen korrekt einordnen. Bei erstmaligem Zeigen wird zusätzlich geprüft, dass dieses spätestens an diesem Tag liegt. Keine zirkuläre Bestimmung der Voraussetzung mit dem hier neu berechneten Nachlauf.
- `tatbestand_erfuellt`: Wahrheitswert des vollständigen rechtlichen Tatbestands für den konkreten Verbrauchsgütermangel: Absatz1 dauerhafte digitale Bereitstellung§475c, Absatz2 Verletzung der Aktualisierungspflicht§475b, Absatz3 erstmaliges Zeigen, Absatz4 qualifizierte vorherige Übergabe zur Nacherfüllung/Garantie an Unternehmer oder von ihm veranlassten Dritten und Rückgabe. Kein Wiederaufleben bereits verjährter Ansprüche unterstellen. FALSE ergibt NICHT_ANWENDBAR.
- `einordnungsnachweis`: Nichtleere Begründung von Anspruch, Tatbestand, zugehörigem Anknüpfungsereignis und bisheriger Frist. Bei mehreren einschlägigen Nachläufen konkurrierende Grenzen rechtlich konsistent bestimmen.

Nachlauf von12/12/4/2Monaten ab gesetzlichem Ereignis berechnen und späteres Ende aus Nachlauf und bisheriger Frist wählen. Absatz3 zusätzlich erstes Zeigen innerhalb bisheriger Frist verlangen.

wert enthält nachlauf_monate als ganze Zahl, mindestablauf und rechnerischer_letzter_tag als ISO-Daten. Ohne qualifizierten Tatbestand, auch bei verspätetem Erstzeigen, NICHT_ANWENDBAR/null.

Kein pauschales Addieren zum bisherigen Fristende; keine automatische Wiederbelebung verjährter Ansprüche. Noch laufende unbestimmte Bereitstellung/Aktualisierungspflicht ohne feststehendes Ende kann mit dieser Datumsfunktion nicht abschließend berechnet werden. Hemmungen/Neubeginne/weitere Nachläufe/§193 gesondert.

ISO-Daten und berechnete Fristgrenzen0001..9999, explizite Auswahl/Wahrheitswerte und nichtleerer Nachweis.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_475e_T0001, BGB_475e_T0002, BGB_475e_T0003, BGB_475e_T0004

```python
from bgbcalc import verbrauchsgueterkauf_verjaehrungsnachlauf
verbrauchsgueterkauf_verjaehrungsnachlauf(
    nachlaufgrund='ende_digitaler_bereitstellung',
    anknuepfung_am='2024-10-31',
    bisheriger_letzter_tag='2024-10-30',
    tatbestand_erfuellt=True,
    einordnungsnachweis='Synthetisch rechtlich qualifizierter konkreter Mangel und maßgebliches Ereignis ohne weitere offene Fristkorrekturen.',
)
```
