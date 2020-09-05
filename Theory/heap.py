import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
#print(heapq.nlargest(3, nums))
#print(heapq.nsmallest(3, nums))


portfolio = [
    {'name': 'IBM', 'shares': 100, 'prices': 91.1},
    {'name': 'AAPL', 'shares': 50, 'prices': 543.22},
    {'name': 'FB', 'shares': 200, 'prices': 21.09},
    {'name': 'HPQ', 'shares': 35, 'prices': 31.75},
    {'name': 'YHOO', 'shares': 45, 'prices': 16.35},
    {'name': 'ACME', 'shares': 75, 'prices': 115.65},   
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['prices'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['prices'])
#print(cheap)
#print(expensive)


pair = [('apple', 3, 40), ('grape', 2, 200), ('melon', 1, 300), ('tomato', 5, 20)]
total = heapq.nlargest(len(pair), pair, key=lambda x: x[1]*x[2])
#print(total)