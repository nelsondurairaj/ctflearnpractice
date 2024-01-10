# Import necessary functions from the 'Cryptodome' library.
from Cryptodome.Util.number import inverse, long_to_bytes

# Define the ciphertext 'c', modulus 'n', and public exponent 'e'.
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
e = 1

# Define the prime factors 'p' and 'q' of the modulus 'n'.
p = 416064700201658306196320137931
q = 416064700201658306196320137931

# Calculate Euler's totient function 'phi' for 'n'.
phi = (p - 1) * (q - 1)

# Calculate the private exponent 'd' using the modular multiplicative inverse of 'e' modulo 'phi'.
d = inverse(e, phi)

# Decrypt the ciphertext 'c' using the private key (n, d) and the 'pow' function.
m = pow(c, d, n)

# Convert the decrypted message 'm' from a long integer to bytes.
flag = long_to_bytes(m)

# Print the flag (decrypted message).
print(f"The flag is- {flag}")