from Book import Book

#  File contains both Node and Linked List classes


#  Node class
#  Represents single object in linked list
class Node:
    
    #  Constructor
    def __init__(self, data, next = None):
    
        self.data = data
        self.next = next
    
    #  To string method
    def __str__(self):
        return str(self.data)
    
    #  Returns number of items in linked list
    #  Does not work for looped lists
    def count(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.count()
        
    #  May only work with books
    def calculate_price(self):
        if self.next is None:
            return self.data.price
        return self.data.price + self.next.calculate_price()

#  Linked list object for storing nodes
class LinkedList:
    #  Constructor
    def __init__(self):
        self.head = None

    #  Adds node to the front of the linked list
    def add_to_front(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
    
    #  To string method
    def __str__(self):
        returnStr = ""
        current = self.head
        while current is not None:
            returnStr += str(current) + " "
            current = current.next
        
        return returnStr

    #  Returns node which contains the target value
    def find(self,targetVal):
        current = self.head
        while current is not None:
            if current.data == targetVal:
                return current
            current = current.next
        return None
    
    #  Creates regular list based on nodes in linked list
    def to_list(self):
        current = self.head
        regList = []
        while current is not None:
            regList.append(current)
            current = current.next
        return regList
    
    #  Finds first instance of target value in linked list, returns none if list does not contain value
    def find_first_index(self, targetVal):
        
        counter = 0
        current = self.head

        while current is not None:
            if current.data == targetVal:
                return counter
            else:
                counter += 1
                current = current.next
        
        return None

    #   Finds last index containing the targetvalue
    def find_last_index(self, targetVal):
        counter = 0
        current = self.head
        lastIndex = None

        while current is not None:
            if current.data == targetVal:
                lastIndex = counter
            counter += 1
            current = current.next
        return lastIndex
    
    #   Returns length of linked list
    def count(self):
        return self.head.count()
    
    #  Works only with books, returns total price of linked list of books
    def calc_price(self):
        return self.head.calculate_price()
    
    #  Returns new linked list based on predicate (which is lambda in driver)
    def iterative_filter(self, predicate):
        #  predicate: lambda that takes in Node object and returns True/False 

        current = self.head
        new_head = None
        newll = LinkedList()
        while current is not None:
            if predicate(current) == True:
                newll.add_to_front(current.data)

            
            current = current.next
        return newll

    #  Checks if linked list has loop
    #   Returns true when ll loops
    #   Returns False when no loop

#  Function outside of LL class
#  Takes in single node
def does_wrap(node):

    current = node
    storedNodes = set()

    while current is not None:
        if current in storedNodes:
            return True
        else:
            storedNodes.add(current)
    return False


'''
newLinkedList = LinkedList()
newLinkedList.add_to_front("A")
newLinkedList.add_to_front("C")
newLinkedList.add_to_front("B")
newLinkedList.add_to_front("A")
'''
#  print(newLinkedList.count())
'''
print(newLinkedList)

regularList = newLinkedList.to_list()
print("Regular List: ")
for value in regularList:
    print(value)

print(newLinkedList.find_last_index("A"))'''

