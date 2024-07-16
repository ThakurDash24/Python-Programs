class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Example of creating a Person object
person1 = Person("T Dash", 20, "Male")

# Accessing attributes
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"Gender: {person1.gender}")
