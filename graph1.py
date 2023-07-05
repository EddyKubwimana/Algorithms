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