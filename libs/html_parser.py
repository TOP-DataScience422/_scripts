from html.parser import HTMLParser
from pathlib import Path
from sys import path


script_dir = Path(path[0]) 
source_file = script_dir / 'python_re.html'

html_doc = source_file.read_text(encoding='utf-8')


class PythonREParser(HTMLParser):
    
    append_tag = False
    append_data = False
    section = []
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            if attrs['id'] == 'module-contents':
                self.append_tag = True
        if self.append_tag:
            if tag == 'span':
                if attrs.get('class', '') == 'pre':
                    self.append_data = True
    
    def handle_endtag(self, tag):
        if self.append_tag:
            if tag == 'section':
                self.append_tag = False
                self.append_data = False
    
    def handle_data(self, data):
        if self.append_data:
            self.section.append(data)
            self.append_data = False
    

parser = PythonREParser()
parser.feed(html_doc)

# >>> parser.section
# ['RegexFlag', 'enum.IntFlag', 'class', 're.', 'RegexFlag', 'enum.IntFlag', '__all__', 're.', 'A', 're.', 'ASCII', '\\w', '\\W', '\\b', '\\B', '\\d', '\\D', '\\s', '\\S', '(?a)', 'U', 'str', 'UNICODE', '(?u)', 're.', 'DEBUG', 're.', 'I', 're.', 'IGNORECASE', '[A-Z]', 'Ü', 'ü', 'ASCII', 'LOCALE', '(?i)', '[a-z]', '[A-Z]', 'IGNORECASE', 'ASCII', 're.', 'L', 're.', 'LOCALE', '\\w', '\\W', '\\b', '\\B', '(?L)', 'LOCALE', 'ASCII', 'LOCALE', 're.', 'M', 're.', 'MULTILINE', "'^'", "'$'", "'^'", "'$'", '(?m)', 're.', 'NOFLAG', '0', 're.', 'S', 're.', 'DOTALL', "'.'", "'.'", '(?s)', 're.', 'U', 're.', 'UNICODE', 'str', 'ASCII', 're.', 'X', 're.', 'VERBOSE', '*?', '(?:', '(?P<...>', '(?', ':', '*', '?', '#', '#', '(?x)']

