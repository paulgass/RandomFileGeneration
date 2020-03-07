import json
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

dictionary = ["apple", "bananas", "pear", "watermelon", "tomato", "potato", "orange", "egg", "toast", "bread", "meat",
              "pork", "chicken", "steak", "onion", "eggplant", "pea", "beet", "grape", "lettuce", "salad", "strawberry",
              "raspberry", "blueberry", "blackberry", "pepper", "salt", "pasta", "rice", "carrot"]

def generateJSON(n):
    a = []
    for b in range(0, n):
        j = {}
        j.update({"_id": "%i" % b})
        j.update({"_name": "%s" % (dictionary[random.randint(0, (len(dictionary) - 1))])})
        j.update({"_age": "%i" % (random.randint(1,122))})
        a.append(j)

    return a

z = generateJSON(random.randint(1,20))
w = json.dumps(z)
u = json.dumps(z, indent=1)

print("1stJSON")
print(z)
print("2ndJSON")
print(w)
print("3rdJSON")
print(u)
