import socket
import commands
import pyeapi
import tools.bok
import csv

class Pyrista_Obj:

	def __init__(self, num=0):
		sw = ['sw0', 'sw1', 'sw2', 'sw3', 'sw4', 'sw5']
		name = sw[num]
		# Config for switch access filepath
		conf = 'eapi.conf'
		self.sw = sw
		self.name = name
		self.conf = conf
		pyeapi.load_config(conf)
		try:
			node = pyeapi.connect_to(sw[num])
			node.enable('show hostname')
			node.conf('hostname %s' % sw[num])
			self.node = node
		except Exception:
			print ('* Failed to connect to switch! Check config at \'/%s\' *' % conf)

	def ip_check(self):
		tcp = '' 
		arp = ''
		# Set public ip via curl
		curlCmd = 'curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\''
		public_IP = commands.getstatusoutput(curlCmd) 
		# Set local ip via socket
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("google.com",80))
		local_IP=(s.getsockname()[0])
		s.close()
		self.public_IP = str(public_IP[1])
		self.local_IP=str(local_IP)
		# Set arp and netstat tables
		arpStat = commands.getstatusoutput('arp -na')
		netStat = commands.getstatusoutput('netstat -n')
		arpList = arpStat[1].splitlines()
		arpArray = []
		for i in arpList:
			arp += i+'\n'
			arpA = arpArray.append((i.split(' ')[1], i.split(' ')[3]) )
		# +2 lines for tcp headers
		i = netStat[1].count('tcp')+2
		netStat = netStat[1].split('\n')[0:i]
		for i in netStat:
			tcp += i+'\n'
		self.arp = arp
		self.tcp = tcp
		self.arpArray = arpArray

	# Versioning switch changes
	def backup(self):
		node = self.node
		self.show_config = node.get_config('running-config')
		self.startup_config = node.get_config('startup-config')
		self.diffs = node.get_config('running-config', 'diffs')
		return self.diffs

	def list_vlan(self):
		vlans = pyeapi.api.vlans()
		vlans = vlans.getAll()
		return vlans

	# Print network tables
	def print_All(self):
		self.ip_check()
		info = ('Arp Table\n%s \n %s \nPublic IP: %s \nLocal IP: %s') % (self.arp, self.tcp, self.public_IP,self.local_IP)
		return info

	def to_csv(self,data,name):
		with open(name, 'w') as fp:
		    a = csv.writer(fp, delimiter=',')
		    data = [configs]
		    a.writerows(data)

	def make_vlanCSV(self):
		data = list_vlan()
		self.to_csv(data,'tools/vlan.csv')
		
	def view_vlans(self):
		# Makes HTML of config. Has default values at the moment.
		self.ip_check()
		x = tools.bok.Make_Site(self.local_IP, self.public_IP, self.arpArray)
		return ('Created \'/switch.html\'')

if __name__ == '__main__':
	# Pass switch number into object
	sw5 = Pyrista_Obj(5)
	print sw5.print_All()
	sw5.view_vlans()
