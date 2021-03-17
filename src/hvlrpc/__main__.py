'''
Created on Feb 7, 2021

@author: mballance
'''

import pkg_resources
import argparse
from hvlrpc.cmds import generate

def getparser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    subparser.required=True
    subparser.dest='command'
    
    generate_cmd = subparser.add_parser("generate")
    generate_cmd.set_defaults(func=generate.cmd)
    generate_cmd.add_argument("-m", "--module", dest="modules",
            help="Specify modules to load", action="append")
    
    return parser
    
def load_extensions():
    """Loads entry-point extensions"""
    for ep in pkg_resources.iter_entry_points('hvlrpc.generators'):
        a = ep.load()
    pass


def main():
    
    parser = getparser()
    
    args = parser.parse_args()
    
    # Before running the command, load extensions
    load_extensions()
    
    args.func(args)
    

if __name__ == "__main__":
    main()
    