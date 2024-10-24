numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = 4
length = len(numbers)
sum_ = sum(numbers[:a]) + sum(numbers[a+1:])
average = sum_/length
numbers[a] = average
print("Измененный список:", numbers)
