class Node(object):
    '''
     - Create a name object for a place
    '''
    
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        ''' 
        - Return the name of the object

        '''
        return self.name
    
    def __str__(self):
        ''' 
        - Return the name of of the object
        
        '''
        return self.name
    

class Edge(object):
    '''
    - Create a Edge object representing two places : Source and Destination
    '''
    
    def  __init__ (self, src, dest):
        self.src= src
        self.dest = dest

    def getSource(self):
        '''
        - Return the source Node
        '''

        return self.src
    
    def getDestination(self):
        
        '''
        - Return the destination node
        '''
        return self.dest
    
    def __str__(self):
        
        return self.src.getName()+ " ---> "+ self.dest.getName()
    

class Digraph(Object):

    



    #.......................................Testing ....................................#
start = Node("Shombo")
end = Node("Buhiga")
connection = Edge(start, end)
    
print(connection)

