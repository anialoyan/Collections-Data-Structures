from abc import ABC, abstractmethod


class Collection(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def print(self):
        pass


class List(Collection):
    @abstractmethod
    def addFirst(e):
        pass

    @abstractmethod
    def removeFirst(self):
        pass  # boolean

    @abstractmethod
    def addLast(self, e):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    # boolean

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

    @abstractmethod
    def replace(self, e, r):
        pass

    # boolean // replaces the first occurrence of e in List with r and returns true
    # if done. If e is not found in the list then false is returned.


class Stack(Collection):
    @abstractmethod
    def push(self, Te):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass


class Linked_List(List):
    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None

    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def first(self):
        return self._first._data

    def last(self):
        return self._last._data

    def replace(self, e, r):
        node = self._first
        while node:
            if node._data == e:
                node._data = r
                return True
            node = node._next
        return False

    def is_empty(self):
        """checks if the list is empty"""
        return self._size == 0

    def empty(self):
        """empties the linkedlist"""
        self._first = None
        
        
    def size(self):
        return self._size


    def print(self):
        """prints the elements of the linkedlist"""
        node = self._first
        while node:
            print(node._data)
            node = node._next

    def addFirst(self, e):
        """adds an element to the beginning of the linkedlist"""
        node = self.Node(e)
        if self.is_empty():
            self._last = node
        node._next = self._first
        self._first = node
        self._size += 1

    def removeFirst(self):
        """removes the first element and returns true after successfully removing it"""
        if self.is_empty():
            return True
        temp = self._first
        self._first = self._first._next
        temp._next = None
        self._size -= 1
        return True

    def addLast(self, e):
        """adds an element to the end ofthe linkedlist"""
        node = self.Node(e)

        if self.is_empty():
            self._first = node
            self._last = node
        else:
            self._last._next = node

        self._size += 1
        self._last = node

    def removeLast(self):
        """removes the last element and returns True after successfully removing it """
        if self.is_empty():
            return True
        elif self._size == 1:
            self._first = None
            self._size = 0
            return True
        node = self._first
        while node._next:
            node = node._next
        self._size -= 1
        self._last = node
        return True
    
    def _reverse_helper(self, node):
        if node == None:
            return node
        if node._next == None:
            self._first = node
            return node
        temp = self._reverse_helper(node._next)
        node._next._next = node
        node._next = None
        return temp

    def reverse(self):
        self._last = self._first
        self._first = self._reverse_helper(self._first)

    def __iter__(self):
        self.current = self._first
        return self

    def __next__(self):

        if self.current != None:

            node = self.current
            self.current = node._next
            return node
        else:
            raise StopIteration

    def odditer(self):
        return self.Odd_Iter(self)

    class Odd_Iter:
        def __init__(self, linked_list):
            self._first = linked_list._first
            self._last = linked_list._last

        def __iter__(self):
            self.current = self._first
            return self

        def __next__(self):
            if self.current != None and self.current != self._last:
                node = self.current._next
                self.current = node._next
                return node
            else:
                raise StopIteration
                
         
    def add_at(self, index, t):
        if self._size == 0 or index >= self._size or index < 0:
            return False
        
        node = self._first
        prev = None
        i = 0
        while i != index:
            prev = node
            node = node._next
            i += 1
            
        if prev == None:
            temp = self.Node(t)
            temp._next = self._first
            self._first = temp
            self._size += 1
            return True 
        
        #if you allow adding at the size 
        # if node == None:
        #     temp = self.Node(t)
        #     self._last._next = temp
        #     self._last = temp
        #     self._size += 1
        #     return True 
        
        temp = self.Node(t)
        prev._next = temp
        temp._next = node
        self._size += 1
        return True
    
    
    def remove_at(self, index):
        if self._size == 0 or index >= self._size or index < 0:
            return False
        
        node = self._first
        prev = None
        i = 0
        while i != index:
            prev = node
            node = node._next
            i += 1
            
        if prev == None:
            temp = self._first 
            self._first = self._first._next
            temp._next = None
            self._size -= 1
            if self._size == 0:
                self._last = None
            return True 
        
        if node == self._last:
            prev._next = None
            self._last = prev
            self._size -= 1
            return True 
        
        prev._next = node._next
        node._next = None
        self._size -= 1
        return True
            
        
        

        
    def remove_after(self, n):
        if self._size == 0:
            return False
        
        node = self._first
        while node._next:
            if node._data == n:
                node._next = node._next._next
                self._size -= 1
                if self._size == 1:
                    self._last = self._first
                elif node == self._last:
                    self._last = node
 
                return True
            node = node._next
        return False

    def remove_after(self, a):
        if self._size == 0:
            return False 
        if self._size == 1:
            return False 
        
        prev = self._first 
        node = self._first 
        while node and prev._data != a:
            prev = node
            node = node._next
        
        if node == None:
            return False
        
        prev._next = node._next 
        node._next = None
        if node == self._last:
            self._last = prev 
        self._size -= 1
        return True
        
            
            
        

    def remove_before(self, a):
        if self._size == 0:
            return False
        
        if self._first._data == a:
            return False
        
        node = self._first
        if node._next and node._next._data == a:
            temp = self._first 
            self._first = self._first._next
            temp._next = None
            self._size -= 1
            return True
            
        while node._next:
            prev = node 
            node = node._next
            if node._next._data == a:
                prev._next = node._next
                self._size -= 1
                return True
        
        return False
    

    
    
    def add_before(self, ourData, newData):
        new_node = self.Node(newData)
        if self._size == 0:
            return False
        if self._size == 1 and self._first._data != ourData:
            return False
        if self._first._data ==ourData:
            
            new_node._next = self._first
            self._first._prev = new_node
            self._first = new_node
            self._size += 1
            return True
        curr = self._first
        while curr._next and curr._next._data != ourData:
            curr = curr._next
        if curr == self._last and self._last._data != ourData:
            return False
        new_node._next = curr._next
        curr._next._prev = new_node
        curr._next = new_node 
        new_node._prev = curr
        
        self._size += 1
        return True
        
        
    

    def add_after(self, ourData, newData):
        new_node = self.Node(newData)
        if self._size == 0:
            return False
        if self._size == 1 and self._first._data != ourData:
            return False
         
        curr = self._first
        while curr and curr._data != ourData: 
            curr = curr._next 
            
        if curr == None:
            return False
        new_node._next = curr._next
        curr._next = new_node
        self._size += 1

        if curr == self._last:
            self._last = new_node
            

        return True
        
    


class DoubleLinkedList(List):
    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None
            self._prev = None

    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def first(self):
        return self._first._data

    def last(self):
        return self._last._data

    def replace(self, e, r):
        node = self._first
        while node:
            if node._data == e:
                node._data = r
                return True
            node = node._next
        return False

    def is_empty(self):
        """checks if the list is empty"""
        return self._size == 0

    def empty(self):
        """empties the linkedlist"""
        self._first = None

    def print(self):
        """prints the elements of the linkedlist"""
        node = self._first
        while node:
            print(node._data)
            node = node._next

    def addFirst(self, e):
        """adds an element to the beginning of the linkedlist"""
        node = self.Node(e)
        if self.is_empty():
            self._first = node
            self._first._next = None
            self._last = node
        else:
            temp = self._first
            self._first._prev = node
            self._first = node
            self._first._next = temp
        self._size += 1


    def removeFirst(self):
        """removes the first element and returns true after successfully removing it"""
        if self.is_empty():
            return True
        temp = self._first
        self._first = self._first._next
        temp._next = None
        self._size -= 1
        return True


    def addLast(self, e):
        """adds an element to the end ofthe linkedlist"""
        node = self.Node(e)
        if self.is_empty():
            self._first = node
            self._last = node
        else:
            self._last._next = node
            temp = self._last
            self._last = node
            node._prev = temp
        self._size += 1

    def removeLast(self):
        """removes the last element and returns True after successfully removing it """
        if self.is_empty():
            return True
        elif self._size == 1:
            self._first = None
            self._last = None
            self._size = 0
            return True

        temp = self._last
        self._last = self._last._prev
        temp._prev = None
        self._last._next = None
        self._size -= 1

        return True
    
    
             
    def add_at(self, index, t):
        if self._size == 0 or index >= self._size or index < 0:
            return False
        
        node = self._first
        prev = None
        i = 0
        while i != index:
            prev = node
            node = node._next
            i += 1
            
        if prev == None:
            temp = self.Node(t)
            temp._next = self._first
            self._first = temp
            temp._next._prev = temp
            self._size += 1
            return True 

        temp = self.Node(t)
        prev._next = temp
        temp._prev = prev
        temp._next = node
        node._prev = temp
        self._size += 1
        return True
    
    
    def remove_at(self, index):
        if self._size == 0 or index >= self._size or index < 0:
            return False
        
        node = self._first
        prev = None
        i = 0
        while i != index:
            prev = node
            node = node._next
            i += 1
            
        if prev == None:
            temp = self._first 
            self._first = self._first._next
            temp._next._prev = None
            temp._next = None
            self._size -= 1
            if self._size == 0:
                self._last = None
            return True 
        
        if node == self._last:
            prev._next._prev = None
            prev._next = None
            self._last = prev
            self._size -= 1
            return True 
        
        prev._next = node._next
        prev._next._prev = prev
        node._next = None 
        node._prev = None
        self._size -= 1
        return True
            
        
        
    def remove_after(self, n):
        if self._size == 0:
            return False
        
        node = self._first
        while node._next:
            if node._data == n:
                temp = node._next
                node._next = node._next._next
                if node._next:
                    node._next._prev = node
                temp._prev = None
                self._size -= 1
                if self._size == 1:
                    self._last = self._first
                elif node == self._last:
                    self._last = node
                return True
            node = node._next
        return False


    def remove_before(self, a):
            if self._size == 0:
                return False
            if self._first._data == a:
                return False
            
            node = self._first
            if node._next._data == a:
                temp = self._first  
                self._first = self._first._next
                self._first._prev = None
                temp._next = None
                self._size -= 1
                return True
            
            while node._next:
                prev = node 
                node = node._next
                if node._next._data != a:
                    prev._next = node._next
                    node._prev = prev
                    self._size -= 1
                    return True
            
            return False

        
    def add_before(self, s, t):
        if self._size == 0:
            return False
        if self._first._data == s:
            temp = self._first
            self._first = self.Node(t)
            self._first._next = temp 
            temp._prev = self._first
            self._size += 1
            return True
        node = self._first 
        prev = None
        while node and node._data != s:
            prev = node
            node = node._next 
            
        if node:
           curr = self.Node(t)
           prev._next = curr
           curr._prev = prev
           curr._next = node
           node._prev = curr
           self._size += 1
           return True
        return False
           
    
    def add_after(self, s, t):
        if self._size == 0:
            return False
        if self._last._data == s:
            temp = self.Node(t)
            self._last._next = temp
            temp._prev = self._last
            self._last = temp
            self._size += 1
            return True
        
        node = self._first 
        while node and node._data != s:
            node = node._next 
            
        if node:
           temp = node._next
           curr = self.Node(t)
           node._next = curr
           curr._prev = node
           curr._next = temp
           temp._prev = curr
           self._size += 1
           return True
       
        return False


class Stack_Linked_List(Stack):
    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None

    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        """checks if the list is empty"""
        return self._size == 0

    def empty(self):
        """empties the linkedlist"""
        self._top = None

    def print(self):
        """prints the elements of the linkedlist"""
        node = self._top
        while node:
            print(node._data)
            node = node._next

    def push(self, top):
        """adds an element to the top of the linkedlist stack"""
        node = self.Node(top)
        node._next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """removes the top element of the linkedlist stack"""
        if self.is_empty():
            return
        temp = self._top
        self._top = self._top._next
        temp._next = None
        self._size -= 1
        return

    def top(self):
        return self._top._data

    def __iter__(self):
        self.current = self._top
        return self

    def __next__(self):

        if self.current is not None:

            node = self.current
            self.current = node._next
            return node
        else:
            raise StopIteration
            
class Queue(Collection):
    
    @abstractmethod 
    def enqueue(self, value):
        pass 
    
    
    @abstractmethod
    def dequeue(self):
        pass
    
    
    @abstractmethod 
    def front(self):
        pass
    
    
    @abstractmethod 
    def back(self):
        pass
    
    
    @abstractmethod
    def swap(self, v1, v2)-> bool:
        pass



class Deque(Queue):
    
    @abstractmethod 
    def left_enqueue(self, value):
        pass
    
    
    @abstractmethod
    def right_dequeue(self):
        pass

class DoubleLinkedListDeque(Deque):
    
    class Node:
        def __init__(self, data):
            self._data = data
            self._prev = None
            self._next = None
            
            
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    
    def empty(self):
        self._front = None
        self._back = None
        self._size = 0

    def print(self):
        pass
    
    
    def size(self):
        return self._size
    
    def enqueue(self, e):
        node = self.Node(e)
        if self.is_empty():
            self._front = node
            self._back = node
            self._size += 1
        else:
            self._back._next = node
            temp = self._back
            self._back = node
            node._prev = temp
            self._size += 1
            
        



    def dequeue(self):
        if self.is_empty():
            return True
        elif self._size == 1:
            self._front = self._back = None
            self._size = 0
            return True
        else:
            temp = self._front
            self._front = self._front._next
            temp._next = None
            self._front._prev  = None
            self._size -= 1        

            return True
        return False
    
    
    def left_enqueue(self, e):

            
        n = self.Node(e)
        if self.is_empty():
            self._front = self._back = n
            self._size += 1
        else:
            n._next = self._front
            self._front._prev = n
            self._front = n
            self._size += 1
            
        
        
        
    def right_dequeue(self):
        
        if self.is_empty():
            return True
        elif self._size == 1:
            self._front = self._back = None
            self._size = 0
            return True
        else:
            temp = self._back 
            self._back = self._back._prev
            temp._prev = None
            self._back._next = None
            self._size -= 1 
            return True
        
        return False



    def front(self):
        return self._front._data
    
    
    def back(self):
        return self._back._data

    def swap(self,v1, v2):
        node1 = node2 = self._front
        while node1:
            if node1._data == v1:
                 while node2:
                     if node2._data == v2:
                         temp = node1._data
                         node1._data = node2._data 
                         node2._data = temp
                         return True
                     node2 = node2._next
            node1 = node1._next
        return False
    
    class lliterator:
        def __init__(self, deque):
            self._current = deque._front
        
            
        def __next__(self):

                if self._current:
                    node = self._current
                    self._current = node._next
                    return node._data
                else:
                    raise StopIteration
                
    def __iter__(self):
        return self.lliterator(self)
    
    
        
class ArrayDeque(Deque):
    def __init__(self):
        self._arr = [None for i in range(20)]
        self._first = 0
        self._size = 0 
        
    def is_empty(self):
        return self._size == 0

    def empty(self):
        self._front = None
        self._back = None
        self._size = 0

    def print(self):
        pass
    
    def size(self):
        return self._size
    
    
    def front(self):
        if self.is_empty():
            return None
        return self._arr[self._first % len(self._arr)]
    
    def back(self):
        if self.is_empty():
            return None
        return self._arr[(self._first + self._size -1) % len(self._arr)]
    
    def dequeue(self):
        if self.is_empty():
            return True
        else:
            d = self._arr[self._first % len(self._arr)]
            self._arr[self._first % len(self._arr)] = None
            self._first = (self._first +1) % len(self._arr)
            self._size -= 1
            return True
        return False
    
    def right_dequeue(self):
        if self.is_empty():
            return True
        else:
            d = self._arr[(self._first + self._size -1) % len(self._arr)]
            self._arr[(self._first + self._size -1) % len(self._arr)] = None
            self._size -= 1
            return d
        return None
    
    def left_enqueue(self, e):

        if self._size == len(self._arr):
            return False
        self._arr[(self._first - 1)%len(self._arr)] = e
        self._first = (self._first - 1)%len(self._arr)
        self._size += 1
        return True
    
    def enqueue(self, e):
        if self._size == len(self._arr):
            return False
        self._arr[(self._first + self._size) % len(self._arr)] = e
        self._size += 1
        return True
    
    def swap(self, v1, v2):
        for i in range(0, self._size):
            if self._arr[(self._first + i) % len(self._arr)] == v1:
                temp1 = (self._first + i) % len(self._arr)
                for i in range(0, self._size):   
                    if self._arr[(self._first + i) % len(self._arr)] == v2:
                        temp2 = (self._first + i) % len(self._arr)
                        self._arr[temp1], self._arr[temp2] = self._arr[temp2], self._arr[temp1]
                        return True
        return False
    
    def dequeue_before(self, s):
        
        if self._size == 0 or self._size == 1:
            return False
        if self._size != len(self._arr) and self._arr[self._first % len(self._arr)] == s:
            return False
        
        for i in range(self._first, self._first + self._size):
            if self._arr[i % len(self._arr)] == s:
                index = (i - 1) % len(self._arr)
                self._arr[index] = None
                for j in range(i - 1, (self._first + self._size)):
                    self._arr[j % len(self._arr)] = self._arr[(j + 1) % len(self._arr)]
                self._size -= 1
                # if self._size == 0:
                #     self._first = 0
                #     return True
        return False
           
                    
    def dequeue_after(self, s):
        
        if self._size == 0 or self._size == 1 or self._arr[(self._first + self._size -1) % len(self._arr)] == s:
            return False
        
        for i in range(self._first, self._first + self._size):
            if self._arr[i % len(self._arr)] == s:
                index = (i + 1) % len(self._arr)
                self._arr[index] = None
                for j in range(i + 1, (self._first + self._size)):
                    self._arr[j % len(self._arr)] = self._arr[(j + 1) % len(self._arr)]
                self._size -= 1
                if self._size == 0:
                    self._first = 0
                    return True
        return False
                    
    
    def enqueue_before(self, s, t):
        if self._size == len(self._arr) or self._size == 0:
            return False
        
        for i in range(self._first, self._first + self._size):
            if self._arr[i % len(self._arr)] == s:
                print(i, self._arr[i % len(self._arr)])
                for j in range(self._first - 1, i):
                    self._arr[ j % len(self._arr)] = self._arr[(j+1) % len(self._arr)]
                self._arr[(i-1) % len(self._arr)] = t
                self._size += 1
                return True
            
        return False
                
    def enqueue_before(self, s, t): 
         if self._size == 0 or self._size == len(self._arr): 
             return False 
         for i in range(self._first, self._first + self._size): 
             if self._arr[i%len(self._arr)] == s: 
                 for j in range((self._first -1), i): 
                     self._arr[j%len(self._arr)] = self._arr[(j+1)%len(self._arr)] 
                 self._arr[(i-1)%len(self._arr)] = t 
                 self._first = self._first+1 
                 self._size += 1 
                 return True  
         return False
    
    def enqueue_after(self, s, t):
        if self._size == len(self._arr) or self._size == 0:
            return False
        
        for i in range(self._first, self._first + self._size):
            if self._arr[i % len(self._arr)] == s:
                for j in range((self._first + self._size), i + 1, -1):
                    self._arr[j % len(self._arr)] = self._arr[(j-1) % len(self._arr)]
                self._arr[(i+ 1) % len(self._arr)] = t
                self._size += 1
                return True
            
        return False
        
                    
    def remove_at(self, index):
        if index >= len(self._arr) or index < 0:
            return False
        if self._size == 0:
            return False
        self._arr[(self._first + index) % len(self._arr)] = None
        for i in range(self._first + index, (self._first + self._size)):
            self._arr[i % len(self._arr)] = self._arr[(i + 1) % len(self._arr)]
        self._size -= 1
        if self._size == 0:
            self._first = 0
            return True
        
        
    def deque_element(self, a):
        if self._size == 0:
            return False
        
        for i in range(self._first, self._first + self._size):
            if self._arr[i % len(self._arr)] == a:
                self._arr[i % len(self._arr)] == None
                for j in range(i, (self._first + self._size)):
                    self._arr[j % len(self._arr)] = self._arr[(j + 1) % len(self._arr)]
                self._size -= 1
                if self._size == 0:
                    self._first = 0
                    return True
                
        return False

    
    class arriterator:
        def __init__(self, deque):
            self._deque = deque
            self._current = deque._first % len(deque._arr)
            self._size = deque._size
            self._count = 0
            
        def __next__(self):
            if self._count != self._size:
                temp = self._current
                self._current = (self._current + 1) % len(self._deque._arr)
                self._count +=1
                return self._deque._arr[temp]
            else:
                raise StopIteration
            
    def __iter__(self):
        return self.arriterator(self)
    
class Set(Collection):

    @abstractmethod
    def contains(self, o):
        pass
    @abstractmethod
    def add(self, value):
        pass #boolean
    @abstractmethod
    def remove(self, value):
        pass #boolean
    @abstractmethod
    def equals(self, s):
        pass #boolean
    @abstractmethod
    def get_element_at(self, index):
        pass #object
        
class Map(Collection):
    
    
    @abstractmethod
    def get(self,key):
        pass # Object(value)
    
    
    @abstractmethod
    def put(self, key, value):
        pass # Object(value)
    
    
    @abstractmethod
    def remove(self,key):
        pass # Object(value)
    
    
    @abstractmethod
    def key_set(self):
        pass    # returns a set of all keys in the map
        
class HashMap(Map):
    class Entry:
        def __init__(self, key = None, value = None, next = None):
            self._key = key
            self._value = value
            self._next = next
            
    def __init__(self):
        self._hash_table = [None] * 37
        self._size = 0
        
    def hash(self, key):
        return hash(key) % 37
    
    
    def index_iterator(self, index: int):
        return self.IndexIter(self, index)
    
    
    class IndexIter:
        def __init__(self, h, index):
            self._current = None 
            self._map = h

            i = 0
            for e in range(0, len(h._hash_table)):
                if self._current != None:
                    print(self._current)
                    break
                if self._map._hash_table[e]:
                    entry = h._hash_table[e]
                    while entry:
                        if i == index:
                            self._current = entry
                            break
                        i += 1
                        entry = entry._next
            
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current 
            self._current = self._current._next
            if self._current == None:
                hashIndex = HashMap.hash(self._map, temp._key)
                for i in range(hashIndex +1, len(self._map._hash_table)):
                    if self._map._hash_table[i]:
                        self._current = self._map._hash_table[i]
                        break 
            return temp._key
        
        
    def get(self, key):
        hashIndex = self.hash(key)
        entry = self._hash_table[hashIndex]
        while entry:
            if entry._key == key:
                return entry._value
            
            entry = entry._next
        return None 


    
    def put(self, key, value):
        hashIndex = self.hash(key)
        entry = self._hash_table[hashIndex]
        while entry:
            if entry._key == key:
                temp = entry._value
                entry._value = value
                return temp
            entry = entry._next
            
        e = HashMap.Entry(key, value, self._hash_table[hashIndex])
        self._hash_table[hashIndex] = e
        self._size += 1
        return value 
    
    
    
    def remove(self, key):
        hashIndex = self.hash(key)
        entry = self._hash_table[hashIndex]
        prev = None
        while entry:
            if entry._key == key:
                temp = entry._value
                if prev:
                    prev._next = entry._next
                else:
                   self._hash_table[hashIndex] = self._hash_table[hashIndex]._next
                self._size -= 1
            
                return temp
            
            prev = entry
            entry = entry._next
        return None 
    
    
    def remove_entries_having_thisval(self):
        count = 0
        for i in range(len(self._hash_table)):
            if self._hash_table[i] != None:
                temp = self._hash_table[i]
                while temp and temp._value == 7:
                    self._hash_table[i] = self._hash_table[i]._next
                    count += 1
                    self._size -= 1
                    temp = temp._next
                if temp:
                    prev = temp 
                    temp = temp._next
                    while temp :
                        if temp._value == 7:
                            prev._next = temp._next
                            count += 1
                            self._size -= 1
                        prev = temp 
                        temp = temp._next
        return count
                        
                    
            # while temp:
            #     if temp._value == 7:
                    
    def key_set(self):
        keys = []
        for i in range(0, len(self._hash_table)):
            if self._hash_table[i]:
                entry = self._hash_table[i]
                while entry:
                    keys.append(entry._key)
                    entry = entry._next
        return keys

    def getNumberOfUniqueValues(self):
        num = 0
        values = []
        for i in range(0, len(self._hash_table)):
            temp = self._hash_table[i]
            while temp:
                if temp._value not in values:
                    num += 1
                    values.append(temp._value)
                temp = temp._next
        return num
        
    def print(self):
        for i in self._hash_table:
            if i:
                temp = i
                while temp:
                    print (temp._key, ":" , temp._value)
                    temp = temp._next
    
    
    def is_empty(self):
        return self._size == 0
    

    def size(self):
        return self._size
    
    def empty(self):
        for i in self._hash_table:
            if i:
                cur = i
                while cur:
                    temp = cur
                    cur = cur._next
                    temp = None
    

            
            
    def gpa_iterator(self, gpa: float):
        return self.GPAIter(self, gpa)


    class GPAIter:
        def __init__(self, m, gpa):
            self._map = m
            self._gpa = gpa
            self._current = None
            found = False
            for e in m._hash_table:
                if found:
                    break
                if e:
                    temp = e
                    while temp:
                        if temp._key.get_gpa() == self._gpa:
                            if not found:
                                self._current = temp
                                found = True
                                break

                
                
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current
            
            while self._current:
                if self._current._key.get_gpa() != self._gpa:
                    break
                self._current = self._current._next
            
            if self._current == None:
                hashIndex = HashMap.hash(self._map, temp._key)
                found = False
                for i in range(hashIndex +1, len(self._map._hash_table)):
                    if found:
                        break
                    if self._map._hash_table[i]:
                        e = self._map._hash_table[i]

                        while e:
                           if e._key.get_gpa() == self._gpa:

                               if not found:
                                   self._current = e
                                   found = True
                                   break

                           e = e._next                

            return temp._key
        
        
    class EntryIterator:
        def __init__(self, m):
            self._map = m
            self._current = None
            for e in m._hash_table:
                if e != None:
                    self._current = e
                    break
                
                
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current 
            self._current = self._current._next
            if self._current == None:
                hashIndex = HashMap.hash(self._map, temp._key)
                for i in range(hashIndex +1, len(self._map._hash_table)):
                    if self._map._hash_table[i]:
                        self._current = self._map._hash_table[i]
                        break 
            return temp
        
                    
                
    def __iter__(self):
        return self.EntryIterator(self)


class HashSet(Set):
    class Node:
        def __init__(self,data = None, next = None):
            self._data = data
            self._next = next
            
    def __init__(self):
        
        self._hash_table = [None] * 37
        self._size = 0
        
    def hash(self, o):
       return hash(o) % 37
    
    def contains(self, o):
        hash_key = self.hash(o)
        temp = self._hash_table[hash_key]
        while temp:
          if  temp._data == o:
                return True
          temp = temp._next
        return False 
    
    
    def remove_element_at(self, index: int)->bool:
            if index < 0 or index >= self._size:
                return False
            i = 0
            for e in range(0, len(self._hash_table)):
                
                if self._hash_table[e]:
                    entry = self._hash_table[e]
                    prev = None
                    while entry:
                        if i == index:
                            if entry == self._hash_table[e]:
                                self._hash_table[e] = self._hash_table[e]._next
                                self._size -= 1
                                return True
                            prev._next = entry._next
                            self._size -= 1
                            return True
                        i += 1
                        prev = entry
                        entry = entry._next
            return False
        
    def add_element_at(self, index, val)->bool:
        if index < 0 or index >= self._size:
            return False
        i = 0
        last = None
        for e in range(0, len(self._hash_table)):
            
            if self._hash_table[e]:
                entry = self._hash_table[e]
                prev = None
                while entry:
                    if i == index:
                        if self.hash(val) != e:
                            if last and entry == self._hash_table[e] and self.hash(last._data) == self.hash(val):
                                last._next = HashSet.Node(val)
                                self._size += 1
                                return True
                            return False
                        node = HashSet.Node(val)

                        if entry == self._hash_table[e]:
                            node._next = entry
                            self._hash_table[e] = node
                            return True
                        prev._next = node
                        node._next = entry
                    i += 1
                    prev = entry
                    entry = entry._next
                    self._size += 1

                last = prev
                print("im the last", last._data)

        return False
        
    def add(self, e) -> bool:
        if self.contains(e):
            return False
        hash_index = self.hash(e)
        node = HashSet.Node(e, self._hash_table[hash_index])
        self._hash_table[hash_index] = node
        self._size += 1
        
    def remove(self, e) -> None:
        hash_index = self.hash(e)
        n = self._hash_table[hash_index]
        prev = None
        while n:
            if n._data == e:
                if prev:
                    prev._next = n._next
                else:
                    self._hash_table[hash_index] = self._hash_table[hash_index]._next
                self._size -= 1
                return True
            else:
                prev = n
                n = n._next
        return False
    
    

    
    
    def removeElementAfter(self, s):
        index = self.hash(s)
        temp = self._hash_table[index]
        while temp:
            if temp._data == s:
                if not temp._next:
                    for i in range(index + 1, len(self._hash_table)):
                        if self._hash_table[i]:
                            self._hash_table[i] = self._hash_table[i]._next
                            self._size -= 1
                            return True
                    return False
                temp._next = temp._next._next 
                self._size -= 1
                return True 
            temp = temp._next 
        return False
    
    
    def removeElementBefore(self, s):
        index = self.hash(s)
        temp = self._hash_table[index]
        if temp._data == s:
            for i in range(index - 1, -1, -1):
                if self._hash_table[i]:
                    if not self._hash_table[i]._next:
                        self._hash_table[i] = None
                        self._size -= 1
                        return True
                    """
                    temp = self._hash_table[i]
                    prev = self._hash_table[i]
                    while temp._next:
                        prev = temp
                        temp = temp._next
                    prev._next = None
                    self._size -= 1
                    return True
                
            prev = self._hash_table[index]
            while temp and temp._data != s:
                prev = temp
                temp = temp._next
                
            if temp == None:
                return False
            
            prev._next = temp._next 
            self._size -= 1
            return True
            
                
            
        
                    """
                    e = self._hash_table[i]
                    k = None
                    while e._next:
                        k = e
                        e = e._next
                    k._next = None
                    self._size -= 1
                    return True
            return False
        
        prev = None
        while temp:
            if temp._next._data == s:
                if temp == self._hash_table[index]:
                    self._hash_table[index] = self._hash_table[index]._next
                    self._size -= 1
                    return True
                prev._next = temp._next
                self._size -= 1
                return True 
            prev = temp
            temp = temp._next 
        return False
    
    
    def addElementAfter(self, s, t):
        if self.hash(s) != self.hash(t):
            return False
        
        index = self.hash(s)
        temp = self._hash_table[index]
        while temp:
            if temp._data == t:
                return False
            temp = temp._next 
            
            
        temp = self._hash_table[index]
        while temp:
            if temp._data == s:
                if not temp._next:
                    temp._next = HashSet.Node(t)
                    self._size += 1
                    return True
                t = HashSet.Node(t)
                m = temp._next
                temp._next = t
                t._next = m
                self._size += 1
                return True 
            temp = temp._next 
        return False
    
    
    def addElementBefore(self, s, t):
        if self.hash(s) != self.hash(t):
            return False
        
        index = self.hash(s)
        temp = self._hash_table[index]
        while temp:
            if temp._data == t:
                return False
            temp = temp._next 
            
           
        temp = self._hash_table[index]
        if temp._data == s:
            self._hash_table[index] = HashSet.Node(t)
            self._hash_table[index]._next = temp
            self._size += 1
            return True
        
        while temp:
            if temp._next._data == s:
                t = HashSet.Node(t)
                m = temp._next
                temp._next = t
                t._next = m
                self._size += 1
                return True 
            temp = temp._next 
        return False
    
    
    def getStudentsGraduatingAt(self, gy):
        stset = Set()
        for i in range(0, len(self._hash_table)):
            temp = self._hash_table[i]
            while temp:
                if temp._data.get_graduation_year() == gy:
                    stset.add(temp._value)
                temp = temp._next
                
        return stset
    
    
    def odd_iter(self):
        return self.OddIter(self)
    
    def even_iter(self):
        return self.EvenIter(self)
    
    
    class EvenIter:
        def __init__(self, hs):
            self._hash_table = hs._hash_table 
            self._current = None
            
            for e in self._hash_table:
                if e != None:
                    self._current = e
                    break
                
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current 
            self._current = self._current._next
            if self._current:
                if self._current._next:
                    self._current = self._current._next
                else:
                    hashIndex = HashSet.hash(self._hash_table, self._current._data)
                    for i in range(hashIndex +1, len(self._map._hash_table)):
                        if self._hash_table[i]:
                            self._current = self._hash_table[i]
                            break 
                    
            else:
                has = False
                hashIndex = HashSet.hash(self._hash_table, temp._data)
                for i in range(hashIndex +1, len(self._hash_table)):
                    if self._hash_table[i]:
                        if has:
                            self._current = self._hash_table[i]
                            break
                        elif self._hash_table[i]._next:
                            self._current = self._hash_table[i]._next
                        else:
                            has = True
            return temp
            
            
            
    class OddIter:
        def __init__(self, hs):
            self._hash_table = hs._hash_table 
            self._current = None
            has = False
            for e in self._hash_table:
                if e != None:
                    if has:
                        self._current = e
                        break
                    elif e ._next:
                        self._current = e._next
                        break
                    else:
                        has = True
            
            
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current 
            self._current = self._current._next
            if self._current:
                if self._current._next:
                    self._current = self._current._next
                else:
                    hashIndex = HashSet.hash(self._hash_table, self._current._data)
                    for i in range(hashIndex +1, len(self._map._hash_table)):
                        if self._hash_table[i]:
                            self._current = self._hash_table[i]
                            break 
                    
            else:
                has = False
                hashIndex = HashSet.hash(self._hash_table, temp._data)
                for i in range(hashIndex +1, len(self._hash_table)):
                    if self._hash_table[i]:
                        if has:
                            self._current = self._hash_table[i]
                            break
                        elif self._hash_table[i]._next:
                            self._current = self._hash_table[i]._next
                        else:
                            has = True
            return temp

    def equals(self, s):
        for i in range(0, len(s._hash_table)):
            temp = s._hash_table[i]
            while temp:
                if self.contains(temp._data) == False:
                    return False
                temp = temp._next
        return True
        
        
    def get_element_at(self, index):
        if index < 0 or index > self._size:
            return None
        i = 0
        for e in range(0, len(self._hash_table)):
            
            if self._hash_table[e]:
                entry = self._hash_table[e]
                while entry:

                    if i == index:
                        return entry._data
                    i += 1
                    entry = entry._next
                    
                #while i != index:
                    #i += 1
                    #entry = entry._next 
                    
                #return entry 
        return None

        
    def empty(self):
        for i in self._hash_table:
            if i:
                cur = i
                while cur:
                    temp = cur
                    cur = cur._next
                    temp = None
    
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def print(self):
        for i in self._hash_table:
            if i:
                temp = i
                while temp:
                    print (temp._data)
                    temp = temp._next
    
    
#HOMEWORK 5

class SortedSet(Collection):
    
    @abstractmethod
    def add(self, value):
        pass
    
    @abstractmethod
    def remove(self, value):
        pass
    
    @abstractmethod
    def contains(self, value):
        pass
    
    @abstractmethod
    def equals(self, s):
        pass
    
    @abstractmethod
    def get_element_at(self, index):
        pass
    
    @abstractmethod
    def get_smallest_element(self):
        pass
    
    @abstractmethod
    def get_largest_element(self):
        pass
        
        
class SortedMap(Collection):
    
    @abstractmethod
    def put(self, key, value):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def remove(self, key):
        pass
    
    @abstractmethod
    def keySet(self): #returns a set of all keys in the map
        pass
    
    @abstractmethod
    def sub_map(self, k1, k2): 
        pass
    
    
class TreeSet(SortedSet):
    class Node:
        def __init__(self, d = None, p = None, c = "R" ):
            self._data = d
            self._parent = p
            self._right = None
            self._left = None
            self._size = None
            self._color = c
            
        def set_parent(self, p):
            self._parent = p
            
            
        def set_black(self):
            self._color = "B"    
            
        def get_left(self):
            return self._left
        
        
        def get_right(self):
            return self._right 
        
        
        def set_red(self):
            self._color = "R"
            
        def color_black(self):
            self._color = "B"
            
        def color_red(self):
            self._color = "R"
            
            
        def color_black_deficit(self):
            self._color = "D"
            
        def is_black(self):
            return self._color == "B"
        
        
        def is_red(self):
            return self._color == "R"
        
    def __init__(self):
        self._root = None
        self._size = 0
        
        
    def __iter__(self):
        self._current_node = self.get_smallest_element()
        return self
        
    def __next__(self):
        if self._current_node is None:
            raise StopIteration
            
        temp = self._current_node
        if temp._parent and temp == temp._parent._left:
            isleft = True
        else:
            isleft = False
        if self._current_node._right is None:
            p = self._current_node._parent
            
            if not isleft:
                while p is not None and self._current_node != p._left:

                    self._current_node = p
                    p = p._parent
                    
                self._current_node = p

            else:
                self._current_node = p
                
        else:  

            self._current_node = self.get_smallest_node(self._current_node._right)

        return temp   
    
    def odd_rec(self, node):
        val = 0
        if node:
            val += self.odd_preorder(node._left)
            if node._data % 2 == 1:
                val += 1
            val += self.odd_preorder(node._right)

        return val
        
    def odd_iterative(self):
            if self._root == None:
                return 0
            l = [self._root]
            val = 0
            while len(l) != 0:

                n = []
                for i in l:
                    if i._data % 2 == 1:
                        val += 1
                    if i._left:
                        n.append(i._left)
                    if i._right:
                        n.append(i._right)
                l = n      
            
            return val
                

      

           
    def right_rotate(self, node):

        p = node._parent
        x = node
        y = node._left
        T = y._right
        y._right = x
        x._parent = y
        x._left = T
        if T:
            T._parent = x
        y._parent = p
        if not p:
            self._root = y
        else:
            if y._data < p._data:
                p._left = y
            else:
                p._right = y

        return y

    
   
    def left_rotate(self, node):

        p = node._parent
        x = node
        y = node._right
        T = y._left
        y._left = x
        x._parent = y
        x._right = T
        if T:
            T._parent = x
        y._parent = p
        if not p:
            self._root = y
        else:
            if y._data < p._data:
                p._left = y
            else:
                p._right = y

        return y
    
    
    def get_smallest_element(self):
        temp = self._root
        while temp._left != None:
            temp = temp._left 
            
        return temp
    
    def get_largest_element(self):
        temp = self._root
        while temp._right != None:
            temp = temp._right 
            
        return temp
    
    
    
    def get_sibling (self, node):
        if node == None or node._parent == None:
            return None 
        if node == node._parent._right:
            return node._parent._left 
        if node == node._parent._left:

            return node._parent._right
    
    
    def add(self, value):
        if self._root is None:
            self._root = self.Node(value)
            self._root.color_black()
            self._size += 1
            return value
        else:
            return self.insert_rec(self._root, value)
        
    
    def insert_rec(self, node, v):
        
        if v > node._data:
            res = None
            if node._right != None:
                res = self.insert_rec(node._right, v)
            else:
                temp = TreeSet.Node(v)
                node._right = temp
                temp._parent = node
                self._size += 1
                self.restructure(node._right)
                return v
                
        elif v < node._data:
            res = None
            if node._left != None:
                res = self.insert_rec(node._left, v)
            else:
                temp = TreeSet.Node(v)
                node._left = temp
                temp._parent = node
                
                self._size += 1
                self.restructure(node._left)
                return v
                
        else:
            return node._data
        
        self.restructure(node)
        return res
    
    

    

    def restructure(self, node):
        if node == None:
            return 
        if node.is_black():
            return 
        if node._parent == None:
            node.color_black()
            return 
            
        if node._parent.is_black():
            return
        
        p = node._parent 
        gp = p._parent 

        if gp == None:
            p.color_black()
            return 
        
        u = self.get_sibling(p)
        if u is not None and u.is_red():
            p.color_black()
            u.color_black()
            gp.color_red()
        
            if gp == self._root:
                self._root.color_black()
                
            return 
        
        if p == gp._left:
            if node == p._right:

                p = self.left_rotate(p)
                
            self.right_rotate(gp)
            gp.color_red()
            p.color_black()
        
        else:

            if node == p._left:
                p = self.right_rotate(p)
                
            self.left_rotate(gp)
            gp.color_red()
            p.color_black()

    
    
    def remove(self, data):
        return self.remove_rec(self._root, data)
            
    
    def get_smallest_node(self, node):
        temp = node
        while temp._left != None:
            temp = temp._left 
            
        return temp
    
    
    def get_largest_node(self, node):
        temp = node
        while temp._right != None:
            temp = temp._right 
            
        return temp
    
    
    def remove_rec(self, node, data):
        if node == None:
            return False
        if node._data > data:
            res = self.remove_rec(node._left, data)
        if node._data < data:
            res = self.remove_rec(node._right, data)
        if node._data == data:
            if node._left is not None:
                c = self.get_largest_node(node._left)
                node._data = c._data
                res = self.remove_rec(node._left, c._data)
            elif node._right is not None:
                c = self.get_smallest_node(node._right)
                node._data = c._data
                res =self.remove_rec(node._right, c._data)
            
            else:
                res = True
                if node.is_black():
                    node.color_deficit()
                    self.resolve_black_deficit(node)
                    
                p = node._parent
                if p is not None:
                    if node == node._parent._right:
                        node._parent._right = None
                    else:
                        node._parent._left = None
                else:
                    self._root = None
                    
        self.resolve_black_deficit(node)
        return res 
        
    def has_only_black_children(self, node):
        if node == None:
            return True
        return (not node._left or node._left.is_black()) and (not node._right or node._right.is_black())
    
    
    def resolve_black_deficit(self, node):
        if not node or not node.is_deficit():
            return 
        
        if node._parent is None:
            node.color_black()
            return 
        
        p = node._parent
        s = self.get_sibling(node)
        if s!= None and s.is_red():
            if node == p._left:
                self.left_rotate(p)
            else:
                self.right_rotate(p)
            s.color_black()
            p.color_red()
        s = self.get_sibling(node)
        if s is not None and self.has_only_black_children(s):
            s.color_red()
            node.color_black()
            if p.is_red():
                p.color_black()
            else:
                p.color_deficit()
        else:
            if node == p._left:
                if s._right is not None and s._right.is_black():
                    s.color_red()
                    s = self.right_rotate(p)
            
                self.left_rotate(p)
            else:
                if s._left is not None and s._left.is_black():
                    s.color_red()
                    s = self.left_rotate(s)
                self.right_rotate(p)
            if p.is_red():
                s.color_red()
            else:
                s.color_black()
            p.color_black()
            s._right.color_black()
    
    
    def contains(self, v):
        node = self._root 
        while node:
            if v == node._data:
                return True
            if v > node._data:
                node = node._right 
            else:
                node = node._left
        return False
                
    
    
    def equals(self, s):
        if self._size != s._size:
            return False 
        l = [self._root]
        while len(l) != 0:
            n = []
            for i in l:
                if not s.contains(i):
                    return False 
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            l = n
            
        return True
        
    
    
    def get_element_at(self, index):
        it = iter(self)
        i = 0
        while True:
            try:
                s = next(it)
                if i == index:
                    return s
                i += 1
            except StopIteration:
                break
        return None
    
    

    def empty(self):
        for i in self:
            self.remove(i._data)

    
    
    def level_orderprint(self):
        if self._root == None:
            return 
        l = [self._root]
        while len(l) != 0:
            n = []
            print("new level")

            for i in l:
                print(i._data, ",", i._color, " ", end = '')
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            print("")
            l = n
            
    def print(self):
        self.level_orderprint() 
    
    def is_empty(self):
        return self._size == 0


class TreeMap(Map):
    class Entry:

        def __init__(self, k = None, v = None, p = None):
            self._key = k
            self._value = v
            self._parent =  p
            self._right = None
            self._left = None
            
        def set_parent(self, p):
            self._parent = p
            
            
        def set_black(self):
            self._color = "B"    
            
        def get_left(self):
            return self._left
        
        
        def get_right(self):
            return self._right 
        
        def get_value(self):
            return self._value
            
    def __init__(self): 
        self._root = None
        self._size = 0
        
    def print(self):
        self.level_order_print()
    
    
    def is_tree_left_skewed(self) -> bool:
        return self.is_tree_left_skewed_helper(self._root)
    
    def is_tree_left_skewed_helper(self, node):
       if node == None or (node._left == None and node._right == None):
           return True
       if node._right:
           return False
       return self.is_tree_left_skewed_helper(node._left)
   
    
    def iterative_preorder_gpa(self, gpa):
        return self.IterGpa(self, gpa)
    
    class IterGpa:
        def __init__(self, t, gpa):
            self._gpa = gpa
            self._stack = [t._root]
            self._current = None
            while len(self._stack) != 0:
                e = self._stack
   
    def iterativePreorder(self, root):
     
        if root is None:
            return
     
        nodeStack = []
        nodeStack.append(root)

        while(len(nodeStack) > 0):
             
            node = nodeStack.pop()
            print (node._key, end=" ")

            if node._right is not None:
                nodeStack.append(node._right)
            if node._left is not None:
                nodeStack.append(node._left)
                
     
    def is_tree_complete(self):
        if self._root == None:
            return
        l = [self._root]
        lvl = 0
        while len(l) != 0 and lvl != max(self.height(self._root._right), self.height(self._root._left)) - 1:
            lvl += 1
            n = []
            for i in l:
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            for i in n:
                if not i._right or not i._left:

                    return False
            l = n
            
        for i in range(0, len(l)):
            if l[i]._left is None and l[i]._right is not None:
                return False
            elif not l[i]._left or not l[i]._right:
                for k in range(i, len(l)):
                    if l[k]._left or l[k]._right:
                        return False
        return True


    def get_set_of_unique_values_rec(self):
        res = self.get_set_of_unique_values_helper(self._root, [])
        return res
    
    def get_set_of_unique_values_helper(self, node, res):
        if node:
            if node._value not in res:
                res.append(node._value)
            self.get_set_of_unique_values_helper(node._left, res)
            self.get_set_of_unique_values_helper(node._right, res)
            
        return res
    def inorder_print(self):
        return self.inorder_print_helper(self._root)
    
    
    def inorder_print_helper(self, node):
        if node:
            self.inorder_print_helper(node._left)
            print(node._key)
            self.inorder_print_helper(node._right)
    
    
    def preorder_print(self):
        return self.preorder_print_helper(self._root)
    
    
    def preorder_print_helper(self, node):
        if node:
            print(node._key)
            self.preorder_print_helper(node._left)
            self.preorder_print_helper(node._right)
            
            
    def postorder_print(self):
        return self.postorder_print_helper(self._root)
    
    
    def postorder_print_helper(self, node):
        if node:
            self.postorder_print_helper(node._left)
            self.postorder_print_helper(node._right)
            print(node._key)        
            
            
    def inorder_iterative(self):
     
        current = self._root
        stack = [] 
         
        while True:
             
            if current is not None:

                stack.append(current)
             
                current = current._left

            elif stack: 
                current = stack.pop()
                print(current._key, end=" ") 

                current = current._right
     
            else:
                break     
            
            
    def key_set(self):
        stack = []
        keyset = []
        current = self._root
        while True:
            if current:
                stack.append(current)
                current = current._left
            elif len(stack) != 0:
                e = stack.pop()
                keyset.append(e._key)
                current=e._right
            else:
                break
        return keyset
                
    
    def empty(self):
        for i in self:
            self.remove(i._key)
    
    
    def is_empty(self):
        return self._size == 0
        
    def put(self, k, v):
        if self._root is None:
            self._root = self.Entry(k, v)
            self._size += 1
            return True
        else:
            return self.put_rec(self._root, k, v)

    def right_rotate(self, node):

        p = node._parent
        x = node
        y = node._left
        T = y._right
        y._right = x
        x._parent = y
        x._left = T
        if T:
            T._parent = x
        y._parent = p
        if not p:
            self._root = y
        else:
            if y._key < p._key:
                p._left = y
            else:
                p._right = y

        return y

    def left_rotate(self, node):

        p = node._parent
        x = node
        y = node._right
        T = y._left
        y._left = x
        x._parent = y
        x._right = T
        if T:
            T._parent = x
        y._parent = p
        if not p:
            self._root = y
        else:
            if y._key < p._key:
                p._left = y
            else:
                p._right = y

        return y

    def submap(self, k1, k2):
        newtree = TreeMap()
        keyset = self.key_set()
        i1 = keyset.index(k1)
        i2 = keyset.index(k2)
        for i in range(i1, i2+1):
            newtree.put(keyset[i], self.get(keyset[i]))
        return newtree    
        
            
    def get_smallest_element(self, node):
        temp = node
        while temp._left:
            temp = temp._left
        return temp   
    
    def is_tree_left_skewed(self):
        temp = self._root
        while temp:
            if temp._right:
                return False
            temp = temp._left
        return True
    
    def get_set_of_unique_values(self):
        newset = TreeSet()
        for i in self:
            newset.add(i._value)
        return newset
    
    
    
    # def __iter__(self):
    #     self._current_node = self.get_smallest_element(self._root)
    #     return self
    
    # def inorder_iter(self):
    #     return self.PreorderIter(self)
            
    # def __iter__(self):
    #     return self.PostOrderGPAIter(self)
    def __iter__(self):
        return self.GPAInorderIter(self)
        
    
    class GPAInorderIter:
        def __init__(self, tr):
            self._tr = tr
            found = False

            temp = tr.get_smallest_element(tr._root)
            if temp._value % 7 == 0:
                self._current = temp
                found = True
            else:
                self._current = None
                while not found:
                    if temp._parent and temp == temp._parent._left:
                        isleft = True
                    else:
                        isleft = False
                    if temp._right is None:
                        p = temp._parent
                        
                        if not isleft:
                            while p is not None and temp != p._left:
    
                                temp = p
                                p = p._parent
                                
                            temp = p
    
                        else:
                            temp = p
                            
                    else:  
    
                        temp = self.get_smallest_element(temp._right)
                        
                        
                    if temp._value % 7 == 0:
                        self._current = temp
                        break
            
        def __next__(self):
            if self._current == None:
                raise StopIteration
            returnval = self._current
            temp = self._current
            self._current = None
            found = False
            while not found:
                if temp:
                    if temp._parent and temp == temp._parent._left:
                        isleft = True
                    else:
                        isleft = False
                    if temp._right is None:
                        p = temp._parent
                        
                        if not isleft:
                            while p is not None and temp != p._left:
    
                                temp = p
                                p = p._parent
                                
                            temp = p
    
                        else:
                            temp = p
                            
                    else:  
    
                        temp = self._tr.get_smallest_element(temp._right)
                        
                    if temp and temp._value % 7 == 0:
                        self._current = temp
                        found = True
                
            return returnval
    
    
    class PreorderIter:
        def __init__(self, tr):
            self._current = None
            self._root = tr._root
            temp = tr._root
            if temp._value == 7:
                self._current = temp 
            else:
                found = False
                while not found:
                    if temp._left != None:
                        temp = temp._left
                        
                        
                    elif temp._right != None:
                        temp = temp._right
                        
                        
                    elif temp._right == None and temp._left == None:
                        p = temp
                        while p._parent:

                            """
                            if p = p._parent._left:
\                                       if p._parent._right:
                                        temp = p._parent._right
                                        break 
                            p = p._parent 
                            """
                            if p == p._parent._left:
                                isLeftChild = True
                                if p._parent._right:
                                    temp = p._parent._right
                                    break
                                elif isLeftChild:
                                    p = p._parent
                                    while p._parent:
                                        if p._right:
                                            temp = p._right
                                            break 
                                        p = p._parent
                                    
                            p = p._parent
       
                        if p is not None and p == self._root:
                            found = True
                            break
                        

                    if temp._value == 7:
                        self._current = temp
                        found = True
            
            
        def __next__(self):
            if self._current is None:
                raise StopIteration
                
            returnval = self._current
            self._current = None
            temp = returnval   
            found = False
            p = None

            while not found:
                if temp._left != None:
                    temp = temp._left
                    
                    
                elif temp._right != None:
                    temp = temp._right
                    
                    
                elif temp._right == None and temp._left == None:
                    p = temp
                    while p._parent:

                        if p == p._parent._left:
                            temp = p._parent._right
                            break
                        p = p._parent
   
                    if p is not None and p == self._root:
                        found = True
                        break
                    

                if temp._value == 7:
                    self._current = temp
                    found = True 

            return returnval
        
        
    def get_leaf(self, node):
        if node == None:
            return None
        while node._left != None or node._right != None:
            if node._left:
                node = node._left
            elif node._right:
                node = node._right
                
        return node 
    
    
    class PostOrderIter:
        def __init__(self, tr):
            self._current = tr.get_leaf(tr._root)
            self._tr = tr
            
        def __next__(self):
            if self._current == None:
                raise StopIteration
                
            temp = self._current 
            self._current = None
            if temp._parent and temp == temp._parent._left:
                    self._current = self._tr.get_leaf(temp._parent._right)
                    if self._current == None:
                        self._current = temp._parent
            elif temp._parent and temp._parent._right == temp:
                self._current = temp._parent
                
            return temp
        

    def get_prev_in_preorder(self, node):
        
        if node == self._root: 
            return None 
        if node._parent: 
           if node == node._parent._left: 
              return node._parent 
        if node == node._parent._right:
            if not node._parent._left:
                return node._parent
            left= node._parent._left
            while left._right or left._left:
               if left._right:
                  left = left._right 
               elif left._left: 
                  left = left._left
            return left    
           
    def get_next_in_preorder(self, temp):
            if temp == None:
                return None
              
            curr = None   
            
            if temp._left != None:
                curr = temp._left
                
            elif temp._right != None:
                curr = temp._right
                
                
            elif temp._right == None and temp._left == None:
                p = temp
                while p._parent:
                    if p == p._parent._left:
                        curr = p._parent._right
                        break
                    p = p._parent

            return curr
        
    class PostOrderGPAIter:
        def __init__(self, tr):
            temp = tr.get_leaf(tr._root)
            self._tr = tr 
            self._current = None
            if temp != None:
                if temp._value == 7:
                    self._current = temp
                else:
                    found = False
                    while not found:
                        if temp._parent and temp == temp._parent._left:
                                temp = self._tr.get_leaf(temp._parent._right)
                                if temp == None:
                                    temp = temp._parent
                        elif temp._parent and temp._parent._right == temp:
                            temp = temp._parent
                        
                        if temp._value == 7:
                            self._current = temp
                            found = True
                            
        def __next__(self):
            if self._current is None:
                raise StopIteration
                
            returnval = self._current
            self._current = None
            temp = returnval   
            found = False

            while not found:
                if temp._parent == None:
                    break
                
                if temp._parent and temp == temp._parent._left:
                        temp = self._tr.get_leaf(temp._parent._right)
                        if temp == None:
                            temp = temp._parent
                elif temp._parent and temp._parent._right == temp:
                    temp = temp._parent
                
                if temp._value == 7:
                    self._current = temp
                    found = True
                    
            return returnval
                
                
    class PreorderIter:
        def __init__(self, tr):
            self._current = tr._root 

            
        def __next__(self):
            if self._current is None:
                raise StopIteration
                
            temp = self._current
            self._current = None
                
            if temp._left != None:
                self._current = temp._left
                
            elif temp._right != None:
                self._current = temp._right
                
                
            elif temp._right == None and temp._left == None:
                p = temp
                while p._parent:
                    if p == p._parent._left:
                        if p._parent._right:
                            self._current = p._parent._right
                            break
                    p = p._parent

            return temp
    
    
    
            
            
     
    
    
    def grad_iter_(self):
        return self.Grad_Iter(self)
    
    
    
    class Grad_Iter:
        
        def __init__(self, t):
            self._stack = [t._root]
            self._current = None
            while len(self._stack) != 0:
                n = []
                e = self._stack.pop()
                
                if e._right:
                    n.append(e._right)
                    
                if e._left:
                    n.append(e._left)


                self._stack += n

                if e._value >= 0:
                    self._current = e
                    break


        def __next__(self):
            if self._current == None: 
                raise StopIteration
            temp = self._current 
            self._current = None
            while len(self._stack) != 0:
                n = []
                e = self._stack.pop()
                if e._right:
                    n.append(e._right)
                    
                    
                if e._left:
                    n.append(e._left)

                self._stack += n     
                if e._value >= 0:
                    self._current = e
                    break


                
            return temp._key
        
    
    

        
    def put_rec(self, node, k, v):
        
        if k > node._key:

            if node._right != None:
                res = self.put_rec(node._right, k, v)
            else:
                temp = TreeMap.Entry(k, v)
                node._right = temp
                temp._parent = node
                self._size += 1
                self.balance(node._right)
                return v
                
        elif k < node._key:

            if node._left != None:
                res = self.put_rec(node._left, k, v)
            else:
                temp = TreeMap.Entry(k, v)
                node._left = temp
                temp._parent = node
                
                self._size += 1
                self.balance(node._left)
                return v
                
        else:
            temp = node._value
            node._value = v
            return temp
        
        self.balance(node)
        return res
    
    def remove(self, v):

        return self.remove_rec(self._root, v)
        
        
    def remove_rec(self, node, v):
        if node == None:
            return None
        if node == self._root and self._size == 1:
            temp = node
            self._root = None
            self._size -= 1
            return temp
        if node._key > v:
            return self.remove_rec(node._left, v)
        elif node._key < v:
            return self.remove_rec(node._right, v)
        else:
            if node._left == None and node._right == None:
                temp = node._value

                if node._parent == None:
                    self._root = None
                else:
                    if node._parent._key > node._key:
                        #if node._parent._left == node same thing
                        node._parent._left = None
                    else:
                        node._parent._right = None
                        
                    self._size -= 1
                    return temp
                
            if node._left != None and node._right == None:
                temp = node
                if node._parent == None:
                    self._root = node._left 
                else:
                    if node._parent._key > node._key:
                        node._parent._left = node._right
                        
                    else:
                        node._parent._right = node._right
                        
                self._size -= 1
                return temp._value
            
            if node._right != None and node._left == None:
                temp = node
                if node._parent == None:
                    self._root = node._right 
                else:
                    if node._parent._key > node._key:
                        node._parent._left = node._left 
                        
                        
                    else:
                        node._parent._right = node._right
                        
            
                self._size -= 1
                self.balance(node)

                return temp._value
            new_key = self.get_smallest_element(node._right)._key
            node._value = self.get_smallest_element(node._right)._value
            node._key = new_key
            return self.remove_rec(node._right, new_key)
        
        
    def remove_at(self, index) -> bool:
        i = 0
        stack = []
        current=self._root
        while True:
            if current:
                stack.append(current)
                current=current._left
            elif len(stack)!=0:

                e=stack.pop()
                
                if i == index:
                    self.remove(e._key)
                    return True

                i += 1
            
                print(e._key)
                current=e._right
            else:
                break 
            
        return False
    
    def remove_before(self, key) -> bool:
        i = 0
        prev = None
        it = iter(self)
        s = next(it)
        if s._key == key:
            return False
        while i < self._size - 1:
            prev = s
            s = next(it)
            if s._key == key:
                self.remove(prev._key)
                return True
            i += 1
            
        return False
            
    def remove_after(self, key) -> bool:
        i = 0
        it = iter(self)
        s = next(it)
        while i < self._size - 1:
            if s._key == key:
                self.remove(next(it)._key)
                return True
            s = next(it)
            i += 1
            
        return False
    
    
    def in_order(self, node):
        stack = []
        current=node
        while True:
            if current:
                stack.append(current)
                current=current._left
            elif len(stack)!=0:
                e=stack.pop()
                print(e._key)
                current=e._right
            else:
                break
            
    def get(self, key):
        node = self._root 
        while node:
            if node._key < key:
                node = node._right
            elif node._key > key:
                node = node._left
            else:
                return node._value
        return None
            
    def height(self, n):
        if not n:
            return 0
        return 1 + max(self.height(n._left), self.height(n._right))
    
    def level_orderprint(self):
        if self._root == None:
            return 
        l = [self._root]
        while len(l) != 0:
            n = []
            print("new level")

            for i in l:
                print(i._key, ",", i._value, " ", end = '')
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            print("")
            l = n


    def balance(self, node):
        if not node:
            return None
        h = self.height(node._left) - self.height(node._right)
        if h > 1:
            lh = self.height(node._left._left) - self.height(node._left._right)
            if lh < 0:
                node._left = self.left_rotate(node._left)
            node = self.right_rotate(node)
            
            
        if h < -1:
            rh = self.height(node._right._left) - self.height(node._right._right)
            if rh > 0:
                node._right = self.right_rotate(node._right)
            node = self.left_rotate(node)
            
        return node



class PriorityQueueADT(ABC):
    @abstractmethod
    def enqueue(self, e):
        pass
    
    
    @abstractmethod
    def dequeue(self): 
        pass
     
    @abstractmethod 
    def head(self):
        pass
     
        
     
class MinPriorityQueue(PriorityQueueADT):
     
    def __init__(self):
        self._plist = []
 
         
    def enqueue(self, e):
        self._plist.append(e)
        i = len(self._plist) - 1
        p = (i - 1) // 2
        while p > 0:
            if self._plist[i] >= self._plist[p]:
                break
            self._plist[i], self._plist[p] = self._plist[p], self._plist[i]
            i = p
            p = (i - 1) // 2
            

             
            
    def getHighestPriorityElement(self):
        if len(self._plist) > 0:
            return self._plist[0]
        return None
     
        
    def dequeue(self):
        if len(self._plist) == 0:
            return None
        v = self._plist[0]
        self._plist[0] = self._plist[len(self._plist) - 1]
        self._plist.pop()
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2
        while i < len(self._plist):
            min_index = i
            if l < len(self._plist) and self._plist[l] < self._plist[min_index]:
                min_index = l
            if r < len(self._plist) and self._plist[r] < self._plist[min_index]:
                min_index = r
            if min_index == i:
                break
            self._plist[i], self._plist[min_index] = self._plist[min_index], self._plist[i]
            i = min_index
            l = 2 * i + 1
            r = 2 * i + 2
             
        return v
     
    def head(self):
        if len(self._plist >= 0):
            return self._pist[0]
        return None
    
    def print_in_order(self):
        self.print_in_order_rec(0)
         
        
    def print_in_order_rec(self, index): 
        if index >= len(self._plist):
            return
        self.print_in_order_rec(2 * index + 1)
        print(self._plist[index])
        self.print_in_order_rec(2 * index + 2)
     
     
    def get_most_left_child(self, index):
        while 2 * index + 1 < len(self._plist):
            index = 2 * index + 1
        return index
     
        
     
    class InOrderIterator: 
        def __init__(self, tree):
            self._tree = tree
            self._cur_index = self._tree.get_most_left_child(0)
            self._size = self._tree.size()
            self._count = 0
            self._isParent = False

            
            
        def __next__(self):
            if self._cur_index >= self._tree.size() or self._count >= self._size:
                raise StopIteration
             
           
            e = self._tree._plist[self._cur_index]
            self._count += 1
            
            if self._isParent:
                self._cur_index = self._tree.get_most_left_child(2 * self._cur_index + 2)
                self._isParent = False
                
            elif 2 * self._cur_index + 2 < self._size:
                self._cur_index = 2 * self._cur_index + 2


            else:
                i = self._cur_index
                p = (i - 1) // 2
                
                while p > 0 and i == 2 * p + 2:
                    i = p
                    p = (p - 1) // 2
                    self._isParent = True
                    
                self._cur_index = p
            return e 
             
                 
             
    def inorder_iterator(self):
        return MinPriorityQueue.InOrderIterator(self) 

    
    def is_empty(self):
        return len(self._plist) == 0
     
        
    def empty(self):
        pass
     
     
    def size(self):
        return len(self._plist)
        
        
        
        
        
        
