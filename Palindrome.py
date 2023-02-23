from Stack import Stack
from Queue import Queue


def stackToReverseString(MyStack):
   #find length of string and add it to the stack to reverse it
   #This needs to use a stack

   #  abcd
   #  
   newStack = Stack()
   

  
   while MyStack.list.head.data != None:
      i = MyStack.pop()
      newStack.push(i)

def reverseStringAndRemoveNonAlpha(string):
   # Remove stuff like ! space ., using a stack
   strippedString = ""
   for i in string:  
      # Store only valid characters
      if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
         strippedString += i
   
   # Push the stripped string into a stack
   newStack = Stack()
   for character in string: 
      newStack.push(character)
      
   # Reverse the stack
   reversedStack = stackToReverseString(newStack)
   return reversedStack

def isPalindrome(string):
   #
   #This needs to use a stack and queue
   skip



# Stack operations
num_stack = Stack()
num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()



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
