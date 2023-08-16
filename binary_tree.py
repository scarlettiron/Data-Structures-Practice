
#a tree is a hierarchy data structure instead a linear data structure such as list, array 
#and linked lists

#a tree is a recursive data structure

class treeNode:
    def __init__(self, data):
        self.data = data
        #stores instances of treeNode
        self.children = []
        #instance of parent node in tree
        self.parent = None
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        return self
    
    def get_level(self):
        level = 0 
        p = self.parent
        while(p):
            p = p.parent
            level += 1
        return level
            
    
    def print_tree(self):
        level = self.get_level()
        prefix = "." * level
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

class linkedTreeNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 
        
    def add_data(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

#All elements lesser go to the left
#All elements greater go to the right
class binarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarySearchTree(data)
                
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binarySearchTree(data)       
    
    #in order means always checking left first
    def tree_order(self):
        elements = []
        if self.left:
            elements += self.left.tree_order()
            
        
        elements.append(self.data)
            
        if self.right:
            elements += self.right.tree_order()
        
        return elements
            
    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data and self.left:
            self.left.search(value)
        elif value > self.data and self.right:
            self.right.search(value)
        return False
    
def build_product_tree():
    root = treeNode('electronics')
    laptop = treeNode('laptop')
    root.addChild(laptop)
    root.print_tree()
    
def build_binary_tree(elements):
    root = binarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
    

if __name__ == "__main__":
    elements = [1,5,8,7,10,23,4,6,7,5]
    
    root = build_binary_tree(elements)
    
    print(root.tree_order())
    
    print(root.search(1))
    
    
    
    