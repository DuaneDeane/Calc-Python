def say_hello():
    print('hello there')
    print("Im inside")
    age = 34
    if(age < 90):
        print('of course it is')
    elif(age == 90):
        print("you are on the border line")
    else:
        print("sorry you are getting old")

def separator():
    print("-------------------")

print("hello world")
say_hello()

# this is a comment

#variables
name = 'Duane'
last_name = 'Deane'
age = 34
found = True
total = 23.54
products = []
separator()

print (name + last_name)
print (age + age)
print (name +str(age)) #need to put str to make something a string
separator()

#math operation
print (21 + 21)
print (21 - 2)
print (21 * 2)
print (21 / 2)
print (21 % 2)
separator()

print('Im outside')