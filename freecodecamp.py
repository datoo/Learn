a = 'tl'
print(a)
b = str.maketrans({'t': 'c', 'l': 'b'})
c = a.translate(b)
print(c)