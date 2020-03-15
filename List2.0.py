if __name__ == '__main__':
    family_names = ['Shraddha','Shrihari','Surekha','Rahul','Chintu','Akshay','Nanda','Nitin','Shunali']
    print(family_names)
    for name in family_names:
            print(name)


if __name__ == '__main__':
    family_names = ('Shraddha','Shrihari','Surekha','Rahul','Chintu','Akshay','Nanda','Nitin','Shunali')
    for tuplename in family_names:
        print(tuplename)

if __name__ == '__main__':
    myinfo = {'name': 'Shraddha', 'surname': 'Nadgauda', 'Age': 30}
    for info in myinfo.keys():
        print(info,':',myinfo[info])