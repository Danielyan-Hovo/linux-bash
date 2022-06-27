#python gcayin havasarum
x=0
def gcayin1(a,b):
    print(f"trvac havasarumn e {a}X={b}")
    if(a!=0):
        print(f"x={b/a}")
        x=b/a
        return x
    elif(a==0 and b==0):
        print("antiv qanaki lucumner")
        return
    else:
        print("havasarumy lucum chuni")
        return

a = float(input("grel havasarman a-i gorcakicy  "))
b = float(input("grel havasarman b-i gorcakicy  "))
gcayin1(a,b)