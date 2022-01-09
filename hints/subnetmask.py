maskInput = 24
#defin a number with mask input count of ones
mask = 2**maskInput-1
#shift ones to complete 32 bit 
mask = mask << (32 - maskInput)

#output the value
print(mask)

#not needed but for better understanding the value
print("{0:b}".format(mask))