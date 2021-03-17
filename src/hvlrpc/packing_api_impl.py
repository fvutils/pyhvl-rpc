'''
Created on Mar 16, 2021

@author: mballance
'''
from hvlrpc.api_rgy import ApiRgy

class PackingApiImpl(object):
    
    @classmethod
    def create(cls, api_t, ep):
        apidef = ApiRgy.inst().api_bytype(api_t)

        ret = cls()
       
        class pack_f(object):
            def __init__(self, m):
                self.m = m
                
            def __call__(self, *args):
                print("__call__: " + str(args))
                
        class pack_t(object):
            def __init__(self, m):
                self.m = m
                
            async def __call__(self, *args):
                print("__call__: " + str(args))
            
        
        for m in apidef.methods:
            if m.is_task:
                setattr(ret, m.name, pack_t(m))
            else:
                setattr(ret, m.name, pack_f(m))
        
        return ret