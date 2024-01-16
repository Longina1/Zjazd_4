import argparse

parser = argparse.ArgumentParser(description='Program reading a text file')

parser.add_argument('filename', help='File name without extension')
parser.add_argument('-m', '--mode', default='r', help='Mode; default: "r"')
parser.add_argument('-ex', '--extension', default='txt', help='Extension; default: "txt"')

args = parser.parse_args()
print(f'File name: {args.filename}')
print(f'Mode: {args.mode}')
print(f'Extension: {args.extension}')

with open (args.filename + '.' + args.extension, args.mode) as file1:
    content = file1.read()

print(content)