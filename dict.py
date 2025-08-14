dict={
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
}

print(dict)

print(dict["model"])

print(len(dict))

print(type(dict))

x = dict.copy()
print(x)

y = dict.get("brand")
print(y)

z= dict.keys()
print(z)

dict.pop("brand")
print(dict)

dict.update({ "color":"white"})
print(dict)