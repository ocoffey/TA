# Assignment 3

### (Due: Dec 6, 2019) 11:59PM  [NO EXTENSIONS WILL BE GRANTED]

### Total points: 100

## Introduction

In this assignment we will be spell checking large text files.

This assignment is to be completed **individually**. You are NOT allowed to share nor acquire source code from other students in the class, current or previous. You must start the assignment early in order to get proper help from the TAs and the instructor. You can also post general questions or ask for clarifications on Piazza, however, **do not post your own source code.**

**_Please read the entire assignment carefully, before starting_**

## Reading Books

Your job is to write a program that will determine if the words in each of three different books are in the provided English dictonary. The script used to download the books has been included in this repository once again, and the command is (same to lab 10,11):

```bash
$source getbooks.sh
```

Note that the books provided for this assignment are different than the ones from the labs. You can find the dictionary needed for your work [here](link).

## Creating the Hash Table

You will design and implement a class which creates a hash table called `HashTable` which contains the methods: `make_hash()`, `make_table()`, `insert()`,  and `lookup()` (refer to the comments in the code given for information on what each function should do). The table is initlized at a size dependent on the size of the dictionary you are reading in and creates a list that size which contains the words in the dictionary. Your class must be implemented in the `assignment3.py` file.

```python
class HashTable:
    """Hast Table Class"""
    def __init__(self, size: int = 0):
        """Constructor
        
        Takes a size, stores it
        Makes a list of the given size
        """
        self.size: int = size
        self.table: list = []
        self.make_table()

    def make_table(self) -> None:
        """Hash Table Creator
        
        Makes a table of the class's size"""

    def make_hash(self, word: str) -> int:
        """Hash Creator
        
        Takes a string, applies a hash method to it,
        and returns an int (the index to store the word)
        """
     def insert(self, word: str) -> None:
        """Insert
        Gets a hash for the given word, and
        attaches the word there
        """
    def lookup(self, word: str) -> bool:
        """Lookup
        Returns True if the word is in the table
        """
```
**DO NOT implement your hash table as a python dictionary. Doing so will result in a zero for the assignment**


## Spell Checker

Once you have downloaded the books and the dictionary and created your `HashTable` class, read all of the words in the **dictionary** provided into a hash-table as an unordered set.

Basically an unordered set is an associative container that contains a set of unique objects of type Key. Search, insertion, and removal can then be done on average in constant-time complexity. Internally, the elements of an unordered set are are not sorted in any particular order, but organized into buckets (hence hash-table). Which bucket an element is placed into depends entirely on the hash of its value. This allows fast access to individual elements, since once a hash is computed, it refers to the exact bucket the element is placed into.

Once you have loaded the dictionary and opened a book you should clean the text of the book by removing non-alphanumeric or apostrophes (') from the text file. You can use code you have from previous labs to do this. Afterwards you should compare the words of the book to those in the dictionary. Print out each word which appears in the book but not in the dictionary. 

#### Note: 
* PLEASE USE the exact method definitions as given for each question. If you do not, then the autograder on Gradescope will not be able to recognize your answer and will give you a zero.
* The hash table for unordered sets has to be implemented by you. You canot use the in-built collections/libraries provided by Python for this purpose

## SUBMISSION

You will submit ONE file called `assignment3.py` to Gradescope for this lab.

`assignment3.py` should contain your entire source code for this assignment.

Please provide meaningful comments and use proper coding style and indentation. There is no need to upload additional files. Feel free to create additional private/public methods, but you can’t change/add data members.

Your program will be automatically graded. For each of the aforementioned tests you either pass the test case (full points) or not (zero points).

**Remember, we can test with any .txt file in the Dataset.**

## Point Distribution

The sections below show the distribution of points for the assignment:

|**Hash Table Methods**| **60 points total**|
| ---| --- |
|`make_table`| |
|`make_hash`| |
|`insert`| |
|`lookup`| |

<br>

|**Spell Checker**| **40 points total**|
| ---| --- |



Students caught cheating or plagiarizing will receive no credit. Additional actions, including a failing grade in the class or referring the case for disciplinary action, may also be taken.

Late submissions will receive a ZERO.

**NOTE: Gradescope allows me to compare all submissions with each other and see how similar they are. If I find submissions which are too similar to each others, all the similar looking assignments will receive a ZERO. Disciplinary action might be taken depending upon the severity of the issue.**

***

## **Your Gradescope submissions will not show how many points you have until after the due date has passed. It is on you to follow the requirements for each section, and to come up with your own thorough test cases that make sure that each part is complete and correct. You are allowed _unlimited_ resubmissions until the due date.**