p = input()
# [::] 슬라이싱 사용하여 if문으로 구현
if p[::] == p[::-1]:
    print(1)
else:
    print(0)