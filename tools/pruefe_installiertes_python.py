"""Nur installiertes Paket verwenden; optional vollständige R-Ergebnisse vergleichen."""
import argparse
import gzip
import json
from importlib.resources import files
import bgbcalc

parser = argparse.ArgumentParser()
parser.add_argument('--r-ergebnisse')
parser.add_argument('--bericht', required=True)
args = parser.parse_args()
faelle = json.loads(gzip.decompress(files('bgbcalc').joinpath('daten/referenzen.json.gz').read_bytes()))
r_ergebnisse = json.load(open(args.r_ergebnisse)) if args.r_ergebnisse else None
for fall in faelle:
    try:
        ergebnis = getattr(bgbcalc, fall['funktion'])(**fall['eingaben'])
    except bgbcalc.Berechnungsfehler as fehler:
        ergebnis = {'status': fehler.status, 'wert': None}
    assert {k: ergebnis[k] for k in ('status', 'wert')} == fall['erwartung'], fall['fall_id']
    if r_ergebnisse is not None:
        r = r_ergebnisse[fall['fall_id']]
        if r.get('nutzervorgaben') == []:
            r['nutzervorgaben'] = {}
        assert ergebnis == r, fall['fall_id']
bericht = dict(status='PASS', referenzfaelle=len(faelle), paketpfad=bgbcalc.__file__,
               vollstaendige_ergebnisparitaet=r_ergebnisse is not None,
               fachliche_vollstaendigkeit_bestaetigt=False)
with open(args.bericht, 'w') as f:
    json.dump(bericht, f, indent=2)
print(json.dumps(bericht))
