k, d  = map(int, input().split())
l = 0
for i in range(100000,999999):
    i = str(i)
    if i[0] > i[ 1] > i[2] > i[ 3] > i[4] > i[5] and int(i) % k ==0:
            l +=1
print(l)