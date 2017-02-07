# -*- coding: utf-8 -*-
        
import pprint
import os
from parser import ParserConfig
from jsonbuilder import JsonSectionBuilder

import jinja2

class TemplateBuilder:

    def build(self, data):
        # parsea los datos propios de la plantilla
        #[...]

        # cargamos la plantilla desde disco
        templateFolder, templateFile = os.path.split(data["template"])
        
        templateLoader = jinja2.FileSystemLoader( searchpath=templateFolder)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template( templateFile)

        body=""
        headers=""
        packages=set()
        
        #parsea cada seccion
        for i in data["sort"]:
            sect = self.buildSection(data["items"][i])
            body += sect["body"]
            headers += sect["head"]
            packages = packages.union(sect["packages"])

        data["body"] = body
        data["headers"] = headers
        data["packages"] = list(packages)


        
        # sustituimos el contenido
        outputText = template.render( data )
        print outputText

    def buildSection(self, data):
        obj = {}
        obj["body"] = ""
        obj["head"] =""
        obj["packages"] = []


        # de momento, suponemos que existe el campo data_type
        if data["data"]["type"] == "bib":
            return obj
            pass
        elif data["data"]["type"] == "json":
            j = JsonSectionBuilder()
            return j.build(data)
        elif data["data"]["type"] == "plain":
            return obj
            pass



def main():
    parser =  ParserConfig()
    d = parser.parse("../config/test/main.json")

    t = TemplateBuilder()
    t.build(d)

    
if __name__ == "__main__":
    main()


    
exit
