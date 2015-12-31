from OptionModule.om import parse_option
from CompileModule.cm import do_compile
from ExceptionModule.em import catchEm
import os

buildlist=[]
projectlist=[]
if __name__=="__main__":
	workspace = parse_option(projectlist)
	os.putenv("PYTHONPATH",os.getcwd())
	for pl in projectlist:
		for bi in pl.buildlist:
			if catchEm(do_compile(workspace+"/"+pl.projectname+"/"+bi.makefile,bi.buildid+" "+bi.nickname+" "+bi.serverpath),bi) > 0:
				print "Error reported, quit the job!"
				continue
			
