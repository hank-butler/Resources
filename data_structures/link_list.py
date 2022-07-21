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
import datetime
print('='*40)
print(f' This is the current working directory: {os.getcwd()}')
print('='*40)

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

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_next = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node




# Testing
print(f'Testing at {datetime.datetime.now()}')
print('='*40)
print('Instantiating linkedlist...')
print('='*40)
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

'''
===================================
        Doubly Linked List
===================================
Doubly Linked Lists Introduction
Like a singly linked list, a doubly linked list is comprised of a series of nodes.
Each node contains data and two links (or pointers) to the next and previous nodes in the list.
The head node is the node at the beginning of the list, and the tail node is
the node at the end of the list.
The head node’s previous pointer is set to null and the tail node’s next pointer is set to null.

Think of your daily commute on the subway as a real-world example of a doubly linked list.
Your home is the head of the list, your place of work is the tail, and every stop in
between is another node in the list.
In the morning when you take the subway to get to work, you are traversing the list
from the head to the tail, using the stop’s next pointer.
While this can also be done using a singly linked list, a doubly linked list
will also allow you to traverse back through the list easily, using the stop’s previous pointer.
You will take the exact same route to get home, just in reverse.

Common operations on a doubly linked list may include:

>adding nodes to both ends of the list
>removing nodes from both ends of the list
>finding, and removing, a node from anywhere in the list
>traversing (or traveling through) the list

===============================
Removing from the Head and Tail
===============================
Due to the extra pointer and tail property, removing the head from a doubly linked list is
slightly more complicated than removing the head from a singly linked list.
However, the previous pointer and tail property make it much simpler to
remove the tail of the list, as we don’t have to traverse the entire list to be able to do it.

=================
Removing the Head
=================
Removing the head involves updating the pointer at the beginning of the list.
We will set the previous pointer of the new head (the element directly after the current head)
 to null, and update the head property of the list.
 If the head was also the tail, the tail removal process will occur as well.

=================
Removing the Tail
=================
Similarly, removing the tail involves updating the pointer at the end of the list.
We will set the next pointer of the new tail (the element directly before the tail)
 to null, and update the tail property of the list.
 If the tail was also the head, the head removal process will occur as well.

====================================
Removing from the Middle of the List
====================================
It is also possible to remove a node from the middle of the list.
Since that node is neither the head nor the tail of the list,
there are two pointers that must be updated:

We must set the removed node’s preceding node’s next pointer to its following node
We must set the removed node’s following node’s previous pointer to its preceding node
There is no need to change the pointers of the removed node,
as updating the pointers of its neighboring nodes will remove it from the list.
If no nodes in the list are pointing to it, the node is orphaned.

'''
