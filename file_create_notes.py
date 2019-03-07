# write a program to prompt the user for a python file and comments out all the lines of the file

from sys import exit
filename = input('Please enter a python filename: ')
if not filename.endswith('.py'):
    print('Error: bad filename')
    print('         {} does not end with ".py"'.format(filename))
    exit()

print('Reading file ({}) contents.....'.format(filename))
with open(filename) as f:
    lines = f.read().split('\n')

# build a new list of commented out code
commented_out_code = []
for line in lines:
    if line.startswith('#') or line = '':
        commented_out_code.append(line)
    else:
        commented_out_code.append('#' + line)

printing('Writing to file: {}'.format(filename))

with open(filename, 'w') as f:
    f.write('\n'.join(commented_out_code))

        
