def greet():
    print("A")
    print("B")
    print("C")

#call the function
#greet()

#function that allows for input
#name - parameter
def greet_with_name(name):
    print(f"hello {name}")
    print(f"A {name}")
    print(f"b {name}")
#yingyi  - argument
#greet_with_name("Yingyi")

#positional argument 
def greet_with(name, location):
    print(f"A {name}")
    print(f"b in {location}")
#greet_with('yingyi','London')
#greet_with(location='London')

#prime_number

# input
num = int(input("type in a random number: "))

# > 1
if num > 1:
   # find Composite Number
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"Not a prime number")
           print("becuase it has ways of wrinting it as a product ")
           print(i,"*",num//i,"=",num)
           continue
   else:
       print(num,"Yes,it is a prime number")
       
# <=1
else:
   print(num,"Not a prime number")
 #break    
