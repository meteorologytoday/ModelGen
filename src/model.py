import random




def genSimpleName(obj):
    return "%s(id=%s)" % (obj.__class__.__name__, str(hash(obj)))

class Node:
    def __init__(self, num_of_links=0):
        #print(type(self))
        #print(isinstance(self, Node))
        self.links = [Link().setFNode(self) for _ in range(num_of_links)]
        self.name = None
        self.desc = None

    def setName(self, name: str):
        self.name = str(name)
        return self

    def getName(self):
        return self.name

    def __str__(self):
        return "[%s]" % (self.getName(),)
 

    def getValue(self):
        print("Hasn't been overwritten yet.")

    def getLinks(self):
        return self.links

    def genMath(self):
        return None

class Link:
    def __init__(self, f_node=None, t_node=None):
        self.setFNode(f_node).setTNode(t_node)
        self.checked = None  # For circular detection

    def setFNode(self, node):
        if((node is not None) and isinstance(node, Node) == False):
            raise Exception("from_node should be a Node.")


        self.f_node = node
        return self

    def setTNode(self, node):
        if((node is not None) and isinstance(node, Node) == False):
            raise Exception("to_node should be a Node.")

        self.t_node = node
        return self

    def setChecked(self, checked):
        self.checked = checked
        return self

    def getChecked(self):
        return self.checked


    def getFNode(self):
        return self.f_node

    def getTNode(self):
        return self.t_node


class Variable(Node):
    def __init__(self):
        super().__init__(num_of_links=0)


    def genMath(self):
        return self.name

       



class Scalar(Variable):
    def __init__(self):
        super().__init__()
        self.val  = None
        self.name = genSimpleName(self)


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
        super().__init__()
        self.val  = None
        self.dims = []
        self.name = genSimpleName(self)

    def setValue(self, val: float):
        self.val = val
        return self

    def clear(self):
        self.val = None
        return self
    


class Target(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(num_of_links=1)
        
    def setEqual(self, node):
        self.links[0].setTNode(node)
        return self

    def getEqual(self):
        return self.links[0].getTNode()

    def genMath(self):
        return self.getName()

class Operator(Node):
    def __init__(self, num_of_operands):
        super().__init__(num_of_links=num_of_operands)
        self.desc = "No Description"

    def setDescription(self, desc: str):
        self.desc = desc
        return self


    def setOperands(self, *args):

        if len(args) > len(self.links):
            raise Exception("Too many operands.")

        for i, arg in enumerate(args):
            self.links[i].setTNode(arg)

        return self

    def getOperands(self):
        return [link.getTNode() for link in self.links]

 
    def clearOperands(self):
        for link in self.links:
            link.setTNode(None)


    def areOperandsAllSet(self):
        empty_cnt = 0
        for link in self.links:
            if link.getTNode() is None:
                empty_cnt += 1
        
        return empty_cnt == 0


class OpMinus(Operator):
    def __init__(self):
        super().__init__(2)
        self.name = genSimpleName(self)

    def genMath(self):
        return "(%s - %s)" % (self.getOperands()[0].genMath(), self.getOperands()[1].genMath())

class OpAdd(Operator):
    def __init__(self):
        super().__init__(2)
        self.name = genSimpleName(self)

    def genMath(self):
        return "(%s + %s)" % (self.getOperands()[0].genMath(), self.getOperands()[1].genMath())


class OpMul(Operator):
    def __init__(self):
        super().__init__(2)
        self.name = genSimpleName(self)

    def genMath(self):
        return "(%s * %s)" % (self.getOperands()[0].genMath(), self.getOperands()[1].genMath())


class Wrapper:
    def __init__(self):
        self.target = None
        self.name = None



    def detectCircular(self, prev_tnode, this_tnode, key):
        
        for link in this_tnode.getLinks():
            next_tnode = link.getTNode()
            if next_tnode is None:
                raise Exception("Node [%s] has empty links." % (str(this_tnode),))
            
            if link.getChecked() == key:
                raise Exception("Circular direction detected at node [%s]" % (str(prev_tnode),))

            link.setChecked(key)
            self.detectCircular(this_tnode, next_tnode, key)


    def check(self):
        key = random.getrandbits(128)
        #print("key = " + str(key))
        self.detectCircular(None, self.target, key)
        print("Checking successful")
        


    def genDOT(self):
        s = "graph %s { \n" % (self.name)

        
    def genMath(self):
        return "%s = %s" % (self.target.genMath(), self.target.getEqual().genMath())




        s += "}"
        return None


    def setTarget(self, target: Target):
        if(isinstance(target, Target) == False):
            raise Exception("Target should be subclass of Target.")

        self.target = target
        return self


    


if __name__ == "__main__":
    nu = Scalar().setName("nu").setValue(20)
    mu = Scalar().setName("mu").setValue(6e-3)
    u  = Field().setName("U") 

    min_op = OpMinus()
    add_op = OpAdd()

    mul_op = OpMul().setOperands(nu, add_op)

    add_op.setOperands(mu, min_op)


    zeta_t = Target().setName("zeta_t").setEqual(mul_op)
    min_op.setOperands(u, nu)
    wrap = Wrapper().setTarget(zeta_t)
    wrap.check()
   
    print(wrap.genMath()) 
     
    
    
