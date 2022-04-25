#!/usr/bin/env python3

"""
tylerpt
using requests & TheMealDB to search for, then cook a tasty dish
"""

import requests
import crayons

mealAPI = 'https://www.themealdb.com/api/json/v1/1/'


def main():
    print("What's for dinner tonight?")
    dinner_tonight = input("> ")
    
    print(dinner_tonight)

    searchedmeal = requests.get(f"{mealAPI}search.php?s={dinner_tonight}")
    searchedjson = searchedmeal.json()

    meal_tonight = searchedjson['meals']
    name_of_meal = meal_tonight[0].key('strMeal')
    print(name_of_meal)


if __name__ == "__main__":
    main()