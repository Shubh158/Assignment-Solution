Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##1
>>> ##2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 6==6
True
>>> a = 20; a+= 30; a% = 3:
	
SyntaxError: invalid syntax
>>> a = 20; a+= 30; a%= 3:
	
SyntaxError: invalid syntax
>>> a = 20; a+= 30; a% = 3;
SyntaxError: invalid syntax
>>> a = 20; a+= 30; a%= 3;
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7>4) or (18==3)) and (9>3)
True
>>> True is False
False
>>> False in False
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    False in False
TypeError: argument of type 'bool' is not iterable
>>> ###3
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> s1 + s2
'Nice to have ithere'
>>> s1 +  s2
'Nice to have ithere'
>>> s1+{''}+s2
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1+{''}+s2
TypeError: can only concatenate str (not "set") to str
>>> s1 + '' + s2
'Nice to have ithere'
>>> s1 + ' ' + s2
'Nice to have it here'
>>> print(s1 + ' ' + s2)
Nice to have it here
>>> ###4
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> ###5
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a += [s1]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it']
>>> a += [s2]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it', 'here']
>>> print([s1] + a + [s2])
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it', 'here', 'here']
>>> ###6
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1 - color_list_2
{'White', 'Black'}
>>> ###8
>>> eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number: ')))
Enter the number: 5
615
>>> ###9
>>> Sentence1 = without,hello,bag,world
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    Sentence1 = without,hello,bag,world
NameError: name 'without' is not defined
>>> Sentence =  'without,hello,bag,output'
>>> Sentence[0]
'w'
>>> Sentence = ['without'],['hello'],['bag'],['world']
>>> Sentence[0]
['without']
>>> Sentence.sort())
SyntaxError: invalid syntax
>>> Sentence.sort()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Sentence.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> Sentence
(['without'], ['hello'], ['bag'], ['world'])
>>> Sentence = ['without','hello','bag','world']
>>> sen.sort()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sen.sort()
NameError: name 'sen' is not defined
>>> Sentence.sort()
>>> print(Sentence)
['bag', 'hello', 'without', 'world']
>>> d =  {‘Student’: [‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’]
      
SyntaxError: invalid character in identifier
>>>  {‘Student’:[‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’],
  
SyntaxError: unexpected indent
>>> d =  {‘Student’:[‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’]
      
SyntaxError: invalid character in identifier
>>> d = {'Student':['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
>>> max(d['Marks'])
87
>>> max(d['Marks']['Student'])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    max(d['Marks']['Student'])
TypeError: list indices must be integers or slices, not str
>>> max(d['Marks']['Student'])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    max(d['Marks']['Student'])
TypeError: list indices must be integers or slices, not str
>>> ##7
>>>  o = input('Write any sentence')
 
SyntaxError: unexpected indent
>>> o = input('Write any sentence')
Write any sentence My name is Shubham
>>> 
