#countAreicles
import re
input = input("Enter a sentance: ")
p = re.compile('a |an |the ')
result = len(p.findall(input))
print(result)