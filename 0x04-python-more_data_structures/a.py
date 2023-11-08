#!/usr/bin/python3

a = [1,2,2,34,44]
print(a)
for i in range(len(a)):
    if a[i] == 1:
        a[i] = 8

b = [a = 2 for i in range(len(a)) if a[i] == 1]
