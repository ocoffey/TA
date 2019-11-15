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

Note that the books are different than the ones from the labs. You can find the dictionary needed for your work [here](link).

## Spell Check

Once you have downloaded the books and the dictionary, read all of the words in the **dictionary** provided into a hash-table as an unordered set.

Basically an unordered set is an associative container that contains a set of unique objects of type Key. Search, insertion, and removal can then be done on average in constant-time complexity. Internally, the elements of an unordered set are are not sorted in any particular order, but organized into buckets (hence hash-table). Which bucket an element is placed into depends entirely on the hash of its value. This allows fast access to individual elements, since once a hash is computed, it refers to the exact bucket the element is placed into.

Once you have loaded the dictionary, open each book, and output words that have spelling errors.

#### Note: 

* No starter code will be given for this assignment. It is entirely up to you to implement the program from scratch.
* The hash table for unordered sets has to be implemented by you. You canot use the in-built collections/libraries provided by Python for this purpose

## SUBMISSION

You will submit ONE file called `assignment3.py` to Gradescope for this lab.

`assignment3.py` should contain your entire source code for this assignment.

Please provide meaningful comments and use proper coding style and indentation. There is no need to upload additional files. Feel free to create additional private/public methods, but you can’t change/add data members.

Your program will be automatically graded. For each of the aforementioned tests you either pass the test case (full points) or not (zero points).

**Remember, we can test with any .txt file in the Dataset.**

Students caught cheating or plagiarizing will receive no credit. Additional actions, including a failing grade in the class or referring the case for disciplinary action, may also be taken.

Late submissions will receive a ZERO.

**NOTE: Gradescope allows me to compare all submissions with each other and see how similar they are. If I find submissions which are too similar to each others, all the similar looking assignments will receive a ZERO. Disciplinary action might be taken depending upon the severity of the issue.**

***

## **Your Gradescope submissions will not show how many points you have until after the due date has passed. It is on you to follow the requirements for each section, and to come up with your own thorough test cases that make sure that each part is complete and correct. You are allowed _unlimited_ resubmissions until the due date.**