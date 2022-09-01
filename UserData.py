# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    kilo_grams = int(input()) * 0.453592

    lst.append(kilo_grams)  # adding the element

print(lst)