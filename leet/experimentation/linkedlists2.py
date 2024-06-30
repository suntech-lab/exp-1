class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_linked_list(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

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

'''
get values of data,
add them,
append to new linkedlist
'''
