value3 = 100
def scope_test3():
    global value3
    value3 = 20
    print("inside =", value3)
scope_test3()
print("outside =", value3)
