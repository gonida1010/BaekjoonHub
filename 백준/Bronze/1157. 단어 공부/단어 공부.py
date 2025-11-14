a = input().upper()

counts = [0] * 26

for char in a:
    index = ord(char) - ord('A')
    counts[index] += 1

max_a = max(counts)
max_a_count = counts.count(max_a)

if max_a_count > 1:
    print('?')
else:
    print(chr(counts.index(max_a) + ord('A')))