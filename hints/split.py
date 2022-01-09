#read user input
cidrAddress = input("Please enter IP-Address in CIDR format ")
#split with slash character
addressParts = cidrAddress.split("/")

print(addressParts)