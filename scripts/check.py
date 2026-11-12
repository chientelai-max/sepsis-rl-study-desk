import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]
data=json.loads((p/'dist/data/papers.json').read_text())
required=set(json.loads((p/'templates/paper-template.json').read_text()))
ids=set()
for d in data:
 assert required<=d.keys(), 'missing fields'
 assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',d['id'])
 assert d['id'] not in ids, 'duplicate id'
 ids.add(d['id'])
 assert isinstance(d['year'],int)
 assert d['tag'] in ['基礎研究','臨床適用性','方法檢查']
 assert len(d['notes'])==7 and all(isinstance(n,str) and n.strip() for n in d['notes'])
 assert re.fullmatch(r'10\.\d{4,9}/[A-Za-z0-9.()_/-]+',d['doi'])
for n in ['index.html','app.js','style.css','AGENTS.md','paper-template.json','SUBMISSION.md']:
 assert (p/'dist'/n).is_file(),n
for root,pub in [('AGENTS.md','AGENTS.md'),('SUBMISSION.md','SUBMISSION.md'),('templates/paper-template.json','paper-template.json')]:
 assert (p/root).read_bytes()==(p/'dist'/pub).read_bytes(), 'stale public copy'
print(f'PASS: {len(data)} papers; schema, IDs, DOI formats, resources and public copies verified.')
