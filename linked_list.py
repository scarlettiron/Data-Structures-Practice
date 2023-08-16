from platform import node


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        

        
class linkedList:
    def __init__ (self):
        self.head = None
        
    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def shift(self, value, pointA, pointB):
        itr = self.head
        
        while itr:
            if self.head is None:
                return
            if itr.data == pointA:
                print(itr.data)
                newNode = Node(value, itr.next.next)
                self.head = newNode
            itr = itr.next
    
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            
        itr = self.head
        while itr:
            itr = itr.next
        itr = Node(data, None)
        
    def print_list(self):
        if self.head is None:
            return
        itr = self.head
        list = ''
        while itr:
            list += str(itr.data) + '-->'
            itr = itr.next
        print(list)
        
def build_list():
    ll = linkedList()
    for x in range(0, 20):
        ll.insert_beginning(x)
    ll.print_list()
    ll.shift(33, 1, 2)
    ll.print_list()
    
if __name__ == "__main__":
    build_list()
                  
    