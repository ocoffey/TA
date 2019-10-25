# Assignment 2

### (Due: Nov 14, 2019) 11:59PM

### Total points: 100

## Introduction

The goal of this assignment is to understand and implement a circular doubly linked list. Be sure to carefully read each of the problems, as every detail will play a role in the solution. The assignment is worth a total of 100 points.

This assignment is to be completed individually. You are NOT allowed to share nor acquire source code from other students in the class, current or previous. You must start the assignment early in order to get proper help from the TAs and the instructor. You can also post general questions or ask for clarifications on Piazza, however, **do not post your own source code.**

**_Please read the entire assignment carefully, before starting_**

## Methodology

I expect you to create a source file `assignment2.py` that will contain the solutions to the question below. For each question you will create a method using the provided defintions. You may add any number of helper methods.

**PLEASE USE the method definitions exactly as given for each question.** If you do not, then the autograder on Gradescope will not be able to recognize your answer and will give you a zero.

## Implementing a Circular Doubly Linked List

You will design and implement a class for a customized Circular Doubly-Linked List named CDLL which contains at least the following public methods: `prepend`, `append`, `print_current`, `go_next`, `go_prev`, `go_first`, `go_last`, `skip` (refer to the comments below for more details). Each node in the list stores two strings, corresponding to the time and text of a Tweet. Your classes must be implemented in the `assignment2.py` file.

```python
class CDLLNode:
    def __init__(self,time="",tweet="",next_node=None,prev_node=None):
    self.time = time
    self.tweet = tweet
    self.next_node = next_node
    self.prev_node = prev_node
```

```python
class CDLL:
 	def __init__(self):
        self.head = None
        self.current = None
        self.numberofnodes = 0
	...
    # makes an insertion at the front of the list
    def prepend(self,time:str, tweet:str):
    
    # makes an insertion at the end of the list
    def append(self,time:str, tweet:str):
    
    # moves 'current' pointer to the next node (circularly)
    def go_next(self):
    
    # moves 'current' pointer to the previous node (circularly)
    def go_prev(self):
    
    # moves 'current' pointer to the head/first node
    def go_first(self):
    
    # moves 'current' pointer to the last node
    def go_last(self):
    
    # moves 'current' pointer n elements ahead (circularly)
    def skip(self,n:int):
    
    # prints the contents of the 'current' node
    # prints the time, then the tweet (each with a newline following)
    def print_current(self):
```

### Circular Doubly Linked List Grading

Your linked list will be tested to ensure that each of its methods work correctly. In addition to checking for correct solutions, the autograder will check for these additional "good practices":

* For `skip()`, your implementation cannot take more time to execute as the size of `n` increases
* For `go_last()`, your method must occur in _O_(1) (constant time), and not _O_(n) (n time)
* Your `append()` method must occur as _O_(1) time, and not _O_(n) time

## Using your class in a Tweet Reader application

You will develop a program that will open and read the contents of an input test file. The file name will be provided **as a command line argument**. Each test file is a text file containing tweets of a news agency. For example, `bbchealth.txt` is related to BBC health news. Each line contains tweets following the format: `tweet id|date` and `time|tweet`. You can assume the separator between fields on each line is always `'|'`. All test files were downloaded from the Health News in Twitter Data Set.

While reading the contents of the input file line-by-line, your program will be inserting each tweet into a circular doubly linked list. After reading all tweets, your program will print to the `stdout` the oldest tweet and then enter a loop waiting for user commands. The user can interact with your program using one of the following commands:

* `n`: prints the next tweet (chronologically) to the stdout
* `p`: prints the previous tweet (chronologically) to the stdout
* `f`: prints the first tweet (oldest) to the stdout
* `l`: prints the last tweet (most recent) to the stdout
* `<number>`: skips tweets circularly and prints the current to the stdout
* `s <word>`: searches for the next occurrence of the substring word in the following tweets (search is case insensitive and performs a circular traversal in the list)
* `q`: quits the program

### Tweet Reader Grading

In addition to having working methods, your tweet reader will also be graded on the following "good practices":

* Error handling for not being passed a filename in the command line
* Error handling for not being able to open the file
* Accounting for an input of `s` without being followed by a word to search for
* `s` accounting for the searched word not being found in the tweets
* Skipping based on the `<number>` input in a way that doesn't take more time as your `number` increases over `n` (size of linked list) times

## SUBMISSION

You will submit ONE file called `assignment2.py` to Gradescope for this lab.

`assignment2.py` should contain your entire source code for this assignment.

Please provide meaningful comments and use proper coding style and indentation. There is no need to upload additional files. Feel free to create additional private/public methods, but you can’t change/add data members.

Your program will be automatically graded. For each of the questions you either pass the test cases (full points) or not (zero points).

The table below shoes the distribution of points:

* **Linked List Methods:** 30 points
* **Linked List Good Practices:** 20 points
* **Tweet Reader Methods:** 30 points
* **Tweet Reader Good Practices:** 20 points

Students caught cheating or plagiarizing will receive no credit. Additional actions, including a failing grade in the class or referring the case for disciplinary action, may also be taken.

Late submissions will receive a ZERO.

## **Your Gradescope submissions will not show how many points you have until after the due date has passed. It is on you to follow the requirements for each section, and to come up with your own thorough test cases that make sure that each part is complete and correct.**

**NOTE: Gradescope allows me to compare all submissions with each other and see how similar they are. If I find submissions which are too similar to each others, all the similar looking assignments will receive a ZERO. Disciplinary action might be taken depending upon the severity of the issue.**
