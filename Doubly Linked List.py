class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def print_list(self):

        temp = self.head
        while temp :
            print(temp.value)
            temp = temp.next


    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.lenght += 1
        return True
    
    def pop(self):
        if self.lenght == 0 :
            return None
        
        temp = self.tail
        if self.lenght == 1 :
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.lenght -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.lenght == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True
    
    def pop_first(self):
        if self.lenght == 0 :
            return None
        temp = self.head
        if self.lenght == 1 :
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.lenght -= 1
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.lenght:
            return None
        if index < self.lenght/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.lenght -1 , index , -1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.lenght += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.lenght:
            return None
        if index == self.lenght - 1 :
            return self.pop()
        if index == 0 :
            return self.pop_first()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None

        self.lenght -= 1
        return temp