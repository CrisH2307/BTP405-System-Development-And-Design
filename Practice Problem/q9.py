dictionary = [
    {
        "name": "Sean Muniz",
        "age": 24
    },
    {
        "name": "Cris Huynh",
        "age": 18
    },
    {
        "name": "Kamella Hoang",
        "age": 19
    },
    {
        "name": "Kabir Narula",
        "age": 18
    },
    {
        "name": "Sukhman Hara",
        "age": 199
    }
]

def findingOldest(obj):
    res = {}
    max_age = 0

    for each in obj:
        name = each.get("name")
        age = each.get("age")

        if age is not None and age > max_age:
            max_age = age
            res = {"name": name, "age" : age}
    return res

oldest = findingOldest(dictionary)
print("The oldest is: ", oldest["name"], "and he/she is: ", oldest["age"])