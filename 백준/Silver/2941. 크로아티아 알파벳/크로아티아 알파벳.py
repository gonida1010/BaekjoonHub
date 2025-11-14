n = input()

# 크로아티아 문자를 저장하기
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 문자들을 순회하면서 ap에 있는 문자는 '*'로 replace 해줌
for ap in croatian:
    n = n.replace(ap, '*')
# 남은 문자열의 길이는 크로아티아 문자의 총 개수가 된다.
print(len(n))