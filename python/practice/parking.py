def whereCanIPark(spots, vehicle):
    for i in spots[:][:]:
        if vehicle == 'regular' and i == 'R':
            print(i) 


print(whereCanIPark(
  [
    # COLUMNS ARE Y
    # 0    1    2    3    4    5
    ['s', 's', 's', 'S', 'R', 'M'], # 0 ROWS ARE X
    ['s', 'M', 's', 'S', 'r', 'M'], # 1
    ['s', 'M', 's', 'S', 'r', 'm'], # 2
    ['S', 'r', 's', 'm', 'r', 'M'], # 3
    ['S', 'r', 's', 'm', 'r', 'M'], # 4
    ['S', 'r', 'S', 'M', 'M', 'S']  # 5
  ],
  'regular'
))

print(whereCanIPark(
  [
    ['M', 'M', 'M', 'M'],
    ['M', 's', 'M', 'M'],
    ['M', 'M', 'M', 'M'],
    ['M', 'M', 'r', 'M']
  ],
  'small'
))

print(whereCanIPark(
  [
    ['s', 's', 's', 's', 's', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['S', 'r', 's', 'm', 'r', 's'],
    ['S', 'r', 's', 'm', 'R', 's'],
    ['S', 'r', 'S', 'M', 'm', 'S']
  ],
  'motorcycle'
))