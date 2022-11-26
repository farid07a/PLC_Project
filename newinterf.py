from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget, QMainWindow, QApplication, QMenu, QMenuBar, \
    QAction


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        #self.resize(800, 600)
        self.resize(1100, 700)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.init_widgets()

    def init_widgets(self):
        self.creation_menu_bar()
        self.creation_panel()
        self.side_menu_container()
        self.actions_buttons_side_menu()

    def creation_menu_bar(self):
        menu_bar = QMenuBar(self)
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))
        menu_bar.setGeometry(QtCore.QRect(0, 0, sizeObject.width(), 25))

        menuFile = QMenu(menu_bar)
        menuFile.setTitle("File")

        # list_item in menuFile
        action = QAction(menu_bar)
        action.setText("New")

        action2 = QAction(menu_bar)
        action2.setText("Close")

        # add list item in menuFile
        menuFile.addAction(action)
        menuFile.addAction(action2)

        # add menuFile in menu bar
        menu_bar.addAction(menuFile.menuAction())

    def side_menu_container(self):
        widget_global = QWidget(self)  # this container for menu buttons
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))
        widget_global.setGeometry(QtCore.QRect(0, 25, 140, sizeObject.height()))

        self.btn_plc = QPushButton('PLC', widget_global)
        self.btn_plc.setGeometry(QtCore.QRect(5, 30, 130, 30))

        self.btn_history = QPushButton('History', widget_global)
        self.btn_history.setGeometry(QtCore.QRect(5, 70, 130, 30))

        self.btn_view_tags = QPushButton('view_tags', widget_global)
        self.btn_view_tags.setGeometry(QtCore.QRect(5, 120, 130, 30))


    
    def actions_buttons_side_menu(self):
        self.btn_plc.clicked.connect(self.show_plc_container)
        self.btn_history.clicked.connect(self.show_history_container)

    def creation_panel(self):
        self.all_container = QtWidgets.QStackedWidget(self)
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))

        self.all_container.setGeometry(150,25,sizeObject.width()-150,sizeObject.height()-25)
        self.all_container.setStyleSheet("background-color: rgb(188, 188, 188)")
        self.all_container.setCurrentIndex(1)
        
        self.plc_container=QWidget()
        self.history_container = QWidget()


        self.all_container.addWidget(self.plc_container)
        self.all_container.addWidget(self.history_container)

        
        table = QTableWidget(self.plc_container)
        table.setGeometry(QtCore.QRect(5,150,500,800))
        table.setRowCount(0)
        table.setColumnCount(4)

    def show_plc_container(self):
        self.all_container.setCurrentWidget(self.plc_container)
        
    def show_history_container(self):
        self.all_container.setCurrentWidget(self.history_container)
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window=Ui_MainWindow()
    window.show()
    app.exec_()