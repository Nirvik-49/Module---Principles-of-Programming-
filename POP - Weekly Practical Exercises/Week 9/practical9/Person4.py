# Implementation of complete hierarchy for Person class
# Adding new classes. 
# For example, UnderGradaute (sub-class of Student), PermanentLecturer (sub-class of Lecturer), 
# PartTimeLecturer (sub-class of Lecturer), HRStaff (sub-class of Person), and Accountant (sub-class of HRStaff)

class Person:
    def __init__(self, firstName="Mr", lastName="X", address="Bristol"):
        self.__firstName = firstName
        self.__lastName = lastName
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
        return (f"Person's name is {self.getFirstName()} {self.getLastName()}\n" f"Address is {self.getAddress()}")
    
class Lecturer(Person):
    def __init__(self, firstName, lastName, address, lecturerID):
        super().__init__(firstName, lastName, address)
        self.__lecturerID = lecturerID
    
    # Getters and setters
    def getLecturerID(self):
        return self.__lecturerID

    def setLecturerID(self, lecturerID):
        self.__lecturerID = lecturerID

    def __str__(self):
        return "Lecturer's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Lecturer ID: " + str(self.__lecturerID)

class PermanentLecturer(Lecturer):
    def __init__(self, firstName, lastName, address, lecturerID, officeRoom):
        super().__init__(firstName, lastName, address, lecturerID)
        self.__officeRoom = officeRoom
    
    # Getters and setters
    def getOfficeRoom(self):
        return self.__officeRoom
    
    def setOfficeRoom(self, officeRoom):
        self.__office = officeRoom

    def __str__(self):
        return "Lecturer's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Lecturer ID: " + str(self.getLecturerID()) + "\n" "Office Room: " + self.__officeRoom


class PartTimeLecturer(Lecturer):
    def __init__(self, firstName, lastName, address, lecturerID, hoursPerWeek):
        super().__init__(firstName, lastName, address, lecturerID)
        self.__hoursPerWeek = hoursPerWeek

    def getHoursPerWeek(self):
        return self.__hoursPerWeek

    def setHoursPerWeek(self, hours):
        self.__hoursPerWeek = hours

    def __str__(self):
        return "Lecturer's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Lecturer ID: " + str(self.getLecturerID()) + "\n" "Hours per week: " + str(self.__hoursPerWeek)
    
class Student(Person):
    def __init__(self, firstName, lastName, address, studentID):
        super().__init__(firstName, lastName, address)
        self.__studentID = studentID

    # Getters and setters
    def getStudentID(self):
        return self.__studentID

    def setStudentID(self, studentID):
        self.__studentID = studentID

    # Override __str__
    def __str__(self):
        return "Student's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Student ID: " + str(self.__studentID)
    
class Undergraduate(Student):
    def __init__(self, firstName, lastName, address, studentID, yearOfStudy):
        super().__init__(firstName, lastName, address, studentID)
        self.__yearOfStudy = yearOfStudy
    
    # Getters and setters
    def getYearOfStudy(self):
        return self.__yearOfStudy

    def setYearOfStudy(self, year):
        self.__yearOfStudy = year

    def __str__(self):
        return "Student's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Student ID: " + str(self.getStudentID()) + "\n" "Year of Study: " + str(self.__yearOfStudy)


class GraduateStudent(Student):
    def __init__(self, firstName, lastName, address, studentID, supervisor):
        super().__init__(firstName, lastName, address, studentID)
        self.__supervisor = supervisor
    
    # Getters and setters
    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, supervisor):
        self.__supervisor = supervisor

    def __str__(self):
        return "Student's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Student ID: " + str(self.getStudentID())  + "\n" "Supervisor’s name: " + self.__supervisor
    
class HRStaff(Person):
    def __init__(self, firstName, lastName, address, employeeID):
        super().__init__(firstName, lastName, address)
        self.__employeeID = employeeID

    # Getters and setters
    def getEmployeeID(self):
        return self.__employeeID
    
    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID

    def __str__(self):
        return "Employee's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Employee ID: " + str(self.getEmployeeID())
    
class Accountant(HRStaff):
    def __init__(self, firstName, lastName, address, employeeID):
        super().__init__(firstName, lastName, address, employeeID)
        # No extra attributes

    def __str__(self):
        return "Employee's name is " + self.getFirstName() + " " + self.getLastName() + "\n" "Address is " + self.getAddress() + "\n" "Employee ID: " + str(self.getEmployeeID())

# Lecturer
lec = PermanentLecturer("Dr. Alice", "Brown", "Frenchay Campus", 1001, "Room 4B12")
print(lec)

# PermanentLecturer
perm_lec = PermanentLecturer("Prof. Cameron", "White", "Frenchay Campus", 102, "Room 5A10")
print(perm_lec)

# PartTimeLecturer
part_lec = PartTimeLecturer("Ms. Sarah", "Clark", "Frenchay Campus", 103, 15)
print(part_lec)

# Student
stu = Student("Harry", "Conway", "Frenchay Campus", 2024001)
print(stu)

# Undergraduate
ug = Undergraduate("Raj", "Sharma", "Frenchay Campus", 2024002, 3)
print(ug)

# GraduateStudent
gs = GraduateStudent("Liam", "Scott", "Frenchay Campus", 2024003, "Prof. Brown")
print(gs)

# HRStaff
hr = HRStaff("Sophia", "Lee", "Frenchay Campus", "Emp001")
print(hr)

# Accountant
acc = Accountant("Oliver", "Stone", "Frenchay Campus", "Emp002")
print(acc)

# Output:
# Lecturer's name is Dr. Alice Brown
# Address is Frenchay Campus
# Lecturer ID: 1001
# Office Room: Room 4B12
# Lecturer's name is Prof. Cameron White
# Address is Frenchay Campus
# Lecturer ID: 102
# Office Room: Room 5A10
# Lecturer's name is Ms. Sarah Clark
# Address is Frenchay Campus
# Lecturer ID: 103
# Hours per week: 15
# Student's name is Harry Conway
# Address is Frenchay Campus
# Student ID: 2024001
# Student's name is Raj Sharma
# Address is Frenchay Campus
# Student ID: 2024002
# Year of Study: 3
# Student's name is Liam Scott
# Address is Frenchay Campus
# Student ID: 2024003
# Supervisor’s name: Prof. Brown
# Person's name is Sophia Lee
# Address is Frenchay Campus
# Employee ID: Emp001
# Employee's name is Oliver Stone
# Address is Frenchay Campus
# Employee ID: Emp002