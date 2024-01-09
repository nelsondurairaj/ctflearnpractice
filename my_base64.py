import base64
base_64 = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
decode_bytes = base64.b64decode(base_64)
print(decode_bytes.decode('utf-8'))