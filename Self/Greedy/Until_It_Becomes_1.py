target, action =map(int, input().split())
count = 0

while target != 1:
    if target%action == 0:
        target //= action
        count += 1
    else:
        target -= 1
        count += 1

print(count)
