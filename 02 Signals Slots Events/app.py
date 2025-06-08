import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button_is_checked = False

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        
        # button.clicked.connect(self.the_button_was_clicked)
        button.toggled.connect(self.the_button_was_toggled)
        
        button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(button)

    # def the_button_was_clicked(self):
    #     print("Clicked!")
        
    def the_button_was_toggled(self, checked):
        # print("Checked?", checked)
        
        self.button_is_checked = checked
        print(self.button_is_checked)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()