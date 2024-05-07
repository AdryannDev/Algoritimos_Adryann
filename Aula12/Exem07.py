def tem_igual(*args):
    for i in range(len(args)-1):
        print(i)
        n = args[i]
        for j in range(i+1, len(args)):
            print(j)
            if n == args[j]:
                return True
    return False

print(tem_igual(1,3,6,8,8))