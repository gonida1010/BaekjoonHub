li1 = []

for i in range(1, 10):
    num = int(input())
    li1.append(num)

max_num = max(li1)
print(max_num)
print(li1.index(max_num) + 1)