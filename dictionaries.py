mydict = dict(name = "Exo", age =27, city = "Harare")
mydict["emal"] = "pearsonmanhuruexo@gmail.com"
value = mydict["name"]
print(mydict)
print(value)

for key, elements in mydict.items():
    print(key, elements)

"""
del mydict["emal"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)





try:
    print(mydict["name"])
    print(mydict["lastname"])
except:
    print("Error")
    
"""