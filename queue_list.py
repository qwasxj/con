

def replace(q_l, src, obj):
    for i in range(len(q_l)):
        if q_l[i] == src:
            q_l[i] = obj


l = [1, 2, 3, 4]
l.insert(0, 1)
l.append(2)
print(l)
l.pop(1)
print(l)
print(l.index(2))
replace(l, 2, "x")
print(l)
