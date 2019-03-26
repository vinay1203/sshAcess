from os import getcwd
from sys import argv, exit
import subprocess

if len(argv)!=4:
	print("Usage of the script is python3 <userName> <grant/revoke> <pubKey file of developer>")
	exit()

pwdir=getcwd()
print(pwdir)
os=open("hosts")
print("The hosts key file was read")
userName=argv[1]
method=argv[2].lower()
#pubKey=open(argv[3]).read()
pubKey=argv[3]

def grant(userName):
	count=1
	for i in os.readlines():
		print("The ", count, " host is ", i)	
		#Creating an user in remote system
		print("Creating an user in host", i)
		createuser=subprocess.Popen(["sh","scripts/createUser.sh", i, userName],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(createuser.communicate()[1])
		print("User successfully created in host", i)
			
		#Copying the key of the user 
		print("Copying the key of user", userName, " to host ",i)
		copykey=subprocess.Popen(["sh","scripts/copyKey.sh", pubKey,userName, i ],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(copykey.communicate())
		print("Key copied successfully to host ",i)

		print("granted the login permission for",userName, " to ", i)

if method=="grant":
	print("The method provided is grant")
	grant(userName)
	os.close()

if method=="revoke":
	print("The method provided is revoke")
	revoke(userName)
	os.close()
