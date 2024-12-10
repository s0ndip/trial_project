import base64

# List of Base64 keys
base64_keys = [
    "8/hCxUzJbLvQvLlqTLioEw",
    "oJiJbSsRxfOQapk8O6XGEA",
]

# Decode each key and convert to hexadecimal
hex_keys = []
for base64_key in base64_keys:
    try:
        # Decode from Base64 to bytes
        decoded_bytes = base64.b64decode(base64_key)
        # Convert bytes to hexadecimal
        hex_key = decoded_bytes.hex()
        hex_keys.append(hex_key)
        print(f"Base64 Key: {base64_key} -> Hex Key: {hex_key}")
    except Exception as e:
        print(f"Error decoding key '{base64_key}': {e}")

# Optional: Use the list of hex keys further
print("\nAll Hex Keys:", hex_keys)
