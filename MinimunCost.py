class Node(object):
    def __init__(self,data):
        self.next = None
        self.data = data


class circularList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

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
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(5)

print(newList.printList())
        



            



