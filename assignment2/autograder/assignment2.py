"""Circular Doubly Linked List"""
import sys
import unittest
import io


# Node
class CDLLNode:
    """ Node for our CDLL

    Requires a timestamp and tweet
    """

    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
        """
        Constructor

        Default values set to none

        If the user passes a value to the constructor, it's set
        """
        self.time: str = time
        self.tweet: str = tweet
        self.next_node: CDLLNode = next_node
        self.prev_node: CDLLNode = prev_node


# Linked List
class CDLL:
    """
    Circular Doubly Linked List

    Each node points to the next and previous nodes

    The head and tail point to each other
    """

    def __init__(self):
        """
        Constructor

        Sets 'head' and 'current' to none

        Sets the number of nodes to 0
        """
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numnodes: int = 0

    def insert(self, time: str, tweet: str):
        """Takes the time and the tweet,

        Creates a node to insert into our list at current

        If our list is empty, adds the node at 'head'

        Otherwise, adds the node at 'current.prev'
        """
        # if empty list
        if self.head == None:
            # make a new node, and point head and current to it
            self.head = self.current = CDLLNode(time, tweet)
            # make the next and prev values the node itself
            self.head.next_node = self.head.prev_node = self.head
        else:
            nnode = CDLLNode(time, tweet)
            # point node before current to this node, and back
            # make a new node
            nnode.prev_node = self.current.prev_node
            nnode.next_node = self.current
            self.current.prev_node.next_node = nnode
            self.current.prev_node = nnode
            if time < self.head.time:
                self.head = self.current = nnode
        # increase the number of nodes we have
        self.numnodes += 1

    def go_next(self):
        """
        Updates current as the next node
        """
        # update current as the next node
        self.current = self.current.next_node

    def go_prev(self):
        """
        Updates current as the previous node
        """
        # update current as the previous node
        self.current = self.current.prev_node

    def go_first(self):
        """
        Updates current as the head node
        """
        # update current as the head
        self.current = self.head

    def go_last(self):
        """
        Updates current as the head.prev (last) node
        """
        # update current as the previous of the head (the tail)
        self.current = self.head.prev_node

    def skip(self, n: int):
        """
        Updates current as the node after n skips
        """
        # makes use of knowing the number of nodes
        # does some math, skips extraneous full loops
        for x in range(n % self.numnodes):
            # updates the correct amount of times
            self.go_next()

    def print_current(self):
        """
        Prints the data of the current node
        """
        print(self.current.time)
        print(self.current.tweet)

def myParser(sentence: str) -> tuple:
    """
    Takes a sentence to parse,
    returns the parsed elements in a tuple as (time, tweet)
    """
    # splits into 3 parts, based on '|'
    parse = sentence.split('|')
    # the third section becomes the tweet
    tdata = parse[2].strip()
    # split the time/date substring based on spaces
    parse = parse[1].split(' ')
    # the fourth part is the time
    ttime = parse[3]
    # append these into our Linked List
    return (ttime, tdata)


def populateList(LList: CDLL, filedat):
    # having tweetdata as a variable, parse it
    # and add it to the linked list
    for x in filedat:
        # parse for the time and tweet
        time, tweet = myParser(x)
        # if empty list, enter node at head, then continue
        if LList.numnodes == 0:
            LList.insert(time, tweet)
            continue
        else:
            LList.go_first()
            # traverse the list, insert if you find a place
            # makes use of python's "For Else" conditional
            for y in range(LList.numnodes):
                if time < LList.current.time:
                    LList.insert(time, tweet)
                    break
                else:
                    LList.go_next()
            # if you go through the entire list, insert it as the tail
            else:
                LList.insert(time, tweet)


