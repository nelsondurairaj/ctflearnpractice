import sys

# Read two files as byte arrays
file1_b = bytearray(open(sys.argv[1], 'rb').read())
file2_b = bytearray(open(sys.argv[2], 'rb').read())

# Set the length to be the smaller one
size = len(file1_b) if len(file1_b) < len(file2_b) else len(file2_b)
xord_byte_array = bytearray(size)






#using pwn tool
# XOR between the files
for i in range(size):
	xord_byte_array[i] = file1_b[i] ^ file2_b[i]

# Write the XORd bytes to the output file	
open(sys.argv[3], 'wb').write(xord_byte_array)

print("[*] %s XOR %s\n[*] Saved to \033[1;33m%s\033[1;m."%(sys.argv[1], sys.argv[2], sys.argv[3]))

from pwn import xor

# Open the first file ('CTFLearn.pdf') in binary mode and read its content
with open('CTFLearn.pdf', 'rb') as file1:
    var1 = file1.read()

# Open the second file ('CTFLearn.txt') in binary mode and read its content
with open('CTFLearn.txt', 'rb') as file2:
    var2 = file2.read()

# Perform XOR operation on the contents of the two files
flag = xor(var1, var2)

# Write the result to a new file ('result') in binary mode
with open('result', 'wb') as result:
    result.write(flag)


