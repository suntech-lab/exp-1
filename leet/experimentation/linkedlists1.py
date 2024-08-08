class Node: #the element in the list. it has data and next. data is the data, next points to the next node.
    def __init__(self, data): #initialise data, do not initialise next
        self.data = data #data has been defined
        self.next = None #set next as None for nodes at the end of the list. or it does not point to anything yet.

class LinkedList: #the list. contains and directs the nodes.
    def __init__(self): #initialises itself
        self.head = None #head is None because there is nothing in the list yet. its the first node.
    
    def append(self, data): #make append method for linked lists
        new_node = Node(data) #the soon-to-be-appended item is called new_node and is the data of the node
        if self.head is None: #if there is no element in the linked list
            self.head = new_node #make the head of the list (currently None) the new_node
        else: #if there is something in the linked list
            last = self.head #the last node is set to the head of the list. tells LinkedList where to start.
            while last.next: #if there is a node after the head (.next is for iterator objects)
                last = last.next #the last node is changed to the node after it if there is one
            last.next = new_node #once the loop has no more 'last's to follow, the next node is set to new_node

    def print_linked_list(self): #print method to show how the nodes are linked for LinkedList
        current = self.head #the current 'iteration' is the first node's data of the LinkedList
        while current: #while there is a current node
            print(current.data, end=' -> ') #print the node's data and a 'tail'(' -> ')
            current = current.next #start operating on the next node
        print('None') #once at the end of the list, the last node has its 'tail' pointed to 'None'. no next node.
    
    def values(self):
        list_of_values = []
        current = self.head

        while current:
            list_of_values.append(current.data)
            current = current.next
        return list_of_values
    
    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

"""
Next challenge:
Complete Leetcode q2
"""

llist = LinkedList()
llist.append('skibidi')
llist.append('dopdopdop')
llist.append('sigma')
llist.append('yesyesyes')
llist.print_linked_list()
llist.delete('skibidi')
llist.delete('dopdopdop')
llist.delete('sigma')
llist.delete('yesyesyes')
llist.print_linked_list()
