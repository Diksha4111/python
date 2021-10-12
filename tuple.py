from builtins import hash
n = int(input())
integer_list = map(int, input().split())
print(list(integer_list))
t=tuple(list(integer_list))
print(hash(t))
