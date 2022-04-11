
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