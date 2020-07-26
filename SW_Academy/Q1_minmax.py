T = int(input())

for idx in range(1, T+1):
    N = int(input())
    test_list = list(map(int, input().split()))
    
    test_max = max(test_list)
    test_min = min(test_list)
    
    print(f"#{idx} ", test_max-test_min)
