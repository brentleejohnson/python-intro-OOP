"""" # Defining my super class
class Cats:

    # initialising my attributes
    def __init__(self, type, name, gender, colour, age):
        self.type = type
        self.name = name
        self.gender = gender
        self.colour = colour
        self.age = age

    # method
    def move(self):
        print("I am a: " + self.type + "\n" +
              "My name is: " + self.name + "\n" +
              "My gender is: " + self.gender + "\n" +
              "My colour is: " + self.colour + "\n" +
              "My age is: " + self.age)


objCats = Cats("Lion", "Mufasa", "Male", "Orange", "5 years old")
objCats.name = "Mountain Lion"
objCats.move()
hasattr(objCats, age) """


# # Task
# # Defining my super class
# class Shapes:
#     def __init__(self, name, side, type, size):
#         self.name = name
#         self.side = side
#         self.type = type
#         self.size = size
#
#     # method
#     def area(self):
#         print("I am a " + self.name + "\n" +
#               "I have " + self.side + "\n" +
#               "I am a " + self.type + "\n" +
#               "It is " + self.size)
#
#
# # calling the function
# objShapes = Shapes("shape", "4 sides", "polygon", "14cm")
# objShapes.area()
#
#
# # Defining my super class
# class Circle(Shapes):
#     # initialising my attributes
#     def __init__(self, radius):
#         self.radius = radius
#
#     # method
#     def area(self):
#         result = 3.14 * self.radius * self.radius
#         return result
#     """ print(result) """
#
#
# # calling the function
# objCoin = Circle(5)
# """" objCoin.area() """
# print(objCoin.area())
#
#
# # Defining my super class
# class Triangle(Shapes):
#     # initialising my attributes
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#
#     # method
#     def area(self):
#         areaTri = (1 / 2) * self.base * self.height
#         return areaTri
#
#
# # calling the function
# objPyramid = Triangle(5, 10)
# print(objPyramid.area())
#
#
# # Defining my super class
# class Rectangle(Shapes):
#     # initialising my attributes
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     # method
#     def area(self):
#         areaRect = self.length * self.width
#         return areaRect
#
#
# # calling the function
# objLaptop = Rectangle(7, 3)
# print(objLaptop.area())
#
#
# # Defining my super class
# class Square(Shapes):
#     # initialising my attributes
#     def __init__(self, side):
#         self.side = side
#
#     # method
#     def area(self):
#         areaSqu = self.side * 4
#         return areaSqu
#
#
# # calling the function
# objBox = Square(5)
# print(objBox.area())


from tkinter import *
root = Tk()
root.title("Tkinter")
root.geometry("300x300")


class Circle:
    myresult = StringVar()

    def __init__(self, window):
        self.lblradius = Label(window, text="Please enter the radius")
        self.lblradius.pack()
        self.txtrad = Entry(window)
        self.txtrad.pack()
        self.btncalc = Button(window, text="Calculate area", borderwidth="10", command=self.area)
        self.btncalc.pack()
        self.lblresult = Label(window, text="", textvariable=self.myresult)
        self.lblresult.pack()

    def area(self):
        radius = int(self.txtrad.get())
        answer = 3.14 * (radius**2)
        self.myresult.set("The area is " + str(answer))


objCircle = Circle(root)
root.mainloop()
