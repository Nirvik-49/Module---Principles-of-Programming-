# UML to Code : Class Book
# Practical 8 - Exercise 2
# Nirvik K.C

class Book:
    def __init__(self, title="Untitled", pageCount=100):
        self.__title = title
        # Use setter
        self.setPageCount(pageCount)

    # Getters
    def getTitle(self):
        return self.__title
    
    def getPageCount(self):
        return self.__pageCount
    
    # Setters

    def setTitle(self, title):
        self.__title = title
    
    def setPageCount(self, pages):
        # Minimum pages : 100 and Maximum pages : 3000
        if pages < 100:
            print(f"Error: Page count cannot be less than 100. Set back to default (100).")
            self.__pageCount = 100
        elif pages > 3000:
            print(f"Error: Page count exceeds the limit. Set to the maximum count of 3000.")
            self.__pageCount = 3000
        else:
            self.__pageCount = pages
    
    # instance/member method
    def display(self):
        print(f"Book Info: {self.__title} and Pages: {self.__pageCount}")

# Display Book's Info
book1 = Book("Python for Beginners", 150)
book1.display()

book2 = Book("Introduction to C Language", 50)  # Less than default number of pages
book2.display()

# Output:
# Book Info: Python for Begineers and Pages: 150
# Error: Page count cannot be less than 100. Set back to default (100).
# Book Info: Introduction to C Langauge and Pages: 100