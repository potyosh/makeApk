import sys
import subprocess
from xml.dom.minidom import parse, parseString

class Svnmods:
	def __init__(self, remote_url):
		self.remote_url = remote_url

	def getSvnRevNum(self):
		cmd = 'svn info --xml ' + self.remote_url
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout_data, stderr_data = p.communicate()
		#parse XML
		svn_info_dom = parseString(stdout_data)
		commit_element = svn_info_dom.getElementsByTagName('commit')[0]
		commit_revision = commit_element.getAttribute('revision')
		return commit_revision
