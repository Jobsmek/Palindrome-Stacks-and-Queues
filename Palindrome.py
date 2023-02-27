from Stack import Stack
from Queue import Queue


def stackToReverseString(MyStack):
   #find length of string and add it to the stack to reverse it
   #This needs to use a stack

   
   # toString
   string = ""
   while MyStack.peek() != None:
      i = MyStack.pop()
      string+=i

   return string
   # Return a string

def reverseStringAndRemoveNonAlpha(stringToReverse):
   string = ""
   for character in stringToReverse:
      if character.isalpha():
         string+=character
   return string
   # Remove stuff like ! space ., using a stack
   # Remove Non Alpha
      

   
   # while stringToReverse.peek() != None:
   #    character = stringToReverse.pop()
   #    if (character >= 'A' and character <= 'Z') or (character >= 'a' and character <= 'z'):
   #       strippedStack.push(character)
   
   # Reverse the stack
   # reversedStack = Stack()
   # reversedStack = stackToReverseString(strippedStack)
   print(stringToReverse)
   return stringToReverse
   # Return a string

def isPalindrome(string):
   #
   #This needs to use a stack and queue
   skip



# Stack operations
num_stack = Stack()
num_stack.push("Stressed was i ! 123 ere I saw desserts")
#num_stack.push("stand")
#num_stack.push("hello")

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()
mystring = stackToReverseString(num_stack)

# Output stack
# print('Stack after reverse:', end=' ')
# node = num_stack.list.head
# while node != None:
#    print(node.data, end=' ')
#    node = node.next
# print()

reverseStringAndRemoveNonAlpha(mystring)

# Output stack
# print('Stack after reverse:', end=' ')
# node = num_stack.list.head
# while node != None:
#    print(node.data, end=' ')
#    node = node.next
# print()

# string=""
# node = num_stack.list.head
# while node != None:
#    string+=node.data
#    node = node.next
# print(string)



"""
# Pop 11
popped_item = num_stack.pop()
print('Popped:', popped_item)

# Output final stack
print('Stack after pop:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print('\n')



# Queue operations
num_queue = Queue()
num_queue.enqueue(17)
num_queue.enqueue(24)
num_queue.enqueue(18)

# Output queue
print('Queue after enqueue:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

# Dequeue 17
dequeued_item = num_queue.dequeue()
print('Dequeued:', dequeued_item)

# Output final queue
print('Queue after dequeue:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()
"""
