x = -3
#simple if
if x>0:
    print("positive")
if x<0:
    print("negative")

#simple if_else
y = 3
if y > 0:
    print("positive")
else:
    print("negative")

#ladder/multiple if
z = 0
if z > 0:
    print("positive")
elif z<0:

    print("negative")
else:
    print("zero")

#nested if else
a = 6
if a>0:
    if a%2==0:
        print("psoitive even:")
    else:
        print("positive odd")
elif a<0:
        print("negative")
else:
    print("zero")

#nested to multiple
a = -6
if a>0 and a%2==0:
    print("psoitive even:")
elif a > 0 and a%2!=0:
        print("positive odd")
elif a<0:
        print("negative")
else:
    print("zero")