#function prints a 32bit integer in dotted decimal notation (DDN)
def printDDN(address):
    bytes = [0,0,0,0]
    bytes[0] = address >> 24 & 0xff
    bytes[1] = address >> 16 & 0xff
    bytes[2] = address >> 8 & 0xff
    bytes[3] = address & 0xff
    print(bytes[0],bytes[1],bytes[2],bytes[3],sep='.')
    
#get user input 
ipInput = input("ip/mask?") or "192.168.0.1/24"

#split address and mask
ipInputParts = ipInput.split("/")
maskInput = ipInputParts[1]

#split octets
octets = ipInputParts[0].split(".")

#check ddn length
if len(octets) != 4:
    exit()
    
#check valid mask
if int(maskInput) > 32 or int(maskInput) < 1:
    exit()
    
#convert ddn to int    
ip = int(octets[0]) << 24
ip += int(octets[1]) << 16
ip += int(octets[2]) << 8
ip += int(octets[3])

#defin a number with mask input count of ones
mask = 2**int(maskInput)-1
#shift ones to complete 32 bit 
mask = mask << (32 - int(maskInput))

#the network address is generated via bitwise and of the ip and the mask
network = ip & mask
#the broadcast address is calculated by setting all host bits to high
broadcast = ip | ~mask

#first get the decimal representation of the ip address
print(ip)
#print the ip in ddn format
printDDN(ip)
#print the subnet mask in ddn format
printDDN(mask)
#print the network address in ddn format
printDDN(network)
#print the broadcast address in ddn format
printDDN(broadcast)
#print the first host ip address
printDDN(network+1)
#print the last host ip address
printDDN(broadcast-1)
