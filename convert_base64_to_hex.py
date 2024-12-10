import base64

# Read the Base64 encoded data from input.txt
with open('input.txt', 'r') as infile:
    base64_data = infile.read().replace("\n", "")  # Remove any newline characters

# Decode the Base64 data
decoded_data = base64.b64decode(base64_data)

# Convert decoded data to hexadecimal
hex_data = decoded_data.hex()

# Write the hexadecimal output to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(hex_data)

print("Conversion complete. Hex data written to output.txt")
