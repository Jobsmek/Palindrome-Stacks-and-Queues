import sys
from Node import Node
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
       
        try:
            popped_item = self.list.head.data
            # Remove list head
            self.list.remove_after(None)
            return popped_item
        except AttributeError:
            print("There is no such attribute")

    def peek(self):
        # Check to see if list is empty, if empty: exit
        if self.list.head.data == None:
            sys.exit("Stack empty")
            
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Return the peeked item
        return popped_item
