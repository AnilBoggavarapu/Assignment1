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