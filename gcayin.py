#python gcayin havasarum

def gcayin(a,b):
    print(f"trvac havasarumn e {a}X={b}")
    if(a!=0):
        print(f"X={b/a}")
    elif(a==0 and b==0):
        print("antiv qanaki lucumner")
    else:
        print("havasarumy lucum chuni")

a = float(input("grel havasarman a-i gorcakicy  "))
b = float(input("grel havasarman b-i gorcakicy  "))


gcayin(a,b)
