#function prints a 32bit integer in dotted decimal notation (DDN)
def printDDN(address):
    bytes = [0,0,0,0]
    bytes[0] = address >> 24 & 0xff
    bytes[1] = address >> 16 & 0xff
    bytes[2] = address >> 8 & 0xff
    bytes[3] = address & 0xff
    print(bytes[0],bytes[1],bytes[2],bytes[3],sep='.')
    
ip = 3232235521
mask = 0b11111111111111111111111100000000
#the complement inverts all ones to zero and all zeros to one
inverseMask = ~mask
#now we do a or conjunction with the inverse mask so all zeros in the mask
#do not change the ip, but every one bit in the inverse mask sets the ip bits to one.
broadcast = ip | inverseMask

printDDN(ip)
printDDN(broadcast)