import web
from language import detection

urls = (
    '/', 'Webservice'
)
app = web.application(urls, globals())


class Webservice:
    """
        Webservice Klasse
    """

    def GET(self):
        """
        Methode für die GET-Requests
        :return: Die Daten aus der Detect Methode werden auf dem Endpunkt ausgegeben
        """

        text1 = web.input().text
        lang = detection.Detection()
        return lang.detect(text1)

    def bla(self):
        # afafafasaasf
        return ''


if __name__ == "__main__":
    app.run()
