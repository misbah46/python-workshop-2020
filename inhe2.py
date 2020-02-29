class first:
    def sum(self,x,y):
        print(x+y)

class second(first):
    def sum(self,x,y):
        print(x-y)
class third(second):
    def sum(second,x,y):
        print(x*y)

obj=third()
obj.sum(3,4)


