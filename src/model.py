




class Scalar:
    def __init__(self):
        self.val  = None
        self.name = "Scalar(" + str(hash(self)) + ")"

    def setName(self, name: str) -> 'Scalar':
        self.name = str(name)
        return self


    def setValue(self, val: float) -> 'Scalar':
        self.val = val
        return self

    def clear(self) -> 'Scalar':
        self.val = None
        return self
    

    def __str__(self) -> 'str':
        return "[%s] = %f" % (self.name, self.val)
        

class Variable:
    def __init__(self):
        pass






if __name__ == "__main__":
    nu = Scalar().setValue(20)
    print(nu)
 
