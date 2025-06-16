""" 
    libWindow.py
"""
import sys, traceback
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QLineEdit,QLabel,QTextEdit)
from PySide6.QtCore import (Signal,QObject,QRunnable,QThreadPool)
from PySide6.QtGui import (QTextCursor)

#----------------------------------------------------------------


#----------------------------------------------------------------
#----------------------------------------------------------------
class WindowUtility(QWidget):
    def __init__(self, parent=None):
        app =  QApplication()   # 事前にAppplicationが必要
        super().__init__()

        self.app = app
        self.threadpool = QThreadPool()

        self.wx = 0
        self.wy = 0
        self.ww = 0
        self.wh = 0
        self.logs = None
        self.inputBox = None

    # UIの初期化
    def InitializeUI(self, title:str, x:int = 0, y:int = 0, w:int = 0, h:int = 0):
        self.wx = x if x != 0 else 300
        self.wy = y if y != 0 else 300
        self.ww = w if w != 0 else 620
        self.wh = h if h != 0 else 800

        self.setStyleSheet('font-family: Kaiti SC; font-size: 14px;')
        self.setWindowTitle(title) # ウィンドウのタイトル
        self.setGeometry(self.wx, self.wy, self.ww, self.wh) # ウィンドウの位置と大きさ

    #----------------------------------------------------------------
    # 汎用ボタン作成
    def createButton(self, name:str, x:int, y:int, w:int, h:int, delegate) -> QPushButton:
        button = QPushButton(name,self)
        button.pressed.connect(delegate)
        button.setGeometry(x,y,w,h)
        return button

    #----------------------------------------------------------------
    # 入力Box処理
    def createInputBox(self, title:str, titlex:int, titlew:int, x:int, y:int, w:int, h:int, delagate) -> QLineEdit:
        label = QLabel(title, self)
        label.setGeometry(titlex, y, titlew, h)

        self.inputBox = QLineEdit('',self)
        self.inputBox.setGeometry(x, y, w, h)
        self.inputBox.returnPressed.connect(delagate)
        return self.inputBox

    # 入力エリアクリア
    def clearInput(self) -> None:
        if self.inputBox is not None:
            self.inputBox.setText("")

    #----------------------------------------------------------------
    # LogView処理
    def createLogView(self, x:int, y:int, w:int, h:int, css:str=None) -> QTextEdit:
        self.logs = QTextEdit(self)
        if css is not None:
            self.logs.setStyleSheet(css)
        self.logs.setGeometry(x,y,w,h)
        self.logs.toHtml()
        return self.logs

    # LogViewへの文字列追加
    def addLogColor(self, newText:str, color:str) -> None:
        if self.logs is not None and newText != "":
            html = self.logs.toHtml() + "<span style='color: "+ color +";'>"+ newText +"</span>\n"
            self.logs.setHtml(html)
            self.logs.moveCursor(QTextCursor.End)
            self.logs.ensureCursorVisible()  # スクロールを自動で調整

    # LogViewへの文字列追加
    def addLogMessage(self, newText:str) -> None:
        self.addLogColor(newText, "white")

    # LogViewへの文字列追加
    def addLogError(self, newText:str) -> None:
        self.addLogColor(newText, "red")
            

    # LogViewへの文字列追加
    def addLogWarning(self, newText:str) -> None:
        self.addLogColor(newText, "yellow")



    # LogClearボタン処理
    def clearLog(self) -> None:
        if self.logs is not None:
            self.logs.setText("")

    #----------------------------------------------------------------
    def getThreadPool(self):
        return self.threadpool
    
    #----------------------------------------------------------------
    # main
    def main(self) -> None:
        self.showNormal()
        self.app.exec()

#----------------------------------------------------------------
# Job Worker
#----------------------------------------------------------------
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = self.WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.process

    class WorkerSignals(QObject):
        finished = Signal()
        error = Signal(tuple)
        process = Signal(tuple)

    def setFunction(self, progressFn, finishedFn):
        self.signals.process.connect(progressFn)
        self.signals.finished.connect(finishedFn)

    def start(self, pool:QThreadPool):
        pool.start(self)
        return

    #@Slot()
    def run(self):
        try:
            self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        finally:
            self.signals.finished.emit()  # Done

#================================================================
# End of file.
#================================================================
