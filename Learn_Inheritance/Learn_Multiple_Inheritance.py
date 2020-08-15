class Gp:

    def x(self):
        print("I'm from Class Gp ------> x")


class A(Gp):

    def a(self):
        print("I'm from Class A")


class B:

    def b(self):
        print("I'm from Class B")

    def x(self):
        print("I'm from Class B ---> X")


class C(B, A):

    def c(self):
        print("I'm from Class C")


ccc = C()
print(C.__mro__)