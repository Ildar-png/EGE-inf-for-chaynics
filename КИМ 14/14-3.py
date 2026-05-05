s = abs(3 * 5**1984 - 7 * 25**777 - 11 * 125**666 - 404)
a = []
while s > 0:
    a.append(s % 5)
    s//=5
print(a.count(2))
