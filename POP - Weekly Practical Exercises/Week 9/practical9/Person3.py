# Implement your classes, create appropriate objects and print the information
# Practical 9 - Exercise 2 - Task 2.3
# Nirvik K.C.

class Person:
    def __init__(self, firstName="Mr", lastName="X", address="Bristol"):
        self.__firstName = firstName
        self.__lastName  = lastName
        self.__address   = address

    # Getters
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAddress(self):
        return self.__address
    
    # __str__ method
    def __str__(self):
        return f"{self.getFirstName()}'s name is {self.getFirstName()} {self.getLastName()}\n" f"Address is {self.getAddress()}"
    
class Lecturer(Person):
    def __init__(self, firstName, lastName, address, lecturerID):
        super().__init__(firstName, lastName, address)
        self.__lecturerID = lecturerID

     # Override __str__ 
    def __str__(self):
        return "Lecturer's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Lecturer ID: " + str(self.__lecturerID)
    
class Student(Person):
    def __init__(self, firstName, lastName, address, studentID):
        super().__init__(firstName, lastName, address)
        self.__studentID = studentID

    # Override __str__
    def __str__(self):
        return "Student's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Student ID: " + str(self.__studentID)
    
class GraduateStudent(Student):
    def __init__(self, firstName, lastName, address, studentID, supervisor):
        super().__init__(firstName, lastName, address, studentID)
        self.__supervisor = supervisor

    # Override __str__
    def __str__(self):
        return "Student's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" + "Student ID: " + str(self._Student__studentID) + "\n" "Supervisor’s name: " + self.__supervisor

# Lecturer
lecturer = Lecturer("Chris", "Simons", "UWE Frenchay Campus 4QXX", 2345)
print(lecturer)

# Student
student = Student("Peter", "Miller", "UWE Frenchay Campus", 5678)
print(student)

# GraduateStudent
gradstudent = GraduateStudent("Dan", "Fielding", "UWE Frenchay Campus", 6789, "Jim Smith")
print(gradstudent)

    
# Output:
# Lecturer's name is Chris Simons
# Address is UWE Frenchay Campus 4QXX
# Lecturer ID: 2345
# Student's name is Peter Miller
# Address is UWE Frenchay Campus
# Student ID: 5678
# Student's name is Dan Fielding
# Address is UWE Frenchay Campus
# Student ID: 6789