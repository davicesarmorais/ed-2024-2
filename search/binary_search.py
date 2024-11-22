def binary_search(target: int, nums: list) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l+r) // 2
        
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
        
    return -1


import random

lista = sorted([random.randint(-10, 10) for _ in range(10)])
targ = random.choice(lista)

print(lista)
print("Target:", targ)
print("Index:", binary_search(targ, lista))
        