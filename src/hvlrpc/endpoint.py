'''
Created on Jan 31, 2021

@author: mballance
'''
from hvlrpc.packer import Packer

class Endpoint(object):
    
    def __init__(self): #, name, kind):
        self.api_impl_m = {}
        pass
    
    async def init(self):
        """Waits for initialization to complete"""
        pass

    def get_api_impl(self, api_t):
        """Obtains a singleton API implementation"""
        if api_t in self.api_impl_m.keys():
            return self.api_impl_m[api_t]
        else:
            return None
        
    def set_api_impl(self, api_t, impl):
        """
        Specifies the implementation for an API of a given type
        """
        self.api_impl_m[api_t] = impl
#        impl_t = type(impl)
#        print("type: " + str(impl_t))
#        print("bases: " + str(impl_t.__bases__))
#        api = self._find_api_def(impl_t)
#        
#        print("api=" + str(api))
        
    def create_packer(self) -> Packer:
        raise NotImplementedError("Class " + str(self) + " does not implement create_packer")
        
    # Need the ability to track instances?
    # - Create instance
    # - Delete instance
    # - Call instance method
        
    def call_func(self, method_t, args : Packer):
        """Invokes a function, given the method and argument pack"""
        raise NotImplementedError("Class " + str(self) + " does not implement call_func")
        pass
    
    async def call_task(self, method):
        """Invokes a task, given the method and argument pack"""
        pass
                
    def _find_api_def(self, cls_t) -> 'ApiDef':
#         api = Registry.inst().get_api_by_cls(cls_t)
#         
#         if api is not None:
#             return api
#         else:
#             for b in cls_t.__bases__:
#                 api = self._find_api_def(b)
#                 
#                 if api is not None:
#                     return api
                
        return None
    
