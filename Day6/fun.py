def add(a,b):
    return a+b

def add(a,b,c=None): #override above func
    if c!=None:
        return a+b+c
    else:
        return a+b
        
def sayHello(name="friend"): #default argument
    
    print("Hello! "+name)


def average(*args):
    avg = sum(args)/len(args)
    return (avg) 

def keyValue(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key,value))


print(f"invoke add(1,2): {add(1,2)}")
print(f"invoke overloaded func add(1,2,3): {add(1,2,3)}")
sayHello("varun")
sayHello()
print(average(2,4,5))

keyValue(first = 'varun', second = 'thapa', third = 'coder')