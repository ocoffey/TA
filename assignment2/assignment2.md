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

You will design and implement a class for a customized Circular Doubly-Linked List named CDLL which contains at least the following public methods: `insert`, `print_current`, `go_next`, `go_prev`, `go_first`, `go_last`, `skip` (refer to the comments below for more details). Each node in the list stores two strings, corresponding to the time and text of a Tweet. Your classes must be implemented in the `assignment2.py` file.

```python
class CDLLNode:
    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
    self.time: str = time
    self.tweet: str = tweet
    self.next_node: CDLLNode = next_node
    self.prev_node: CDLLNode = prev_node
```

```python
class CDLL:
 	def __init__(self):
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numberofnodes: int = 0
	...
    # makes an insertion based on 'current'
    def insert(self,time: str, tweet: str):
    
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

## Using your class in a Tweet Reader application

You will develop a program that will open and read the contents of an input test file. The file name will be provided **as a command line argument**. This means that your code will need a `main()` function. <br>Each test file is a text file containing tweets of a news agency. For example, `bbchealth.txt` is related to BBC health news. Each line contains tweets following the format: `tweet id|date` and `time|tweet`. You can assume the separator between fields on each line is always `'|'`.

Here is an example tweet from the dataset:

```
515169518445146112|Thu Sep 25 16:02:39 +0000 2014|American #Ebola patient Dr. Rick Sacra has been released from the hospital
```

From this, the `time` will only be this section: `16:02:39` (It's in military time)<br>
Additionally, the `tweet` would only be this section: `American #Ebola patient Dr. Rick Sacra has been released from the hospital`

All test files were downloaded from the [Health News in Twitter Data Set](https://archive.ics.uci.edu/ml/machine-learning-databases/00438/, "Data Set") (we encourage you to use the dataset for personal testing).

While reading the contents of the input file line-by-line, your program will be inserting each tweet into a circular doubly linked list. After reading all tweets, your program will print to the `stdout` the oldest tweet and then enter a loop waiting for user commands. The user can interact with your program using one of the following commands:

* `n`: prints the next tweet (chronologically) to the stdout
* `p`: prints the previous tweet (chronologically) to the stdout
* `f`: prints the first tweet (oldest) to the stdout
* `l`: prints the last tweet (most recent) to the stdout
* `num`: prints the number of tweets stored in the list
* `<number>`: skips tweets circularly and prints the current to the stdout
* `s <word>`: searches for the next occurrence of the substring word in the following tweets (search is case insensitive and performs a circular traversal in the list)
* `q`: quits the program

## Point Distribution

The sections below show the distribution of points for the assignment:

|**Linked List Methods** |**30 Points Total**|
|      ---      |       ---         |
|insert()       |     10 points     |
|go_next()      |     3 points      |
|go_prev()      |     3 points      |
|go_first()     |     3 points      |
|go_last()      |     3 points      |
|skip()         |     5 points      |
|print_current()|     3 points      |

<br>

|**Tweet Reader Input Functionality**                       |**50 Points Total**|
|      ---                                                  |       ---         |
|`n`    (go to the next tweet)                              |     4 points      |
|`p`    (go to the previous tweet)                          |     4 points      |
|`f`    (go to the first tweet)                             |     4 points      |
|`l`    (go to the last tweet)                              |     4 points      |
|`num`  (prints the number of tweets in the list)           |     8 points      |
|`<number>` (go to the tweet `<number>` tweets away)        |     10 points     |
|`s <word>` (search for a word from the tweets in your list)|     14 points     |
|`q` (quit the program)                                     |     2 points      |

<br>

|**Additional Tests**                                       |**20 Points Total**|
|      ---                                                  |       ---         |
|Test for all the tweets being read into your linked list   |     6 points      |
|Test for your tweets being in chronological order          |     7 points      |
|Test for two random tweets to be where they should be      |     7 points      |

## SUBMISSION

You will submit ONE file called `assignment2.py` to Gradescope for this lab.

`assignment2.py` should contain your entire source code for this assignment.

Please provide meaningful comments and use proper coding style and indentation. There is no need to upload additional files. Feel free to create additional private/public methods, but you can’t change/add data members.

Your program will be automatically graded. For each of the questions you either pass the test cases (full points) or not (zero points).

Students caught cheating or plagiarizing will receive no credit. Additional actions, including a failing grade in the class or referring the case for disciplinary action, may also be taken.

Late submissions will receive a ZERO.

## **Your Gradescope submissions will not show how many points you have until after the due date has passed. It is on you to follow the requirements for each section, and to come up with your own thorough test cases that make sure that each part is complete and correct. You are allowed unlimited resubmissions until the due date.**

**NOTE: Gradescope allows me to compare all submissions with each other and see how similar they are. If I find submissions which are too similar to each others, all the similar looking assignments will receive a ZERO. Disciplinary action might be taken depending upon the severity of the issue.**
