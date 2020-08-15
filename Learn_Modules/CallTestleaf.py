# Way1
# import Learn_Modules.Testleaf
#
# Learn_Modules.Testleaf.TestLeaf01.python()
#
# Learn_Modules.Testleaf.TestLeaf01
# Learn_Modules.Testleaf.Testleaf02
# Learn_Modules.Testleaf.Basic_info()

# Way2
from Learn_Modules.Testleaf import TestLeaf01
TestLeaf01.python()

# Way3
from Learn_Modules.Testleaf import TestLeaf01 as x
x.python()

# Way4 - Multiclass import statement
from Learn_Modules.Testleaf import TestLeaf01 as x, Testleaf02 as y

x.python()
y.selenium()