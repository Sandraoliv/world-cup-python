from exceptions import *


def data_processing(data):
    titles = data.get("titles")
    first_cup = data.get("first_cup")
    current_year = 2023
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_year = int(first_cup[:4])
    years_of_cup = []
    for year in range(1930, current_year, 4):
        years_of_cup.append(year)
    if first_cup_year < 1930 or first_cup_year not in years_of_cup:
        raise InvalidYearCupError("there was no world cup this year")

    max_possible_titles = (current_year - first_cup_year) // 4 
   
    if titles > max_possible_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
    return data
