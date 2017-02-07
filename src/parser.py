# -*- coding: utf-8 -*-

import json
import pprint
import os
from jsoncomment import JsonComment

class ParserConfig:
    """ Parser of config files """

    def parse(self,filecfg):
        result = {}
        try:
            configuration = open(filecfg,'r')
            parser = JsonComment(json)
            obj = parser.load(configuration,"utf-8")
            result = self.openObj(obj)
            configuration.close()
        except IOError as e:
            print e
            exit
        except Exception as e:
            print "Error al parsear el fichero:", filecfg
            print e
        return result 

    def openObj(self,data):
        if isinstance(data,dict):
            result = {}
            if ("src" in data):
                pth = os.getcwd() + "/../" + data["src"]
                result = self.parse(pth)
                
            for key in data :
                if key != "src":
                    result[key] = self.openObj(data[key])
        elif isinstance(data,list):
            result = []
            for item in data:
                result.append(self.openObj(item))
        else:
            result = data
        return result




def main():
    parser =  ParserConfig()
    d = parser.parse("../default.json")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(d)
    


if __name__ == "__main__" :
    main()
