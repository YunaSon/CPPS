rows = [
    {'fname': 'Brian', 'lname': 'Jhones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jhones', 'uid': 1004},
    {'fname': 'John', 'lname': 'Park', 'uid': 1005},    
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

#print(rows_by_fname)
#print(rows_by_uid)

rows_by_fname_id = sorted(rows, key=itemgetter('fname', 'uid'))
#print(rows_by_fname_id)

rows_byfname =sorted(rows, key = lambda x: x['fname'])
rows_byfnameid =sorted(rows, key = lambda x: (x['fname'], x['uid']))

print(rows_byfname)
print(rows_byfnameid)


