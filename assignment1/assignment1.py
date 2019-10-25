import sys
import copy

def calendar(year: int) -> list:
    date = (1 +  5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7  # equation to get date

    if (year % 100 == 0) & (year % 400 == 0): #calculate if the given year is a leap year
        leapyear = True
    elif (year % 100 != 0) & (year % 4 == 0):
        leapyear = True
    else:
        leapyear = False

    daysofyear = [date] #make a list recording the year and the days of the week within it
    if leapyear == True: #loop to fill the year. This one is for leap year
        for i in range(1,366):
            dayofweek = (date + i)%7
            daysofyear.append(dayofweek)
    else: #loop to fill list of regular year
        for i in range(1,365):
            dayofweek = (date + i) % 7
            daysofyear.append(dayofweek)

    days_of_week = {  # dictionary that stores what numbers match what day of the week
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }

    months = {  #dictionary that stores the months of the year
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }

    shortdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"] #list of dates for making the calendar itself

    print("In the year ",year, ", January 1st was/will be on a", days_of_week[date])
    if leapyear == True:
        print("It is a leap year")
    for num in range(1, 13): #print out the calendar itself
        print(months[num - 1])
        print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
              .format(*shortdays, sep=" "))
        if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12: #check what month is next, could probably be written
            daysmonthhas = 31                                                                 #cleaner
        elif (num == 2) and leapyear == True:
            daysmonthhas = 29
        elif (num == 2) and leapyear == False:
            daysmonthhas = 28
        else:
            daysmonthhas = 30
        print(date * 4 * ' ' + '{:>3}'.format(1), end=' ')
        for today in range(2, daysmonthhas + 1):
            if (date + today-1) % 7 == 0:
                print()
            print('{:>3}'.format(today), end=' ')
            if today == daysmonthhas:
                print()
            lastday = (date + today) % 7 #record what the last day of the month is
        date = lastday #set date to the last day so the next month starts on the correct date

    #print (daysofyear, len(daysofyear))
    return daysofyear


def alt_bubblesort(A: list, size: int) -> list:
    newlist = [A.copy()] #append does not work for this. Have to use the copy function instead
   # print(A)
    for i in (range(size)):
        for j in reversed(range(0, size - 1)):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]
        newlist.append(A.copy())
    #    print(A)

    print(newlist)
    return newlist


def bubbleSort(A: list, size: int) -> list: #just for reference for switch_bubblesort
    print(A)
    for i in range(size):
        for j in range(0, size - i - 1):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]
        print(A)

    return A

def switch_bubblesort(A: list, size: int) -> list:
    newlist = [A.copy()]
  #  print(A)
    start = 0
    end = size
    len = end-start
    switch = True
    while(len>0):
        while switch == True:
            for j in reversed(range(start, end - 1)): #alt bubble sort
                if A[j] > A[j + 1]:
                    A[j + 1], A[j] = A[j], A[j + 1]
            newlist.append(A.copy())
        #    print("Alt:", A)
            start=start+1
            switch = False

        while switch == False:
            for k in range(start, end - 1): #regular bubble sort
                if A[k] > A[k + 1]:
                    A[k + 1], A[k] = A[k], A[k + 1]
            newlist.append(A.copy())
        #    print("Reg:", A)
            end = end-1
            switch = True
        len = end-start
    print(newlist)
    return newlist

# sorts each column within the rectangle
def sortRect(Rect: list):
    for i in Rect:
        insertionsort(i)

# print the rectangle
def pRect(Rect: list, S: int, R: int):
    # for each row
    for i in range(R):
        # and each column of each row
        for j in range(S):
            # if element is the last on the row
            if j == S-1:
                # print the element, and a newline
                print(Rect[j][i])
            else:
                # print the element, followed by a tab
                print(Rect[j][i],end='\t')

# print the shift
def pShift(Shifted: list, S: int, R: int):
    # note the halfway point of the column
    halfway = R//2
    # for each row
    for i in range(R):
        # for each column withing rows
        for j in range(S):
            # skips printing column 0 until past the halfway mark
            if j == 0 and i < halfway:
                print(" ",end='\t')
            # after the last column shift has been printed, then print spaces
            elif j == S-1 and i >= halfway:
                print(" ")
            # only prints past the halfway mark
            elif j == 0:
                print(Shifted[j][i-halfway],end='\t')
            # if printing numbers in last column
            elif j == S-1:
                print(Shifted[j][i])
            # default print inner cols
            else:
                print(Shifted[j][i],end='\t')

