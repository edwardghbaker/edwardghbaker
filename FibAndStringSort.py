
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def stringSorter(O_list,Add_list,Sub_list):
    for s in Add_list:
        if s not in O_list:
            O_list.append(s)
    for s in Sub_list:
        if s in O_list:
            O_list.remove(s)
    print(O_list)
    print(type(O_list))
    O_list.sort(reverse=True)
    O_list.sort(key = len)
    return O_list
    