Store = {
    "Graound Beef" : "$6.99",
    "Smoked Chicken Sausage" : "$6.49",
    "Boneless Skinless Chicken Breasts" : "$11.97",
    "Banana" : "$0.24",
    "Avacado" : "$2.19",
    "Cucumber" : "$0.99",
    "Strawberries" : "$4.99",
    "Milk" : "$2.99",
    "Eggs Large Garde AA" : "$1.99",
    "Cream Cheese" : "$1.67"
}

print (Store)
for listValue in Store.values():
    print (listValue)

print ("--------------------------")
for listKey in Store.keys():
    print (listKey)

print ("--------------------------")

for list_price in Store.keys():
    print (Store[list_price])

print ("--------------------------")
for listItem in Store.items():
    print (listItem)

print ("--------------------------")
isExist = "Carrot" in Store
print (isExist)
 isExist = "Milk" in Store
    print (isExist)
