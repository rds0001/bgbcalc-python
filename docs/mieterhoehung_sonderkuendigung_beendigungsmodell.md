<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## mieterhoehung_sonderkuendigung_beendigungsmodell

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `zugang_erhoehungsmitteilung_am`: Tatsächlicher Zugang der558/559-Erhöhungserklärung.
- `verlangter_erhoehungsbeginn_am`: Rechtlich verlangter Beginn am Monatsersten, nicht vor regulärem Beginn.
- `kuendigungseingang_am`: Tatsächlicher Eingang der561-Kündigung innerhalb des Erklärungsfensters.
- `beendigungsmodell`: Zwingend rechtlich vorgegebener Bezug: kuendigungszugangsmonat oder letzter_ausuebungsmonat. Keine automatische Auslegung einer früher erklärten Kündigung.
- `bisherige_monatsmiete`: Unveränderte rechtlich geschuldete Monatsmiete bei wirksamer561-Kündigung.
- `einordnungsnachweis`: Wirksame561-Kündigung, rechtlicher Beendigungsbezug und Monatsmiete ausdrücklich qualifizieren; später gewünschte Termine, ordentliche Kündigung und Vertragsaufhebung gesondert.

561-Erklärungsfenster prüfen und zwei Monatsendbezüge berechnen; ausschließlich rechtlich vorgegebenes Modell auswählen und unveränderte Miete ausweisen.

Beide bedingten Monatsendtermine, ausgewählter Beendigungstermin und bisherige Monatsmiete.

561-Beendigungsrechnung als ausdrücklich bedingtes Modell: Ende des zweiten Monats nach tatsächlichem Kündigungszugangsmonat oder nach letztem Ausübungsmonat. Beide Termine ausweisen, keine stille Gleichsetzung früher Erklärung mit voller Fristausnutzung. Vorhandenes561-Fenster berücksichtigt später verlangte Erhöhung nachBGH25.9.2013VIIIZR280/12; diese Quelle belegt volle Fristausnutzung, nicht universell den früheren Beendigungsbezug. Rechtliche Auswahl daher zwingend. Eingang muss im berechneten Fenster liegen. Bei rechtlich wirksamer561-Kündigung tritt die Erhöhung nicht ein, bisherige Monatsmiete bleibt bis Ende maßgeblich. Keine automatische Wirksamkeitsfeststellung oder taganteilige Schlussabrechnung. Monatsendtermin nicht wegen Wochenende verschieben.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_561_T0001, BGB_561_T0002, BGB_561_T0003

```python
from bgbcalc import mieterhoehung_sonderkuendigung_beendigungsmodell
mieterhoehung_sonderkuendigung_beendigungsmodell(
    zugang_erhoehungsmitteilung_am='2024-01-15',
    verlangter_erhoehungsbeginn_am='2024-04-01',
    kuendigungseingang_am='2024-02-10',
    beendigungsmodell='kuendigungszugangsmonat',
    bisherige_monatsmiete='800',
    einordnungsnachweis='561-Beendigungsrechnung als ausdrücklich bedingtes Modell: Ende des zweiten Monats nach tatsächlichem Kündigungszugangsmonat oder nach letztem Ausübungsmonat. Beide Termine ausweisen, keine stille Gleichsetzung früher Erklärung mit voller Fristausnutzung. Vorhandenes561-Fenster berücksichtigt später verlangte Erhöhung nachBGH25.9.2013VIIIZR280/12; diese Quelle belegt volle Fristausnutzung, nicht universell den früheren Beendigungsbezug. Rechtliche Auswahl daher zwingend. Eingang muss im berechneten Fenster liegen. Bei rechtlich wirksamer561-Kündigung tritt die Erhöhung nicht ein, bisherige Monatsmiete bleibt bis Ende maßgeblich. Keine automatische Wirksamkeitsfeststellung oder taganteilige Schlussabrechnung. Monatsendtermin nicht wegen Wochenende verschieben.',
)
```
