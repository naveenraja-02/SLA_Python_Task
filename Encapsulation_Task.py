class Student:
    def __init__(self,name,mark):
        self.__name = name
        self.__mark = mark
        
    def update_mark(self,updated_mark):
        self.__mark = updated_mark
        
    def display_details(self):
        print("Name : ",self.__name)
        print("Mark : ",self.__mark)
        
std = Student("Naveen",85)
std.display_details()

std.update_mark = int(input("Enter your mark:"))
print(f"After updated mark : ")
std.display_details()
print(f"updated mark : {std.update_mark}")


Output : 

Name :  Naveen
Mark :  85
Enter your mark:89
After updated mark : 
Name :  Naveen
Mark :  85
updated mark : 89
