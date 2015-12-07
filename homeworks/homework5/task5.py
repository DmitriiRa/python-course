import re
import sys

pattern = "\W+"
data = sys.stdin.read()
result = re.sub(pattern, " ", data)
print(result)
