'''
Created on Jan 31, 2021

@author: mballance
'''
from hvlrpc.methoddef import MethodDef
from typing import List, Dict
from hvlrpc.apidef import ApiDef

class Registry(object):
   
    _inst = None
    
    def __init__(self):
        self.apis : List[ApiDef] = []
        self.api_m : Dict[str,ApiDef] = {}
        pass
    
    def add_api(self, api : ApiDef):
        if api.name in self.api_m.keys():
            raise Exception("Attemping to add duplicate API " + api.name)
        
        self.apis.append(api)
        self.api_m[api.name] = api
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = Registry()
        return cls._inst
    
    @classmethod
    def reset(cls):
        cls._inst = None
        