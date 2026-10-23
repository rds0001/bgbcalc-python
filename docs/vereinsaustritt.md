<!-- Automatisch aus Fachverträgen erzeugt; fachliche Freigabe bleibt separat. -->

## verein_austrittskalender

Feste lokale BGB-Fassung; gesetzlicher Anwendungsbereich und externe Bewertungen ausdrücklich vorqualifiziert.

Parameter:

- `kuendigungszugang_am`: Rechtlich feststehender Zugangstag der AustrittserklärungYYYY-MM-DD.
- `fristdauer`: Nichtnegative ganze Zahl der satzungsmäßig vorgesehenen Kündigungsfrist in fristeinheit;0 bedeutet keine zusätzliche Kündigungsfrist. Höchstens3652059, alle berechneten Daten einschließlich Zweijahresvergleich im Kalenderbereich.
- `fristeinheit`: tage, wochen, monate oder jahre; satzungsmäßige Dauer, keine freie Wahl zur Änderung der Frist.
- `nur_zum_geschaeftsjahresende`: Expliziter Wahrheitswert zur qualifizierten Satzungsbindung an das Geschäftsjahresende.
- `geschaeftsjahresenden`: Nur bei Geschäftsjahresbindung vollständige streng aufsteigende Liste1..1000 maßgeblicher Geschäftsjahresenden alsISO-Daten, ab Zugang bis mindestens zum benötigten Termin. Sonst null. Kein Kalenderjahr automatisch unterstellen.
- `satzungsnachweis`: Nichtleerer Nachweis von Zugang, satzungsmäßiger Frist, Geschäftsjahr und gegebenenfalls rechtlich qualifizierter Kombination. Ergebnis ist ein Rechenvergleich, kein Wirksamkeitsurteil.

Ereignisfrist und Zweijahresgrenze kalendergenau berechnen; gegebenenfalls erstes einschlägiges Geschäftsjahresende ab Fristende auswählen und beide Termine getrennt mit der Zweijahresgrenze vergleichen.

wert enthält rechnerisches_kuendigungsfristende, rechnerischer_austrittstermin, zweijahresgrenze und zwei getrennte Wahrheitswerte zur zeitlichen Grenzüberschreitung. Kein automatisches Gültigkeitsurteil.

§39II: rechnerischer Vergleich einer satzungsmäßig vorgegebenen Kündigungsfrist mit höchstens zwei Kalenderjahren sowie Auswahl des nächsten einschlägigen Geschäftsjahresendes. Fristdauer0 bedeutet keine zusätzliche Kündigungsfrist. Geschäftsjahr und gegebenenfalls Kombination beider Satzungsbedingungen rechtlich vorqualifizieren; keine automatische Satzungsauslegung. Die beiden Zweijahresvergleiche betreffen getrennt die Kündigungsfrist und den resultierenden Kalendertermin. Eine Überschreitung wird sichtbar gemacht, nicht durch eine erfundene geltungserhaltende Reduktion geheilt; keine automatische Wirksamkeitsentscheidung für die Satzung oder den Austritt. Alle einschlägigen Geschäftsjahresenden ab Zugang bis zum benötigten Termin vollständig und geordnet vorgeben. Keine automatische193-Verschiebung eines Geschäftsjahresendes. Die Zweijahresgrenze wird kalendergenau berechnet, nicht pauschal als730Tage.

Gemeinsame exakte Zahlengrenzen nach NUMERIK.md. Fehlende Pflichteingaben EINGABE_FEHLT, unzulässige Typen/Bereiche EINGABE_UNGUELTIG.

Quelle: BGB_PDF_SHA256_9b5a99536e7b00756e9fa5f20082bd9ad3951b37c381fc0f5d52aa5a556839eb; BGB_39_T0002

```python
from bgbcalc import verein_austrittskalender
verein_austrittskalender(
    kuendigungszugang_am='2024-02-29',
    fristdauer=1,
    fristeinheit='jahre',
    nur_zum_geschaeftsjahresende=False,
    geschaeftsjahresenden=None,
    satzungsnachweis='§39II: rechnerischer Vergleich einer satzungsmäßig vorgegebenen Kündigungsfrist mit höchstens zwei Kalenderjahren sowie Auswahl des nächsten einschlägigen Geschäftsjahresendes. Fristdauer0 bedeutet keine zusätzliche Kündigungsfrist. Geschäftsjahr und gegebenenfalls Kombination beider Satzungsbedingungen rechtlich vorqualifizieren; keine automatische Satzungsauslegung. Die beiden Zweijahresvergleiche betreffen getrennt die Kündigungsfrist und den resultierenden Kalendertermin. Eine Überschreitung wird sichtbar gemacht, nicht durch eine erfundene geltungserhaltende Reduktion geheilt; keine automatische Wirksamkeitsentscheidung für die Satzung oder den Austritt. Alle einschlägigen Geschäftsjahresenden ab Zugang bis zum benötigten Termin vollständig und geordnet vorgeben. Keine automatische193-Verschiebung eines Geschäftsjahresendes. Die Zweijahresgrenze wird kalendergenau berechnet, nicht pauschal als730Tage.',
)
```
