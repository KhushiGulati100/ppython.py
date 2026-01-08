def fac(a):
    if (a==0 or a==1):
        return 1
    else:
        res = a * fac(a-1)
    return res
n = int(input("Enter a number: "))
ans = fac(n)
print(ans)