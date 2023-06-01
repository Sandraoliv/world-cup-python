class NegativeTitlesError(Exception):
    def __init__(self):
        self.message = "Titles cannot be negative."


class InvalidYearCupError(Exception):
    def __init__(self):
        self.message = "There was no World Cup this year."


class ImpossibleTitlesError(Exception):
    def __init__(self):
        self.message = "Impossible to have more titles than disputed cups."

