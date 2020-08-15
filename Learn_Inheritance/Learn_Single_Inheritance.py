class A:

    def a(self):
        print("I'm from Class A")



class B(A):

    def b(self):
        print("I'm from Class B")




aaa = A()
aaa.a()


bbb = B()
bbb.b()
bbb.a()
