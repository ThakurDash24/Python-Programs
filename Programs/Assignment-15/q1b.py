class Person:
    def __init__(self, name, age, gender):
    
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
    
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Example of creating a Person object and introducing
person1 = Person("Thakur Dash", 20, "Male")
person1.introduce()
