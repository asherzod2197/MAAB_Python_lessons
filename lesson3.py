# ==================================================
# LIST TASKS
# ==================================================

lst = [1, 2, 3, 2, 4, 2]
lst2 = [7, 8]
element = 2

# 1 Count occurrences
print(lst.count(element))

# 2 Sum of elements
print(sum(lst))

# 3 Max element
print(max(lst))

# 4 Min element
print(min(lst))

# 5 Check element
print(element in lst)

# 6 First element
print(lst[0] if lst else None)

# 7 Last element
print(lst[-1] if lst else None)

# 8 Slice first three
print(lst[:3])

# 9 Reverse list
print(lst[::-1])

# 10 Sort list
print(sorted(lst))

# 11 Remove duplicates
print(list(set(lst)))

# 12 Insert element
lst_copy = lst.copy()
lst_copy.insert(1, 99)
print(lst_copy)

# 13 Index of element
print(lst.index(element))

# 14 Check empty list
print(len(lst) == 0)

# 15 Count even numbers
print(sum(1 for x in lst if x % 2 == 0))

# 16 Count odd numbers
print(sum(1 for x in lst if x % 2 != 0))

# 17 Concatenate lists
print(lst + lst2)

# 18 Find sublist
sub = [2, 3]
print(any(lst[i:i+len(sub)] == sub for i in range(len(lst))))

# 19 Replace element
lst_replace = lst.copy()
if element in lst_replace:
    lst_replace[lst_replace.index(element)] = 100
print(lst_replace)

# 20 Second largest
unique_sorted = sorted(set(lst))
print(unique_sorted[-2] if len(unique_sorted) > 1 else None)

# 21 Second smallest
print(unique_sorted[1] if len(unique_sorted) > 1 else None)

# 22 Filter even
print([x for x in lst if x % 2 == 0])

# 23 Filter odd
print([x for x in lst if x % 2 != 0])

# 24 List length
print(len(lst))

# 25 Copy list
copy_lst = lst.copy()
print(copy_lst)

# 26 Middle element
mid = len(lst)//2
print((lst[mid-1], lst[mid]) if len(lst)%2==0 else lst[mid])

# 27 Max of sublist
sublist = lst[1:4]
print(max(sublist))

# 28 Min of sublist
print(min(sublist))

# 29 Remove element by index
lst_removed = lst.copy()
idx = 2
if 0 <= idx < len(lst_removed):
    lst_removed.pop(idx)
print(lst_removed)

# 30 Check if list sorted
print(lst == sorted(lst))

# 31 Repeat elements
n = 2
print([x for x in lst for _ in range(n)])

# 32 Merge and sort
print(sorted(lst + lst2))

# 33 Find all indices
print([i for i, x in enumerate(lst) if x == element])

# 34 Rotate list right
k = 1
print(lst[-k:] + lst[:-k])

# 35 Create range list
print(list(range(1,11)))

# 36 Sum positive
print(sum(x for x in lst if x > 0))

# 37 Sum negative
print(sum(x for x in lst if x < 0))

# 38 Check palindrome
print(lst == lst[::-1])

# 39 Create nested list
size = 2
nested = [lst[i:i+size] for i in range(0,len(lst),size)]
print(nested)

# 40 Unique in order
seen = set()
unique_order = [x for x in lst if not (x in seen or seen.add(x))]
print(unique_order)


# ==================================================
# TUPLE TASKS
# ==================================================

tpl = (1,2,3,2,4)

print(tpl.count(2))
print(max(tpl))
print(min(tpl))
print(2 in tpl)
print(tpl[0] if tpl else None)
print(tpl[-1] if tpl else None)
print(len(tpl))
print(tpl[:3])
print(tpl + (5,6))
print(len(tpl) == 0)
print([i for i,x in enumerate(tpl) if x==2])

s = sorted(set(tpl))
print(s[-2] if len(s)>1 else None)
print(s[1] if len(s)>1 else None)

single = (5,)
print(single)
print(tuple(lst))
print(tpl == tuple(sorted(tpl)))

subtpl = tpl[1:4]
print(max(subtpl))
print(min(subtpl))

print(tuple(x for x in tpl if x != 2))
print(tuple(tuple(tpl[i:i+2]) for i in range(0,len(tpl),2)))
print(tuple(x for x in tpl for _ in range(2)))
print(tuple(range(1,11)))
print(tpl[::-1])
print(tpl == tpl[::-1])

seen=set()
print(tuple(x for x in tpl if not (x in seen or seen.add(x))))


# ==================================================
# SET TASKS
# ==================================================

set1={1,2,3}
set2={3,4,5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1.issubset(set2))
print(2 in set1)
print(len(set1))
print(set(lst))

s_copy=set1.copy(); s_copy.discard(2); print(s_copy)

empty=set()
print(empty)
print(len(set1)==0)
print(set1 ^ set2)

s=set1.copy(); s.add(10); print(s)

s=set1.copy(); s.pop(); print(s)

print(max(set1))
print(min(set1))
print({x for x in set1 if x%2==0})
print({x for x in set1 if x%2!=0})
print(set(range(1,11)))
print(set(lst+lst2))
print(set1.isdisjoint(set2))
print(list(set(lst)))
print(len(set(lst)))

import random
print({random.randint(1,50) for _ in range(5)})


# ==================================================
# DICTIONARY TASKS
# ==================================================

d = {'a':1,'b':2,'c':1}

print(d.get('a'))
print('a' in d)
print(len(d))
print(list(d.keys()))
print(list(d.values()))

d2={'d':4}
print({**d, **d2})

copy_d=d.copy(); copy_d.pop('a',None); print(copy_d)

empty_d={}
print(empty_d)
print(len(d)==0)

key='a'
print((key,d[key]) if key in d else None)

d['a']=100
print(d)
print(list(d.values()).count(1))
print({v:k for k,v in d.items()})

val=1
print([k for k,v in d.items() if v==val])

keys=['x','y']; values=[10,20]
print(dict(zip(keys,values)))
print(any(isinstance(v,dict) for v in d.values()))

nested={'a':{'inner':5}}
print(nested['a']['inner'])

from collections import defaultdict
def_d=defaultdict(int)
print(def_d['missing'])

print(len(set(d.values())))
print(dict(sorted(d.items())))
print(dict(sorted(d.items(), key=lambda x:x[1])))
print({k:v for k,v in d.items() if v>1})
print(set(d.keys()) & set(d2.keys()))
print(dict((('a',1),('b',2))))
print(next(iter(d.items())))
