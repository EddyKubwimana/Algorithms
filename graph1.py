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


     def childrenOf(self,node):
         ''' 
         - Return the list of destination that you can access  through the node

         '''
         try:
             return self.edges[node]
         except:
             raise KeyError("The location does not exist in the system")
     
     def hasNode(self, node):
         '''
         - Return True if the node exist in the system
         - Return False if the node does not exist
         '''
         return node in self.edges
     
     def getNode(self, name):
         '''
         - Return the node given a name of it
         
         '''
         for n in self.edges:
             if n.getName()== name:
                 return n
             raise NameError(name)

     def __str__(self):
         result = ""
         for src in self.edges:
             
             for dest in  self.edges[src]:
                 
                 result = result+ src.getName()+ "--------------->"+ dest.getName() + "\n"
    
         return result




         
         
         

    



    #.......................................Testing ....................................#
node1 = Node("Shombo")
node2 = Node("Buhiga")
node3 = Node("Bugenyuzi")
connection1 = Edge(node1, node2)
connection2 = Edge(node1, node3)


graph = Digraph()
graph.addNode(node1)
graph.addNode(node2)
graph.addNode(node3)
graph.addEdge(connection1)
graph.addEdge(connection2)
print(graph)
print(graph.hasNode(node1))

