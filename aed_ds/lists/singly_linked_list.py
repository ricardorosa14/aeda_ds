<<<<<<< HEAD
from .tad_list import List 
from .nodes import SingleListNode
from ..exceptions import EmptyListException, InvalidPositionException, NoSuchElementException 

class SinglyLinkedList(List):
=======
from .tad_list import List
from .nodes import SingleListNode
from .singly_linked_list_iterator import SinglyLinkedListIterator
from ..exceptions import EmptyListException, InvalidPositionException
from .singly_linked_list_iterator import SinglyLinkedListIterator

class SinglyLinkedList(List):

>>>>>>> upstream/develop
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

<<<<<<< HEAD
    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.num_elements == 0

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.head == None:
            raise EmptyListException()
        else:
            return self.head.get_element()
            
            
    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self): 
        if self.head == None:
            raise EmptyListException()
        else:
            return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): 
        if self.is_empty():
            raise EmptyListException()
        elif position < 0 or position > (self.size() - 1):
            raise InvalidPositionException()
        current_positon = 0
        node = self.head
        while current_positon < position:
            node = node.get_next()
            current_positon += 1
        return node.get_element()


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): 
        if self.is_empty():
            raise EmptyListException()
        current_position = 0
        node = self.head
        while node is not None:
            if node.get_element() == element:
                return current_position
            node = node.get_next()
            current_position += 1
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        f_node = SingleListNode(element, self.head)
        self.head = f_node
        if self.num_elements == 0:
            self.tail = f_node
        self.num_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        l_node = SingleListNode(element, None)
        if not self.head:
            self.head = l_node
        self.tail.next_node = l_node
        self.tail = l_node
        self.num_elements += 1
    
    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            self.insert_first(element)
        elif position == self.size():
            self.insert_last(element)
        else:
            current_positon = 0
            node = self.head
            while current_positon < self.size():
                if current_positon == position - 1:
                    node.next_node = SingleListNode(element, node.next_node)
                    break
                node = node.get_next()
                current_positon += 1
            self.num_elements += 1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        self.head = self.head.next_node
        self.num_elements -= 1


    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        current_position = 0
        node = self.head
        while current_position < self.size() :
            if node.next_node == self.tail:
                node.next_node = None
                self.tail = node
                break
            node = node.get_next()
            current_position += 1
        self.num_elements -= 1
        
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): 
        if position < 0 or position > (self.size() - 1):
            raise InvalidPositionException
        current_position = 0
        node = self.head
        while (current_position < postion -1):
            node = node.get_next()
            current_position += 1


            if current_position == position - 1:
                node = node.next_node.next_node
                break

        self.num_elements -= 1
    
    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass
=======
    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def get_first(self): 
        if not self.head:
            raise EmptyListException
        return self.head.get_element()

    def get_last(self): 
        if not self.head:
            raise EmptyListException
        return self.tail.get_element()

    def get(self, position): 
        if not self.head:
            raise EmptyListException()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                return cur_node.get_element()
            cur_node = cur_node.get_next()
            idx += 1

    def find(self, element): 
        cur_node = self.head
        idx = 0
        while cur_node:
            if element == cur_node.get_element():
                return idx
            cur_node = cur_node.get_next()
            idx += 1
        return -1            

    def insert_first(self, element):
        new_node = SingleListNode(element, self.head)
        if not self.head:
            self.tail = new_node
        self.head = new_node
        self.num_elements += 1
    
    def insert_last(self, element):
        new_node = SingleListNode(element, None)
        if not self.head: 
            self.head = new_node
        else:    
            self.tail.set_next(new_node)
        self.tail = new_node
        self.num_elements += 1

    def insert(self, element, position): 
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        prev_node = self.head
        cur_node = self.head
        idx = 0
        while prev_node:
            if position == idx: 
                new_node = SingleListNode(element, cur_node)
                prev_node.set_next(new_node)
                self.num_elements += 1
                break
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1 

    def remove_first(self):
        if not self.head:
            raise EmptyListException()
        elif self.head == self.tail:
            self.make_empty()
        else:
            old_head = self.head
            self.head = self.head.get_next()
            self.num_elements -= 1
            return old_head.get_element()

    def remove_last(self): 
        if not self.head:
            raise EmptyListException()
        elif self.size() == 1:
            return self.remove_first()
        elif self.size() == 2:
            self.head.set_next(None)
            old_node = self.head
            self.tail = self.head
            self.num_elements -= 1
            return old_node.get_element() 
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        old_node = self.tail
        self.tail = cur_node
        cur_node.set_next(None)
        self.num_elements -= 1
        return old_node.get_element()

    def remove(self, position): 
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                prev_node.set_next(cur_node.get_next())
                old_node = cur_node
                cur_node.set_next(None)
                self.num_elements -= 1
                return old_node.get_element()
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0    

    def iterator(self):
        return SinglyLinkedListIterator(self)
>>>>>>> upstream/develop
