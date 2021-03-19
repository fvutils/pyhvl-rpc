'''
Created on Jan 31, 2021

@author: mballance
'''
from hvlrpc.packer import Packer
from hvlrpc.api_rgy import ApiRgy

class Endpoint(object):
    
    def __init__(self): #, name, kind):
        self.api_impl_m = {}
        self.exp_api_m = {}
        pass
    
    async def init(self):
        """Waits for initialization to complete"""
        pass
    
    def register_export_api(self, api_t):
        """Registers an export API as being recognized by this endpoint.
        Typically done by the launching environment
        """
        apidef = ApiRgy.inst().api_bytype(api_t)
        if apidef in self.exp_api_m.keys():
            raise Exception("Api \"" + str(api_t) + "\" is already registered")
        self.exp_api_m[apidef] = None
    
    def set_export_impl(self, api_t, impl=None):
        """Sets the class implementing an export API. Almost always set by the user"""
        apidef = ApiRgy.inst().api_bytype(api_t)
        if apidef not in self.exp_api_m.keys():
            raise Exception("Api \"" + str(api_t) + "\" is not supported")
        pass
    
    def get_export_api_impl(self, api_t):
        pass
    
    def get_method_impl(self, m : 'MethodDef'):
        if m.parent not in self.exp_api_m:
            raise Exception("API " + str(m.parent.cls) + " not supported")
        
        impl = self.exp_api_m[m.parent]

        if impl is None:
            impl = m.parent.cls()
            self.exp_api_m[m.parent] = impl
            
        return getattr(impl, m.name)

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
    
