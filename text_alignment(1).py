Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> width=20
>>> print 'diksha'.ljust(width,'.')
SyntaxError: invalid syntax
>>> width=20
>>> print('diksha'.ljust(width,'.'))
diksha..............
>>> width=7
>>> print('diksha'.ljust(width,'.'))
diksha.
>>> print('diksha'.rjust(width,'.'))
.diksha
>>> print('diksha'.center(width,'.'))
.diksha
>>> width=8
>>> print('diksha'.center(width,'.'))
.diksha.
>>> 