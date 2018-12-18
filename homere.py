practice
1

import re

pattern = r'w'
text1 = 'The quick brown fox jumps over the lazy dog.'
text2 = 'Python Exercises.'
res1 = re.search(pattern, text1)
res2 = re.search(pattern, text2)
if res1:
	print('Match!')
	print(res1.group())

else:
    print('Not a match')	


if res2:
    print('Match!')
    print(res2.group())
else: 
    print('Not a match!')     

-----------------------------------------------------------
2

import re 

pattern = r'^w|w$'
text1 = 'wonderful'
text2 = 'owner'
res1 = re.findall(pattern, text1)
res2 = re.findall(pattern, text2)

if res1:
	print('Not a match')
else:
    print('Match!')	

if res2:
    print('Not a match') 
else:
    print('Match')   

------------------------------------------------------------------
3

import re 

pattern = r'^42'
text1 = '23 street'
text2 = '42 meaning of life'
res1 = re.findall(pattern, text1)
res2 = re.findall(pattern, text2)

if res1:
	print('Match!')
else:
	print('Not a match!')

if res2:
	print('Match!')
else:
    print('Not a match!')	

------------------------------------------------------------------------
4

import re 


pattern1 = r'^0'
pattern2 = r'+996'
text = '0770775596'
print(text)
res = re.sub(pattern1, pattern2, text)
print(res)

------------------------------------------------------------------
5

import re

pattern = r'ilovepython'
text = 'localhost:8888/ilovepython'
m = re.search(pattern,text)
print(m.group())

------------------------------------------------------------------
homework

1

import re


pattern1 = r' '
pattern2 = r''
text = 'Python  Exercises'
res = re.sub(pattern1, pattern2, text)
print(res)

--------------------------------------------------------------------
2

import re

def validate():
    while True:
        password = input('Enter a password: ')
        if len(password) < 8:
            print('Make sure your password is at lest 8 letters')
        elif re.search('[$%!@#^&]', password) is None:
            print('Make sure your password has a number in it')    
        elif re.search('[0-9]', password) is None:
            print('Make sure your password has a number in it')
        elif re.search('[A-Z]', password) is None: 
            print('Make sure your password has a capital letter in it')
        else:
            print('Your password seems fine')
            break

validate()



