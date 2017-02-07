# -*- coding: utf-8 -*-

import jinja2
import os

class JsonSectionBuilder:
    def build(self, data):
        print data
        templateFolder, templateFile = os.path.split(data["template"]["file"])
        
        templateLoader = jinja2.FileSystemLoader( searchpath=templateFolder)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template( templateFile)


        obj = {}

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
        outputText = template.render( data["data"] )


        print outputText


if __name__ == "__main__":

    s=	"{\
	\"data_type\": \"json\",\
	    \"data\" :  {\"src\": \"../data/test/personal.json\"},\
	    \"template\" : \"../templates/test/personal.tex\",\
	    \"title\" : \"Datos\",\
	    \"pre-text\" : \"\",\
	    \"post-text\" : \"\"\
    }"

    j = JsonSectionBuilder()

    print     j.build(s);


    
