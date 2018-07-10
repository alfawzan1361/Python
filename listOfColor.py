import re
input = input("Enter a sentance: ")
p = re.compile('black|brown|blue|red|yellow|orange|purple|green|gray|pink')
result = p.findall(input)
print(result)

