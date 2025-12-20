class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None :
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value :
                return False
            
            if new_node.value < temp.value:
                if temp.left == None :
                    temp.left = new_node
                    return True
                temp = temp.left

            if new_node.value > temp.value:

                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right            

    def contain(self,value):
        temp = self.root
        while temp:

            if value < temp.value :
                temp = temp.left

            elif value > temp.value :
                temp = temp.right

            else:
                return True
            
        return False
    
    def r_contain(self,value):
        return self.__r_contain(self.root,value)
    
    def __r_contain(self,current_node,value):
        if current_node == None :
            return False
        if current_node.value == value :
            return True
        if value > current_node.value :
            return self.__r_contain(current_node.right,value)
        if value < current_node.value :
            return self.__r_contain(current_node.left,value)
        
    def r_insert(self,value):
        self.__r_insert(self.root,value)

    def __r_insert(self,current_node,value):
        if current_node == None:
            current_node = Node(value)
            return True
        if current_node.value == value :
            return False

        if value > current_node.value :
            return self.__r_insert(current_node.right,value)
        if value < current_node.value :
            return self.__r_insert(current_node.left,value)