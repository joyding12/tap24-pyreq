#Collections in Python

a = [1,2,"Three",4]
b = {
    "id" : 1234
}

print(a, type(a))
print(b, type(b))

#Access patterns for the data types
#    0 1 2       3
a = [1,2,"Three",4]

print("ELement 1: ",a[0])
print("Element Last: ",a[-1], a[3])

print("Slice a list: ",a[1:3], type(a[1:3]))

print("-" * 10)

for el in a:
    print(el)
