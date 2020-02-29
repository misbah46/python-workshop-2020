class abc:
    @classmethod
    def example(cls):
        print("in example class method")
        cls.statfunc()
    @staticmethod
    def statfunc():
        print("in stat func")
obj=abc()
obj.example()            
                     

    