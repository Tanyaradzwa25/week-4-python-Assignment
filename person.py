
class Person:
    def __init__(self, name, age, gender,school ,grade,placement,majors,location):
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school
        self.grade = grade
        self.placement = placement
        self.majors = majors
        self.location = location

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.l am in {self.grade} at {self.school} and my majors are {self.majors}.For my clinical training l am placed at {self.placement} in {self.location}.")

# Create an instance of the Person class

person = Person(name="Samantha Tanyaradzwa Maponga", age=30, gender="Female" ,school="Life healthcare" ,grade="3rd year of learning" ,placement="Rosearces Hospital" ,majors="General Nursing Science,Pharmacology,Applied Psychological Science and anatomy & Physiology" ,location="Primrose,Germiston")

# Call the introduce method
person.introduce()
