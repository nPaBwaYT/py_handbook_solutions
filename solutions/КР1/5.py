min_ = float('INF')

for n in range(int(input())):
    s = 0
    count = 0
    while (st := input()) != 'end':
        s += int(st)
        count += 1
    average = round(s / count, 2)

    min_ = min(min_, average)

print(f'{min_ :.2f}')
