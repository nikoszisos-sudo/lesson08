from random import randrange

numbers = {}
for i in range(1, 6+1):
    numbers[i] = 0
print(numbers)

for i in range(1, 30+1):
    num = randrange(1, 6+1)
    numbers[num] += 1
print(numbers)
