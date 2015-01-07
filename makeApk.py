import sys
import subprocess
import config as conf
from svnmods import Svnmods

#Functions
def execCommand(argCmd):
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout_data, stderr__data = p.communicate()
	return stderr__data

#Main Program
#Trim BOM From .java File
cmd = conf.FIND_PATH+" "+conf.PROJECT_ROOT+" -type f -name \"*.java\" -exec "+conf.NKF_PATH+" -w --overwrite {} \;"
print execCommand(cmd)

#PROJECT1 Build
cmd = conf.ANDROID_PATH+" update project -p "+conf.PROJECT_ROOT+"/"+conf.PROJECT1
print execCommand(cmd)

cmd = conf.ANT_PATH+" clean debug -f "+conf.PROJECT_ROOT+"/"+conf.PROJECT1+"/"+"build.xml"
print execCommand(cmd)

#PROJECT2 Build
cmd = conf.ANDROID_PATH+" update project -p "+conf.PROJECT_ROOT+"/"+conf.PROJECT2
print execCommand(cmd)

cmd = conf.ANT_PATH+" clean debug -f "+conf.PROJECT_ROOT+"/"+conf.PROJECT2+"/"+"build.xml"
print execCommand(cmd)

#PROJECT3 Build
cmd = conf.ANDROID_PATH+" update project -p "+conf.PROJECT_ROOT+"/"+conf.PROJECT3
print execCommand(cmd)

cmd = conf.ANT_PATH+" clean debug -f "+conf.PROJECT_ROOT+"/"+conf.PROJECT3+"/"+"build.xml"
print execCommand(cmd)

#Copy and Filename Change
svnModule = Svnmods(conf.SVN_REPOSITORY)
svnRevNum = svnModule.getSvnRevNum()
copyPath = conf.PROJECT_ROOT+"/"+conf.PROJECT3+"/"+"bin"+"/"
cmd = "cp "+copyPath+"testapp.apk"+" "+copyPath+"2015"+conf.PRODUCT+"_Ver1_0_0_Rev"+str(svnRevNum)+".apk"
execCommand(cmd)


