

a = 3
i = 100

def something(i):
    i = 50
    return i
    

#print(something(i))

a_parameter = 10

def a_function(a_parameter):
    a_parameter += 1
    return a_parameter
 
a_parameter = a_function(a_parameter)
print(a_parameter)