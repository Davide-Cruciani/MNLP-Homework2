import json

with open('data/ita/original_ocr.json', 'r') as f:
    data = json.load(f)
    f.close()

keys = list(data.keys())

keys.sort()
with open('original.txt', 'w') as f:
    for i in keys:
        f.write(data[i])
    f.close()