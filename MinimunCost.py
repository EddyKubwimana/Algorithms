class Node(object):
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data


class circularList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.size = 0

    
    def append(self, item):
        self.size += 1
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        curr_node = self.head
        while curr_node.next:
            if curr_node.next is None:
                curr_node.next = new_node

    def appendlist(self, arr):
        for i in range(len(arr)):
            self.append(arr[i])

    def printList(self):
         arr = []
         curr= self.head
         while curr:
             arr.append(curr.data)
             curr= curr.next
         return arr
    
         



            


       
    




numbers = [1,6,9,10,11]

newList = circularList()
newList.appendlist(numbers)
print(newList.head.next)
print(newList.printList())
print(newList.size)
        



            



