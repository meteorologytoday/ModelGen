
def genSimpleName(obj):
    return "%s(%s)" % (obj.__class__.__name__, str(hash(obj)))


class Variable:
    def __init__(self):
        pass

class Scalar(Variable):
    def __init__(self):
        self.val  = None
        self.name = "Scalar(" + str(hash(self)) + ")"

    def setName(self, name: str):
        self.name = str(name)
        return self


    def setValue(self, val: float):
        self.val = val
        return self

    def clear(self):
        self.val = None
        return self
    

    def __str__(self):
        return "[%s] = %f" % (self.name, self.val)
        

class Field(Variable):
    def __init__(self):
        self.val  = None
        self.dims = []
        self.name = genSimpleName(self)

    def setName(self, name: str):
        self.name = str(name)
        return self


    def setValue(self, val: float):
        self.val = val
        return self

    def clear(self):
        self.val = None
        return self
    

    def __str__(self):
        return "[%s]" % (self.name)


class Operator:
    def __init__(self):
        pass


class UnaryOperator(Operator):
    def __init__(self):
        pass


 
class BinaryOperator(Operator):
    def __init__(self):
        self.var1 = None
        self.var2 = None
        self.op_name = genSimpleName(self)

    def setOpName(self, op_name: str):
        self.op_name = op_name
        return self


    def setVars(self, var1: Variable, var2: Variable):
        self.var1 = var1
        self.var2 = var2
        return self
        






if __name__ == "__main__":
    nu = Scalar().setValue(20)
    u  = Field().setName("U velocity") 


    print(isinstance(nu, Scalar))
    print(isinstance(nu, Variable))
    print(u)


    mul_op = BinaryOperator().setVars(nu, u)
