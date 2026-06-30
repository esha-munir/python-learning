#add fun
def fun1(x,y):
    print("addition of two numbers is:",x+y)

fun1(2,5)
#sub fun
def sub(a,b):
    print("subtraction of two numbers is:",a-b)
    print("function completed")

sub(3,4)
#covert to list
def fun2(*t):
    l=list(t)
    print(l,type(l))

fun2(2,4,5,6,7,7,8,9,5,3,2,3)

#display dictionary
def fun3(**t):
    print(t)

fun3(name="Esha",rollnum=18,age=20,phoneno=9026)

