from queue import Queue
from stack import Stack
from Palindrome import stackToReverseString, reverseStringAndRemoveNonAlpha, isPalindrome, toString

def test_stackToReverse1():
    calcStack = Stack()
    testList= ["A","R","B","A","D","A","C","A","B","B","A"]
    testResult = stackToReverseString(testList)
    assert testResult == "ABBACADABRA"