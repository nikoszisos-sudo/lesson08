from random import randrange
N=10
numbers = {}
for i in range(1, 6+1):
    numbers[i] = 0
print(numbers)

for i in range(1, N+1):
    num = randrange(1, 6+1)
    numbers[num] += 1
print(numbers)

for i in numbers:
    percent = ((numbers[i]/N)*100)
    print ("Το νούμερο " + str(i) + " έχει ποσοστό " + str(percent) + "%")

for i in range(1, N+1):
    num = randrange(1, 6+1)
    numbers[num] += 1
print(numbers)