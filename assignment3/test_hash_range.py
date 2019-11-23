import random
import sys

orig_stdout = sys.stdout
with open('hashsize.txt','w') as myhash:
    # point stdout to that file
    sys.stdout = myhash
    # print into the file
    for x in range(2000):
        temp = ""
        for y in range(20):
            # make a random letter between 'a' and 'z'
            myLet = random.randrange(ord('a'), ord('z'))
            temp += chr(myLet)
        print(temp)
sys.stdout = orig_stdout