names = ['Jeff', 'Gary', 'Jill', 'Samantha']

#for name in names:
    #print('Hello there, ' + name)
    #print(' '.join(['Hello there,', name]))

#print(', '.join(names))

import os

location_of_files = 'D:/Project/Python/Intermediate Programming'
file_name = 'Part1.py'

print(location_of_files + '/' +  file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
    
who = "Gary"
how_many = 12

print('{} bought {} apples today'.format(who,how_many))
