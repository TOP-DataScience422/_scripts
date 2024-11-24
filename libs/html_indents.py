from pathlib import Path
from re import compile
from sys import path


script_dir = Path(path[0]) 
source_file = script_dir / 'date_formats.html'
edited_file = script_dir / 'date_formats_ed.html'

no_indented_tags = (
    'br',
    'meta',
    'link',
    'input',
    'script',
)

html_doc = source_file.read_text(encoding='utf-8')


pat_whitespaces = compile(r'\s+')
pat_tag_name = compile(r'<(?P<name>[a-z]+)')

html_ed = pat_whitespaces.sub(' ', html_doc)

indent = ' '*2
lvl = 0
end = 0
html_ed2 = ''
pat_tag = compile(r'(?P<open>\<(?P<name>[a-z]+))|(?P<close>\</)')
indent_flag = False
close_flag = False

# breakpoint()

for mo in pat_tag.finditer(html_ed):
    if mo['open']:
        if indent_flag and not close_flag:
            lvl += 1
        indent_flag = mo['name'] not in no_indented_tags
        close_flag = False
    elif mo['close']:
        if close_flag or not indent_flag:
            lvl -= 1
        close_flag = True
    html_ed2 += f'{html_ed[end:mo.start()]}\n{indent*lvl}{mo.group()}'
    end = mo.end()



edited_file.write_text(html_ed2, encoding='utf-8')

