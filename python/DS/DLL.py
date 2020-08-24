class DLLnode:
        val = None
        prev = None
        next = None
        def __init__(self, val=None, prev=None, next=None):
            self.val = val; self.prev = prev; self.next = next

class DLL:            
    head = None
    def append(self, val):
        new_node = DLLnode(val)
        if self.head == None:
            self.head = new_node
            return None
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    

    def remove(self, key):
        if self.head == None:
            return False
        if self.head.val == key:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            return True
        temp = self.head
        while(temp.next != None):
            if temp.next.val == key:
                temp.next = temp.next.next
                if temp.next != None:
                    temp.next.prev = temp
                    return True
            temp = temp.next
        return False

    def sendToLast(self, key):
        if self.remove(key):
            self.append(key)
            return True
        return False
    
    def removeHead(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        return temp.val

    def getHead(self):
        return self.head.val if self.head != None else None

d = DLL()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.remove(1)
d.sendToLast(2)
d.remove(3)
d.remove(4)
d.remove(2)
print(d.getHead())