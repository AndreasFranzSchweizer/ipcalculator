ipDDN = "192.168.0.1"
octets = ipDDN.split(".")
#convert ddn to int    
ip = int(octets[0]) << 24
ip += int(octets[1]) << 16
ip += int(octets[2]) << 8
ip += int(octets[3])

print(ip)