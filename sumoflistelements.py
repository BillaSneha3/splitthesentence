numbers = input()
numbers = numbers.split()
length = len(numbers)
sum = 0

for i in range(length):
    character = numbers[i]
    sum = sum + int(character)
print(sum)