'''
Created on Mar 13, 2021

@author: mballance
'''

class GeneratorRgy(object):
    """Generators register themselves here"""
    
    _inst = None
    
    def __init__(self):
        pass
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = GeneratorRgy()
        return cls._inst
    
    @classmethod
    def test_init(cls):
        cls._inst = None

