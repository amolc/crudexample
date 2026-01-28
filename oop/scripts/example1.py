

def say_hello():
    print("hello world")

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"hello {self.name} you are {self.age} years old")




def run():
    p = person("amol", 30)