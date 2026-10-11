#create the class
class FamilyMember:
    def __init__( self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height = height_cm

    def show_traits(self):
        print('eye colour:',self.eye_colour)
        print('height:',self.height_cm)



#part 2: create the child class that inherits from the family class
class Kid(FamilyMember):
    #part3: give the child it's own details, plus the inherited traits
    def __init__(self,name, eye_colour, height_cm, age):
        super().__init__(eye_colour, height_cm)
        self.name = name
        self.age = age
        super(). __init__(eye_colour, height_cm) # call the parent constructor to set the eye colour and height

    #continue in the next class

    #part4: override the show_traits method to include the child's name and age
    def show_traits(self):
        print('name:',self.name)
        print('age:',self.age)
        super().show_traits() # call the parent method to show the eye colour and height

    # part 5 : add a brand new method dat only kid has
    def favorite_hobby(self, hobby):
        print(self.name, 'loves', hobby)

    #part 6 : create a kid object with real family trait values
    child = Kid('maya', 'brown', 140, 10)


    child.show_traits()
    child.favorite_hobby('painting')

    #part 8 : check whether kid iz really a sub class of family member
    print('iz kid a subclass of family member?', issubclass(Kid, FamilyMember))
