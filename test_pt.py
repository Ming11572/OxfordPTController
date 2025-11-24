import pyvisa

rm = pyvisa.ResourceManager()

ips = rm.open_resource("TCPIP0::192.168.1.50::7020::SOCKET")
ips.read_termination = '\n'
