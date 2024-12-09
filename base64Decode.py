import base64

# Base64 encoded string
encoded_str = "ADD BINARY STRING HERE"

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_str)

# Convert bytes to string (if the original data was a string)
decoded_str = decoded_bytes.decode('utf-8')

print(decoded_str)
