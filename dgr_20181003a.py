Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=12
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12, '__name__': '__main__', '__doc__': None}
>>> y=14
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x=100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x1q3z9ocd=35.0
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x1q3z9afd = 12.50
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x1q3p9afd=x1q3z9ocd*x1q3z9afd
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 2, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=x+2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 4, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=3.9*x*(1-x)
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': -46.8, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=0,6
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': (0, 6), 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=3.9*x*(1_x)
SyntaxError: invalid syntax
>>> x=3,9*x*(1-x)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x=3,9*x*(1-x)
TypeError: unsupported operand type(s) for -: 'int' and 'tuple'
>>> x=0.6
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 0.6, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=3.9*x*(1-x)
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 0.9359999999999999, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=0.936
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 0.936, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=3.9*x*(1-x)
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 0.23362559999999982, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> xx=2
>>> xx=xx+@
SyntaxError: invalid syntax
>>> print(yy)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(yy)
NameError: name 'yy' is not defined
>>> x=2
>>> xx=xx+2
>>> print(xx)
4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'xx': 4, 'x1q3p9afd': 437.5, 'x': 2, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> yy=440*12
>>> print(yy)
5280
>>> zz+yy/1000

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    zz+yy/1000
NameError: name 'zz' is not defined
>>> zz=yy/1000
>>> primt(zz)

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    primt(zz)
NameError: name 'primt' is not defined
>>> print(zz)
5
>>> zz=yy/1000
>>> print(zz)
5
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x=1+2*3-4/5**6
>>> vars()
{'jj': 23, 'zz': 5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'yy': 5280, 'x1q3z9afd': 12.5, 'xx': 4, 'kk': 3, 'x1q3p9afd': 437.5, 'x': 7, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=1+2*33/4*5
>>> print(x)
81
>>> x=1+2**3/4*5
>>> print(x)
11
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> class'int'>
SyntaxError: invalid syntax
>>> f=float (i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print (10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> print 11.0/2.0)
SyntaxError: invalid syntax
>>> print(10.00/2)
5.0
>>> print(99.0/100.0)
0.99
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+2)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(sval+2)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='heloo bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'heloo bob'
>>> nam=input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print('Welcome',nam)
NameError: name 'nam' is not defined
>>> nam=input('Liana')
Liana

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    nam=input('Liana')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('Welcome',nam)
NameError: name 'nam' is not defined
>>> eee= 'hello'+'there'
>>> eee=eee+1

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    eee=eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello'°
     
SyntaxError: invalid syntax
>>> 
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> 5/4.
1.25
>>> 5/4
1
>>> inp=input('Ēurope floor?')
Ēurope floor?

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    inp=input('Ēurope floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf=int(inp)+1

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    usf=int(inp)+1
NameError: name 'inp' is not defined
>>> print('ŪS floor',usf)

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print('ŪS floor',usf)
NameError: name 'usf' is not defined
>>> 


