class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor(stores the teacher of the student)
        self._teacher = None
        Student.all.append(self) #adds each student object to the all list

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        # ensures that the assigned object can be a student's teacher
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self
        
# Create Students
s1 = Student("John", 18)
s2 = Student("Jane", 19)

# Create a Teacher
t1 = Teacher("Mr. Smith")

# Assign Students to the Teacher
t1.add_student(s1)
t1.add_student(s2)

# Check Students of the Teacher
print(t1.students())  # Output: [s1, s2]

# Check the Teacher of a Student
print(s1.teacher.name)  # Output: Mr. Smith
print(s2.teacher.name)  # Output: Mr. Smith

