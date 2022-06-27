#amenamec bajanarar python
def bajanarar(a,b):   
    if (b==0):
        return a
    else:
        return bajanarar(b,a%b)

a = int(input("greq arajin tivy "))
b = int(input("greq erkrord tivy "))

num = bajanarar(a,b)
print(num)
