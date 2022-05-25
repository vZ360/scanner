
from cgitb import text
import socket
from termcolor import colored
import terminal_banner

banner_text = colored("[*] This is simple Port Scanner.\n [*]Created by vishnu",'yellow')

mybnr= terminal_banner.Banner(banner_text)
print(mybnr)

def scan(targets,ports):
	print('\n' + 'Starting Scan For ' +str(targets))
	for port in range(1,ports):
		scan_port(targets,port)

def scan_port(ipaddress,port):
	try:
		sock = socket.socket()	
		sock.connect((ipaddress,port))
		print(colored(f"[+] Open Port",'green')+' '+str(port))
		sock.close()
	except:
		print(colored(f"[-] Port Closed",'red')+' '+str(port))
targets =input(colored("[*] Enter Target to Scan(Split them by ','):",'yellow'))
ports =int(input(colored("[*] Enter How many Ports You want to Scan ",'yellow' )))
if ',' in targets:
	print("[*] Scanning Multiple Target")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets,ports)
		
