# Vermögensschaden nach Mitverschuldensquote

## vermoegensschaden_mitverschulden

Kürzungsbetrag = ersatzfähiger Vermögensschaden mal vorgegebene Mitverschuldensquote. Verbleibender Ersatzbetrag = Vermögensschaden minus Kürzungsbetrag. Exakte Bruchrechnung ohne automatische Cent-Rundung.

Parametrisierte Rechenstufe für eine rechtlich bereits bestimmte Vermögensschadensposition und deren Mitverschuldensquote nach § 254. Die Abwägung der Verursachungs- und Verschuldensanteile einschließlich Absatz2 wird nicht durch eine erfundene Bewertungsformel ersetzt. Unterschiedlich zu quotierende Schadenspositionen getrennt rechnen. Keine automatische Anwendung auf Schmerzensgeld oder sonstige billige Entschädigung, deren Gesamtbemessung eine eigenständige Abwägung erfordert. Weitere Anspruchsvoraussetzungen, Vorteilsausgleichung, Zahlungen und Rangfolgen anderer Abzüge sind nicht enthalten. Die gleiche Quote nicht doppelt berücksichtigen.

wert enthält kuerzungsbetrag und verbleibender_ersatzbetrag als exakte EUR-Brüche; ihre Summe entspricht dem eingegebenen Vermögensschaden. Bei NICHT_ANWENDBAR ist wert null. Die Nutzerquote und ihre Begründung bleiben unter eingaben und nutzervorgaben sichtbar.

- `vermoegensschaden`: Nichtnegative EUR-Dezimalzeichenfolge oder exaktes Bruchobjekt mit zaehler/nenner nach NUMERIK.md. Für diese konkrete Schadensposition rechtlich ermittelter ersatzfähiger Vermögensschaden vor der hier anzuwendenden Mitverschuldenskürzung. Kein bereits um dieselbe Quote gekürzter Betrag.
- `mitverschuldensquote`: Dezimalzeichenfolge oder exaktes Bruchobjekt nach NUMERIK.md im geschlossenen Bereich 0 bis 1. Anteil der Kürzung wegen des dem Geschädigten zuzurechnenden Mitverschuldens; beispielsweise 0.25 für 25 Prozent, nicht 25. Die Quote muss für die konkrete Position aus der Abwägung nach § 254 ermittelt sein; sie wird nicht allein aus der Zahl Beteiligter oder einer bloßen Verschuldensbehauptung berechnet.
- `quotenbegruendung`: Nichtleere deutsche fachliche Begründungs-/Herkunftsangabe für die Nutzerquote. Insbesondere sind die einschlägigen Verursachungsbeiträge und gegebenenfalls Warnpflicht, Schadensabwendungs-/Schadensminderungspflicht oder nach § 278 zugerechnetes Verhalten zuvor rechtlich zu bewerten; der Text wird als Nutzervorgabe dokumentiert, nicht als richtig bestätigt.
- `kuerzung_nach_254_anwendbar`: Expliziter Wahrheitswert zur rechtlichen Anwendung der vorgegebenen Quote auf diese Vermögensschadensposition. FALSE ergibt NICHT_ANWENDBAR. Keine automatische Feststellung der Ersatzpflicht oder eines Mitverschuldens.
