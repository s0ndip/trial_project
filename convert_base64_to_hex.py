import base64

def base64_to_hex(b64_string):
    # Decode the Base64 string
    raw_bytes = base64.b64decode(b64_string)
    # Convert to hexadecimal
    return raw_bytes.hex()

def convert_keys_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        base64_keys = input_file.readlines()

    with open(output_file_path, 'w') as output_file:
        for key in base64_keys:
            key = key.strip()
            if key:  # Skip empty lines
                hex_key = base64_to_hex(key)
                output_file.write(f"{hex_key}\n")

# Usage example
convert_keys_file('input.txt', 'output.m3u')
