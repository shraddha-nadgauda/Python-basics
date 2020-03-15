import clr as clr

if __name__ == "__main__":
    dict1 = {'Fruit': 'Mango', 'Season': 'Summer', 'Colour': 'Yellow', 'Quantity': 100}
    print(dict1['Fruit'])
    dict1['Fruit'] = 'Apple'
    dict1['Season'] = 'Fall'
    dict1['Colour'] = 'Red'
    dict1['Quantity'] =  200
    print(dict1)
    del dict1['Quantity']
    print(dict1)
    dict1.clear()
    print(dict1)

