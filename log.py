n = int(input())
a = 0
k = 0
for i in range(n):
    q = int(input())
    if q >= a and a!=0:
        k += 1
    a = q
print(k)