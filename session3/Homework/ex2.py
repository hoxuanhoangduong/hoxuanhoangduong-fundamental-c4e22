size = [10, 2, 3, 4, 60, 300, 42]
print("Hello, my name is Duong and these are my ships sizes")
print(size)

m = max(size)
print("Now my biggest ship has size", m, "let's shear it")

r = size.index(m)
size[r]=8
print("After shearing, here is my flock ")
print(size)

# print("One month has passed ,now here is my flock ")
# size = [x+50 for x in size]
# print(size)

for i in range(6):
    print("Month", i)
    print("One month has passed ,now here is my flock ")
    size = [x+50 for x in size]
    print(size)
    m = max(size)
    print("Now my biggest ship has size", m, "let's shear it")
    r = size.index(m)
    size[r]=8
    print("After shearing, here is my flock ")
    print(size)

total = sum(size)
print("My flock has size in total : ",total)
money = 2*total
print("I would get", total,"*2$ =", money,"$")
