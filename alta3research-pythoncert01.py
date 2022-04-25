#!/usr/bin/env python3

"""
https://github.com/tylerpt/alta3research-python-cert/
using requests & TheMealDB to search for, then cook a tasty dish
"""

import requests
import crayons

MEAL_API = 'https://www.themealdb.com/api/json/v1/1/' #TheMealDB API using dev/educational (free) key


def main():
    print("What's for dinner tonight?")
    dinner_tonight = input("> ") #gathering search term from user for API

    searchedmeal = requests.get(f"{MEAL_API}search.php?s={dinner_tonight}") #using requests to get the result of our search term
    searchedjson = searchedmeal.json() #JSON decoding (using requests)
    meal_tonight = searchedjson['meals'] #the API returns a dictionary with a length of 1 - 'meals' reuturns our results in a list
    
    #most search terms return just 1 meal - will print just the first result
    meal_name = meal_tonight[0].get('strMeal') #pulling the name of the meal, under dictionary key 'strMeal' under the first search term result
    print("On the menu for tonight is: "+ crayons.green(meal_name, bold = True)) #printing the name of the meal in bold green using crayons

    meal_source = meal_tonight[0].get('strSource') #pulling the source of the meal
    print(crayons.green("Source: ",bold = True) + meal_source) #printing the source of the meal. this usually seems to be the link to the recipe, sometimes returns blank



if __name__ == "__main__":
    main()