# first transposition
def ftrans(Rect: list, S: int, R: int) -> list:
    # deep copy, since python is a jerk and doesn't by default
    # (took me like an hour of scratching my head to remember that)
    temp = copy.deepcopy(Rect)
    # for each column in our list
    for i in range(S):
        # and for each row in those columns
        for j in range(R):
            # transpose our rectangle into our temporary one
            # using some fun index math
            temp[j%S][((R//S)*i)+(j//S)] = Rect[i][j]

    return temp

# detranspose
def dtrans(Rect: list, S: int, R: int) -> list:
    temp = copy.deepcopy(Rect)
    # go through row by row
    for row in range(R):
        # then the columns within those rows
        for col in range(S):
            # detranspose with more fun index math
            temp[row//(R//S)][((S*row)%R)+col] = Rect[col][row]

    return temp

# generic insertion sort
def insertionsort(arr: list) -> list:
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

def bucketsort(A: list, size: int) -> list:
    # save the original stdout
    orig_stdout = sys.stdout

    # Overarching list for buckets
    temp = []

    # Populate the large list with sublists (buckets) at each index
    for i in range(size):
        temp.append([])

    # For each of our passed elements
    for j in A:
        # Find a home for it in our overarching list
        subidx = int(size * j)
        # Append it there
        temp[subidx].append(j)

    """
    Print the unsorted buckets
    """
    # open a file as u(nsorted)buckets
    with open('bucket1.txt', 'w') as ubuckets:
        # point stdout to that file
        sys.stdout = ubuckets
        # print into the file
        for x in temp:
            print(x)

    # For each bucket in our list
    for k in range(size):
        # Sort those
        temp[k] = insertionsort(temp[k])

    """
    Print the sorted buckets
    """
    # open a file as s(orted)buckets
    with open('bucket2.txt','w') as sbuckets:
        # point stdout to that file
        sys.stdout = sbuckets
        # print into the file
        for x in temp:
            print(x)

    """
    Notes: Could have refactored this last section to be nicer/
    easier/more pythonic. Didn't.
    """   
    # For overwriting our input list
    idx = 0
    # For the amount of buckets we have
    for i in range(size):
        # And the amount of elements within each bucket
        for j in range(len(temp[i])):
            # Overwrite our original list with the sorted element
            A[idx] = temp[i][j]
            idx += 1
    
    # redirect stdout back
    sys.stdout = orig_stdout
    return A

# N is the size of the list
def columnsort(A: list, N: int) -> list:
    # save the original stdout
    orig_stdout = sys.stdout

    # initial values
    S = 1
    R = N
    # to account for the 'anamoly'
    if (N == 18):
        S = 3
        R = 6
    # else calculate S according to the formula
    # 2(S^2) <= R
    else:
        while True:
            if 2*(S*S) <= R:
                S += 1
                R = N // S
                continue
            else:
                S -= 1
                R = N // S
                break

    # Create and populate our rectangle
    Rect = []
    # make S columns
    for i in range(S):
        Rect.append([])
        # Make R rows
        for j in range(R):
            # For each row, grab the corresponding element from A, and append it
            Rect[i].append(A[i+(S*j)])

    # somewhat bad practice but slightly more efficient
    # of only resetting sys.stdout at the end of the function

    # open a file for our rectangle
    with open('column1.txt','w') as cols:
        # point stdout to that file
        sys.stdout = cols
        # print our rectangle after creating it into the file
        pRect(Rect, S, R)

    # sort the columns
    sortRect(Rect)

    # print first column sort into the file
    with open('column2.txt','w') as socols:
        sys.stdout = socols
        pRect(Rect, S, R)

    # transpose the rectangle
    Rect = ftrans(Rect, S, R)
    # print first transposition to the file
    with open('column3.txt','w') as tcols:
        sys.stdout = tcols
        pRect(Rect, S, R)

    sortRect(Rect)
    
    # detranspose the rectangle
    Rect = dtrans(Rect,S,R)

    sortRect(Rect)

    """
    *Shift Rectangle*
    """
    # Make new list
    Shifted = []
    # for S+1 columns
    for i in range(S+1):
        # Make a column
        Shifted.append([])
        # if looking at the first column in shifted,
        # append first half of first Rect column
        if i == 0:
            Shifted[i].extend(Rect[0][0:(R//2)])
        # if looking at last column in shifted,
        # append the last half of the last Rect column 
        elif i == S:
            Shifted[i].extend(Rect[S-1][(R//2):])
        # otherwise, append based on i
        else:
            # last half of previous column
            Shifted[i].extend(Rect[i-1][(R//2):])
            # first half of this column
            Shifted[i].extend(Rect[i][0:(R//2)])

    # print our shifted rectangle to file
    with open('column4.txt','w') as shcols:
        sys.stdout = shcols
        # print our shifted rectangle
        pShift(Shifted, S+1, R)
    
    sortRect(Shifted)
    
    # put shifted back into array
    # (no need to translate it back into a rectangle)
    A.clear()
    for x in range(S+1):
        A.extend(Shifted[x][:])

    # redirect stdout back
    sys.stdout = orig_stdout
    return A


if __name__ == '__main__':

    print("Question 1")
    calendar(2019)

    print("Question 2a")
    switch_bubblesort([10,4,6,1,9,0,8], 7)

    print("Question 2b")
    switch_bubblesort([8,7,6,5,4,3,2,1], 8)

    print("Question 3")
    bucketsort([0.1, 0.6, 0.4, 0.5, 0.9],3)
    
    print ("Question 4")
    columnsort([84, 50, 14, 95, 73, 33, 61, 70, 51, 75, 17, 25, 56, 91, 7, 21, 28, 16, 67, 90, 5, 10, 4, 23, 18, 34, 77, 46,
           88, 47, 15, 9, 1, 59, 44, 2],36)
