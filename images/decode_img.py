import json, base64, sys

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

b64 = data['data'][0]['b64_json']
img_bytes = base64.b64decode(b64)

with open(sys.argv[2], 'wb') as f:
    f.write(img_bytes)

print(f"Decoded {len(img_bytes)} bytes -> {sys.argv[2]}")