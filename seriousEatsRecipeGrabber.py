##Setup
import requests
import os
from bs4 import BeautifulSoup

#Change cwd
os.chdir(r"C:\Users\gabee\OneDrive\Documents\Programming\Python\Serious Eats Recipe Shopping List Generator")

#Read ingredient lists
allVeggies = []
allHerbs = []
allFruits = []
allDairy = []
allMeat = []
allFish = []
allCondiments =[]
allSpices = []
allDryGoods = []

with open("vegetableList.txt") as file:
    for i in file:
        allVeggies.append(i.strip().lower())
        
with open("herbList.txt") as file:
    for i in file:
        allHerbs.append(i.strip().lower())
        
with open("fruitList.txt") as file:
    for i in file:
        allFruits.append(i.strip().lower())
        
with open("fishList.txt") as file:
    for i in file:
        allFish.append(i.strip().lower())
allFish.append('fish')

with open("condimentList.txt") as file:
    for i in file:
        allCondiments.append(i.strip().lower())
        
with open("spiceList.txt") as file:
    for i in file:
        allSpices.append(i.strip().lower())
        
with open("dryGoodsList.txt") as file:
    for i in file:
        allDryGoods.append(i.strip().lower())

allDairy = ['milk', 'egg', 'cheese', 'custard', 'yogurt', 'yoghurt', 'cream', 'butter', 'custard', 'kefir', 'ricotta', 'whey']
allMeat = [
    'beef', 'lamb', 'mutton', 'pork', 'sausage', 'bacon', 'veal', 'venison', 'goat',
    'chicken' 'turkey', 'duck', 'goose', 'rabbit',
    'buffalo', 'bison', 'deer', 'elk', 'frog', 'goose', 'hare', 'heart', 'horse', 'kangaroo',
    'moose', 'oxe', 'squirrel', 'toad', 'turtle', 'yak', 'zebra'
]
        
url = "https://www.seriouseats.com/best-potato-leek-soup-recipe"
url2 = "https://www.seriouseats.com/crispy-enoki-and-onion-fritter-with-thai-curry-mayo-recipe"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")



#Get the ingredient list using class id
results = soup.find(id="structured-ingredients_1-0")

#Get ingredients using span
ingredientsListItems = soup.find_all("li", class_="structured-ingredients__list-item")

#Create recipe list by iterating through the results
listy = []
veggieList = []
meatList = []
fishList = []
fruitList = []
grainList = []
dairyList = []
herbList = []
condimentList = []
spiceList = []
dryGoodsList = []
otherList = []

lists = {"vegetables": veggieList, "meats": meatList, "fish":fishList, "fruits": fruitList,
         "grains":grainList, "dairy":dairyList, "herbs":herbList, "condiments":condimentList, 
         "spices":spiceList, "dry goods": dryGoodsList, 
         "other":otherList}
count=0
for i in ingredientsListItems:
    ingredient_name = i.find_all("span")
    ingStart = 0
    ingEnd = 0
    qtyStart = 0
    qtyEnd = 0
    unitStart = 0
    unitEnd = 0
    
    #Set the categories to false
    isVeggie = False
    isMeat = False
    isFruit = False
    isGrain = False
    isDairy = False
    isHerb = False
    isOther = False
    isFish = False
    isCondiment=False
    isSpice=False
    isDryGood=False
    
    #set ingredients to none
    qty = ""
    name = ""
    unit = ""
    
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
    
    
    while isVeggie == False & isMeat == False & isFruit == False & isGrain == False & isDairy == False & isHerb == False & isDryGood==False:
        count+=1

        for j in allHerbs:
            if j in name.lower():
                herbList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isHerb = True
                break
        if isHerb==True:
            print('fifth')
            break
        
        for j in allFruits:
            if j in name.lower():
                fruitList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isFruit = True
        if isFruit==True:
            break
        
        for j in allDairy:
            if j in name.lower():
                dairyList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isDairy = True
        if isDairy==True:
            break
        
        for j in allMeat:
            if j in name.lower():
                meatList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isMeat = True
        if isMeat==True:
            break
        
        for j in allFish:
            if j in name.lower():
                fishList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isFish = True
        if isFish==True:
            break
        
        for j in allCondiments:
            if j in name.lower():
                condimentList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isCondiment = True
                break
        if isCondiment==True:
            break
        
        for j in allSpices:
            if j in name.lower():
                spiceList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isSpice = True
                break
        if isSpice==True:
            break
        
        for j in allDryGoods:
            if j in name.lower():
                dryGoodsList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isDryGood = True
                break
        if isDryGood==True:
            break
        
        for j in allVeggies:
            if j.lower() in name.lower():
                veggieList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
                isVeggie = True
                break
        if isVeggie==True:
            break
        
        isOther=True
        if isOther==True:
            otherList.append([(str(name.strip()) + ", " + str(qty.strip()) + " " + str(unit.strip())).strip().title()])
            break

for list in lists:
    if lists[list]:
        lists[list].sort()
        for item in range(len(lists[list])):
            print(lists[list][item])
        print()

with open("groceryList.txt", "w") as file:
    for list in lists:
        if lists[list]:
            file.write("List for " + list)
            file.write("\n")
            lists[list].sort()
            for item in range(len(lists[list])):
                file.write(str(lists[list][item]).strip("'[]"))
                file.write("\n")
            file.write("\n")
           
                
    
"""
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
""" 
