# shorthand operators
#+= -= *= /= //= %=  **=

a = 6
b = 6
#a = a +b  
a + b

# in python we dont use increment or decrement operators
# > >= < <= == !=(not equals to)

#answer will aways ne in boolean in python whilw comparing

print(12>11)
print(12>=13)


#always compares non equal characters


print("john" > "hello)")  #true
print("adhhk" > "Ajolk") #true
print("qjohn" > "z") #false
print("12" > "z") #false
print(ord("1"))


#falsey values 0 "" / '' false none are falsey values 

#logical oprators --- and , or , not

a = 8
print(a>10 and a%2==0) # and prints true if both are true and false if one of them is false
print(a>8 or a % 2==0) #or prints true if one is true and false if both are false

a = 23
b = 0
c = -9

print(a and b and c)


a = 23
b = 0
c = -9
print(a or b or c)

a = 0 # it will print false  
b = 1
c = -9
print(a or b or c)


a = 23
b = 0
c = -9

print(a or b and c)

a = ""
b = "hello"
print(a and b)









