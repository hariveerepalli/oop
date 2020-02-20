class One():
    name = 'sriram'

    def add(self):
        print(' addition is :', 5 + 7)

    def sum(self, a, b):
        return a + b

# To create a instance to the class
inst = One()
inst1 = One()

# To print class variable name
print(' Name is :', inst.name)

# To call add method
inst.add()

# To call sum method
r = inst.sum(50,60)
print(' Sum is :', r)
