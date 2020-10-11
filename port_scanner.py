import socket

socket.timeout(5)
s = socket.socket()
ip_address = input("Enter the website or IP address to scan: ")
ip_address = socket.gethostbyname(ip_address)
open_ports = 0
print("Scanning %s..." % ip_address)
for port in range(20, 81):
	try:
		s.connect((ip_address, port))
		print("port %s is open." % port)
		open_ports += 1
	except:
		print("port %s is closed." % port)
s.close()
print("\nScan complete.\n%s ports open on %s" % (open_ports, ip_address))
