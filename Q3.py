# Write a Python program to count the number of even and odd numbers from a series of numbers.

list_number = [7,3,5,2,8,15,25]
print("Numbers are : ",list_number)
count_even = 0
count_odd = 0
for i in list_number :
    if i%2 == 0:
        count_even += 1
    else:
        count_odd += 1
i += 1
print("Count of even numbers = ",count_even)
print("Count of odd numbers = ",count_odd)