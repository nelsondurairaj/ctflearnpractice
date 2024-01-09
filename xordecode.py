cipher = "q{vpln'bH_varHuebcrqxetrHOXEj"

for key in range(256):
    attempt = ''.join([chr(ord(char) ^ key) for char in cipher])
    print("flag is {}".format(attempt))