import base64

# Open the input.txt file and output.txt file
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read each line from input.txt
    for line in infile:
        # Remove any leading/trailing whitespace and quotes
        base64_line = line.strip().replace('"', '')
        
        if base64_line:  # Skip empty lines
            # Decode the Base64 data
            decoded_data = base64.b64decode(base64_line)
            
            # Convert decoded data to hexadecimal
            hex_data = decoded_data.hex()
            
            # Write the hexadecimal data to output.txt, enclosed in quotes
            outfile.write(f'"{hex_data}"\n')

print("Conversion complete. Hex data written to output.txt")
