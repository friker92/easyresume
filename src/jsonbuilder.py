# -*- coding: utf-8 -*-

import jinja2
import os

class JsonSectionBuilder:
    def build(self, data):
        obj = {}
        
        #lo relacionado con la plantilla
        templateFolder, templateFile = os.path.split(data["template"]["file"])
        
        templateLoader = jinja2.FileSystemLoader( searchpath=templateFolder)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template( templateFile)

        if "headers" in data["template"]["headers"]:
            obj["headers"] = data["template"]["headers"]
        else:
            obj["headers"] = ""
            
        if "packages" in data["template"]["packages"]:
            obj["packages"] = data["template"]["packages"]
        else:
            obj["packages"] = ""

            
        # mix de todo y return de lo correcto
        # sustituimos el contenido
        obj["body"] = template.render( data["data"]["data"] )

        return obj



if __name__ == "__main__":

    j = JsonSectionBuilder()

    print     j.build(s);


    
