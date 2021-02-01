'''
Created on Jan 31, 2021

@author: mballance
'''

class ApiDef(object):
    
    def __init__(self, name, methods):
        self.name = name
        self.methods = methods
        
        for m in self.methods:
            m.parent = self
            