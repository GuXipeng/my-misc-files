from DeployModule.dm import emailMsg
import os


def catchEm(error_no,bi):
	if error_no == 0:
		emailMsg("shuo.liu@sim.com",bi.nickname+" Building completed!","Please check it!");
		return 0
	if error_no == 100:
		emailMsg("shuo.liu@sim.com",bi.nickname+" Error","repo sync error!");
	if error_no == 101:
		emailMsg("shuo.liu@sim.com",bi.nickname+" Error","make update-api error!");
	if error_no == 102:
		emailMsg("shuo.liu@sim.com",bi.nickname+" Error","make error!");
	if error_no == 103:
		pass
	return 1



if __name__=="__main__":
	print os.getcwd()
	for i in range(4):
		catchEm(100+i,bi)
