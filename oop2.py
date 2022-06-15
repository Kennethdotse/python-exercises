class rec:
    #def __init__(self,colour,length,width): the commented section was fir the first instance without inputs
    def __init__(self,colour=None,length=None,width=None):
        self.colour = colour
        self.length = length
        self.width = width

    def input_colour(self):
        colour = input("Enter colour: ")
        self.colour = colour

    def input_length(self):
        length = float(input("Enter length: "))
        self.length = length

    def input_width(self):
        width = float(input("Enter width: "))
        self.width = width

    def Area(self):
        return self.length * self.width

    def Per(self):
        return 2*self.length + 2*self.width

#rec1 = rec("red",50,4)
rec1 = rec()
rec1.input_colour()
rec1.input_length()
rec1.input_width()
print(rec1.Area())
print(rec1.Per())