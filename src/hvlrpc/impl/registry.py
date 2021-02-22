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
        self.name_api_m : Dict[str,ApiDef] = {}
        self.cls_api_m : Dict[type,ApiDef] = {}
        pass
    
    def add_api(self, api : ApiDef):
        if api.name in self.name_api_m.keys():
            raise Exception("Attemping to add duplicate API " + api.name)
        
        self.apis.append(api)
        self.name_api_m[api.name] = api
        self.cls_api_m[api.cls] = api
        
        print("add_api: " + str(api.cls))
        
    def get_api_by_cls(self, cls):
        print("get_api_by_cls: " + str(cls))
        if cls in self.cls_api_m.keys():
            return self.cls_api_m[cls]
        else:
            return None
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = Registry()
        return cls._inst
    
    @classmethod
    def reset(cls):
        cls._inst = None
        