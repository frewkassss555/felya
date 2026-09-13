a = int(input())
b=0
c=0
for i in range(10,100,1):
    b=i//10 #десятки
    c=i%10 #единицы
    if b==a or c==a:
        print(i,end=' ')