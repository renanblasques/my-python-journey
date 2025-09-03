a = int(input())
b = int(input())
c = int(input())
triangle = True

if (a <= 0) or (b <= 0) or (c <= 0):
    triangle = False

if (a >= b + c) or (b >= a + c) or (c >= a + b):
    triangle = False

print(triangle)