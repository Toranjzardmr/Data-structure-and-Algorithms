class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0 :
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0 :
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp
    
class Queue:

    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.lenght = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.lenght == 0 :
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        return True
    
    def dequeue(self):
        if self.lenght == 0 :
            return None
        temp = self.first
        if self.lenght == 1 :
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.lenght -= 1
        return temp