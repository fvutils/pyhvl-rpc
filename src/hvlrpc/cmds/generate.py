'''
Created on Mar 13, 2021

@author: mballance
'''
import importlib


def cmd(args):
    if hasattr(args,"modules") and args.modules is not None:
        for m in args.modules:
            try:
                importlib.load_module(m)

            print("m: " + str(m))
    pass