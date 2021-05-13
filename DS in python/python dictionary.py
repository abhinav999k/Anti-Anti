thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["kol"] = 18
print(thisdict["brand"])
thisdict["kol"] = 19
print(thisdict.items())

if "year" in thisdict:
    print("Yes model is there in dict")

for x in thisdict:
    print(thisdict[x])

