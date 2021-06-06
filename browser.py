from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back",self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reaload_btn = QAction("reaload", self)
        reaload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reaload_btn)

        home_btn = QAction("Home",self)
        home_btn.triggered.connect(self.to_home)
        navbar.addAction(home_btn)

        self.Urlbar = QLineEdit()
        self.Urlbar.returnPressed.connect(self.Search)
        navbar.addWidget(self.Urlbar)
        self.browser.urlChanged.connect(self.update_url)


    def to_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def Search(self):
        url = self.Urlbar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.Urlbar.setText(q.toString())




app = QApplication(sys.argv)
QApplication.setApplicationName("nizBrowser")
window = MainWindow()
app.exec_()