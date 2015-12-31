import os
import sys
import xml.dom.minidom

listname = []
def gen_option(codelist):
	with open(codelist,"r") as document:
		doc = xml.dom.minidom.parseString(document.read())
	mdoc = xml.dom.minidom.Document()
	automake = mdoc.createElement("automake")
	automake.setAttribute("version","1.0")
	automake.setAttribute("workspace","")
	mdoc.appendChild(automake)

	for node in doc.getElementsByTagName("code"):
		listname.append(node.getAttribute("project"))
		project = mdoc.createElement("project")
		project.setAttribute("name",node.getAttribute("project"))
		project.setAttribute("pullcode","no")
		project.setAttribute("compileid","")
		makefilelist = node.getAttribute("makefile").split('|')
		for mkname in makefilelist:
			buildInstance = mdoc.createElement("build-instance")
			buildInstance.setAttribute("buildid","")
			buildInstance.setAttribute("nickname","")
			buildInstance.setAttribute("makefile",mkname)
			buildInstance.setAttribute("serverpath","")
			buildInstance.setAttribute("compileid","")
			project.appendChild(buildInstance)
		automake.appendChild(project)
	with open("option.xml","w") as f:
		f.write(mdoc.toprettyxml())
		f.close()
	document.close()

if __name__=="__main__":
	if len(sys.argv) != 2:
		print "Error!\n"+"useage:python mkoption.py codelist.xml"
		sys.exit()
	gen_option(sys.argv[1])
