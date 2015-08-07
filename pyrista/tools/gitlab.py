import socket
import commands

class Version_Ctrl:
	def __init__(self):
		#if sc == None:
		self.status = commands.getstatusoutput('git status')[1]
		self.changes = 'Untracked files' in self.status
		self.commit = commands.getstatusoutput('git add .')[1]
		# git commit -m 'your message here'
		# git push 
if __name__ == '__main__':
	x = Version_Ctrl()
	print x.changes

