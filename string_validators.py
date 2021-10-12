"""You are given a string .
Your task is to find out if the string  contains:
alphanumeric characters, alphabetical characters, digits,
lowercase and uppercase characters."""

s = raw_input()
print(any(i.isalnum()for i in s))
print(any(i.isalpha()for i in s))
print(any(i.isdigit()for i in s))
print(any(i.islower()for i in s))
print(any(i.isupper()for i in s))


""" any() in python returns
True is any of element of the iterable(list,tuple,dict,set etc) are true
to the condition else returns False."""
