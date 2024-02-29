from typing import List


base_tower = [8,7,6,5,4,3,2,1]
second_tower = []
third_tower = []

    
# move_four(base_tower, second_tower, third_tower)


count = 0
def full_rearrange(current:list, next:list, free:list, n:int) -> tuple[list, list, list]:
    current = current[:]
    next = next[:]
    free = free[:]
    global count
    if n == 1:
        next.append(current.pop())
        print(f'{current, next, free=}')
        count += 1
    else:
        current, free, next = full_rearrange(current, free, next, n-1)
        current, next, free = full_rearrange(current, next, free, 1)
        free, next, current = full_rearrange(free, next, current, n-1)
    return current, next, free

current, next, free = full_rearrange(base_tower, second_tower, third_tower, 8)
print(f'{current, next, free, count=}')
print(f'{base_tower, second_tower, third_tower=}')