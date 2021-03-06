# -*- coding: utf-8 -*-

import sys
import codecs
from parser import ParserConfig
from templateBuilder import TemplateBuilder
import pprint
sys.stdout=codecs.getwriter('utf-8')(sys.stdout)

def getParams():
    p = {}
    p["config_file"] = "../default_moderncv.json"
    return p

def getConfig(filename):
    parser =  ParserConfig()
    d = parser.parse(filename)
    return d
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(d)


def main():
    params = getParams()
    d = getConfig(params["config_file"])

    t = TemplateBuilder()
    t.build(d["template_config"])



if __name__ == "__main__" :
    main()



    
