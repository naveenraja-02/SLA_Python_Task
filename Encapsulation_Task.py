class Student:
    def __init__(self,name,mark):
        self.__name = name
        self.__mark = mark
        
    def update_mark(self,updated_mark):
        self.__mark = updated_mark
        
    def display_details(self):
        print(self.__name)
        print(self.__mark)
        
std = Student("Naveen",85)
std.display_details()

std.update_mark = int(input("Enter your mark:"))
std.display_details()
print(f"updated mark : {std.update_mark}")