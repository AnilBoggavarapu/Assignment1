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
dog = {
    "name": "Harry",
    "color": "Black",
    "breed": "Bull Dog",
    "legs": 4,
    "age": 6
}
print(dog)
print('-------------------------------')


def getlist(studentDictionary):
    mylist = []
    for key in studentDictionary.keys():
        mylist.append(key)

    return mylist


studentDictionary = [{
    "first_name": "Harry",
    "last_name": "Poster",
    "gender": "Male",
    "martial-status": "Single",
    "age": 23,
    "country": "UK",
    "City": "London",
    "Address": "3-71",
    "skills": ["Java", "JavaScript", "HTML"]
},
    {
        "first_name": "Tom",
        "last_name": "Just",
        "gender": "Male",
        "martial-status": "Single",
        "age": 23,
        "country": "UK",
        "City": "London",
        "Address": "3-71",
        "skills": ["Java", "JavaScript", "HTML"]
    }]
studentDictionary[0]['skills'].append('Css')

print("Length of dictionary:", len(studentDictionary))
print(studentDictionary)

print(getlist(studentDictionary))
print('-----------------------')
print('Q3')
print('Q4')
print('---------------------------')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(len(it_companies))
update_set = ['X', 'Y', 'Z']
it_companies.update(update_set)
print(len(it_companies))
it_companies.remove('Z')
print(len(it_companies))

# The built-in method,
# remove() in Python, removes the element from the set only if the element is present in the set,
# just as the discard() method does but If the element is not present in the set, then an error or exception is raised.

Join = A.union(B)
print(Join)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
AB = A.union(B)
print(AB)
BA = B.union(A)
print(BA)
s = A.symmetric_difference(B)

print(s)
print('----------------')
