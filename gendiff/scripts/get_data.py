import json
import os

def get_data(file_path):
    absolute_path = os.path.abspath(file_path)

    with open(absolute_path,'r') as f:
        return json.load(f)
    

data1 = get_data('tests/fixtures/file1.json')
data2 = get_data('tests/fixtures/file2.json')

print("Data first file:", data1)
print("Data second file", data2)