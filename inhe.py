class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

    def parimeter(self):
        return 2*self.length+2*self.width

class Square(Rectangle):
    def __init__(self,length):
        super(Square,self).__init__(length,length)

obj=Square(66)
print(obj.area())  
print(obj.parimeter())                            