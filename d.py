import sys
import de
import os
import subprocess
import fitz

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolTip, QAction
from PyQt5.QtGui import QFont, QIcon


class ExampleApp(QtWidgets.QMainWindow, de.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.browse_folder)
        self.listWidget.itemClicked.connect(self.openf)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.label.setToolTip('<b>Автор: Abanazar Helper: DeitySenpai</b>')

        white = QAction(QIcon('loW.svg'), '&White', self)
        white.triggered.connect(self.white)

        discord = QAction(QIcon('loD.svg'), '&Dis', self)
        discord.triggered.connect(self.dis)

        cloud = QAction(QIcon('loC.png'), '&Cloud', self)
        cloud.triggered.connect(self.cloud)

        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&Theme')
        fileMenu.addAction(white)
        fileMenu.addAction(discord)
        fileMenu.addAction(cloud)
    
    def white(self):
        subprocess.call(['python3', 'd.py'])
    
    def dis(self):
        subprocess.call(['python3', 'm.py'])
    
    def cloud(self):
        subprocess.call(['python3', 'dewasik.py'])

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        os.chdir(directory)
        self.listWidget_2.clear()
        self.listWidget_2.addItem(directory)

        if directory:
            for file in os.listdir(directory):
                if file.endswith(".pdf"):
                    self.listWidget.addItem(os.path.join(file))
                elif file.endswith(".txt"):
                    self.listWidget.addItem(os.path.join(file))
                    
    def openf(self):
        self.textEdit.clear()
        s = self.listWidget
        for item in s.selectedItems():            
            document = item.text()
            
            if document.endswith(".pdf"):
                doc = fitz.open(document)
                for current_page in range(len(doc)):
                    page = doc.loadPage(current_page)
                    page_text = page.getText("text")
                    self.textEdit.append((page_text))
            
            elif document.endswith(".txt"):
                for item in s.selectedItems():            
                    s = item.text()
                    self.textEdit.append(open(s, 'r').read())
                

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
