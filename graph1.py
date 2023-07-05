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
    

class Digraph(object):
     '''
     - Create a place and its associated places
     '''

     def __init__(self):
         self.edges = {}

     
     def addNode(self, node):
         ''' 
         - Add a place in the graph

         '''
         if node in self.edges:
             raise ValueError("Duplicate Node")
         else:
             self.edges[node]=[]


     def addEdge(self, edge):
         '''
         - Add a edge between two areas
         '''
         src = edge.getSource()
         dest = edge.getDestination()

         if not ( src in self.edges and dest in self.edges):
             raise ValueError("The node does not exists in edge")
         else:
             self.edges[src].append(dest)




         
         
         

    



    #.......................................Testing ....................................#
start = Node("Shombo")
end = Node("Buhiga")
connection = Edge(start, end)
    
print(connection)

