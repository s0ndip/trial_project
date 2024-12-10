import base64

# Function to ensure correct Base64 padding
def add_padding(base64_string):
    # Add padding if necessary
    padding = len(base64_string) % 4
    if padding != 0:
        base64_string += '=' * (4 - padding)
    return base64_string

# Open the input.txt file and output.txt file
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read each line from input.txt
    for line in infile:
        # Remove any leading/trailing whitespace and quotes
        base64_line = line.strip().replace('"', '')
        
        if base64_line:  # Skip empty lines
            # Ensure correct Base64 padding
            base64_line = add_padding(base64_line)
            
            try:
                # Decode the Base64 data
                decoded_data = base64.b64decode(base64_line)
                
                # Convert decoded data to hexadecimal
                hex_data = decoded_data.hex()
                
                # Write the hexadecimal data to output.txt, enclosed in quotes
                outfile.write(f'"{hex_data}"\n')
            except Exception as e:
                print(f"Error decoding Base64 string: {base64_line}")
                print(f"Error message: {e}")

print("Conversion complete. Hex data written to output.txt")
