# -*- coding: utf-8 -*-

from parser import ParserConfig
import pprint

def getParams():
    p = {}
    p["config_file"] = "../default.json"
    return p

def getConfig(filename):
    parser =  ParserConfig()
    d = parser.parse(filename)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(d)


def main():
    params = getParams()
    getConfig(params["config_file"])



if __name__ == "__main__" :
    main()



    
