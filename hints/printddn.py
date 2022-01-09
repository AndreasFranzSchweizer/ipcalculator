#function prints a 32bit integer in dotted decimal notation (DDN)
def printDDN(address):
    bytes = [0,0,0,0]
    bytes[0] = address >> 24 & 0xff
    bytes[1] = address >> 16 & 0xff
    bytes[2] = address >> 8 & 0xff
    bytes[3] = address & 0xff
    print(bytes[0],bytes[1],bytes[2],bytes[3],sep='.')
    
printDDN(3232235521)