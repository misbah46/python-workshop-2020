class ut1:
    #name="finglish"
    """this is a OBJECT ORIENTED FILE"""
    def __init__(self,dept1):
        self.dept=dept1
       #print("HEY THERE!")
    def display(self):
        """this is FUNCTION"""
        print("HI I AM IN A CLASS",self.dept)

        
ob1=ut1("FUN")
#print(ob1.name)
ob1.display()
print(ob1.__doc__)
print(ob1.display.__doc__)