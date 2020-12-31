# #2 (The number of Test Cases)
# #5 (T: turnaround time)
# #3 2 (NA(A->B), NB(B->A))
# #NA 09:00 12:00 3hrs
# #NA 10:00 13:00 3hrs
# #NA 11:00 12:30 1.5hrs
# #NB 12:02 15:00 3hrs
# #NB 09:00 10:30 1.5hr
# #2
# #2 0
# #NA 09:00 09:01 1min
# #NA 12:00 12:02 2min

# #return "Case#x: A->B 차 대수, B->A차 대수"
# # Case#1: 2 2


# def answer():
#     T = int(input())
#     NA, NB = map(int, input().split())
#     trips = []
#     for i in range(NA+NB)
    

# def compute():
#     t = input()
#     na, nb = map(int, input().split())

#     trips = []
#     for i in range(na+nb):
#     	tt1, tt2 = input().split()
# 	    t1 = 60*int(tt1[0:2]) + int(tt1[3:5])
# 	    t2 = 60*int(tt2[0:2]) + int(tt2[3:5])
#     	if i < na:
# 	        stat = 0
# 	    else:
# 	        stat = 1
#     	trips.append([t1,t2,stat])
#     trips.sort()

#     trains = []
#     act = 0
#     bct = 0
#     for x in trips:
#     	assigned = 0
# 	    ck = 0
# 	    for iy in range(len(trains)):
# 	        y = trains[iy]
# 	        if y[2] != x[2] and x[0] >= y[1] + t:
# 		        trains[iy] = x
# 		        assigned = 1
# 		        break
#     	if assigned == 0:
# 	        trains.append(x)
# 	        if x[2] == 0:
# 		    act += 1
# 	        else:
# 		        bct +=1
    
#     return "%d %d" % (act, bct)

# for i in range(input()):
#     print "Case #%d: %s" % (i+1, compute())


# def compute():

#     def rep(prefix, q, can, prev):
#         if len(q) == 0:
#             can.append(prefix)
#             return
#         else:
#             for i in q:
#                 if prev[i] == q:
#                     rep(prefix+[i], [], can, prev)
#                 else:
#                     rep(prefix+[i], prev[i], can, prev)

#     def lcs(a, n, prods):
#         max = -1
#         best = []
#         prev = []
#         for i in xrange(n):
#             best.append(1)
#             prev.append([i])

#         for i in xrange(1, n):
#             for j in range(i):
#                 if a[i] > a[j] and best[i] <= best[j] + 1:
#                     if best[i] < best[j] + 1:
#                         best[i] = best[j] + 1
#                         prev[i] = [j]
#                     else:
#                         prev[i].append(j)
                   
#         end = [0]
#         for i in xrange(n):
#             if max <= best[i]:
#                 if max < best[i]:
#                     max = best[i]
#                     end = [i]
#                 else: 
#                     end.append(i)

#         candidates = []
#         queue = []

#         rep([], end, candidates, prev)

#         return candidates


#     ret = []
#     prods = raw_input().split()
#     vals = map(int, raw_input().split())

#     assoc = []
#     for i, x in enumerate(vals):
#         assoc.append([x, i])

#     assoc.sort()

#     assoc2 = map(lambda x: [x[1], x[0], 0], assoc)
#     for i, x in enumerate(assoc2):
#         x[2] = i
    
#     assoc2.sort()
        
#     lt = map(lambda x: x[2], assoc2)

#     lc = lcs(lt, len(lt), prods)

#     for k, x in enumerate(lc):
#         ret.append([])
#         for i in xrange(len(lt)):
#             if i not in x:
#                 ret[k].append(prods[i])

#         ret[k].sort()
#         ret[k] = ' '.join(ret[k])

#     ret.sort()
#     return ret[0]
            
# for i in range(int(input())):
#     print("Case #%d: %s" % (i+1, compute()))



def SolveCase(case_index, case):
    T, tripsa, tripsb = case
    trips = []
    for trip in tripsa:
        trips.append([trip[0], trip[1], 0])
    for trip in tripsb:
        trips.append([trip[0], trip[1], 1])
    trips.sort()
    
    start = [0, 0]
    trains = [[], []]
    
    for trip in trips:
        d = trip[2]
        if trains[d] and trains[d][0] <= trip[0]:
            heappop(trains[d])
        else:
            start[d] += 1
        heappush(trains[1-d], trip[1]+T)
    
    print("Case #%d: %d %d" % (case_index, start[0], start[1]))

SolveCase(2, (3,2))