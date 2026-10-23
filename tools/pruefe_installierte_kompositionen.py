"""Ausgelieferte Anwendungsketten ausschließlich gegen das installierte Python-Paket."""
import argparse
import gzip
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from importlib.resources import files
import bgbcalc

parser = argparse.ArgumentParser()
parser.add_argument('--bericht', required=True)
parser.add_argument('--testdatei', action='append', help='Explizite Teilprüfung; Dateiname im ausgelieferten Testverzeichnis.')
args = parser.parse_args()
inhalte = json.loads(gzip.decompress(files('bgbcalc').joinpath('daten/kompositionen.json.gz').read_bytes()))
with tempfile.TemporaryDirectory(prefix='bgb-kompositionen-') as tmp:
    wurzel = Path(tmp)
    for name, text in inhalte.items():
        pfad = Path(name)
        if pfad.is_absolute() or '..' in pfad.parts or '\\' in name:
            raise ValueError('Unzulässiger Ressourcenpfad: ' + name)
        ziel = wurzel / pfad
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(text, encoding='utf-8')
    tests = sorted((wurzel / 'python/tests').glob('test_*.py'))
    if args.testdatei:
        unbekannt=set(args.testdatei)-{p.name for p in tests}
        if unbekannt:
            raise ValueError('Unbekannte Testdateien: '+', '.join(sorted(unbekannt)))
        tests=[p for p in tests if p.name in args.testdatei]
    if not tests:
        raise RuntimeError('Keine ausgelieferten Anwendungstests.')
    umgebung = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTEST_DISABLE_PLUGIN_AUTOLOAD='1')
    # Nur das tatsächlich importierte Paket weiterreichen, keine fremden Quellpfade.
    umgebung['PYTHONPATH']=str(Path(bgbcalc.__file__).resolve().parent.parent)
    subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', *map(str, tests)],
                   cwd=tmp, env=umgebung, check=True)
bericht = dict(status='PASS', umfang='TEILPRUEFUNG' if args.testdatei else 'ALLE_AUSGELIEFERTEN_KOMPOSITIONEN', testdateien=len(tests), paketpfad=bgbcalc.__file__, fachliche_vollstaendigkeit_bestaetigt=False)
Path(args.bericht).write_text(json.dumps(bericht, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(bericht))
