'''
Created on Mar 13, 2021

@author: mballance
'''
from hvlrpc.apidef import ApiDef

class ApiRgy(object):
    
    _inst = None
    
    def __init__(self):
        self.api_l = []
        self.api_byname_m = {}
        self.api_bytype_m = {}
        
    def add_api(self, api : ApiDef):
        self.api_l.append(api)
        self.api_byname_m[api.name] = api
        self.api_bytype_m[api.cls] = api
        
    def apis(self):
        return self.api_l
    
    def api_byname(self, name):
        if name in self.api_byname_m.keys():
            return self.api_byname_m[name]
        else:
            return None
        
    def api_bytype(self, api_t):
        if api_t in self.api_bytype_m.keys():
            return self.api_bytype_m[api_t]
        else:
            return None
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = ApiRgy()
        return cls._inst
    
    @classmethod
    def test_init(cls):
        cls._inst = None