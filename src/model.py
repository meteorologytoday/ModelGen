
def genSimpleName(obj):
    return "%s(id=%s)" % (obj.__class__.__name__, str(hash(obj)))



class Gettable:
    def getValue(self):
        print("Hasn't been overwritten yet.")



class Variable(Gettable):
    def __init__(self):
        pass





class Scalar(Variable):
    def __init__(self):
        self.val  = None
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


class Target(Field):
    def __init__(self, *args, **kwargs):
        super(Target, self).__init__(*args, **kwargs)


class DummyTarget(Field):
    def __init__(self, *args, **kwargs):
        super(DummyTarget, self).__init__(*args, **kwargs)





class Operator(Gettable):
    def __init__(self, num_of_operands):
        self.operands = [None for _ in range(num_of_operands)]
        self.num_of_operands = num_of_operands

    def setOperands(self, *args):

        if len(args) > self.num_of_operands:
            raise Exception("Too many operands.")

        for i, arg in enumerate(args):
            if(isinstance(arg, Gettable) == False):
                raise Exception("Operand should be Gettable.")
            self.operands[i] = arg

        return self

    def clearOperands(self):
        self.operands = [None for _ in range(self.num_of_operands)]


    def areOperandsAllSet(self):
        empty_cnt = 0
        for i, operand in enumerate(self.operands):
            if operand is None:
                empty_cnt += 1
        
        return empty_cnt == 0


class OpMinus(Operator):
    def __init__(self):
        super(OpMinus, self).__init__(2)
        self.op_name = genSimpleName(self)
        self.desc = "No Description"

    def setDescription(self, desc: str):
        self.desc = desc
        return self




class Wrapper:
    def __init__(self):
        self.target = None

    def genGraph(self):
        return None


    def setTarget(self, target: Target):
        if(isinstance(target, Target) == False):
            raise Exception("Target should be subclass of Target.")

        self.target = target
        return self





if __name__ == "__main__":
    nu = Scalar().setValue(20)
    u  = Field().setName("U velocity") 


    print(u)


    mul_op = OpMinus().setOperands(nu, u)
    mul_op.getValue()

    zeta = Target()

    wrap = Wrapper().setTarget(zeta)
