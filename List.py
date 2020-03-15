if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = ['orange', 'mango', 'apple']
    print(list)
    print(list[5])
    list[2] = 50
    print(list)
    print(list[1:4])
    print(list[::-8])
    print(list[1:11:1])
    del list[8]
    print(list)
    list.remove(7)
    print(list)
    list.append(11)
    print(list)
    list.append(list2)
    print(list)



