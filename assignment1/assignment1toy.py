import sys
import unittest
import csv

# dumb change

def bucketsort(A: list, size: int) -> list:
    # save the original stdout, so we can reset it at the end
    orig_stdout = sys.stdout

    # Overarching list 
    temp = []

    # Populate the large list with sublists (buckets) at each index
    for i in range(size):
        temp.append([])
    
    """
    Put passed list into buckets
    """
    # For each of our passed elements
    for j in A:
        # Find a home for it in a bucket
        subidx = int(size * j)
        # Append it there
        temp[subidx].append(j)

    """
    Print the unsorted buckets
    """
    # open a file as 'unsorted_buckets'
    unsorted_buckets = open('bucket1.txt', 'w')
    # point stdout to that file
    sys.stdout = unsorted_buckets
    # print all the buckets into the file
    for i in temp:
        print(i)

    # close the file
    unsorted_buckets.close()

    """
    Sort the buckets
    """
    # For each bucket in our list
    for k in range(size):
        # Sort those (uses sorted so I didn't have to include insertion sort in the file)
        temp[k] = sorted(temp[k])

    """
    Print the sorted buckets
    """
    sorted_buckets = open('bucket2.txt','w')
    sys.stdout = sorted_buckets
    for i in temp:
        print(i)
    sorted_buckets.close()

    """
    Overwrite Input List with Sorted List
    """
    # For overwriting our input list
    idx = 0
    # Using our large list
    for i in range(size):
        # And each sublist
        for j in range(len(temp[i])):
            # Overwrite our original list with the sorted element
            A[idx] = temp[i][j]
            idx += 1
    
    # Point stdout where it needs to go
    sys.stdout = orig_stdout
    # Return our sorted list
    return A

def main():
    """
    orig_stdout = sys.stdout
    randlist = []
    for i in range(1000):
        randlist.append(random.randrange(0,1000000)/1000000)
    
    with open('randlist.txt', 'w') as myfile:
        # point stdout to that file
        sys.stdout = myfile
        # print into the file
        print("[", end='')
        for x in randlist:
            print("%f"%(x),end=', ')
        print("]", end='')
        sys.stdout = orig_stdout
    
    # inplist = [0.31, 0.72, 0.612, 0.61]
    sortbuc = bucketsort(randlist, 1000)
    with open('randsortlist.txt', 'w') as testfile:
        # point stdout to that file
        sys.stdout = testfile
        # print into the file
        print("[", end='')
        for x in sortbuc:
            print("%f"%(x),end=', ')
        print("]", end='')
        sys.stdout = orig_stdout
    """
    # big list, so stored it as a csv
    with open('autograder/tests/buckettests/randlist.csv', 'r') as randinp:
        # open the document object
        cinplist = csv.reader(randinp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        """
        it opens as a 2d list with one element, that element being
        the full list (for a reason completely beyond me)
        """
        # convert it to a list
        inplist = list(*cinplist)
    
    ourout = bucketsort(inplist, 1000)

    with open('autograder/tests/buckettests/randsortlist.csv', 'r') as sortedret:
        cretlist = csv.reader(sortedret, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        retlist = list(*cretlist)
    assert (ourout == retlist),"Something went wrong :("

    return

class Tests(unittest.TestCase):

    """
    Test 1 in bucket sort is making sure that they intake the passed list into buckets correctly, 
    and that they output it to a file correctly
    """

    def test_bucket1(self):
        # opens our test case file
        with open('bucket1test.txt', 'r') as test1:
            buckettest1 = test1.read()
        # opens their corresponding output file
        with open('bucket1.txt', 'r') as user1:
            bucketuser1 = user1.read()
        # asserts that they're equal (they are)
        self.assertEqual(buckettest1, bucketuser1)
        """
        This example is for if the user's program didn't intake values correctly,
        or if they didn't follow our instructions (so the files don't match)
        """
        # open their incorrect file
        with open('bucket2.txt', 'r') as user2:
            bucketuser2 = user2.read()
        # check for equality against our test file (unequal, fails the test)
        self.assertEqual(buckettest1, bucketuser2)

    """
    More tests would be made for the other files we'd get, and I'd imagine a larger loop that goes
    "Given this input list, and the corresponding test files, have their program output file, then compare
    their outputs against each subtest"
    """

# Taken from one of the labs
# Didn't check if I could just disclude main(), figured I had other important things to work on
if __name__ == "__main__":
    #unittest.main() 
    main()