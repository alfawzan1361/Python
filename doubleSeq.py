#double
seq = input('Enter seq: ')
seq = [int(x) for x in seq.split()]
result = [i * 2 for i in seq]
print(result)