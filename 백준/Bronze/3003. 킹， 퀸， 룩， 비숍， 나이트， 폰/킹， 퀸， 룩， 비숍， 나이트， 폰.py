pieces = [1, 1, 2, 2, 2, 8]

result_pieces = []

in_picees = list(map(int, input().split()))

for i in range(6):
        sum1 = pieces[i] - in_picees[i]
        result_pieces.append(sum1)

print(*result_pieces)