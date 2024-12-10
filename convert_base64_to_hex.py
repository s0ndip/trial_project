import base64
import re

# Function to convert Base64 to Hexadecimal
def base64_to_hex(base64_key):
    # Add padding if necessary
    padding = len(base64_key) % 4
    if padding != 0:
        base64_key += "=" * (4 - padding)  # Add required padding

    # Decode the Base64 string to bytes
    decoded_bytes = base64.b64decode(base64_key)
    # Convert the bytes to hexadecimal
    hex_key = decoded_bytes.hex()
    return hex_key

# Path to input and output M3U files
input_m3u_file = 'input.m3u'  # Change to your input M3U file path
output_m3u_file = 'output.m3u'  # Output M3U file path

# Read the content of the input M3U file
with open(input_m3u_file, 'r') as file:
    m3u_content = file.read()

# Regular expression to match the Base64 keys in the license_key field
base64_regex = r'"k":"(.*?)"'

# Find all Base64 keys in the M3U content
base64_keys = re.findall(base64_regex, m3u_content)

# Convert Base64 keys to hexadecimal
hex_keys = [base64_to_hex(key) for key in base64_keys]

# Replace the Base64 keys with hexadecimal ones in the license_key section
updated_m3u_content = m3u_content
for base64_key, hex_key in zip(base64_keys, hex_keys):
    updated_m3u_content = updated_m3u_content.replace(base64_key, hex_key)

# Replace the license_key URL with the new format including the hexadecimal keys
for i, (base64_key, hex_key) in enumerate(zip(base64_keys, hex_keys)):
    updated_m3u_content = updated_m3u_content.replace(
        f'{{ "keys":[ {{ "kty":"oct", "k":"{base64_key}", "kid":"{base64_key}" }} ], "type":"temporary" }}',
        f'#KODIPROP:inputstream.adaptive.license_key=https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid={hex_key}&key={hex_key}'
    )

# Write the updated content to the output M3U file
with open(output_m3u_file, 'w') as file:
    file.write(updated_m3u_content)

print(f"Updated M3U content has been written to '{output_m3u_file}'")
