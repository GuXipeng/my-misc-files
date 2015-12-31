import xml.dom.minidom
import os

class Project:
	def __init__(self,buildlist=[],projectname="",pullcode="no",compileid=""):
		self.projectname = projectname
		self.buildlist = buildlist
		self.pullcode = pullcode
		self.compileid = compileid

class BuildInstance:
	def __init__(self,buildid,nickname,makefile,serverpath,compileid):
		self.buildid=buildid
		self.nickname=nickname
		self.makefile=makefile
		self.serverpath=serverpath
		self.compileid=compileid
	def getId():
		return self.buildid
	def getNickName():
		return self.nickname

def getCode(branchname,manifestUrl,repoUrl,onlygit):
	'''Fix me: Add error handler'''
	res = 0;
	os.chdir(projectpath)
	if onlygit == "true":
		res = os.system("git clone "+manifestUrl+" -b "+branchname)
	else:
		res = os.system("repo init -u "+manifestUrl+" -b "+branchname+" --repo-url="+repoUrl)
		res = os.system("repo sync -j4")
	os.chdir(currentdir)

def parse_option(projectlist):
	global currentdir
	global projectpath
	currentdir = os.getcwd()
	workspace = os.getcwd()+"/mycode"
	document = open("option.xml","r");
	doc = xml.dom.minidom.parseString(document.read())
	compileid=''
	automakehead = doc.getElementsByTagName("automake")
	buildlist = [] 
	if automakehead[0].getAttribute("workspace").strip() != "":
		workspace = automakehead[0].getAttribute("workspace")
	if not os.path.exists(workspace):
		os.mkdir(workspace)
	for pnode in doc.getElementsByTagName("project"):
		projectname = pnode.getAttribute("name")
		pullcode = pnode.getAttribute("pullcode")
		pcompileid = pnode.getAttribute("compileid");
		buildlist = []
		for childnode in pnode.getElementsByTagName("build-instance"):
			buildid = childnode.getAttribute("buildid")
			nickname = childnode.getAttribute("nickname")
			makefile = childnode.getAttribute("makefile")
			serverpath = childnode.getAttribute("serverpath")
			compileId = childnode.getAttribute("compileid")
			if compileId > '0':
				bi = BuildInstance(buildid,nickname,makefile,serverpath,compileid)
				buildlist.append(bi)
		if len(buildlist) > 0 and pcompileid > '0':
			projectpath = workspace+"/"+projectname
			if not os.path.exists(projectpath):
				os.mkdir(projectpath)
			buildlist.sort(key=lambda bi:bi.compileid)
			project = Project(buildlist,projectname,pullcode,pcompileid)
			projectlist.append(project)
			projectlist.sort(key=lambda project:project.compileid)
		if pullcode.strip() == "yes":
			codelistdoc = open(currentdir+"/OptionModule/codelist.xml","r");
			doctemp = xml.dom.minidom.parseString(codelistdoc.read())
			for node in doctemp.getElementsByTagName("code"):
				if projectname == node.getAttribute("project"):
					branchname = node.getAttribute("branchname")
					onlygit = node.getAttribute("onlygit")
					manifestUrl = node.getAttribute("manifest-url")
					repoUrl = node.getAttribute("repo-url")
					getCode(branchname,manifestUrl,repoUrl,onlygit)
	return workspace

#test module
if __name__=="__main__":
	projectlist=[]
	parse_option(projectlist)
