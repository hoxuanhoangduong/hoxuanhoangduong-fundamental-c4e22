import collections

a = input("Enter something : ")
b = list(a)

data = {}
collections.Counter()

data = collections.Counter(b)

for k,v in sorted(data.items()):
    print(k,v)