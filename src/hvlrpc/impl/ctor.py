'''
Created on Jan 31, 2021

@author: mballance
'''
from hvlrpc.methoddef import MethodDef
from hvlrpc.paramdef import ParamDef
from hvlrpc.impl.registry import Registry
from hvlrpc.apidef import ApiDef

class Ctor(object):

    _inst = None
    _supported_types = set()
    
    def __init__(self):
        # Methods collected to be 
        self.methods = []
        pass
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = Ctor()
        return cls._inst
    
    @classmethod
    def reset(cls):
        cls._inst = None
        
    def add_method(
            self,
            T,
            is_import,
            is_task):
        fi = T.__code__
        

        rtype = None
        params = []        
        if fi.co_argcount > 0:
            if hasattr(T, "__annotations__"):
                if is_task and "return" in T.__annotations__.keys():
                    raise Exception("Cannot specify a return type for a task")
                elif not is_task and hasattr(T.__annotations__, "return"):
                    rtype = T.__annotations__["return"]
                    
                for pname in fi.co_varnames[1:fi.co_argcount]:
                    if pname in T.__annotations__.keys():
                        ptype = T.__annotations__[pname]
                        # TODO: validate type
                        print("pname: " + pname + " " + str(ptype))
                        params.append(ParamDef(pname, ptype))
                    else:
                        raise Exception("Type for parameter " + pname + " unspecified")
            else:
                raise Exception("No annotations")
            
        m = MethodDef(None, T.__name__, is_import, is_task, rtype, params)
        self.methods.append(m)
        pass
    
    def add_api(self, T, is_static):
        methods = self.methods
        self.methods.clear()
        api = ApiDef(T.__name__, methods)
        Registry.inst().add_api(api)
        pass
    
    