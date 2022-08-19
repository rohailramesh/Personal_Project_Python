import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from pytube import YouTube

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube Video Downloader') # Title for window
        self.setWindowIcon(QIcon('add icon path here')) #Adding icon to the app
        self.resize(1000, 1000) #Size of window

        layout = QVBoxLayout()
        self.setLayout(layout)

        #Widgets
        self.label = QLabel('Enter the url below:')
        self.inputField = QLineEdit()
        button = QPushButton('&Download', clicked = self.download_video)
        self.output = QTextEdit()

        #adding widgets to the scree
        layout.addWidget(self.label)
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def download_video(self):
        url = self.inputField.text()
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()
        yd.download('ADD PATH HER')
        self.output.setText(f'Downloaded {yt.title}')

app = QApplication(sys.argv)


# creating an instance of the class
Window = MyApp() 
Window.show()



app.exec()