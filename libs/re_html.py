from pathlib import Path
from re import compile, DOTALL
from sys import path


html_doc = Path(path[0]) / 'python_re.html'
html_doc = html_doc.read_text(encoding='utf-8')


pat_href = compile(r'<a.+?href=\"(?P<url>(?:(?:\.\.)|(?:http))[\w/\.:-]*?)\">')
links = list(pat_href.finditer(html_doc))
# print(*[l['url'] for l in links], sep='\n')


pat_h2 = compile(r'<h2.*?>(?P<header>[\w ]+)\W?.*?</h2>')
headers = list(pat_h2.finditer(html_doc))
# print(*[h['header'] for h in headers], sep='\n')


pat_modifications = compile(
    r'<dl.*?'
    r'class="sig-name descname"><span class="pre">(?P<func_name>\w+?)<.*?'
    r'class="versionmodified.*?</dl>',
    DOTALL
)
modifications = list(pat_modifications.finditer(html_doc))
print(*[m['func_name'] for m in modifications], sep='\n')

