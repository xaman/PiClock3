from presentation.formatter.formatter import Formatter


class TextFormatter(Formatter):

    def __init__(self):
        super(TextFormatter, self).__init__()

    def format(self, text):
        return text \
            .replace('á', 'a') \
            .replace('é', 'e') \
            .replace('í', 'i') \
            .replace('ó', 'o') \
            .replace('ú', 'u') \
            .replace('ü', 'u') \
            .replace('ñ', 'n') \
            .replace('Á', 'A') \
            .replace('É', 'E') \
            .replace('Í', 'I') \
            .replace('Ó', 'O') \
            .replace('Ú', 'U') \
            .replace('Ñ', 'N') \
            .replace('ç', 'c') \
            .replace('Ç', 'C')
