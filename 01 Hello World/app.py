from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("My App")
        button = QPushButton("Press me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window. 
        self.setCentralWidget(button)
        

if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    # Note, any widget can be a window.
    
    # window = QWidget() # Empty default
    # window = QPushButton("Push me!")
    window = MainWindow() # Pre-made with standard features.
    
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
