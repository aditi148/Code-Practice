class node:
    def init(self ,data):
        self.left = none
        self.right = none
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is none:
                self.left= node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is none:
                self.right = node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent= None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.rightt is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent
    
    def children_count(self):
        count = 0
        if self.left:
            count += 1 
        if self.right:
            count +=1
        return count
    
    def delete(self, data):
        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left= None
                else:
                    parent.right = None
                del node
            else:
                self.data = None
            
        elif children_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data
                  

        else:
            #if node has 2 children
            parent = node
            successor= node.right
            
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print (self.data())
        if self.right:
            self.right.print_tree()
        

