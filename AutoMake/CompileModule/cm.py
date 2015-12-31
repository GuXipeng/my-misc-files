import os

def do_compile(makefile,cmdlist=""):
	mlist = makefile.split("/")
	mlen = len(mlist)
	for i in range(0,2*mlen-1):
		if i%2:
			mlist.insert(i,"/")
	makefile_path="".join(mlist[0:len(mlist)-1])
	print "Entering path:+++++"+makefile_path
	os.chdir(makefile_path)
	return os.system(makefile+' '+cmdlist) >> 8

#test module
if __name__=="__main__":
	do_compile("/home/liushuo/workspace/titanLSR/titan.sh","xxx yyy zzz")
