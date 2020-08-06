numbers = [3, 1, 4, 1, 5, 9, 2]
#numbers[0] -> 3
#numbers[-1] -> 2
#numbers[3] -> 1
#numbers[:-1] -> [3,1,4,1,5,9]
#numbers[3:4] -> [1]
#5 in numbers -> True
#7 in numbers -> True
#"3" in numbers  -> False
#numbers + [6, 5, 3] [3,1,4,1,5,9,2,6,5,3]
numbers[0] = 'ten'
print(numbers)
numbers[-1] = 1
print(numbers)
new_number = numbers[2:7]
for i in new_number:
    print(i)
print('9 in numbers', 9 in numbers)