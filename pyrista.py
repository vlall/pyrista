import socket
import commands
import pyeapi


class Pyrista_Obj:
	
	def __init__(self):
		sw = ['sw0', 'sw1', 'sw2', 'sw3', 'sw4', 'sw5']
		conf = 'eapi.conf'
		pyeapi.load_config(conf)
		node = pyeapi.connect_to(sw[0])
		node.enable('show hostname')
		node.conf('hostname %s' % sw[0])
		self.conf = conf
		self.sw = sw

	def macAddress(self):
		connection = pyeapi.connect(host='192.168.1.16')
		output = connection.execute(['enable', 'show version'])
		self.mac = output['result'][1]['systemMacAddress']

	def ip_check(self):
		# get public via curl
		public_IP = commands.getstatusoutput('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\'') 
		# get Local via socket
		self.tcp = '' 
		self.arp = ''
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("gmail.com",80))
		local_IP=(s.getsockname()[0])
		s.close()
		self.public_IP = public_IP[1]
		self.local_IP=str(local_IP)
		arpStat=commands.getstatusoutput('arp -na')
		netStat=commands.getstatusoutput('netstat -n')
		for i in arpStat[1].splitlines():
			self.arp += i+'\n'
		# Add 2, for the table's labels
		i = netStat[1].count('tcp')+2
		netStat = netStat[1].split('\n')[0:i]
		for i in netStat:
			self.tcp += i+'\n'

	def backup(self, switchList):
		self.show_config = node.get_config('running-config')
		self.startup_config = node.get_config('startup-config')
		self.diffs = node.get_config('running-config', 'diffs')
		print self.diffs

	def list_vlan(self):
		vlans = pyeapi.api.vlans()
		vlans = vlans.getAll()

	def print_All(self):
		info = ('Arp Table\n%s \n %s \n Public IP: %s \nLocal IP: %s')% (self.arp, self.tcp, self.public_IP,self.local_IP)
		return info

if __name__ == '__main__':
	network = Pyrista_Obj()
	network.ip_check()
	print network.show_all()
