
# design a linkedlist

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
     
     def __init__(self):
         self.head = None
         self.tail = None

    # add node to the list

     def append(self,value):
         
         '''
         - Take a value
         - append it to the linkedList
         - Takes a O(n) time 
         '''
         node = Node(value)
         if self.head == None:
             self.head = node
             self.tail =node
             return 
         cur_node = self.head

         while cur_node:
             
             if cur_node.next == None:
                 cur_node.next = node
                 self.tail = node
                 return
             cur_node = cur_node.next

     def elements(self):
         array = []

         cur_node= self.head
         
         while cur_node:
             array.append(cur_node.value)
             cur_node = cur_node.next
         return array


array = LinkedList()
array.append(10)
array.append(20)
array.append(30)
print(array.elements())
                 



             
    
    
        