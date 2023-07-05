class Node(object):
    
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
    
    def __init__(self, src, dest):
        self.scr= src
        self.dest = dest

    def getSource(self):
        '''
        - Return the source Node

        '''

        return self.scr
    
    def getDestination(self):
        
        '''
        - Return the destination node

        '''

        return self.dest
    
    def __str__(self):
        
        return self.scr + " ---> "+ self.dest

