#function is a block of code that runs when you call it
#you can pass data to it using parameters
#you need to define the function before calling it

#simple declaration of function
def say_hello():
    print("hello guys")

#calling a function
say_hello()

#you can also set parameters like this
def introduce(name):
    print("Hello! My name is", name)

#then add the argument 
introduce("Cedrick") #put it inside the parenthesis
introduce("Andres")

#arbitrary args is when you don't know how many args will be passed