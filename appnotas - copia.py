import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
from PyQt5.QtCore import QSize

class appnotas (QMainWindow):
    #variables
    id_nota = 1
    lista_notas = []


    def __init__(self, nota_ref=str()):
        super().__init__()
        self.nota_ref = nota_ref
        appnotas.lista_notas.append(self)
        self.configurar()


    def configurar(self):
        self.setMinimumSize(QSize(250,250))
        self.setWindowTitle("Notas")
        self.widget_central = QTextEdit()
        self.widget_central.setFont(QFont("Georgia", 11))
        self.setCentralWidget(self.widget_central)
        self.crear_menu()
        self.crear_clipboard()

    def crear_menu(self):
        self.acc_nueva_nota = QAction("nueva nota",self)
        self.acc_nueva_nota.setShortcut("Ctrl+N")
        self.acc_nueva_nota.triggered.connect(self.nueva_nota)

        self.acc_limpiar = QAction("limpiar", self)
        self.acc_limpiar.setShortcut("Ctrl+W")
        self.acc_limpiar.triggered.connect(self.limpiar)

        self.acc_salir = QAction("Salir", self)
        self.acc_salir.setShortcut("Ctrl+Q")
        self.acc_salir.triggered.connect(self.close)

        #crear las acciones para menu color
        self.acc_amarillo = QAction("amarillo", self)
        self.acc_amarillo.triggered.connect(lambda: self.cambiar_fondo(self.acc_amarillo.text()))

        self.acc_azul = QAction("azul", self)
        self.acc_azul.triggered.connect(lambda: self.cambiar_fondo(self.acc_azul.text()))

        self.acc_verde = QAction("verde", self)
        self.acc_verde.triggered.connect(lambda: self.cambiar_fondo(self.acc_verde.text()))


        #crear acciones menu pegar
        self.acc_pegar = QAction("Pegar", self)
        self.acc_pegar.setShortcut("Ctrl+v")
        self.acc_pegar.triggered.connect(self.pegar_a_clipboard)

        #seleccionar barra de menu
        barra_menu=self.menuBar()
        barra_menu.setNativeMenuBar(False)

        #crear menu archivo y agregar acciones
        menu_archivo = barra_menu.addMenu("Archivo")
        menu_archivo.addAction(self.acc_nueva_nota)
        menu_archivo.addAction(self.acc_limpiar)
        menu_archivo.addAction(self.acc_salir)


        menu_color = barra_menu.addMenu("Color")
        menu_color.addAction(self.acc_amarillo)
        menu_color.addAction(self.acc_azul)
        menu_color.addAction(self.acc_verde)

        menu_pegar = barra_menu.addMenu("pegar")
        menu_pegar.addAction(self.acc_pegar)


    def crear_clipboard(self):
        self.clipboard=QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copiar_a_clipboard)


    def nueva_nota(self):
        #crear una nueva instancia de la clase appnotas
        self.nota_ref= str("nota%d" % appnotas.id_nota)
        appnotas().show()
        # incrementar la variable con el id de la nota
        appnotas.id_nota+=1
    def limpiar (self):
        #limpiar texto de la nota
        self.widget_central.clear()
    def copiar_a_clipboard(self):
        # leer el contenido del clipboard del so
        return self.clipboard.text()
    def pegar_a_clipboard(self):
        # leer el contenido del clipboard de la app y pegarlo en la nota
        texto=self.copiar_a_clipboard()
        self.widget_central.insertPlainText(texto + "\n")

    def cambiar_fondo(self, text_color):
        #cambiar el fondo de la nota por el menu
        if text_color=="amarillo":
            self.widget_central.setStyleSheet("background-color: rgb(248, 253, 145)")
        elif text_color == "azul":
            self.widget_central.setStyleSheet("background-color: rgb(145, 253, 251)")
        elif text_color == "verde":
            self.widget_central.setStyleSheet("background-color: rgb(148, 253, 145)")
        else:
            self.widget_central.setStyleSheet("background-color: white")


if __name__=='__main__':
    app = QApplication(sys.argv)
    ventana = appnotas()
    ventana.show()
    sys.exit(app.exec_())