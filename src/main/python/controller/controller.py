import sys

from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from view import view
import requests


class Controller(QMainWindow):
    """
        Controller Klasse
    """

    def __init__(self):
        """
            Konstruktor des Controllers, Initialisiert die Objekte der View
        """
        super().__init__()
        self.ui = view.Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.checkButton.clicked.connect(self.check)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.closeButton.clicked.connect(self.close)
        self.url = "http://localhost:8080"
        self.output = ""

    def check(self):
        """
        Die Methode die den Text aus der Eingabe nimmt und an das Webservice schickt
        :return: Die überprüften Daten des Textes werden im Browser ausgegben
        """

        # der eingegebene Text
        text = self.ui.provideEdit.toPlainText()

        # Hier wird das Request mit der ?text= Option geschickt
        param = {"text": text}
        resp = requests.get(self.url, params=param)
        if resp.status_code != 200:
            raise ValueError(self.output.format(resp.status_code))

        self.output = resp.json()

        reliable = self.output["reliability"]
        language = self.output["language"]
        probability = self.output["probability"]

        if reliable:
            yon = "yes"
        else:
            yon = "no"

        html = '<p>reliable: <b>' + yon + '</b></p>' + '<p>language: <b>' + language + '</b></p>' + '<p>probability: <b>' + str(
            probability) + '</b></p></br>'

        self.ui.resultBrowser.append(html)

    def reset(self):
        """
            Methode die die Felder leert
        :return: Alle Felder der UI sind leer
        """
        self.ui.provideEdit.setText("")
        self.ui.resultBrowser.setText("")

    def close(self):
        """
        Eine Alternative um das Fenster zu schließen und das Programm zu beenden
        :return: Die Application wird geschlossen
        """

        # QtCore.QCoreApplication.instance().quit()
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
