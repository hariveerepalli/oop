## Using constructor we can create instance varables.
class One():
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        print('__INIT__')

    def add(self):
       print(' Add method ', self.uname , self.password)
       
    def sub(self, hostname,port):
        print(' Sub method ', self.uname, self.password, hostname, port)

    def mul(self):
        print(' Mul method ', self.uname, self.password )

inst = One('Admin', 'Admin123')
inst.add()
inst.sub('67', 23)
inst.mul()
