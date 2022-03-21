t_jug_cap = 12
e_jug_cap = 8
f_jug_cap = 5

t_jug = 0
e_jug = 0
f_jug = 0
flag = 0
print(t_jug, e_jug, f_jug)

while flag == 0:
    t_jug += t_jug_cap
    print(t_jug, e_jug, f_jug)
    while t_jug > 0 and e_jug != e_jug_cap:
        t_jug -= 1
        if e_jug < e_jug_cap:
            e_jug += 1
    print(t_jug, e_jug, f_jug)
    flag = 1
flag = 0
while flag == 0:
    while e_jug > 0 and f_jug != f_jug_cap:
        e_jug -= 1
        if f_jug < f_jug_cap:
            f_jug += 1
    print(t_jug, e_jug, f_jug)
    flag = 1
flag = 0
f_jug -= f_jug_cap
t_jug += f_jug_cap
print(t_jug, e_jug, f_jug)
while e_jug > 0:
    e_jug -= 1
    f_jug += 1
print(t_jug, e_jug, f_jug)
while e_jug < e_jug_cap:
    t_jug -= 1
    e_jug += 1
print(t_jug, e_jug, f_jug)
while f_jug < f_jug_cap:
    e_jug -= 1
    f_jug += 1
print(t_jug, e_jug, f_jug)
while t_jug != 6:
    f_jug -= 1
    t_jug += 1
print(t_jug, e_jug, f_jug)