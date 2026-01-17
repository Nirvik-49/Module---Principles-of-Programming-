# Inheritance with Person, Lecturer, Student, GraduateStudent
# Practical 9 - Exercise 2 - Task 2.2
# Nirvik K.C.

class Person:
    def __init__(self, firstName="Mr", lastName="X", address="Bristol"):
        self.__firstName = firstName
        self.__lastName  = lastName
        self.__address   = address

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setAddress(self, address):
        self.__address = address

    # Getters
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAddress(self):
        return self.__address
    
    # __str__ method
    def __str__(self):
        return f"Person's name is {self.getFirstName()} {self.getLastName()}\nAddress is {self.getAddress()}"
    
class Lecturer(Person):
    def __init__(self, firstName, lastName, address, lecturerID):
        super().__init__(firstName, lastName, address)
        self.__lecturerID = lecturerID

    # Getters and setters for lecturerID
    def getLecturerID(self):
        return self.__lecturerID
        
    def setLecturerID(self, lecturerID):
        self.__lecturerID = lecturerID

    # Override __str__ 
    def __str__(self):
        return super().__str__() + f"\nLecturer ID: {self.getLecturerID()}"
    

class Student(Person):
    def __init__(self, firstName, lastName, address, studentID):
        super().__init__(firstName, lastName, address)
        self.__studentID = studentID

    # Getters and setters for studentID
    def getStudentID(self):
        return self.__studentID

    def setStudentID(self, studentID):
        self.__studentID = studentID

    # Override __str__
    def __str__(self):
        return super().__str__() + f"\nStudent ID: {self.getStudentID()}"

    
class GraduateStudent(Student):
    def __init__(self, firstName, lastName, address, studentID, supervisor):
        super().__init__(firstName, lastName, address, studentID)
        self.__supervisor = supervisor

    # Getters and setters for supervisor
    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, supervisor):
        self.__supervisor = supervisor

    # Override __str__
    def __str__(self):
        return super().__str__() + f"\nSupervisor: {self.getSupervisor()}"
    

# Lecturer
lec = Lecturer("Dr. Wilson", "Smith", "London", 101)
print(lec)
print()

# Student
stu = Student("Harry", "Conway", "Bristol", 239201)
print(stu)
print()

# GraduateStudent
grad = GraduateStudent("Joe", "Clark", "Manchester", 2023002, "Prof. David")
print(grad)

# Output:
# Person's name is Dr. Wilson Smith
# Address is London
# Lecturer ID: 101

# Person's name is Harry Conway
# Address is Bristol
# Student ID: 239201

# Person's name is Joe Clark
# Address is Manchester
# Student ID: 2023002
# Supervisor: Prof. David