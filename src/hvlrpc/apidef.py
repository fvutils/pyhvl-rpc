'''
Created on Jan 31, 2021

@author: mballance
'''
from endpoint_mgr import EndpointMgr

class ApiDef(object):
    
    def __init__(self, name, cls, is_imp, methods):
        self.name = name
        self.cls = cls
        self.is_imp = is_imp
        self.methods = methods

        # Default import instance        
        self.default_imp_inst = None
        
        for m in self.methods:
            m.parent = self
            
    def get_imp_inst(self):
        """Returns the global singleton instance of this API"""
        print("get_imp_inst")
        if self.default_imp_inst is None:
            eng_l = EndpointMgr.inst().find_implementing_endpoints(self.cls)
            
            if len(eng_l) == 0:
                raise Exception("Failed to find an endpoint with API \"" + 
                                self.cls.__name__ + "\"")
            elif len(eng_l) != 1:
                raise Exception("Multiple endpoints implement API \"" + 
                                self.cls.__name__ + "\"")
            else:
                self.default_imp_inst = eng_l[0].get_api_impl(self.cls)
                
            if self.default_imp_inst is None:
                # Stub this out so we don't error out over and over
                self.default_imp_inst = self.cls()
                raise Exception("Failed to find an endpoint with API \"" + 
                                self.cls.__name__ + "\"")
                #
                
        return self.default_imp_inst
            