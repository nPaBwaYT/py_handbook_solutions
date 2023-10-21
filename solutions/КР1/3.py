n = int(input())
m = int(input())
d = int(input())

nums = [num for num in range(n, m + 1, d)]
nums += [num for num in range(m, n - 1, -d)]

print(*nums, sep=' - ')
