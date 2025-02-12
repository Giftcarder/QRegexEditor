import re
from qregexeditor.qt import QtGui


class MatchHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super(MatchHighlighter, self).__init__(document)
        self.prog = None
        self._format = QtGui.QTextCharFormat()
        self._format.setBackground(QtGui.QBrush(QtGui.QColor('#0051ff')))

    def highlightBlock(self, text):
        if self.prog and text:
            for m in self.prog.finditer(text):
                start, end = m.span()
                self.setFormat(start, end - start, self._format)
