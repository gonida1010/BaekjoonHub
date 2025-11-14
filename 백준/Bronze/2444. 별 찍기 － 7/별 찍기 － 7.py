n = int(input())

for i in range(n):
    for j in range(n-1-i):  # 공백이 (5-1-0)=4 => (5-1-1)=3 => (5-1-2)=2 ...
        print(' ', end='')
    for k in range(2*i+1):  # 별이 2씩 증가, (2*0+1)=1 => (2*1+1)=3 => (2*2+1)=5 ...
        print('*', end='')
    print()

for e in range(n-1):  # 밑에 별이 더 적음 (n-1) == (5-1)
    for h in range(e+1):  # 공백수 (0+1)=>(1+1)=>(2+1)...
        print(' ', end='')
    for y in range((2*n-3)-2*e):  # (2*5-3)-2*0= 7 => 7-2=5 => 7-4=3 ...
        print('*', end='')
    print()