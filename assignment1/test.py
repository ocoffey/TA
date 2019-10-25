try:
        arr[0]
    except IndexError:
        return []
    else:
        try:
            arr[1]
        except IndexError:
            return arr
    for i in range(1, len(arr)):
        ournum = arr[i]
        j = i - 1
        while j >= 0 and ournum < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ournum
    return arr    


"""
def main():

    mylist = [10, 14, 5, 8, 7, 17, 12, 1, 6, 16, 9, 11, 4, 15, 2, 18, 3, 13]
    myval = columnsort(mylist,18)
    print(*myval)
    
    listofmany = list(range(-100,100))
    
    list_s36 = random.sample(listofmany, 36)

    for x in list_s36:
        print(x,end=', ')
    print()
    my36val = columnsort(list_s36,36)
    for x in my36val:
        print(x,end=', ')
    print()

    list_s72 = random.sample(listofmany, 72)
    for x in list_s72:
        print(x,end=', ')
    print()
    my72val = columnsort(list_s72,72)
    for x in my72val:
        print(x,end=', ')
    print()
    
    nega_list = random.sample(listofmany,72)
    
    for x in nega_list:
        print(x,end=', ')
    print()
    mynega = columnsort(nega_list,72)
    for x in mynega:
        print(x,end=', ')
    print()

    return


if __name__ == "__main__":
    #unittest.main() 
    main()

"""