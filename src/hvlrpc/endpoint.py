'''
Created on Jan 31, 2021

@author: mballance
'''
from hvlrpc.impl.registry import Registry
from hvlrpc.apidef import ApiDef

class Endpoint(object):
    
    def __init__(self, name, kind):
        
        pass

    def register_api_t(self, api):
        """Register an API supported by this endpoint"""
        pass
    
    def register_obj_t(self, obj):
        """Register an object type supported by this endpoint"""
        pass
    
    def set_method_impl(self, method_t, impl):
        """Sets the implementation of an individual method"""
        pass
        
    def set_api_impl(self, impl):
        """
        Specifies the implementation for an API of a given type
        """
        impl_t = type(impl)
        print("type: " + str(impl_t))
        print("bases: " + str(impl_t.__bases__))
        api = self._find_api_def(impl_t)
        
        print("api=" + str(api))
        
    def call_impl(self, api):
        pass
                
    def _find_api_def(self, cls_t) -> ApiDef:
        api = Registry.inst().get_api_by_cls(cls_t)
        
        if api is not None:
            return api
        else:
            for b in cls_t.__bases__:
                api = self._find_api_def(b)
                
                if api is not None:
                    return api
                
        return None