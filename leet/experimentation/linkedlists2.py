class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        
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
            print(current.val, end=' -> ')
            current = current.next
        print('None')
    
    def delete(self, val):
        current = self.head
        previous = None

        while current:
            if current.val == val:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def values(self):
        list_of_values = []
        current = self.head

        while current:
            list_of_values.append(current.val)
            current = current.next
        return list_of_values
    
    def addition(linkedlist1, linkedlist2):
        linkedlist1 = LinkedList()
        linkedlist2 = LinkedList()

        unlinkedlist1 = linkedlist1.values()
        unlinkedlist2 = linkedlist2.values()

        unlinkedlist1 = int(''.join(str(x) for x in unlinkedlist1))
        unlinkedlist2 = int(''.join(str(x) for x in unlinkedlist2))

        sum = str(unlinkedlist1 + unlinkedlist2)
        result = []
        for x in sum:
            result.append(int(x))
        return result

'''
get values of data,
add them,
append to new linkedlist
'''
