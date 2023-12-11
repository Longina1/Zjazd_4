import argparse

parser = argparse.ArgumentParser(description='Program reads a text file')
parser.add_argument('filename', help='File name without extension')
parser.add_argument('-m', '--mode', default='r', help='Mode - default r')
parser.add_argument('-ex', '--extension', default='txt', help='Default extnsion ".txt"')
parser.add_argument('-t', '--test')

args = parser.parse_args() # tu są przeczytane parametry
print(f'File name: {args.filename}')
print(f'Mode: {args.mode}')
print(f'Extension: {args.extension}')
print(f'Test argument: {args.test}')

#with open (args.filename, 'r') as file1:
#    content = file1.read()
#print(content)

#with open (args.filename, args.,mode) as file1:
#    content = file1.read()
#print(content)


file = args.filemame + '.' + args.extension
print(file)
with open (file, args.mode) as file1:
    content = file1.read()
print(content)
