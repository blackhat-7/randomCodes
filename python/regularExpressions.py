import re

my_string = '''

123-456-7983
800-123-123
900-123-123
901-243-683

Mr. Abc
Mr Asad
Ms Asdas
Mrs. Gdcx
Mr. H

iuwendsjkn@gmail.com
ene923e-@yahoo.edu

'''

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z0-9]+)\.(com|net|edu)', re.I)
matches = pattern.findall(my_string)

for match in matches:
    print(match)
