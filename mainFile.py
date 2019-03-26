from os import getcwd
from sys import argv, exit
import subprocess

if len(argv)<3 or len(argv)>4:
	print("Usage of the script is python3 <userName> <grant/revoke> <pubKey file of developer>")
	exit()

pwdir=getcwd()
print("The current working directory is ",pwdir)
userName=argv[1]
method=argv[2].lower()

def grant(userName):
	count=1
	opf=open("hosts")
	print("The hosts key file was read")
	for i in opf.readlines():
		print(count, ". host is ", i)	
		#Creating an user in remote system
		print("Creating an user in host", i)
		createuser=subprocess.Popen(["sh","scripts/createUser.sh", i, userName],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(createuser.communicate())
		print("User ", userName, " successfully created in host", i)
			
		#Copying the key of the user 
		print("Copying the key of user", userName, " to host ",i)
		copykey=subprocess.Popen(["sh","scripts/copyKey.sh", pubKey,userName, i ],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(copykey.communicate())
		print("Key of the user ",i," copied successfully to host ",i)

		print("granted the login permission for",userName, " to ", i)
		count+=1
	opf.close()

def revoke(userName):
	count=1	
	opf=open("hosts")
	for i in opf.readlines(): 
		print(count, ". host is ", i)	
		#Deleting the user in remote host
		deleteuser=subprocess.Popen(["sh","scripts/deleteUser.sh", i, userName], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(deleteuser.communicate())
		print("User", userName, " was successfully deleted from the host ", i)
		count+=1
	opf.close()

if method=="grant":
	print("The method provided is grant")
	pubKey=argv[3]
	grant(userName)

if method=="revoke":
	print("The method provided is revoke")
	revoke(userName)
