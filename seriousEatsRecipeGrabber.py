import requests
import os
from bs4 import BeautifulSoup

url = "https://www.seriouseats.com/best-potato-leek-soup-recipe"
url2 = "https://www.seriouseats.com/crispy-enoki-and-onion-fritter-with-thai-curry-mayo-recipe"

page = requests.get(url2)
soup = BeautifulSoup(page.content, "html.parser")

#Get the ingredient list using class id
results = soup.find(id="structured-ingredients_1-0")

#Get ingredients using span
ingredientsListItems = soup.find_all("li", class_="structured-ingredients__list-item")

#Create recipe list by iterating through the results
listy = []
for i in ingredientsListItems:
    ingredient_name = i.find_all("span")
    ingStart = 0
    ingEnd = 0
    qtyStart = 0
    qtyEnd = 0
    unitStart = 0
    unitEnd = 0
    
    #Get ingredient name
    ingStart = str(ingredient_name).find("data-ingredient-name=\"true\"")
    if ingStart != -1:
        ingEnd = ingStart + len("data-ingredient-name=\"true\">")
        name = str(ingredient_name)[ingEnd:str(ingredient_name).find("<", ingEnd)]

    
    
    #Get quantity
    qtyStar = str(ingredient_name).find("<span data-ingredient-quantity=\"true\">")
    if qtyStar != -1:
        qtyEnd = qtyStar + len("<span data-ingredient-quantity=\"true\">")
        qty = str(ingredient_name)[qtyEnd:str(ingredient_name).find("<", qtyEnd)]

        
    #Get ingredient-unit
    unitStart = str(ingredient_name).find("data-ingredient-unit=\"true\"")
    if unitStart != -1:
        unitEnd = unitStart + len("data-ingredient-unit=\"true\"") + 1
        unit = str(ingredient_name)[unitEnd:str(ingredient_name).find("<", unitEnd)]
       
        
    if qtyStart != -1 & unitStart != -1:
        print(name.strip() + ", "  + qty.strip() + " " + unit.strip())
        listy.append([name.strip(), qty.strip(), unit.strip()])
    else:
        print(name.strip())
        listy.append([name.strip()])
        
listy.sort()
    
for i in listy:
    if len(i) == 3:
        print(str(i[0]) + ", " + str(i[1]) + " " + str(i[2]))
    else:
        print(i[0])
