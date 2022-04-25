#!/usr/bin/env python3

"""
tylerpt
using requests & TheMealDB to search for, then cook a tasty dish
"""

import requests
import crayons

mealAPI = 'https://www.themealdb.com/api/json/v1/1/'

def searchmeal(foodstr):
    searchedmeal = requests.get(f"{mealAPI}search.php?s={foodstr}")
    searchedjson = searchedmeal.json()

print(searchmeal("beef"))
