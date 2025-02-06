import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaz import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar el botón con la función que cuenta los caracteres correctamente
        self.pushButton.clicked.connect(self.contar_caracteres)

    def contar_caracteres(self):
        cadena = self.lineEdit.text().strip()  # Captura el texto sin espacios adicionales
        print(f"Texto capturado: {cadena}")  # Para depuración: muestra el texto capturado
        cantidad = len(cadena)
        self.label.setText(f"Cantidad de caracteres: {cantidad}")  # Mostrar el conteo en QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
