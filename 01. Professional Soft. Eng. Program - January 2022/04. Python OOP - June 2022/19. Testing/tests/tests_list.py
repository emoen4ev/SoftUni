"""
3.	List

You are provided with a class IntegerList.
It should only store integers.
The initial integers should be set by the constructor.
They are stored as a list.
IntegerList has a functionality to add, remove_index, get, insert, get the biggest number,
and get the index of an element. Your task is to test the class.

Note: You are not allowed to change the structure of the provided code

Constraints
•	add operation, should add an element and returns the list.
    - If the element is not an integer, a ValueError is thrown
•	remove_index operation removes the element on that index and returns it.
    - If the index is out of range, an IndexError is thrown
•	__init__ should only take integers, and store them
•	get should return the specific element
    - If the index is out of range, an IndexError is thrown
•	insert
    - If the index is out of range, IndexError is thrown
    - If the element is not an integer, ValueError is thrown
•	get_biggest
•	get_index

Hint
Do not forget to test the constructor
"""