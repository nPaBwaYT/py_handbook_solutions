n = int(input())
m = int(input())
max_ = -float("INF")

nums = [int(input()) for i in range(n)]

for idx in range(1, n):
    if abs(nums[idx] - nums[idx - 1]) < m:
        max_ = max(max_, nums[idx])

print(max_)
