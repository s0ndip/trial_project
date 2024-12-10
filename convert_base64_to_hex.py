import base64
import json
import re

def base64_to_hex(b64_string):
    # Decode the Base64 string
    raw_bytes = base64.b64decode(b64_string)
    # Convert to hexadecimal
    return raw_bytes.hex()

def convert_keys_in_m3u(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        match = re.search(r'#KODIPROP:inputstream.adaptive.license_key=\{.*?\}', line)
        if match:
            json_string = match.group().split('=', 1)[1]
            license_data = json.loads(json_string)
            for key_info in license_data['keys']:
                key_info['k'] = base64_to_hex(key_info['k'])
                key_info['kid'] = base64_to_hex(key_info['kid'])
            new_line = line.replace(json_string, json.dumps(license_data))
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(output_file_path, 'w') as file:
        file.writelines(new_lines)

# Usage example
convert_keys_in_m3u('input.m3u', 'output.m3u')
