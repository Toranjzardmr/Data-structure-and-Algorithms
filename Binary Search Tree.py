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
        
    def delete_node(self,value):
        self.__delete_node(self.root,value)

    def __delete_node(self,current_node,value):

        if current_node == None :
            return None
        
        if value > current_node.value :
            current_node.right = self.__delete_node(current_node.right,value)

        elif value < current_node.value :
            current_node.left = self.__delete_node(current_node.left,value)
        
        else :
            
            if current_node.right == None and current_node.left == None :
                return None
            elif current_node.right == None :
                current_node = current_node.left
            elif current_node.left == None :
                current_node = current_node.right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right,sub_tree_min)

        return current_node
    
    def min_value(self,current_node):
        while current_node.left :
            current_node = current_node.left
        return current_node.value
