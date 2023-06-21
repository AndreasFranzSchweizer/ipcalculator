#function prints a 32bit integer in dotted decimal notation (DDN)
def get_ddn_string(address):
    bytes = [0,0,0,0]
    bytes[0] = address >> 24 & 0xff
    bytes[1] = address >> 16 & 0xff
    bytes[2] = address >> 8 & 0xff
    bytes[3] = address & 0xff
    return ".".join(str(item) for item in bytes)
    

def get_user_input():
    #get user input 
    userInput = input("ip/mask?") or "192.168.0.1/24"
    #split address and mask
    userInputParts = userInput.split("/")
    ipInput = userInputParts[0]
    maskInput = int(userInputParts[1])

    return ipInput, maskInput

def get_int_from_ip(ddn_string):
    #split octets
    octets = ddn_string.split(".")

    #check ddn length
    if len(octets) != 4:
        exit()

    #convert ddn to int    
    ip = int(octets[0]) << 24
    ip += int(octets[1]) << 16
    ip += int(octets[2]) << 8
    ip += int(octets[3])

    return ip
    

def generate_subnet_mask(size):
    #check valid mask
    if size > 32 or size < 1:
        exit()
    #defin a number with mask input count of ones
    mask = 2**int(size)-1
    #shift ones to complete 32 bit 
    mask = mask << (32 - size)

    return mask


ip, subnet_size = get_user_input()
ip = get_int_from_ip(ip)
mask = generate_subnet_mask(subnet_size)

#the network address is generated via bitwise and of the ip and the mask
network = ip & mask
#the broadcast address is calculated by setting all host bits to high
broadcast = ip | ~mask

#first get the decimal representation of the ip address
print(f"IP Address decimal representation: {ip}")
print(f"IP DDN format: {get_ddn_string(ip)}")
print(f"Subnet mask DDN format: {get_ddn_string(mask)}")
print(f"Network address DDN format: {get_ddn_string(network)}")
print(f"Broadcast address DDN format: {get_ddn_string(broadcast)}")
print(f"First host address DDN format: {get_ddn_string(network+1)}")
print(f"Last host address DDN format: {get_ddn_string(broadcast-1)}")
