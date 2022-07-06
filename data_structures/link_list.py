'''
===========
LINKED LIST
===========

Linking together nodes using next_node property craetes a singly
linked link.
Extremely versatile and useful.
Used as foundations for future data structures.

'''

'''
===================
Doubly Linked Lists
===================


Single linked list consists of nodes with links from one node to the next.
A doubly linked list has a link to the node before it.
prev_node links, along with the added tail_nail property, allow you to iterate
backward through the list as easily as you could iterate forward singly linked list.

'''


'''
======
Queues
======
A linear collection of nodes that exclusively asdds nodes to the tail
and removes nodes from the head of the queue.

Implemented using different underlying data structures, but more common method
is a singly linked list.

Think of like a line in a grocery store.
'''

'''
======
Stacks
======

Like a queue, a stack is a linear collection of nodes that adds (pushes) data to the head
of the stack. However, a stack removes data from the head of the stack. Think of like a stack of books.

'''

import os
print(f' This is the current working directory: {os.getcwd()}')

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value = None):
    self.head_node = Node(value)
  def get_head_node(self):
    return self.head_node
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
