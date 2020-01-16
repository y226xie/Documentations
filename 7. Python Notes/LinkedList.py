class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length :
            return -1

        counter = 0
        tmp = self.head
        while (counter < index) :
            tmp = tmp.next
            counter = counter + 1

        return tmp.val

        
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None :
            self.head = newNode
            self.tail = newNode
        else :
            newNode.next = self.head
            self.head = newNode
        self.length = self.length + 1
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode
        self.length = self.length+1
        

    def addAtIndex(self, index, val) -> None:
        if index < 0 or index > self.length: 
            return
        elif index == 0 :
            self.addAtHead(val)
            return
        elif index == self.length :
            self.addAtTail(val)
            return
        else :
            newNode = Node(val)

            prev = self.head
            counter = 0
            while (counter < index-1): 
                prev = prev.next
                counter = counter + 1
            
            newNode.next = prev.next
            prev.next = newNode
            self.length = self.length+1
            return
 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0 :
            tmp = self.head 
            self.head = tmp.next
            self.length = self.length - 1
            if self.length == 0 :
                self.tail = None
        elif index == self.length - 1 :
            self.pop()
        else :
            prev = self.head
            counter = 0
            while (counter < index-1): 
                prev = prev.next
                counter = counter + 1
            tmp = prev.next
            prev.next = tmp.next
            self.length = self.length - 1
        
    def pop(self) :
        if self.length < 0 :
            return
        tmp = self.head
        counter = 0
        while counter < self.length :
            tmp = tmp.next
            counter = counter + 1
        
        del tmp
        self.length = self.length - 1
        return 

    def print(self) :
        tmp = self.head
        counter = 0
        while counter < self.length :
            print(tmp.val)
            tmp = tmp.next
            counter = counter + 1