def userinloop(LList: CDLL) -> None:
    """Event Loop

    Input:

    `n`: prints the next tweet (chronologically) to the stdout

    `p`: prints the previous tweet (chronologically) to the stdout

    `f`: prints the first tweet (oldest) to the stdout

    `l`: prints the last tweet (most recent) to the stdout

    `num`: prints the number of nodes in the list to the stdout

    `<number>`: skips tweets circularly and prints the current to the stdout

    `s <word>`: searches for the next occurrence of the substring word in the following tweets (search is case insensitive and performs a circular traversal in the list)

    `q`: quits the program
    """
    # declares usercom
    usercom = ""
    # if user input is 'q', leave the event loop
    while usercom != 'q':
        # gets input for which command to do
        usercom = input()
        # if 'n', print the next tweet
        if usercom == 'n':
            LList.go_next()
            LList.print_current()

        # if 'p', print the previous tweet
        elif usercom == 'p':
            LList.go_prev()
            LList.print_current()
        # if 'f', print the oldest tweet
        elif usercom == 'f':
            LList.go_first()
            LList.print_current()
        # if 'l', print the newest tweet
        elif usercom == 'l':
            LList.go_last()
            LList.print_current()
        #if 'num', print the number of nodes
        elif usercom == 'num':
            print(LList.numnodes)
        # if they're trying to search for a word
        elif usercom[0] == 's':
            # start at the next node (next occurrence)
            LList.go_next()
            # strip the 's' and 'space'
            pusercom = usercom.split("s")
            usercom = pusercom[1].strip().lower()
            # loop for all the nodes, print if you find it
            # make sure to convert the node data as lowercase
            for x in range(LList.numnodes):
                # check for the search term within the tweet
                if usercom in LList.current.tweet.lower():
                    # print the current tweet
                    LList.print_current()
                    break
                # if not there, go to the next tweet
                else:
                    LList.go_next()
            # if we loop all the way through, didn't find the word
            else:
                print("Word not found")
        # else input might be a number to skip ahead to
        else:
            # see if the input is actually a number
            try:
                x = int(usercom)
                # suggesting we got a number, skip to it, and print the tweet
                LList.skip(x)
                LList.print_current()
            # if not a number, account for error
            except ValueError:
                if usercom == 'q':
                    continue
                else:
                    print("Please enter a valid command")
    # go back to main
    return


def main():
    try:
        sys.argv[1]
    except IndexError:
        print("File Not Passed")
        return
    # make sure we can actually open the passed filename
    with open(sys.argv[1],'r') as f:
        tweetdata = f.readlines()

    # make linked list
    TweetLL = CDLL()

    # populate the Linked List with the tweet data
    populateList(TweetLL, tweetdata)

    # go to the first element in the list
    TweetLL.go_first()

    # print the head tweet
    TweetLL.print_current()

    # makes an event loop for the user
    userinloop(TweetLL)

    # done
    return



class TestLinkedList(unittest.TestCase):
    """
    30 Points
    """
    """
    def test_eval_prepend(self):
        llpre = CDLL()
        for i in range(3,0,-1):
            llpre.prepend("",str(i))
        sout = []
        for i in range(3,0,-1):
            sout.append(llpre.current.tweet)
            llpre.go_next()
        self.assertListEqual(sout,["1", "2", "3"])

    def test_eval_append(self):
        llapp = CDLL()
        for i in range(0,10):
            llapp.append(str(i),"")
        sout = []
        for i in range(0, 10):
            sout.append(llapp.current.time)
            llapp.go_next()
        self.assertListEqual(sout,["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def test_eval_go_next(self):
        llgn = CDLL()
        for i in range(2):
            llgn.append("",str(i))
        self.assertEqual(llgn.current.tweet, "0")
        llgn.go_next()
        self.assertEqual(llgn.current.tweet, "1")

    def test_eval_go_prev(self):
        llgp = CDLL()
        for i in range(5):
            llgp.prepend(str(i),"")
        self.assertEqual(llgp.current.time, "4")
        llgp.go_prev()
        self.assertEqual(llgp.current.time, "0")

    def test_eval_go_first(self):
        llgf = CDLL()
        for i in range(20):
            llgf.append(str(i),"")
        for i in range(10):
            llgf.go_next()
        self.assertEqual(llgf.current.time, "10")
        llgf.go_first()
        self.assertEqual(llgf.current.time, "0")

    def test_eval_go_last(self):
        llgl = CDLL()
        for i in range(50):
            llgl.prepend("",str(i))
        for i in range(27):
            llgl.go_prev()
        self.assertEqual(llgl.current.tweet, "26")
        llgl.go_last()
        self.assertEqual(llgl.current.tweet, "0")

    def test_eval_skip(self):
        lls = CDLL()
        for i in range(40):
            if i%3 == 0:
                lls.append("Hello","")
            elif i%3 == 1:
                lls.append("There","")
            else:
                lls.append("Again","")
        self.assertEqual(lls.current.time, "Hello")
        lls.skip(50)
        self.assertEqual(lls.current.time, "There")

    def test_eval_print_cur(self):
        llpc = CDLL()
        studout = io.StringIO()
        origout = sys.stdout

        llpc.append("This Is","The Test")

        sys.stdout = studout
        llpc.print_current()

        self.assertEqual(studout.getvalue(),"This Is\nThe Test\n")
        sys.stdout = origout
    """


if __name__ == "__main__":
    main()