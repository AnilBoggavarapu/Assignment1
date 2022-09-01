import statistics


def average(lst):
    return sum(lst) / len(lst)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print('The given list in the sorted order:', ages)
print('The Minimum age is', min(ages))
print('The Maximum age is', max(ages))
print('The Median of the given list is', statistics.median(ages))
print('The average of the given list is', average(ages))
print('The Range for the given list is:', max(ages) - min(ages))
print('-------------------------------')