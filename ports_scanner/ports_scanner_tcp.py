import socket
import sys

remoteServerIP = input("Enter a remote host to scan: ")

try:
	for port in range(1,5000):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print("Port {}:      Open".format(port))
		sock.close()

except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()

