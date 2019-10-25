# Lab 7: HeapSort

Today you will be playing with HeapSort, a sorting algorithm that guarantees $O(n \log n)$ run-time.

You will be submitting your code on Gradescope as usual. 
The lab should be done **individually**.

## 1. Child and Parent Functions

Your goal is to implement HeapSort, such that you can sort a list `A` of integers. 
Remember when dealing with heaps, even though we are manipulating an implicit binary tree structure, we do not actually create a tree data structure. 
In HeapSort, we manipulate a list of numbers based on a *mental-model* of a binary tree. 
Thus, our first step is to picture the list as binary tree.

Please take a piece of paper and draw a binary tree representing the list `A = [4, 1, 19, 18, 10, 3, 7, 9, 1, 0, 2].`

**Question:** Does this tree follow the *Heap* property?

**Question:** For a given node in the list at index `i`, let `left(i)` be the index of the left-child of node `i`. What is the index of `left(i)`?

**Question:** For a given node in the list at index `i`, let `right(i)` be the index of the right-child of node `i`. What is the index of `right(i)`?

**Question:** For a given node in the list at index `i`, let `parent(i)` be the index of the parent of node `i`. What is the index of `parent(i)`?

The next step is to implement `left(i)`, `right(i)`, and `parent(i)` in your `lab.py` file. 

The header for the three functions for you to write are as follows:

```python
def left(i: int) -> int:
def right(i: int) -> int:
def parent(i: int) -> int:
```

**Question:** What will be the left-child and right-child of leaf nodes?

**Question:** What will be the parent of the root node?

Once you are satisfied that your functions produce the correct index of the left-child, right-child and parent of an element in the list, you can move on to the next step.

## 2. Heapify

The next steps is to write the function called `heapify`.
This function should take a random list, and return a new list that adheres to the properties of being a heap.
To implement this function, think recursively about the problem and consider your starting point very carefully.

```python
def heapify(A: list, i: int) -> list
```

Where:

* `A` is a list;
* `i` is the index of an element within `A`

> When we call `heapify(A, i)` we assume, in our implementation, that the trees starting at `left(i)` and `right(i)` are valid heaps themselves. 

**Question:** What is the heap property? How do you know if a list is following the heap property?

## 3. Build a Max-Heap

Now that you have a function which can transform a list into a heap, the next step for you is to build a MAX-Heap out of the input list you have been given. 

> The amount of work you have to do here is dependant on your implementation of heapify.

**Question:**  What is the difference between a heap and a max heap? How can we tell if a heap is a min or a max heap?

Now write a function to Build Max-Heap, called `build_max_heap` which converts an input list into a max heap. 
The header for the function is as follows:

```python
def build_max_heap(A: list) -> list
```

## 4. HeapSort

The next step is to actually perform the HeapSort itself. 
Given an unsorted list `A`, write a function that does the following:

1. Builds a heap from the list.
2. Extracts elements from the heap into a new list, such that the new list is sorted.
3. Returns the new list.

The header for the heapify function for you to write is as follows:

```python
def heapsort(A: list) -> list
```

Once you feel that you're ready, test your `heapsort` function.

If your functions work correctly, the program will print out a success message for each of the test trials, along with an overall success message. 
Otherwise, it will print at least one trial failure message, along with an overall failure message.

## 5. What to Submit

You will submit one text files named `lab.py` Gradescope; `lab.py` should contain your entire source code including all the functions you have written.
