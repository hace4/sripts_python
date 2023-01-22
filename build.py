n_kamen = int(input())
right_amount_kamen = int(input())
limit_money = int(input())
money_kamen=[]
all_comb = []
for i in range(n_kamen):
    money_kamen.append(int(input()))
for j in range(len(money_kamen)):
    for i in range(len(money_kamen)):
        a = money_kamen[j] + money_kamen[i]
        if a <= limit_money:
             all_comb.append(a)
        
if max(all_comb) <= limit_money:
    print(max(all_comb))
else:
    print(0)