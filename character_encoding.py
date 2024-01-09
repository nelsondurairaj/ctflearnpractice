encoded_data = ["41", "42", "43", "54", "46",  "7B",  "34",  "35",  "43",  "31",  "31",  "5F",  "31",  "35",  "5F",  "55",  "35",  "33",  "46",  "55",  "4C",  "7D"]
for i in range(len(encoded_data)):
    print(chr(int(encoded_data[i], 16)),end="")

#alternative easy
hex_string = input("enter a hex string: ")
text_string = bytes.fromhex(hex_string).decode('utf-8')
print(text_string)
