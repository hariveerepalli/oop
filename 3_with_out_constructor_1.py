## Using without constructor, how do we create instance varables.
class One():
    def add(self, uname, password):
       print(uname , password)
       
    def sub(self, uname, password, hostname,port):
        print(uname, password, hostname, port )

    def mul(self, uname, password):
        print(uname, password )

inst = One()
inst.add('admin','admin123')
inst.sub('admin','admin123','12.45.67.8', 23)
inst.mul('admin','admin123')
inst1 = One()
inst1.add('hursh345','@@5668778')