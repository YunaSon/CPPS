from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt, type(cnt))
print(sorted(cnt.elements()))
print(cnt.most_common())
print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)


Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

