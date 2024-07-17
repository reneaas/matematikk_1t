from pygments.lexers import PythonLexer
from pygments.filter import Filter
from pygments.filters import CodeTagFilter

class CustomPythonLexer(PythonLexer):
    def __init__(self, **options):
        super().__init__(**options)
        self.add_filter(CodeTagFilter(codetags=['TODO', 'XXX', 'BUG', 'NOTE']))


