
from Book import Book
from Node_LL import Node
from Node_LL import LinkedList

ll = LinkedList()
ll.add_to_front(Book("City of Glass", False))
ll.add_to_front(Book("The Way of Kings", True))
ll.add_to_front(Book("Intro to Linear Algebra", False))
ll.add_to_front(Book("Fire", True))
ll.add_to_front(Book("Water", True))

paperback = lambda node: True if node.data.is_paperback else False

new_ll = ll.iterative_filter(paperback)
print(new_ll)

current = new_ll.head
reglist = []
while current is not None:
    reglist.append(current.data)
    
    current = current.next

for object in reglist:
    print(object.title)

#  Function outside of LL class
#  Takes in single node
def does_wrap(node):
    #  Initializes set
    setofnodes = set()

    while node is not None:

        if node in setofnodes:
            return True

        #  Node gets added to set if it is not already in set
        #  Not adding data of node, but node object itself to tell if we encounter the same node object twice
        setofnodes.add(node)

        node = node.next

    #  Returns false
    return False


newLL = LinkedList()

tail = Node("D", None)
middle2 = Node("C", tail)
middle1 = Node("B", middle2)
head = Node("A", middle1)
tail.next = head

print("Loop, Should be true: " + str(does_wrap(head)))

tail_good = Node("D", None)
m1 = Node("C", tail_good)
m2=Node("B", m1)
head_good= Node("A", m2)

print()
print("No Loop, Should be False: " + str(does_wrap(head_good)))
#  should return False
