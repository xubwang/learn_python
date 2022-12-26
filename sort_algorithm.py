#### sort algorithms
## insertion sort
l = [5,7,3,1,2]
print(f'insertion sort \n'
      f'original list: {l}')
# anchor the i th figure as target, compare it repetitively with the figures to the left of it - for loop from most left
# if target is smaller, bring the left figure to right by 1 place, and continue compare - while loop
# if target is larger - stop while loop, and set the last compare position with target value
for i in range(1,len(l)):
    target = l[i]
    j = i - 1
    while target < l[j] and j >= 0:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = target
print(f'sorted list: {l}')

## bubble sort
l = [5,7,3,1,2]
print(f'insertion sort \n'
      f'original list: {l}')
# each i loop squeeze the i th largest figure to the i th right position
for i in range(len(l)-1,0,-1):
    for j in range(i):
        if l[j] > l[j+1]:
            temp = l[j+1]
            l[j+1] = l[j]
            l[j] = temp
print(f'sorted list: {l}')

## selection sort
l = [5,7,3,1,2]
print(f'insertion sort \n'
      f'original list: {l}')
# each i loop finds the i th smallest value
for i in range(len(l)-1):
    c_min = i
    for j in range(i,len(l)):
        if l[j] < l[c_min]:
            c_min = j
    temp = l[i]
    l[i] = l[c_min]
    l[c_min] = temp
print(f'sorted list: {l}')