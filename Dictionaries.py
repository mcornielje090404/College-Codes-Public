keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keyvalues = dict(zip(keys, values))

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary":8000,
    "city": "New york"

}

keysToRemove = ["name", "salary"]

for i in keysToRemove:
    sampleDict.pop(i)

sampleDict2 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sampleDict2["location"] =  sampleDict2.pop("city")


print(sampleDict)

print(sampleDict2)


print(keyvalues['Ten'])
