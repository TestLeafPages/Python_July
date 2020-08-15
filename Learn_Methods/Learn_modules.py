class Testleaf:

    def python(self):               # -----> instance method
        print("Dev and DS")


    def java(self):
        print("Dev")

    @classmethod                # ---------> class method
    def emi(cls):
        print("from class method")

    @staticmethod
    def conf_python():          # --------> static method
        pass




per1 = Testleaf()
per1.python()
per1.emi()


per2 = Testleaf()
per2.java()
per2.emi()


Testleaf.emi()
Testleaf.python()

Testleaf.conf_python()

