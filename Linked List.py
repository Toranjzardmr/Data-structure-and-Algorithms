class Node:
    #constructor
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    #constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    #Print method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #Append method
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
    
    #Pop method
    def pop(self):
        if self.lenght == 0 :
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1
        if self.lenght == 0 :
            self.head = None
            self.tail = None
        return temp
    
    #Prepend method
    def prepend(self,value):
        new_node = Node(value)
        if self.lenght == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True
    
    #Pop first
    def pop_first(self):
        if self.lenght == 0 :
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.lenght -= 1
        if self.lenght == 0 :
            self.tail = None
        return temp
    
    #Get method
    def get(self,index):
        if index < 0 or index >= self.lenght :
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    #Set method
    def set_value(self,index,value):
        temp = self.get(index)
        if temp :
            temp.value = value
            return True
        return False
    
    #Insert method
    def insert(self,index,value):
        if index < 0 or index > self.lenght :
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True           

    #Remove mothod
    def remove(self,index):
        if index < 0 or index >= self.lenght :
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.lenght - 1 :
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.lenght -= 1
        return temp
    
    #Reverse method
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while (after):
            after = temp.next
            temp.next = before
            before = temp
            temp = after