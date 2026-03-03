god = {"name": "Gaurav", "age": 19}
god["age"] = 20
print(god)
print(god["name"])
print()
print(god.get("band", "Tame Impala")) # it will search for band if not found then will return tame impala as a default value
print("name" in god)
print(god.pop("name"))
print(god.popitem()) # it will remove the last item from the dictionary and return it as a tuple
print(list(god.keys())) # it will return a list of all the keys in the dictionary
print(list(god.values())) # it will return a list of all the values in the dictionary
print(list(god.items())) # it will return a list of all the key-value pairs in the dictionary as tuples
god["hobby"] = "coding"
print(god)
del god["hobby"] # it will remove the key "hobby" from the dictionary
print(god)
newgod = god.copy() # it will create a shallow copy of the dictionary
print(newgod)
