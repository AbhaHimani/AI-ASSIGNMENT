f_jug = 0
t_jug = 0

f_jug_cap = 4
t_jug_cap = 3
flag = 0
print("The 3 litre jug has: ", t_jug)
print("The 4 litre jug has: ", f_jug)
print("\n")
while flag == 0:
    t_jug += t_jug_cap
    print("The 3 litre jug has: ", t_jug)
    print("The 4 litre jug has: ", f_jug)
    print("\n")
    while t_jug > 0:
        t_jug -= 1
        if t_jug == 0 and f_jug == 3:
            print("The 3 litre jug has: ", t_jug)
            print("The 4 litre jug has: ", f_jug)
            print("\n")
        if f_jug <= f_jug_cap:
            f_jug += 1
        # print("The 3 litre jug has: ", t_jug)
        # print("The 4 litre jug has: ", f_jug)
        # print("\n")
        if f_jug == 4 and t_jug == 2:
            print("The 3 litre jug has: ", t_jug)
            print("The 4 litre jug has: ", f_jug)
            print("\n")
            f_jug = 0
            f_jug += t_jug
            print("The 3 litre jug has: ", t_jug)
            print("The 4 litre jug has: ", f_jug)
            print("\n")
            t_jug = 0
            print("The 3 litre jug has: ", t_jug)
            print("The 4 litre jug has: ", f_jug)
            print("\n")
            flag = 1
            break