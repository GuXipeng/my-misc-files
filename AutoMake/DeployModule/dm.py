#!/usr/bin/python
#coding: utf-8  
import smtplib
import pickle
from email.mime.text import MIMEText  
from email.header import Header
import os 
#from OptionModule import getEmailOption
currentDir=os.getcwd()

def emailMsg(receiver,subject,text):
	print os.getcwd()
	emailoption={}
	emailoption = getEmailOption()
	msg=MIMEText(text,'text','utf-8')
	msg['Subject'] = Header(subject,'utf-8')
	smtp=smtplib.SMTP()
	smtp.connect(emailoption['server'])
	smtp.login(emailoption['username'],emailoption['password'])
	smtp.sendmail(emailoption['sender'],receiver,msg.as_string())
	smtp.quit()

def getEmailOption():
	try:
		with open(currentDir+"/DeployModule/"+"email.config",'r') as efile:
			emailoption=pickle.load(efile)
			return emailoption
	except IOError as err:
		print str(err)

def dumpEmailConfig():
	config={}
	config['server'] = raw_input("Email server: ")
	config['username'] = raw_input("Email server username:")
	config['password'] = raw_input("Email server password:")
	config['sender'] = raw_input("Email address:")
	with open("email.config","wb") as efile:
		pickle.dump(config,efile)

if __name__=="__main__":
	dumpEmailConfig()
#emailMsg('xinbo.wu@sim.com','python test','Hello Python!');

