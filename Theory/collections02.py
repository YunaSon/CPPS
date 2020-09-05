from collections import defaultdict, Counter

d = {
     'a' : [1, 2, 3],
     'b' : [4, 5]
     }

e ={
    'a' : {1, 2, 3},
    'b' : {4, 5}
    }

k = defaultdict(list)
k['a'].append(1)


Text = 'python is beutiful and easy'
dic = defaultdict(int)
for i in Text.split():
    dic[i] += 1

print(dic)

cnt = Counter(Text.split())
print(cnt)