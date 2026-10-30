from pathlib import Path
from html.parser import HTMLParser
import re, json
root=Path(__file__).resolve().parents[1]/'site'
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[];self.local=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id'in d:
   assert d['id'] not in self.ids, f'Duplicate id {d["id"]}'
   self.ids.add(d['id'])
  for a in ['src','href']:
   x=d.get(a,'')
   if x.startswith('#'):self.refs.append(x[1:])
   elif x and not re.match(r'^(https?:|data:|mailto:)',x):self.local.append(x)
s=Scan();s.feed((root/'index.html').read_text())
for x in s.refs:assert x in s.ids,x
for x in s.local:assert (root/x).is_file(),x
j=(root/'data.js').read_text();data=json.loads(j[len('window.TRIP='):-1])
assert len(data['days'])==6 and len(data['places'])==8
assert sum(len(d['events'])for d in data['days'])==36
assert all(d['events']for d in data['days'])
assert '1lE7UFUHc2npUgthw_yn-MtbtvPUCnrU'in(root/'app.js').read_text()
json.loads((root/'manifest.webmanifest').read_text())
print('PASS: HTML ids, internal links, assets, manifest, 6 days / 36 events / 8 locations, user My Maps ID')
