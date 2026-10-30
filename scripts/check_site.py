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
# Photo credits and self-hosted fonts must remain valid in the offline guide.
for place in data['places']:
 assert all(place.get(k) for k in ['cn','pinyin','name','fullName']), place['id']
 photo=place['photo']
 assert (root/photo['src']).read_bytes().startswith(b'\xff\xd8'), photo['src']
 assert all(photo.get(k) for k in ['author','source','license','licenseUrl','caption']), place['id']
 assert photo['source'].startswith('https://commons.wikimedia.org/wiki/File:'), place['id']
 assert photo['licenseUrl'].startswith('https://creativecommons.org/'), place['id']
css=(root/'assets/fonts/fonts.css').read_text()
for font in re.findall(r'url\("([^\"]+)"\)',css):
 assert (root/'assets/fonts'/font).read_bytes().startswith(b'wOF2'), font
sw=(root/'sw.js').read_text()
for asset in list((root/'assets/fonts').glob('*.woff2'))+list((root/'assets/photos').glob('*.jpg')):
 assert str(asset.relative_to(root)) in sw, asset
assert 'IBM Plex Sans Thai Looped' in css
assert len({p['id'] for p in data['locations']})==len(data['locations'])
print('PASS: trilingual place data, 8 credited JPEGs, WOFF2 fonts and offline asset coverage')

import xml.etree.ElementTree as ET
ns={'k':'http://www.opengis.net/kml/2.2'}
extra=ET.parse(root/'Songzanlin_2026_Addition.kml')
assert len(extra.findall('.//k:Placemark',ns))==1
assert extra.find('.//k:coordinates',ns).text=='99.70417,27.86333,0'
assert 'Sōngzànlín Sì' in extra.find('.//k:Placemark/k:name',ns).text
assert 'Songzanlin_2026_Addition.kml' in sw
assert 'route-options' in s.ids
print('PASS: one-point Songzanlin KML and route-options anchor')
