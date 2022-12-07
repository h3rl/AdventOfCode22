import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

data = parseAOC("./1.txt")
test_data = parseAOC_test("""\
Testdata
""")

a = 0
b = 0
# solution


print("Solution a: " + str(a))
print("Solution b: " + str(b))