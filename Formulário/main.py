import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from formr import Ui_MainWindow 

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.limp_form)
        self.ui.pushButton_2.clicked.connect(self.salvar)

    def limp_form(self):
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_3.clear()


    def salvar(self):
        caminho = QFileDialog.getSaveFileName(self, "Salvar", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(self.ui.lineEdit_7.text() + "\n")
                f.write(self.ui.lineEdit_6.text() + "\n")
                f.write(self.ui.lineEdit_3.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())