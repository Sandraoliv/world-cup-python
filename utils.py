from exceptions import *


def data_processing(data):
    titles = data.get("titles")
    first_cup = data.get("first_cup")

    if titles < 0:
        raise NegativeTitlesError()

    first_cup_year = int(first_cup[:4])
    if first_cup_year < 1930:
        raise InvalidYearCupError()

    current_year = 2023
    max_possible_titles = (current_year - first_cup_year) // 4 + 1
    if titles > max_possible_titles:
        raise ImpossibleTitlesError()
    return data
