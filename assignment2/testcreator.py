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
        if not self.head:
            # make a new node, and point head and current to it
            self.head = self.current = CDLLNode(time, tweet)
            # make the next and prev values the node itself
            self.head.next_node = self.head.prev_node = self.head
        else:
            # make a new node
            nnode = CDLLNode(time, tweet)
            # point node before current to this node, and back
            nnode.prev_node = self.current.prev_node
            self.current.prev_node.next_node = nnode
            # point current to this node, and back
            nnode.next_node = self.current
            self.current.prev_node = nnode
            # if we went through the entire list
            if self.current is self.head:
                # check for prepending the node
                prep = self.time_check(time)
                # if we need to prepend it
                if prep:
                    # update head
                    self.head = nnode
            # set current to the newly created node
            self.current = nnode

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

    def time_check(self, time: str) -> bool:
        """Compare the time of the current node against the passed time"""
        if self.head == None:
            return True
        # x iterates through Hours, Minutes, Seconds
        for x in range(3):
            # If current x is more than the passed one
            if int(self.current.time[3 * x:(3 * x) + 2]) > int(time[3 * x:(3 * x) + 2]):
                # Prepend the tweet
                return True
            # If the current x is less than the passed one
            elif int(self.current.time[3 * x:(3 * x) + 2]) < int(time[3 * x:(3 * x) + 2]):
                # leave, check the next tweet
                return False
            # arbitrarily prepend if all values equal
            elif x == 2:
                return True
            # if current x is equal, try next x
            else:
                continue


def myParser(sentence: str) -> tuple:
    """
    Takes a sentence to parse,
    returns the parsed elements in a tuple as (time, tweet)
    """
    # splits into 3 parts, based on '|'
    parse = sentence.split('|')
    # the third section becomes the tweet
    tdata = parse[2]
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
        LList.go_first()
        # traverse the list, insert if you find a place
        for y in range(LList.numnodes):
            toInsert = LList.time_check(time)
            if toInsert:
                LList.insert(time, tweet)
                break
            else:
                LList.go_next()
        # if you go through the entire list, insert it as the tail
        else:
            LList.insert(time, tweet)
        # LList.print_all()
def main():
    # make sure the file is passed as a command line arg
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please include a filename as a command line argument")
        return

    # make sure we can actually open the passed filename
    try:
        with open(filename) as f:
            tweetdata = f.readlines()
    except FileNotFoundError:
        print("Couldn't open the file, please make sure it's within the directory")
        return

    # make linked list
    TweetLL = CDLL()
    # populate the Linked List with the tweet data
    populateList(TweetLL, tweetdata)

    # go to the first element in the list
    TweetLL.go_first()

    # print the head tweet
    TweetLL.print_current()


    # makes an event loop for the user

    # done
    return

if __name__ == "__main__":
    # unittest.main()
    main()
