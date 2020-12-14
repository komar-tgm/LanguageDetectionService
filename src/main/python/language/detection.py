import pycld2 as cld2
import json


class Detection:
    """
        Klasse die die Detection durchführt
    """
    def __init__(self):
        pass

    def detect(self, text):
        """
        Methode in der die Detection durchgeführt wird
        :param text: Der Text der überprüft wird
        :return: ein JSON Objekt mit den Ergebnissen der Überprüfung
        """
        isReliable, textBytesFound, details = cld2.detect(text)
        first, second, third = details

        lang, short, prob, other = first

        data = {
            "reliability": isReliable,
            "language": lang,
            "short": short,
            "probability": prob
        }

        return json.JSONEncoder().encode(data)
